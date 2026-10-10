#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""Omni-Compass on top of a Kafka consumer group's operator-set size (docs/KAFKA_PREREGISTRATION.md).

Apache Kafka as shipped (one KRaft broker on the machine, its server.properties untouched but for the log directory) carries
a topic of 8 partitions. A producer offers messages at a stepped rate, the same in both arms; a consumer group reads them,
spends a declared service time of CPU on each (the work the messages are for), and records each message's end-to-end
latency, produce to consume. An operator sets the consumer count once; that fixed number is the native controller here.

  native  the consumer group at the operator's count (2 consumers) for the whole run
  omni    the same group, with the compass law (omnicompass/compass_law.py) on one knob, the consumer count, inside the
          cover [1, 8] (never under one consumer, never more consumers than partitions): the compass reads the group's own
          end-to-end latency on a band from 0 to the response line and holds it at 40% of the line; the service slow and
          messages waiting add consumers; calm gives back one idle consumer a second; at 95% of the line every consumer the
          topic can use is started at once (fail up); the count is handed back to the operator's at the end and read back

Gauges from the consumers' own records (every message's latency), the group's lag (produced minus consumed) and the
host's /proc/stat (CPU seconds, the consumers' and the compass's own cost, counted against Omni). No energy is claimed
beyond the host's CPU seconds. Every row is reported, losses included.

  python3 tools/run_kafka.py --setup                      # start a broker and make the topics (the workflow does this)
  python3 tools/run_kafka.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_kafka.py --report-only DIR            # re-read finished <workload>.json files and write KAFKA.md
"""
from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import os
import statistics
import subprocess
import sys
import threading
import time
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 2: the brain's own verdict)

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
PARTITIONS = 8
LINE_MS = 500.0           # the response line: a message handled within 500 ms of being produced
CENTER = 0.4              # the compass holds the service at 40% of the line
DT = 1.0                  # one decision a second
TAU = 3.0                 # a consumer added or removed shows in the latency within a few seconds (the group rebalances)
SMOOTH = 0.5
NATIVE_CONSUMERS = 2      # the operator's count
COVER = (1, PARTITIONS)   # never under one consumer, never more than partitions
DWELL_S = 5.0             # no taking back within five seconds of a change
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
PEAK_SHARE = 0.9          # the peak notch offers nine tenths of native's measured capacity
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}
SAME_REL = 1e-6

WORKLOADS = {
    # name: (service ms of CPU per message, payload bytes, steps, tuning?)
    "tuning": (2.0, 256, STEPS, True),
    "light": (1.0, 128, STEPS, False),
    "heavy": (5.0, 1024, STEPS, False),
    "burst": (2.0, 256, BURST, False),
}

GAUGES = [  # key, label, direction
    ("work_inside_line_mps", "work inside the response line (messages a second handled within the line)", "higher"),
    ("mps", "throughput (messages a second consumed)", "higher"),
    ("p95_ms", "end-to-end latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "end-to-end latency, 99th percentile (ms)", "lower"),
    ("p50_ms", "end-to-end latency, median (ms)", "lower"),
    ("mean_ms", "end-to-end latency, mean (ms)", "lower"),
    ("lag_max", "consumer lag, most messages waiting at once", "lower"),
    ("lag_mean", "consumer lag, mean messages waiting", "lower"),
    ("lost", "messages produced and never consumed", "never more"),
    ("consumers_mean", "consumers running, mean (the resources held)", "lower"),
    ("consumers_max", "consumers running, most at once", "lower"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "lower"),
    ("cpu_seconds", "host CPU-seconds", "lower"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 messages inside the line", "lower"),
    ("rebalances", "consumer changes written (the knob's moves)", "shown"),
]


# ------------------------------------------------------------------ the producer and the consumers
def busy_ms(ms):
    """Spend `ms` of CPU on a message (the work the message is for)."""
    end = time.perf_counter() + ms / 1000.0
    x = 0.0
    while time.perf_counter() < end:
        x = math.sqrt(x + 1.0)
    return x


def producer_proc(topic, rate_steps, step_s, payload_bytes, produced, stop, log_path):
    """Offer messages at the stepped rate; every message carries its produce time (ns, the machine's monotonic clock)."""
    from kafka import KafkaProducer
    p = KafkaProducer(bootstrap_servers=BOOTSTRAP, linger_ms=5, acks=1)
    pad = b"x" * max(0, payload_bytes - 40)
    seq = 0
    with open(log_path, "w") as log:
        for rate in rate_steps:
            t_end = time.perf_counter() + step_s
            interval = 1.0 / max(rate, 1e-9)
            nxt = time.perf_counter()
            log.write(f"{time.time():.3f} rate {rate:.1f}\n"); log.flush()
            while time.perf_counter() < t_end and not stop.is_set():
                now = time.perf_counter()
                if now >= nxt:
                    p.send(topic, key=str(seq % PARTITIONS).encode(), value=f"{seq}:{time.perf_counter_ns()}:".encode() + pad)
                    seq += 1; nxt += interval
                    with produced.get_lock():
                        produced.value = seq
                else:
                    time.sleep(min(0.001, nxt - now))
            if stop.is_set():
                break
        p.flush(); p.close()


def consumer_proc(topic, group, service_ms, consumed, stop_evt, rec_path, idle_flag):
    """One consumer of the group: poll, spend the service time per message, record (consume time, latency ms)."""
    from kafka import KafkaConsumer
    c = KafkaConsumer(topic, bootstrap_servers=BOOTSTRAP, group_id=group, auto_offset_reset="earliest",
                      enable_auto_commit=True, max_poll_records=50, session_timeout_ms=10000, heartbeat_interval_ms=3000)
    n = 0
    with open(rec_path, "a") as rec:
        while not stop_evt.is_set():
            batch = c.poll(timeout_ms=200)
            got = 0
            for msgs in batch.values():
                for m in msgs:
                    seq, t_ns, _ = m.value.split(b":", 2)
                    busy_ms(service_ms)
                    lat_ms = (time.perf_counter_ns() - int(t_ns)) / 1e6
                    rec.write(f"{time.time():.3f} {seq.decode()} {lat_ms:.3f}\n")
                    got += 1
            if got:
                n += got; rec.flush()
                with consumed.get_lock():
                    consumed.value += got
            idle_flag.value = 0 if got else 1
    c.close()


class Group:
    """The consumer group as a fleet of processes: start one, stop one, how many run, which are idle."""

    def __init__(self, topic, group, service_ms, out: Path):
        self.topic, self.group, self.service_ms, self.out = topic, group, service_ms, out
        self.consumed = mp.Value("l", 0); self.procs = []; self.k = 0; self.changes = 0

    def start_one(self):
        stop = mp.Event(); idle = mp.Value("i", 1)
        self.k += 1
        p = mp.Process(target=consumer_proc, args=(self.topic, self.group, self.service_ms, self.consumed, stop, str(self.out / f"consumer-{self.k}.log"), idle), daemon=True)
        p.start(); self.procs.append((p, stop, idle)); self.changes += 1

    def stop_one(self, prefer_idle=True):
        if not self.procs:
            return False
        order = sorted(range(len(self.procs)), key=lambda i: -self.procs[i][2].value) if prefer_idle else range(len(self.procs))
        i = list(order)[0]
        p, stop, _ = self.procs.pop(i); stop.set(); p.join(timeout=15); self.changes += 1
        return True

    def count(self):
        return len(self.procs)

    def idle(self):
        return sum(1 for _, _, f in self.procs if f.value)

    def stop_all(self):
        for p, stop, _ in self.procs:
            stop.set()
        for p, _, _ in self.procs:
            p.join(timeout=15)
        self.procs = []


# ------------------------------------------------------------------ the compass on the consumer count
def service_sample(rec_files, since_s, line_ms=LINE_MS):
    """The brain's sample from the consumers' own records: (the mean end-to-end latency in s of the messages consumed in the
    last second, or None when none was; how many were consumed; how many of them inside the line)."""
    now = time.time(); lat = []
    for f in rec_files:
        try:
            with open(f) as fh:
                fh.seek(0, 2); size = fh.tell(); fh.seek(max(0, size - 65536))
                for ln in fh.read().splitlines()[-400:]:
                    t, _, l = ln.split(" ")
                    if float(t) >= now - since_s:
                        lat.append(float(l) / 1000.0)
        except (OSError, ValueError):
            pass
    if not lat:
        return None, 0, 0
    return sum(lat) / len(lat), len(lat), sum(1 for l in lat if l * 1000.0 <= line_ms)


def service_reading(rec_files, since_s):
    """The group's own reading: the mean end-to-end latency (s) of the messages consumed in the last second; nothing
    consumed reads as the lag's age (messages waiting with no one taking them), capped at the line."""
    return service_sample(rec_files, since_s)[0]


def decide(p, force, lag, idle, cur, last_change_age, wall=0.95):
    """The knob's move this second: (target, direction, why). The service slow with messages waiting adds consumers,
    ceil(force / 0.1) at a time; calm gives back one idle consumer a second, after the dwell; past the wall, every
    consumer the topic can use at once."""
    lo, hi = COVER
    if p is not None and p >= wall:
        return hi, 0, "fail up: the line is at hand, every consumer at once"
    if force > 0.05 and lag > 0:
        want = min(hi, cur + max(1, math.ceil(force / 0.1)))
        return want, (1 if want != cur else 0), f"slow with {lag} waiting: add {want - cur}"
    if force < -0.05 and idle > 0 and cur > lo and last_change_age >= DWELL_S and lag == 0:
        return cur - 1, -1, "calm, an idle consumer given back"
    return cur, 0, "hold"


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit; the knob is handed back at the end and read back. Amendment 2 (the
    brain's own verdict, 2026-10-09): the group's size starts in watch and is written only inside the allowance a paired trial
    on the group itself has earned under the declared objective (tools/knob_verdict.py around the engine's own Verdict); a
    trial holds the count; a fail-up never spends beyond the allowance."""

    def __init__(self, grp: Group, produced, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE):
        super().__init__(daemon=True)
        self.grp, self.produced, self.audit, self.line_ms, self.objective = grp, produced, audit_path, line_ms, objective
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.failups = 0; self.handed_back = False; self.verdict = None

    def run(self):
        snapshot = self.grp.count()                        # read once, before the first write: the operator's count
        t0 = time.monotonic(); cpu_prev = cpu_times()
        self.verdict = KnobVerdict(snapshot, 1, COVER, objective=self.objective, settle_s=2 * TAU)   # a consumer that joins rebalances the group first
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                recs = [self.grp.out / f"consumer-{k}.log" for k in range(1, self.grp.k + 1)]
                lag = max(0, self.produced.value - self.grp.consumed.value)
                reading, n_msg, inside = service_sample(recs, 1.0, self.line_ms)
                if reading is None:
                    reading = min(LINE_MS / 1000.0, 0.0 if lag == 0 else LINE_MS / 1000.0)   # waiting with no one consuming: the line
                f = self.law.force(reading)
                cur = self.grp.count(); idle = self.grp.idle()
                cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                cpu_share = (1.0 - d_idle / d_total) if d_total > 0 else None
                cost = sample_cost(self.objective, inside, reading if n_msg else None, cur, cpu_share)
                self.verdict.observe(cost, tick - t0)                                    # measured under the count of the last second
                target, d, why = decide(self.law.p, f, lag, idle, cur, tick - self.last_change, wall=self.law.band.wall_high)
                fail_up = why.startswith("fail up")
                target, why, vinfo = self.verdict.decide(target, spend_ok=(f > 0.05 and lag > 0), give_ok=(f < -0.05 and idle > 0 and lag == 0),
                                                         t=tick - t0, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=fail_up)
                if target > cur:
                    for _ in range(target - cur):
                        self.grp.start_one()
                    self.last_change = tick
                    if fail_up:
                        self.failups += 1
                elif target < cur:
                    for _ in range(cur - target):
                        self.grp.stop_one()
                    self.last_change = tick
                fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 2), "p": round(self.law.p, 4), "force": round(f, 4),
                                     "lag": lag, "idle": idle, "consumers": cur, "target": target, "consumed_last_s": n_msg, "inside_last_s": inside,
                                     "cpu_share": None if cpu_share is None else round(cpu_share, 4), "cost": None if cost is None else round(cost, 9),
                                     **vinfo, "why": why}) + "\n")
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        # the hand-back: the operator's count, read back
        while self.grp.count() > snapshot:
            self.grp.stop_one(prefer_idle=False)
        while self.grp.count() < snapshot:
            self.grp.start_one()
        self.handed_back = self.grp.count() == snapshot


class Sampler(threading.Thread):
    """Consumers running and lag, once a second, in both arms."""

    def __init__(self, grp: Group, produced):
        super().__init__(daemon=True)
        self.grp, self.produced, self.stop_flag, self.rows = grp, produced, threading.Event(), []

    def run(self):
        while not self.stop_flag.is_set():
            self.rows.append((self.grp.count(), max(0, self.produced.value - self.grp.consumed.value)))
            time.sleep(DT)


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    idle = vals[3] + vals[4]
    return sum(vals), idle


def kafka_bin(name):
    home = os.environ.get("KAFKA_HOME", "")
    return str(Path(home) / "bin" / name) if home else name


def make_topic(topic):
    subprocess.run([kafka_bin("kafka-topics.sh"), "--bootstrap-server", BOOTSTRAP, "--create", "--if-not-exists", "--topic", topic,
                    "--partitions", str(PARTITIONS), "--replication-factor", "1"], check=True, capture_output=True, text=True)


def delete_topic(topic):
    subprocess.run([kafka_bin("kafka-topics.sh"), "--bootstrap-server", BOOTSTRAP, "--delete", "--topic", topic], capture_output=True, text=True)


# ------------------------------------------------------------------ one arm, one repetition
def run_arm(arm, wl_dir: Path, rep, service_ms, payload, steps, step_s, base, line_ms, objective=DEFAULT_OBJECTIVE):
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    topic = f"omni-{wl_dir.name}-{rep}-{arm}-{int(time.time())}"; group = topic + "-g"
    make_topic(topic)
    rates = [base * int(s) for s in steps.split()]
    produced = mp.Value("l", 0); stop_prod = mp.Event()
    grp = Group(topic, group, service_ms, d)
    for _ in range(NATIVE_CONSUMERS):
        grp.start_one()
    time.sleep(8)                                              # the group forms and settles (both arms)
    sampler = Sampler(grp, produced); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(grp, produced, d / "audit.jsonl", line_ms, objective); omni.start()
    cpu0 = cpu_times(); t0 = time.time()
    prod = mp.Process(target=producer_proc, args=(topic, rates, step_s, payload, produced, stop_prod, str(d / "producer.log")))
    prod.start(); prod.join()
    # drain: up to 30 s for the group to catch up, then stop
    t_drain = time.time()
    while grp.consumed.value < produced.value and time.time() - t_drain < 30:
        time.sleep(0.5)
    t1 = time.time(); cpu1 = cpu_times()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=60)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    changes = grp.changes
    grp.stop_all()
    # the gauges, from every consumer's record
    lats = []
    for f in sorted(d.glob("consumer-*.log")):
        for ln in f.read_text().splitlines():
            try:
                t, seq, lat = ln.split(" "); lats.append((float(t), float(lat)))
            except ValueError:
                pass
    seconds = t1 - t0
    lat_sorted = sorted(l for _, l in lats)
    n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    cons = [c for c, _ in sampler.rows] or [NATIVE_CONSUMERS]; lags = [l for _, l in sampler.rows] or [0]
    total = (cpu1[0] - cpu0[0]); idle = (cpu1[1] - cpu0[1]); tick_hz = os.sysconf("SC_CLK_TCK")
    cpu_s = (total - idle) / tick_hz
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "produced": produced.value, "consumed": n,
         "work_inside_line_mps": inside / seconds, "mps": n / seconds, "p95_ms": q(0.95), "p99_ms": q(0.99), "p50_ms": q(0.5),
         "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "lag_max": max(lags), "lag_mean": sum(lags) / len(lags),
         "lost": max(0, produced.value - n), "consumers_mean": sum(cons) / len(cons), "consumers_max": max(cons),
         "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s, "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside),
         "rebalances": changes, "handed_back": (omni.handed_back if omni else True), "failups": (omni.failups if omni else 0),
         "verdict": (omni.verdict.record() if omni and omni.verdict else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    delete_topic(topic)
    print(f"   {arm} rep {rep}: {n} of {produced.value} consumed, inside the line {inside / seconds:.1f}/s, p95 {g['p95_ms']:.0f} ms, "
          f"lag max {g['lag_max']}, consumers {g['consumers_mean']:.2f}, CPU {cpu_s:.1f} s, handed back {g['handed_back']}"
          + (f", verdict {g['verdict']['state']}" if g.get("verdict") else ""), flush=True)
    return g


def capacity(wl_dir: Path, service_ms, payload, calib_s):
    """Native's unlimited capacity: the operator's consumers fed faster than they can take for calib_s seconds."""
    d = wl_dir / "capacity"; d.mkdir(parents=True, exist_ok=True)
    topic = f"omni-{wl_dir.name}-cap-{int(time.time())}"; make_topic(topic)
    produced = mp.Value("l", 0); stop_prod = mp.Event()
    grp = Group(topic, topic + "-g", service_ms, d)
    for _ in range(NATIVE_CONSUMERS):
        grp.start_one()
    time.sleep(8)
    c0 = grp.consumed.value
    prod = mp.Process(target=producer_proc, args=(topic, [5000.0], calib_s, payload, produced, stop_prod, str(d / "producer.log")))
    prod.start(); t0 = time.time(); prod.join(); t1 = time.time()
    rate = (grp.consumed.value - c0) / (t1 - t0)
    grp.stop_all(); delete_topic(topic)
    return rate


def paired(reps, key, direction):
    """omni against native on one gauge over the repetitions: means, the mean paired difference, its 95% interval."""
    d = [r["omni"][key] - r["native"][key] for r in reps if _num(r["omni"].get(key)) and _num(r["native"].get(key))]
    if not d:
        return None
    n = len(d)
    nat = sum(r["native"][key] for r in reps) / n
    om = sum(r["omni"][key] for r in reps) / n
    mean = sum(d) / n
    if n > 1:
        sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (n - 1))
        half = T95.get(n - 1, 1.96) * sd / math.sqrt(n)
    else:
        half = float("nan")
    lo, hi = mean - half, mean + half
    same = abs(mean) <= SAME_REL * max(abs(nat), 1e-12)
    clear = n > 1 and (lo > 0 or hi < 0) and not same
    if direction == "shown":
        reading = "shown, not judged"
    elif direction == "never more" and any(x > 0 for x in d):
        reading = "**WORSE**"
    elif same:
        reading = "same"
    elif not clear:
        reading = "no difference beyond the noise"
    elif direction == "never more":
        reading = "better"
    else:
        reading = "better" if (mean > 0) == (direction == "higher") else "**WORSE**"
    return {"native": nat, "omni": om, "diff": mean, "ci95": [lo, hi], "n": n, "significant": clear, "reading": reading}


def _num(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))


def engine():
    try:
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], cwd=ROOT, capture_output=True, text=True, timeout=120).stdout.strip()
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return {"version": out.splitlines()[0] if out else "unknown", "commit": sha[:12]}
    except (OSError, subprocess.SubprocessError):
        return {"version": "unknown", "commit": "?"}


def run_workload(name, out: Path, reps, step_s, calib_s, line_ms, objective=DEFAULT_OBJECTIVE):
    service_ms, payload, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"kafka-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    print(f"== {name}: {service_ms} ms of work a message, {payload} B, steps {steps}, {step_s} s a notch, the verdict's objective {objective}", flush=True)
    cap = capacity(wl_dir, service_ms, payload, calib_s)
    peak = max(int(s) for s in steps.split())
    base = PEAK_SHARE * cap / peak
    print(f"   native capacity with {NATIVE_CONSUMERS} consumers: {cap:.0f} messages a second; base rate {base:.1f}/s (peak notch {peak} offers {PEAK_SHARE:.0%} of it)", flush=True)
    rec = {"workload": name, "tuning": tuning, "service_ms": service_ms, "payload_bytes": payload, "steps": steps, "step_s": step_s,
           "line_ms": line_ms, "native_consumers": NATIVE_CONSUMERS, "cover": list(COVER), "capacity_mps": cap, "base_rate_mps": base,
           "objective": objective, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, service_ms, payload, steps, step_s, base, line_ms, objective)
        rec["reps"].append(r)
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
    (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    return rec


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.3g}"


def report(recs, out: Path):
    L = ["# Kafka: Omni-Compass on top of a consumer group's operator-set size", "",
         f"Apache Kafka as shipped (one broker, a topic of {PARTITIONS} partitions); native: the consumer group at the operator's count "
         f"({NATIVE_CONSUMERS}); omni: the compass law on the consumer count inside [{COVER[0]}, {COVER[1]}], holding the group's own "
         f"end-to-end latency at {CENTER:.0%} of the {LINE_MS:.0f} ms line. The same offered load in both arms. Energy is the host's CPU "
         "seconds, the compass's own cost included. Every row is reported, losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: {rec['service_ms']} ms of work a message, {rec['payload_bytes']} B, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"Native capacity {rec['capacity_mps']:.0f} messages a second; base rate {rec['base_rate_mps']:.1f}/s; {len(rec['reps'])} paired repetitions; "
              f"engine {rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to the operator's count: {'yes' if hb else 'NO'}; fail-ups: "
              f"{sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "KAFKA.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "KAFKA.md"


def setup():
    """The workflow's broker: Kafka as shipped from KAFKA_HOME, one KRaft node, the log directory the only change."""
    home = Path(os.environ["KAFKA_HOME"]); props = Path("/tmp/omni-kafka-server.properties"); logs = Path("/tmp/omni-kraft-logs")
    txt = (home / "config" / "kraft" / "server.properties").read_text().replace("log.dirs=/tmp/kraft-combined-logs", f"log.dirs={logs}")
    props.write_text(txt)
    uuid = subprocess.run([str(home / "bin" / "kafka-storage.sh"), "random-uuid"], capture_output=True, text=True, check=True).stdout.strip().splitlines()[-1]
    subprocess.run([str(home / "bin" / "kafka-storage.sh"), "format", "-t", uuid, "-c", str(props)], check=True, capture_output=True, text=True)
    subprocess.Popen([str(home / "bin" / "kafka-server-start.sh"), str(props)], stdout=open("/tmp/omni-kafka-server.log", "w"), stderr=subprocess.STDOUT)
    for _ in range(60):
        if "Kafka Server started" in Path("/tmp/omni-kafka-server.log").read_text():
            print("broker up"); return 0
        time.sleep(2)
    print("broker did not start", file=sys.stderr); return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--calib-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--out", default="kafka-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, consumers and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("kafka-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.calib_s, a.line_ms, a.objective) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
