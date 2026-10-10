#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of the Linux kernel's own CPU frequency governor, energy read by the processor's own meter
(docs/CPU_POWER_PREREGISTRATION.md).

The machine as it runs: the kernel's frequency governor as shipped (schedutil, or the processor driver's own) choosing the
clock every few milliseconds under a fixed ceiling, the processor's energy counter (RAPL, /sys/class/powercap) ticking in
microjoules, and a CPU-bound service answering requests offered at a fixed rate that steps up and down. The governor is the
native controller here; it keeps running in both arms.

  native  the machine as found: the governor as shipped, the frequency ceiling where the operator left it (the top)
  omni    the same machine, the same governor, with the compass law (omnicompass/compass_law.py) on one knob, the frequency
          ceiling (cpufreq scaling_max_freq, written through the kernel's own interface on every CPU), inside the cover
          [half the top clock, the top]: the compass reads the service's own request latency on a band from 0 to the response
          line and holds it at 40% of the line; a slow service raises the ceiling by notches, calm gives one notch back after
          a dwell, at 95% of the line the ceiling goes to the top at once (fail up); the brain's own verdict
          (tools/knob_verdict.py around the engine's omnicompass/verdict.py) tries every notch down on the machine itself
          before it is allowed, under the declared objective, and a notch that does not pay is not taken; the ceiling is
          handed back to the operator's at the end and read back; a ceiling found at a value Omni did not write stops it
          writing (one writer); the master switch and the lease (omnicompass/master.py) hand back if Omni dies

Gauges from the service's own records (every request's latency), the processor's energy counter (joules over the window,
class P: the processor's own meter), a wall plug where one is fitted (WALL_METER, tools/wall_meter.py: the whole machine,
independent of Omni), the kernel's own frequency readings and /proc/stat. Energy is the resource; the machine count is one
in both arms. Every row is reported, losses included.

  sudo python3 tools/run_cpu_power.py --probe                       # can this machine run it? (the governor writable, the meter readable)
  sudo python3 tools/run_cpu_power.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_cpu_power.py --report-only DIR                  # re-read finished <workload>.json files and write CPU_POWER.md
  python3 tools/run_cpu_power.py --restore DIR/snapshot.json        # put the ceiling back by hand (the watchdog runs this if Omni dies)
  python3 tools/run_cpu_power.py --plant sim --workloads tuning --reps 1 --step-s 2 --out DIR   # the harness on a modelled machine (tests only)
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import math
import multiprocessing as mp
import os
import queue
import random
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
from omnicompass import master  # noqa: E402
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402

SYSFS_CPU = "/sys/devices/system/cpu"
SYSFS_RAPL = "/sys/class/powercap"
LINE_MS = 20.0            # the response line: a request answered within 20 ms (the service itself takes about 5 ms at the top clock)
CENTER = 0.4              # the compass holds the service's latency at 40% of the line
DT = 1.0                  # one decision a second
TAU = 2.0                 # a ceiling written shows in the latency within a couple of seconds
SMOOTH = 0.5
NOTCH_SHARE = 0.05        # one notch of the knob: 5% of the top clock
FLOOR_SHARE = 0.5         # the cover: never under half the top clock (and never under the processor's own minimum)
DWELL_S = 5.0             # after raising the ceiling, no giving back within five seconds (no hunting)
SERVICE_MS = 5.0          # the work unit: about 5 ms of one core at the top clock, calibrated once per run and then fixed for every arm
UTIL_AT_TOP_STEP = 0.9    # the offered rate at step 8 is 90% of the machine's capacity at the top clock
TOP_STEP = 8
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
STEADY = "3 3 3 3 3 3"
BURST = "1 6 1 8 1 6"
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}
SAME_REL = 1e-6

WORKLOADS = {
    # name: (steps, tuning?)
    "tuning": (STEADY, True),     # the tuning case: steady at step 3 (the rules are frozen on it; shown, not counted)
    "wandering": (STEPS, False),  # demand that wanders one step at a time
    "burst": (BURST, False),      # bursts sized to the machine
}

GAUGES = [  # key, label, direction
    ("work_inside_line_rps", "work inside the response line (requests a second answered within the line)", "higher"),
    ("rps", "throughput (requests a second)", "higher"),
    ("p95_ms", "latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed requests (not answered by the end of the arm)", "never more"),
    ("energy_j", "energy, CPU package (J; the processor's own meter, the resource)", "lower"),
    ("power_w_mean", "power, CPU package mean (W)", "lower"),
    ("j_per_1k_inside", "energy per 1,000 requests inside the line (J)", "lower"),
    ("wall_j", "energy, whole machine at the wall (J; where a plug is fitted)", "lower"),
    ("ceiling_mhz_mean", "frequency ceiling held, mean (MHz; the knob)", "shown"),
    ("freq_mhz_mean", "frequency run at, mean (MHz; the governor's own choice under the ceiling)", "shown"),
    ("cpu_busy_share", "CPU busy (share of the run)", "shown"),
    ("writes", "ceiling changes written (the knob's moves)", "shown"),
]


# ------------------------------------------------------------------------------------------------------- the plant
class Plant:
    """The machine through the kernel's own files: the frequency ceiling of every CPU (the knob), the governor (read only,
    the native controller), the processor's energy counter (the meter). `root` is / on a real machine; a modelled tree in a
    directory for the tests (SimPlant)."""

    def __init__(self, root="/"):
        self.root = Path(root)
        self.cpu_dir = self.root / SYSFS_CPU.lstrip("/")
        self.rapl_dir = self.root / SYSFS_RAPL.lstrip("/")
        self.cpus = sorted((d for d in self.cpu_dir.glob("cpu[0-9]*") if (d / "cpufreq").is_dir()), key=lambda d: int(d.name[3:]))
        self.packages = sorted(d for d in self.rapl_dir.glob("*rapl*:[0-9]*") if d.name.count(":") == 1 and (d / "energy_uj").exists())
        self.snapshot, self.last_written, self.expected = None, None, None
        self._e_prev = None

    # the knob
    def _read(self, cpu, name):
        return (cpu / "cpufreq" / name).read_text().strip()

    def _put(self, path: Path, text: str):
        """One kernel attribute written (the kernel takes the value whole); the modelled machine replaces the file whole."""
        path.write_text(text)

    def top_khz(self):
        """The top clock: the highest any CPU reaches (on a machine with two kinds of core the smaller cores clamp a higher
        ceiling to their own top, which the kernel does by itself)."""
        return max(int(self._read(c, "cpuinfo_max_freq")) for c in self.cpus)

    def min_khz(self):
        return max(int(self._read(c, "cpuinfo_min_freq")) for c in self.cpus)

    def governors(self):
        return sorted({self._read(c, "scaling_governor") for c in self.cpus})

    def driver(self):
        try:
            return self._read(self.cpus[0], "scaling_driver")
        except OSError:
            return "?"

    def cur_khz_mean(self):
        vals = []
        for c in self.cpus:
            for name in ("scaling_cur_freq", "cpuinfo_cur_freq"):
                try:
                    vals.append(int(self._read(c, name))); break
                except (OSError, ValueError):
                    continue
        return sum(vals) / len(vals) if vals else float("nan")

    def attach(self):
        """The snapshot, taken once: every CPU's governor and ceiling, as found. The knob starts at the operator's ceiling."""
        if self.snapshot is None:
            self.snapshot = {c.name: {"governor": self._read(c, "scaling_governor"), "max_khz": int(self._read(c, "scaling_max_freq")),
                                      "min_khz": int(self._read(c, "scaling_min_freq"))} for c in self.cpus}
        self.expected = {c.name: int(self._read(c, "scaling_max_freq")) for c in self.cpus}
        self.last_written = max(self.expected.values())
        return self.last_written

    def ceiling_actual(self):
        """The ceiling as the kernel holds it now (the highest over the CPUs)."""
        return max(int(self._read(c, "scaling_max_freq")) for c in self.cpus)

    def lever(self, check=True):
        """The knob's value (the ceiling last written, the operator's at first); every CPU's ceiling must still read what
        our last write left there, or another writer has the knob and Omni stops writing."""
        cur = {c.name: int(self._read(c, "scaling_max_freq")) for c in self.cpus}
        if check and self.expected is not None and cur != self.expected:
            moved = {k: (self.expected[k], v) for k, v in cur.items() if self.expected.get(k) != v}
            raise RuntimeError(f"another writer moved the ceiling (expected -> found, kHz): {moved}: Omni stops writing")
        return self.last_written if self.last_written is not None else max(cur.values())

    def write(self, khz):
        """One value to every CPU; the kernel clamps a core's ceiling to its own range, and what it reads back is what
        Omni expects to find there from now on."""
        for c in self.cpus:
            self._put(c / "cpufreq" / "scaling_max_freq", f"{int(khz)}\n")
        self.expected = {c.name: int(self._read(c, "scaling_max_freq")) for c in self.cpus}
        self.last_written = int(khz)
        return int(khz)

    def restore(self):
        try:
            if not self.snapshot:
                return False
            for c in self.cpus:
                self._put(c / "cpufreq" / "scaling_max_freq", f"{self.snapshot[c.name]['max_khz']}\n")
            return all(int(self._read(c, "scaling_max_freq")) == self.snapshot[c.name]["max_khz"] for c in self.cpus)
        except OSError:
            return False

    def writable(self):
        """Can the ceiling be written? Tried with the value already there, so nothing changes."""
        try:
            c = self.cpus[0]; cur = self._read(c, "scaling_max_freq")
            self._put(c / "cpufreq" / "scaling_max_freq", cur + "\n")
            return True
        except (OSError, IndexError):
            return False

    # the meter
    def energy_j(self):
        """The processor's energy counter summed over the packages, in joules, wrap-around taken care of."""
        tot = 0.0
        cur = []
        for p in self.packages:
            e = int((p / "energy_uj").read_text().strip())
            try:
                rng = int((p / "max_energy_range_uj").read_text().strip())
            except (OSError, ValueError):
                rng = None
            cur.append((e, rng))
        if self._e_prev is None:
            self._e_prev = cur; self._acc = 0.0
            return 0.0
        for (e, rng), (e0, _) in zip(cur, self._e_prev):
            d = e - e0
            if d < 0 and rng:
                d += rng + 1
            tot += max(0, d)
        self._e_prev = cur
        self._acc += tot / 1e6
        return self._acc

    def meter_readable(self):
        try:
            return bool(self.packages) and all(int((p / "energy_uj").read_text().strip()) >= 0 for p in self.packages)
        except (OSError, ValueError):
            return False

    def tick(self, busy_share):  # the real machine needs nothing; the modelled one advances its counter
        pass


class SimPlant(Plant):
    """A modelled machine in a directory for the tests: four CPUs with the kernel's files, a governor that reads
    'schedutil', a top clock of 2,800 MHz, an energy counter that grows as idle power plus a dynamic part rising with busy share
    and the clock to the power 2.5; the service time of a request grows as the top clock over the ceiling."""

    TOP_KHZ, MIN_KHZ = 2_800_000, 800_000
    P_IDLE_W, P_DYN_W = 5.0, 80.0

    def __init__(self, root, cpus=4):
        root = Path(root)
        for i in range(cpus):
            d = root / SYSFS_CPU.lstrip("/") / f"cpu{i}" / "cpufreq"; d.mkdir(parents=True, exist_ok=True)
            for name, val in (("scaling_governor", "schedutil"), ("scaling_driver", "modelled"), ("scaling_max_freq", self.TOP_KHZ),
                              ("scaling_min_freq", self.MIN_KHZ), ("cpuinfo_max_freq", self.TOP_KHZ), ("cpuinfo_min_freq", self.MIN_KHZ),
                              ("scaling_cur_freq", self.TOP_KHZ)):
                (d / name).write_text(f"{val}\n")
        r = root / SYSFS_RAPL.lstrip("/") / "intel-rapl:0"; r.mkdir(parents=True, exist_ok=True)
        (r / "energy_uj").write_text("0\n"); (r / "max_energy_range_uj").write_text("262143328850\n"); (r / "name").write_text("package-0\n")
        super().__init__(root)
        self._uj = 0

    def _put(self, path: Path, text: str):
        tmp = path.with_name(path.name + ".tmp")
        tmp.write_text(text); os.replace(tmp, path)

    def service_factor(self):
        """How much slower a request is than at the top clock, under the ceiling as the modelled governor runs it."""
        return self.TOP_KHZ / max(self.MIN_KHZ, self.ceiling_actual())

    def tick(self, busy_share, dt=DT):
        cur = self.ceiling_actual(); f = cur / self.TOP_KHZ
        for c in self.cpus:                                            # the modelled governor runs at the ceiling while busy
            self._put(c / "cpufreq" / "scaling_cur_freq", f"{int(cur)}\n")
        p = self.P_IDLE_W + self.P_DYN_W * max(0.0, min(1.0, busy_share)) * f ** 2.5
        self._uj = (self._uj + int(p * dt * 1e6)) % (262143328850 + 1)
        self._put(self.packages[0] / "energy_uj", f"{self._uj}\n")


# ------------------------------------------------------------------------------------------------------- the service
def work_unit(k, buf=b"\x5a" * 65536):
    """One request's work: k passes of SHA-256 over 64 KB, the same count in every arm (CPU-bound, no I/O)."""
    h = b""
    for _ in range(k):
        h = hashlib.sha256(buf + h).digest()
    return h


def calibrate(target_ms=SERVICE_MS, trials=25):
    """k such that one request takes about target_ms of one core at the clock the machine runs at now; fixed for the run."""
    t = time.perf_counter(); work_unit(20); per_pass = (time.perf_counter() - t) / 20
    k = max(1, int(round(target_ms / 1000.0 / max(per_pass, 1e-6))))
    ts = []
    for _ in range(trials):
        t = time.perf_counter(); work_unit(k); ts.append(time.perf_counter() - t)
    return k, statistics.median(ts) * 1000.0


VERDICT_KW = {}            # the brain's verdict as the engine ships it; the tests shorten its trials here


def _worker(req_q, res_q, k, sim_root, service_ms):
    plant = SimPlant.__new__(SimPlant) if sim_root else None
    if plant is not None:
        Plant.__init__(plant, sim_root)
    while True:
        item = req_q.get()
        if item is None:
            break
        rid, t_issue = item
        if plant is not None:
            try:
                factor = plant.service_factor()
            except (OSError, ValueError):                              # the modelled file mid-replacement: the last factor stands
                factor = getattr(plant, "_last_factor", 1.0)
            plant._last_factor = factor
            time.sleep(service_ms / 1000.0 * factor * random.uniform(0.95, 1.05))
        else:
            work_unit(k)
        res_q.put((rid, t_issue, time.monotonic()))


class Service(threading.Thread):
    """The CPU-bound service and the open-loop load in front of it: requests offered at the step's rate whether or not the
    last were answered (equal work in both arms), a pool of one worker per CPU, every request's latency recorded."""

    JITTER = (0.5, 1.5)        # the spacing of requests around the rate (a Poisson-like spread); the tests narrow it

    def __init__(self, steps, step_s, unit_rps, k, workers, seed, sim_root=None, service_ms=SERVICE_MS):
        super().__init__(daemon=True)
        self.steps, self.step_s, self.unit, self.k, self.n_workers = [int(s) for s in steps.split()], step_s, unit_rps, k, workers
        self.last_done_t = None
        self.rng, self.sim_root, self.service_ms = random.Random(seed), sim_root, service_ms
        self.ctx = mp.get_context("fork") if "fork" in mp.get_all_start_methods() else mp.get_context()
        self.req_q, self.res_q = self.ctx.Queue(), self.ctx.Queue()
        self.records, self.lock = [], threading.Lock()
        self.issued = self.done = 0
        self.t0 = None
        self.stop_flag = threading.Event()

    def _collect(self):
        while not self.stop_flag.is_set() or self.done < self.issued:
            try:
                rid, t_issue, t_done = self.res_q.get(timeout=0.2)
            except queue.Empty:
                if self.stop_flag.is_set():
                    break
                continue
            with self.lock:
                self.records.append((t_issue - self.t0, t_done - t_issue)); self.done += 1; self.last_done_t = t_done

    def run(self):
        procs = [self.ctx.Process(target=_worker, args=(self.req_q, self.res_q, self.k, self.sim_root, self.service_ms), daemon=True) for _ in range(self.n_workers)]
        for p in procs:
            p.start()
        self.t0 = time.monotonic()
        col = threading.Thread(target=self._collect, daemon=True); col.start()
        rid = 0
        for step in self.steps:
            rate = step * self.unit; period = 1.0 / rate
            n_step = int(round(rate * self.step_s))                            # the step's requests, the same count in both arms
            next_t = time.monotonic()
            for _ in range(n_step):
                while True:
                    now = time.monotonic()
                    if now >= next_t:
                        break
                    time.sleep(min(0.002, next_t - now))
                self.req_q.put((rid, now)); rid += 1; self.issued += 1
                next_t += period * self.rng.uniform(*self.JITTER)              # a Poisson-like spread around the rate, the same seed in both arms
        deadline = time.monotonic() + 5.0                                     # the queue drains for at most five seconds
        while self.done < self.issued and time.monotonic() < deadline:
            time.sleep(0.05)
        self.stop_flag.set()
        for _ in procs:
            self.req_q.put(None)
        col.join(timeout=2.0)
        for p in procs:
            p.join(timeout=2.0)
            if p.is_alive():
                p.terminate()

    def last_second(self, line_ms, since_s=1.0):
        """(answered, inside the line, mean latency s) over the last second's answered requests."""
        if self.t0 is None:
            return 0, 0, None
        cut = time.monotonic() - self.t0 - since_s
        with self.lock:
            lat = [l for t, l in self.records[-5000:] if t + l >= cut]
        if not lat:
            return 0, 0, None
        return len(lat), sum(1 for l in lat if l * 1000.0 <= line_ms), sum(lat) / len(lat)

    def reading(self, since_s=1.0):
        """What the compass reads: the mean latency of the last second's answered requests, in seconds; the line when requests
        have waited longer than the line with nothing answered (a service that answers nothing is at the line); nothing
        when nothing is asked."""
        n, _, mean_s = self.last_second(LINE_MS, since_s)
        if mean_s is not None:
            return mean_s
        if self.issued > self.done and self.t0 is not None:
            waited = time.monotonic() - (self.last_done_t or self.t0)
            if waited > LINE_MS / 1000.0:
                return LINE_MS / 1000.0
        return 0.0

    @property
    def failed(self):
        return max(0, self.issued - self.done)


# ------------------------------------------------------------------------------------------------------- the brain
def decide(p, force, cur, top, floor, notch, last_change_age, wall=0.95):
    """The knob's move this second, in kHz: a slow service raises the ceiling by ceil(force / 0.1) notches toward the top;
    calm gives one notch back after the dwell, never under the floor; past the wall the top at once."""
    if p is not None and p >= wall:
        return top, "fail up: the line is at hand, the ceiling to the top at once"
    if force > 0.05:
        return min(top, cur + notch * max(1, math.ceil(force / 0.1))), "the service slow: the ceiling up"
    if force < -0.05 and cur > floor and last_change_age >= DWELL_S:
        return max(floor, cur - notch), "calm: a notch given back"
    return cur, "hold"


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    return sum(vals), vals[3] + vals[4]


def grid(top, min_khz):
    """The notch and the floor on this machine, from the top clock."""
    notch = max(1000, int(round(top * NOTCH_SHARE / 1000.0)) * 1000)
    floor = max(min_khz, int(top * FLOOR_SHARE))
    n = int((top - floor) // notch)
    return notch, top - n * notch


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit; the knob is handed back at the end and read back. The ceiling
    starts in watch and is written only inside the allowance a paired trial on the machine itself has earned under the
    declared objective (tools/knob_verdict.py around the engine's own Verdict); a trial holds the ceiling; a fail-up never
    spends beyond the allowance; toward the operator's ceiling is always free. The master switch and the lease are honoured."""

    def __init__(self, plant: Plant, svc: Service, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE, power=None):
        super().__init__(daemon=True)
        self.plant, self.svc, self.audit, self.line_ms, self.objective = plant, svc, audit_path, line_ms, objective
        self.power = power                                             # a callable giving the last second's package power (W), or None
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.writes = 0; self.failups = 0
        self.foreign = False; self.handed_back = False; self.verdict = None; self.switched_off = False

    def run(self):
        top = self.plant.attach(); notch, floor = grid(self.plant.top_khz(), self.plant.min_khz())
        top = min(top, self.plant.top_khz())
        t0 = time.monotonic()
        self.verdict = KnobVerdict(top, notch, (floor, top), objective=self.objective, **{"settle_s": TAU, **VERDICT_KW})
        with open(self.audit, "w") as fh:
            fh.write(json.dumps({"snapshot": self.plant.snapshot, "top_khz": top, "notch_khz": notch, "floor_khz": floor, "objective": self.objective,
                                 "governors": self.plant.governors(), "driver": self.plant.driver()}) + "\n")
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    master.heartbeat()
                    if master.is_off():
                        self.switched_off = True
                        fh.write(json.dumps({"t": round(tick - t0, 2), "master": "OFF: handing back"}) + "\n")
                        break
                    reading = self.svc.reading(1.0)
                    n_req, inside, mean_s = self.svc.last_second(self.line_ms)
                    f = self.law.force(reading)
                    cur = self.plant.lever()
                    p_w = self.power() if self.power else None
                    cost = sample_cost(self.objective, inside, mean_s, p_w if p_w is not None else 1.0, None)   # one machine: energy x latency / work
                    self.verdict.observe(cost, tick - t0)
                    target, why = decide(self.law.p, f, cur, top, floor, notch, tick - self.last_change, wall=self.law.band.wall_high)
                    target, why, vinfo = self.verdict.decide(target, spend_ok=False, give_ok=(f < -0.05), t=tick - t0, why=why,
                                                             stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
                    wrote = None
                    if target != cur:
                        wrote = self.plant.write(target); self.writes += 1
                        if target > cur:
                            self.last_change = tick
                        if why.startswith("fail up"):
                            self.failups += 1
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "p": round(self.law.p, 4), "force": round(f, 4),
                                         "ceiling_khz": cur, "target_khz": target, "wrote_khz": wrote, "requests_last_s": n_req, "inside_last_s": inside,
                                         "power_w": None if p_w is None else round(p_w, 2), "cost": None if cost is None else round(cost, 9),
                                         **vinfo, "why": why}) + "\n")
                except Exception as e:                        # a foreign writer or a lost file: say so, stop writing
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plant.restore()


class Sampler(threading.Thread):
    """Once a second in both arms: the energy counter, the ceiling, the clock run at, the host's busy share, the wall plug."""

    def __init__(self, plant: Plant, svc: Service, wall_spec=None):
        super().__init__(daemon=True)
        self.plant, self.svc, self.wall_spec = plant, svc, wall_spec
        self.stop_flag, self.rows, self.lock = threading.Event(), [], threading.Lock()
        self.last_power_w = None

    def run(self):
        e_base = e_prev = self.plant.energy_j(); cpu_prev = cpu_times(); t_prev = time.monotonic()
        while not self.stop_flag.is_set():
            time.sleep(DT)
            now = time.monotonic()
            cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
            busy = (1.0 - d_idle / d_total) if d_total > 0 else 0.0
            if isinstance(self.plant, SimPlant):                       # the modelled machine: busy from the service's own work
                n, _, mean_s = self.svc.last_second(LINE_MS)
                busy = min(1.0, n * (self.svc.service_ms / 1000.0) * self.plant.service_factor() / max(1, self.svc.n_workers))
                self.plant.tick(busy, now - t_prev)
            e = self.plant.energy_j(); p_w = (e - e_prev) / max(1e-3, now - t_prev); e_prev = e; t_prev = now
            wall_w = None
            if self.wall_spec:
                try:
                    from tools.wall_meter import read as wall_read
                    wall_w = float(wall_read(self.wall_spec))
                except Exception:
                    wall_w = None
            with self.lock:
                self.last_power_w = p_w
                self.rows.append({"t": now, "energy_j": e - e_base, "power_w": p_w, "ceiling_khz": self.plant.ceiling_actual(),
                                  "cur_khz": self.plant.cur_khz_mean(), "busy": busy, "wall_w": wall_w})

    def power(self):
        with self.lock:
            return self.last_power_w


# ------------------------------------------------------------------------------------------------------- the arms
def probe(plant: Plant, wall_spec=None, out=print):
    """Can this machine run the benchmark? Prints what it has; returns 0 when it can, 2 when it cannot (and why)."""
    why = []
    if not plant.cpus:
        why.append("no cpufreq under /sys/devices/system/cpu: the kernel exposes no frequency governor here (a virtual machine, or a kernel without cpufreq)")
    else:
        out(f"CPUs with a governor: {len(plant.cpus)}; governor(s): {', '.join(plant.governors())}; driver: {plant.driver()}; "
            f"clock {plant.min_khz() / 1000:.0f} to {plant.top_khz() / 1000:.0f} MHz")
        if not plant.writable():
            why.append("the frequency ceiling (scaling_max_freq) is not writable: run as root on a machine whose driver allows it")
    if not plant.packages:
        why.append("no energy counter under /sys/class/powercap (RAPL): the processor's meter is not exposed here")
    elif not plant.meter_readable():
        why.append("the energy counter (energy_uj) is not readable: run as root")
    else:
        out(f"energy meter: {len(plant.packages)} package(s) under {plant.rapl_dir}")
    out(f"wall plug: {wall_spec or 'none (set WALL_METER=<spec> for the whole machine at the wall)'}")
    if why:
        for w in why:
            out("CANNOT RUN HERE: " + w)
        return 2
    out("this machine can run the benchmark")
    return 0


def run_arm(arm, wl_dir: Path, rep, steps, step_s, line_ms, seed, k, unit_rps, workers, plant: Plant, objective=DEFAULT_OBJECTIVE, wall_spec=None,
            sim_root=None):
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    svc = Service(steps, step_s, unit_rps, k, workers, seed, sim_root=sim_root)
    sampler = Sampler(plant, svc, wall_spec); sampler.start()
    omni = None
    if arm == "omni":
        master.refuse_if_off("cpu_power")
        snap_path = d / "snapshot.json"
        omni = Omni(plant, svc, d / "audit.jsonl", line_ms, objective, power=sampler.power)
        plant.attach(); snap_path.write_text(json.dumps({"root": str(plant.root), "snapshot": plant.snapshot}, indent=1))
        master.register("cpu_power", restore=[[sys.executable, str(ROOT / "tools" / "run_cpu_power.py"), "--restore", str(snap_path)]])
        omni.start()
    cpu0 = cpu_times(); t0 = time.time()
    svc.start(); svc.join()
    t1 = time.time(); cpu1 = cpu_times()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=30)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    seconds = t1 - t0
    with open(d / "requests.log", "w") as fh:
        for t, lat in svc.records:
            fh.write(f"{t:.3f} {lat * 1000:.3f}\n")
    rows = sampler.rows
    with open(d / "samples.jsonl", "w") as fh:
        for r in rows:
            fh.write(json.dumps({k2: (round(v, 3) if isinstance(v, float) else v) for k2, v in r.items()}) + "\n")
    lat_sorted = sorted(l * 1000.0 for _, l in svc.records); n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    energy = rows[-1]["energy_j"] if rows else float("nan")
    wall_rows = [r["wall_w"] for r in rows if r.get("wall_w") is not None]
    wall_j = sum(wall_rows) * DT if wall_rows and len(wall_rows) >= 0.9 * len(rows) else float("nan")
    total = cpu1[0] - cpu0[0]; idle = cpu1[1] - cpu0[1]
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "requests": n, "issued": svc.issued,
         "work_inside_line_rps": inside / seconds, "rps": n / seconds,
         "p95_ms": q(0.95), "p99_ms": q(0.99), "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "failed": svc.failed,
         "energy_j": energy, "power_w_mean": energy / seconds if seconds else float("nan"), "j_per_1k_inside": 1000.0 * energy / max(1, inside),
         "wall_j": wall_j, "ceiling_mhz_mean": (sum(r["ceiling_khz"] for r in rows) / len(rows) / 1000.0) if rows else float("nan"),
         "freq_mhz_mean": (sum(r["cur_khz"] for r in rows) / len(rows) / 1000.0) if rows else float("nan"),
         "cpu_busy_share": (total - idle) / max(1, total), "writes": (omni.writes if omni else 0),
         "handed_back": (omni.handed_back if omni else True), "foreign_writer": (omni.foreign if omni else False), "failups": (omni.failups if omni else 0),
         "switched_off": (omni.switched_off if omni else False), "verdict": (omni.verdict.record() if omni and omni.verdict else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    print(f"   {arm} rep {rep}: {n} requests, inside the line {g['work_inside_line_rps']:.0f}/s, p95 {g['p95_ms']:.2f} ms, energy {energy:.0f} J "
          f"({g['power_w_mean']:.1f} W), ceiling {g['ceiling_mhz_mean']:.0f} MHz, failed {g['failed']}, handed back {g['handed_back']}"
          + (f", verdict {g['verdict']['state']}" if g.get("verdict") else ""), flush=True)
    return g


def paired(reps, key, direction):
    """omni against native on one gauge over the repetitions: means, the mean paired difference, its 95% interval."""
    d = [r["omni"][key] - r["native"][key] for r in reps if _num(r["omni"].get(key)) and _num(r["native"].get(key))]
    if not d:
        return None
    n = len(d)
    nat = sum(r["native"][key] for r in reps if _num(r["native"].get(key))) / n
    om = sum(r["omni"][key] for r in reps if _num(r["omni"].get(key))) / n
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


def machine(plant: Plant):
    model = "?"
    try:
        for line in open("/proc/cpuinfo"):
            if line.startswith("model name"):
                model = line.split(":", 1)[1].strip(); break
    except OSError:
        pass
    return {"model": model, "cpus": len(plant.cpus), "governors": plant.governors(), "driver": plant.driver(),
            "top_mhz": plant.top_khz() / 1000.0, "min_mhz": plant.min_khz() / 1000.0, "kernel": os.uname().release, "modelled": isinstance(plant, SimPlant)}


def run_workload(name, out: Path, reps, step_s, line_ms, plant: Plant, objective=DEFAULT_OBJECTIVE, wall_spec=None, sim_root=None, workers=None):
    steps, tuning = WORKLOADS[name]
    wl_dir = out / f"cpu-power-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    workers = workers or len(plant.cpus) or os.cpu_count() or 2
    if sim_root:
        k, measured_ms = 0, SERVICE_MS
    else:
        plant.attach(); plant.write(plant.top_khz())                       # the work unit is calibrated at the top clock, once, then fixed
        k, measured_ms = calibrate(); plant.restore()
    capacity = workers * 1000.0 / measured_ms                             # requests a second the machine answers at the top clock
    unit = capacity * UTIL_AT_TOP_STEP / TOP_STEP
    notch, floor = grid(plant.top_khz(), plant.min_khz())
    print(f"== {name}: steps {steps} x {step_s} s, {unit:.1f} requests/s a step (step {TOP_STEP} = {UTIL_AT_TOP_STEP:.0%} of {capacity:.0f}/s), work unit "
          + (f"modelled, {measured_ms:.2f} ms" if sim_root else f"{k} passes = {measured_ms:.2f} ms") + f", {workers} workers; the ceiling's cover "
          f"{floor / 1000:.0f} to {plant.top_khz() / 1000:.0f} MHz by {notch / 1000:.0f} MHz; the verdict's objective {objective}", flush=True)
    rec = {"workload": name, "tuning": tuning, "steps": steps, "step_s": step_s, "line_ms": line_ms, "unit_rps": unit, "work_unit_passes": k,
           "service_ms_at_top": measured_ms, "workers": workers, "cover_khz": [floor, plant.top_khz()], "notch_khz": notch, "objective": objective,
           "wall_meter": bool(wall_spec), "machine": machine(plant), "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, steps, step_s, line_ms, 1000 + rep, k, unit, workers, plant, objective, wall_spec, sim_root)
        rec["reps"].append(r)
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    rec["paired"] = {k2: paired(rec["reps"], k2, dr) for k2, _, dr in GAUGES}
    (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    return rec


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.3g}"


def report(recs, out: Path):
    L = ["# CPU power: Omni-Compass on top of the Linux kernel's own frequency governor", "",
         "The machine as it runs is native: the kernel's frequency governor as shipped under the operator's ceiling (the top clock). "
         f"Omni is the compass law on the ceiling through the kernel's own interface inside [half the top, the top], holding the service's "
         f"own request latency at {CENTER:.0%} of the {LINE_MS:.0f} ms line, a notch given back only after a paired trial on the machine itself "
         "allowed it under the declared objective. The same requests in both arms. Energy is the processor's own meter (RAPL); the whole "
         "machine at the wall where a plug is fitted. Every row is reported, losses included.", ""]
    for rec in recs:
        m = rec.get("machine", {})
        L += [f"## {rec['workload']}: steps {rec['steps']} × {rec['step_s']} s" + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"{m.get('model', '?')}, {m.get('cpus', '?')} CPUs, governor {', '.join(m.get('governors', []))} ({m.get('driver', '?')}), kernel {m.get('kernel', '?')}"
              + (" — **a modelled machine, tests only**" if m.get("modelled") else "") + f"; {rec['unit_rps']:.1f} requests a second a step; the work unit "
              f"{rec['work_unit_passes']} passes = {rec['service_ms_at_top']:.2f} ms at the top clock; the cover {rec['cover_khz'][0] / 1000:.0f} to "
              f"{rec['cover_khz'][1] / 1000:.0f} MHz by {rec['notch_khz'] / 1000:.0f} MHz; {len(rec['reps'])} paired repetitions; engine "
              f"{rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"]); fw = any(r["omni"]["foreign_writer"] for r in rec["reps"])
        L += ["", f"Every omni arm handed the ceiling back to the operator's and read it back: {'yes' if hb else 'NO'}; another writer seen: "
              f"{'yes' if fw else 'no'}; fail-ups: {sum(r['omni']['failups'] for r in rec['reps'])}; the brain's verdict: "
              + "; ".join(f"rep {r['omni']['rep']}: {r['omni']['verdict']['state']}" for r in rec["reps"] if r["omni"].get("verdict")) + ".", ""]
    (out / "CPU_POWER.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "CPU_POWER.md"


def restore_from(path):
    """Put every CPU's ceiling back from a snapshot file (the watchdog's hand-back when Omni died)."""
    s = json.loads(Path(path).read_text())
    plant = Plant(s.get("root", "/")); plant.snapshot = s["snapshot"]
    ok = plant.restore()
    print(f"ceiling restored from {path}: {'yes' if ok else 'NO'}")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", action="store_true", help="say whether this machine can run the benchmark, and exit")
    ap.add_argument("--plant", default="real", help="real (the machine through /sys) or sim (a modelled machine in a directory, tests only)")
    ap.add_argument("--sim-dir", default="", help="where the modelled machine's files live (default: a fresh temporary directory)")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=60.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--workers", type=int, default=0, help="service workers (default: one per CPU)")
    ap.add_argument("--out", default="cpu-power-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a notch by: resource (energy, speed and work together, the index's reading for one machine), "
                         "per-work (energy per request inside the line, the line itself the guardrail) or service (speed and work alone)")
    ap.add_argument("--report-only", default="")
    ap.add_argument("--restore", default="", help="restore the ceiling from this snapshot file and exit")
    a = ap.parse_args(argv)
    if a.restore:
        return restore_from(a.restore)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("cpu-power-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    sim_root = None
    if a.plant == "sim":
        import tempfile
        sim_root = a.sim_dir or tempfile.mkdtemp(prefix="omni-cpu-sim-")
        plant = SimPlant(sim_root)
    else:
        plant = Plant("/")
    wall_spec = os.environ.get("WALL_METER") or None
    rc = probe(plant, wall_spec)
    if a.probe or rc:
        return rc
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.line_ms, plant, a.objective, wall_spec, sim_root, a.workers or None) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
