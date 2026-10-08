#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of a database's operator-set cache size: YCSB on MongoDB (docs/YCSB_PREREGISTRATION.md).

MongoDB as its publisher ships it, with the one setting an operator sets once for its storage engine's cache: the WiredTiger
cache size. YCSB (Yahoo's Cloud Serving Benchmark, the published core workloads) asks for records drawn from a key space that
widens and narrows over the run, so the working set steps through the operator's cache and past it. The operator's fixed
cache is the native controller here.

  native  MongoDB at the operator's cache size (512 MB) for the whole run
  omni    the same MongoDB, with the compass law (omnicompass/compass_law.py) on one knob, the cache size, through the
          server's own console (setParameter wiredTigerEngineRuntimeConfig cache_size), inside the cover [256 MB, 2,048 MB]:
          the compass reads the server's own mean read latency over the last second (serverStatus opLatencies) on a band from
          0 to the response line and holds it at 40% of the line; slow reads with the cache full push the cache up (slow reads
          with room to spare are not the cache's to mend), calm gives memory back 64 MB a second when the cache is not evicting;
          at 95% of the line with the cache full a quarter of the cover is added at once (fail up); the cache size is handed
          back to the operator's at the end and read back; a size found at a value Omni did not write stops it writing

Gauges from YCSB's own per-operation records (every operation's latency, raw), the server's own serverStatus (the cache
configured, the bytes in it, pages read into it) and the host's /proc/stat (CPU seconds, the compass's own cost included).
Memory held is the resource; no energy is claimed beyond the host's CPU seconds. Every row is reported, losses included.

  python3 tools/run_ycsb.py --setup                        # fetch and check YCSB, point the server at the operator's cache
  python3 tools/run_ycsb.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_ycsb.py --report-only DIR              # re-read finished <workload>.json files and write YCSB.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402

URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017")
DB = "ycsb"
MB = 1024 * 1024
LINE_MS = 2.0             # the response line: an operation answered within 2 ms (a cache hit is inside; a read that misses the cache is slower)
CENTER = 0.4              # the compass holds the server's own read latency at 40% of the line
DT = 1.0                  # one decision a second
TAU = 2.0                 # memory given or taken shows in the misses within a couple of seconds
SMOOTH = 0.5
NATIVE_MB = 512           # the operator's cache
COVER_MB = (256, 2048)    # never under 256 MB (the server's own floor), never over 2 GB
STEP_MB = 64              # one notch of the knob
FAILUP_MB = 448           # past the wall: a quarter of the cover at once, and again the next second if still past it
DWELL_S = 5.0             # after growing, no taking back within five seconds; giving back is a notch a second
FULL = 0.9                # the cache counts as full when the bytes in it are 90% of its size or more
RATE = 3000               # operations a second offered by YCSB (-target), the same in both arms
THREADS = 32              # YCSB's client threads
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
RECORD_BYTES = 1000       # YCSB's default: 10 fields of 100 bytes
YCSB_VERSION = "0.17.0"
YCSB_URL = f"https://github.com/brianfrankcooper/YCSB/releases/download/{YCSB_VERSION}/ycsb-mongodb-binding-{YCSB_VERSION}.tar.gz"
YCSB_SHA256 = "6a054a706812269c80bfc6ed1e83457990c1c60b01f5083c873aaed05577e30d"   # recorded from the release before any run
YCSB_HOME = Path(os.environ.get("YCSB_HOME", str(Path.home() / f"ycsb-mongodb-binding-{YCSB_VERSION}")))
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}
SAME_REL = 1e-6

WORKLOADS = {
    # name: (YCSB core workload file, base record count (keys at notch 1), steps, tuning?)
    #   250,000 records of 1 KB are about 275 MB in the cache at notch 1; notch 6 is about 1.6 GB, past the operator's 512 MB
    "tuning": ("workloada", 250_000, STEPS, True),      # 50/50 read/update, zipfian: the rules were set here
    "b": ("workloadb", 250_000, STEPS, False),          # 95/5 read/update, zipfian
    "c": ("workloadc", 250_000, STEPS, False),          # 100% read, zipfian
    "f": ("workloadf", 250_000, STEPS, False),          # read-modify-write, zipfian
    "burst": ("workloadb", 250_000, BURST, False),      # 95/5, the burst schedule
}

GAUGES = [  # key, label, direction
    ("work_inside_line_ops", "work inside the response line (operations a second answered within the line)", "higher"),
    ("ops", "throughput (operations a second)", "higher"),
    ("p95_ms", "latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed operations", "never more"),
    ("cache_mb_mean", "cache size held, mean (MB; the knob, the resource)", "lower"),
    ("cache_used_mb_mean", "bytes in the cache, mean (MB)", "lower"),
    ("pages_read", "pages read into the cache (misses)", "shown"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "lower"),
    ("cpu_seconds", "host CPU-seconds", "lower"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 operations inside the line", "lower"),
    ("writes", "cache size changes written (the knob's moves)", "shown"),
]


class CacheSize:
    """The plug on the server's cache size: read once before the first write, write through the server's own console, read
    back, yield to any other writer, restore."""

    def __init__(self, client):
        self.c, self.snapshot, self.last_written = client, None, None

    def _status(self):
        return self.c.admin.command("serverStatus")

    def configured_mb(self, st=None):
        st = st or self._status()
        return int(st["wiredTiger"]["cache"]["maximum bytes configured"]) // MB

    def attach(self):
        self.snapshot = self.configured_mb(); self.last_written = self.snapshot
        return self.snapshot

    def lever(self, st=None):
        cur = self.configured_mb(st)
        if self.last_written is not None and cur != self.last_written:
            raise RuntimeError(f"another writer set the cache to {cur} MB (we wrote {self.last_written}): Omni stops writing")
        return cur

    def write(self, mb):
        self.c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={int(mb)}M"})
        back = self.configured_mb(); self.last_written = back
        return back

    def restore(self):
        try:
            self.c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={int(self.snapshot)}M"})
            return self.configured_mb() == self.snapshot
        except Exception:
            return False


def cache_stats(st):
    """(configured MB, bytes in cache MB, pages read into cache, pages evicted) from one serverStatus."""
    c = st["wiredTiger"]["cache"]
    evicted = sum(int(c.get(k, 0)) for k in ("unmodified pages evicted", "modified pages evicted", "pages evicted by application threads"))
    return int(c["maximum bytes configured"]) // MB, int(c["bytes currently in the cache"]) / MB, int(c.get("pages read into cache", 0)), evicted


def read_latency(st):
    """(total read latency in microseconds, read operations) from one serverStatus (opLatencies)."""
    r = st["opLatencies"]["reads"]
    return int(r["latency"]), int(r["ops"])


def decide(p, force, evicted_last_s, cur_mb, last_change_age, full, wall=0.95):
    """The knob's move this second, in MB: slow reads (the service slow) grow the cache by ceil(force / 0.1) notches, but only
    while the cache is full (a slow read with room to spare is not the cache's to mend); calm with the cache not evicting gives
    back one notch after the dwell; past the wall, with the cache full, a quarter of the cover at once."""
    lo, hi = COVER_MB
    if p is not None and p >= wall and full:
        return min(hi, cur_mb + FAILUP_MB), "fail up: the line is at hand and the cache is full, a quarter of the cover at once"
    if force > 0.05:
        if not full:
            return cur_mb, "slow with room to spare: not the cache's to mend"
        return min(hi, cur_mb + STEP_MB * max(1, math.ceil(force / 0.1))), "slow with the cache full: grow"
    if force < -0.05 and evicted_last_s == 0 and cur_mb > lo and last_change_age >= DWELL_S:
        return max(lo, cur_mb - STEP_MB), "calm, nothing evicted: a notch given back"
    return cur_mb, "hold"


class Omni(threading.Thread):
    """The brain, one decision a second, reading the server's own read latency, writing the audit; the knob is handed back at
    the end and read back."""

    def __init__(self, plug: CacheSize, audit_path: Path, line_ms=LINE_MS):
        super().__init__(daemon=True)
        self.plug, self.audit = plug, audit_path
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.writes = 0; self.failups = 0
        self.foreign = False; self.handed_back = False

    def run(self):
        self.plug.attach(); st = self.plug._status(); lat0, ops0 = read_latency(st); _, _, _, ev0 = cache_stats(st); t0 = time.monotonic()
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    st = self.plug._status()
                    lat, ops = read_latency(st); dl, do = lat - lat0, ops - ops0; lat0, ops0 = lat, ops
                    reading = (dl / do / 1e6) if do > 0 else 0.0           # the mean read latency of the last second, in seconds; no reads reads calm
                    f = self.law.force(reading)
                    cur, used, _, ev = cache_stats(st); ev_last = ev - ev0; ev0 = ev
                    cur = self.plug.lever(st); full = used >= FULL * cur
                    target, why = decide(self.law.p, f, ev_last, cur, tick - self.last_change, full, wall=self.law.band.wall_high)
                    wrote = None
                    if target != cur:
                        wrote = self.plug.write(target); self.writes += 1
                        if target > cur:
                            self.last_change = tick
                        if why.startswith("fail up"):
                            self.failups += 1
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "reads": do, "p": round(self.law.p, 4), "force": round(f, 4),
                                         "evicted_last_s": ev_last, "cache_mb": cur, "used_mb": round(used, 1), "full": full, "target_mb": target, "wrote_mb": wrote, "why": why}) + "\n")
                except Exception as e:
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """The cache configured, the bytes in it and the pages read into it, once a second, in both arms."""

    def __init__(self, client):
        super().__init__(daemon=True)
        self.c, self.stop_flag, self.rows = client, threading.Event(), []

    def run(self):
        while not self.stop_flag.is_set():
            try:
                self.rows.append(cache_stats(self.c.admin.command("serverStatus")))
            except Exception:
                pass
            time.sleep(DT)


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    return sum(vals), vals[3] + vals[4]


def parse_raw(path: Path):
    """YCSB's raw measurements: one line per operation, 'op, timestamp(ms), latency(us)'; returns [(t_s, latency_ms)]."""
    out = []
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        parts = [x.strip() for x in line.split(",")]
        if len(parts) < 3 or not parts[2].lstrip("-").isdigit():
            continue
        try:
            out.append((float(parts[1]) / 1000.0, float(parts[2]) / 1000.0))
        except ValueError:
            continue
    return out


def parse_failed(summary_text):
    """Failed operations from YCSB's summary: every '[<OP>-FAILED], Operations, n' line."""
    n = 0
    for line in summary_text.splitlines():
        p = [x.strip() for x in line.split(",")]
        if len(p) >= 3 and p[0].endswith("-FAILED]") and p[1] == "Operations":
            try:
                n += int(p[2])
            except ValueError:
                pass
    return n


def ycsb(cmd, workload_file, props, out_file: Path):
    """One YCSB invocation (load or run) with raw per-operation measurements written to out_file; returns its summary text."""
    args = ["bash", str(YCSB_HOME / "bin" / "ycsb.sh"), cmd, "mongodb", "-s", "-P", str(YCSB_HOME / "workloads" / workload_file),
            "-p", f"mongodb.url={URL}/{DB}?w=1", "-p", "measurementtype=raw", "-p", f"measurement.raw.output_file={out_file}"]
    for k, v in props.items():
        args += ["-p", f"{k}={v}"]
    r = subprocess.run(args, capture_output=True, text=True, cwd=str(YCSB_HOME))
    return r.stdout + "\n" + r.stderr


def load_dataset(workload_file, records, log: Path):
    """The dataset for a workload, loaded once per workload (both arms read the same records); the collection is dropped first."""
    import pymongo
    c = pymongo.MongoClient(URL); c.drop_database(DB); c.close()
    txt = ycsb("load", workload_file, {"recordcount": records, "threads": THREADS, "insertorder": "ordered"}, log.with_suffix(".raw"))
    log.write_text(txt)
    if "[OVERALL]" not in txt:
        raise RuntimeError(f"YCSB load failed: {txt[-2000:]}")


def fresh_server(cache_mb):
    """The cache emptied and the operator's size restored before an arm, both arms alike: the server restarted at the
    operator's configured size, the OS page cache dropped."""
    subprocess.run(["sudo", "systemctl", "restart", "mongod"], check=True)
    subprocess.run(["sudo", "sh", "-c", "sync; echo 3 > /proc/sys/vm/drop_caches"], check=False)
    import pymongo
    for _ in range(60):
        try:
            c = pymongo.MongoClient(URL, serverSelectionTimeoutMS=2000); st = c.admin.command("serverStatus")
            got = int(st["wiredTiger"]["cache"]["maximum bytes configured"]) // MB
            if got != cache_mb:
                c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={cache_mb}M"})
            return c
        except Exception:
            time.sleep(1)
    raise RuntimeError("mongod did not come back after the restart")


def run_arm(arm, wl_dir: Path, rep, workload_file, base, steps, step_s, line_ms, seed):
    import pymongo
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    c = fresh_server(NATIVE_MB)
    sampler = Sampler(pymongo.MongoClient(URL)); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(CacheSize(pymongo.MongoClient(URL)), d / "audit.jsonl", line_ms); omni.start()
    records, failed, summaries = [], 0, []
    cpu0 = cpu_times(); t0 = time.time()
    for i, notch in enumerate(int(s) for s in steps.split()):
        raw = d / f"notch-{i + 1}.raw"
        # the notch's key space: the first base x notch records of the loaded dataset, YCSB's own distribution over them
        txt = ycsb("run", workload_file, {"recordcount": base * notch, "operationcount": 10 ** 9, "maxexecutiontime": int(step_s), "target": RATE,
                                          "threads": THREADS, "insertstart": 0, "seed": seed * 100 + i}, raw)
        summaries.append(txt); failed += parse_failed(txt); records += parse_raw(raw)
    t1 = time.time(); cpu1 = cpu_times()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=30)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    (d / "ycsb.log").write_text("\n\n".join(summaries))
    seconds = t1 - t0
    lat_sorted = sorted(l for _, l in records); n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    rows = sampler.rows or [(NATIVE_MB, 0.0, 0, 0)]
    total = cpu1[0] - cpu0[0]; idle = cpu1[1] - cpu0[1]; cpu_s = (total - idle) / os.sysconf("SC_CLK_TCK")
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "operations": n,
         "work_inside_line_ops": inside / seconds, "ops": n / seconds, "p95_ms": q(0.95), "p99_ms": q(0.99),
         "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "failed": failed,
         "cache_mb_mean": sum(x[0] for x in rows) / len(rows), "cache_used_mb_mean": sum(x[1] for x in rows) / len(rows),
         "pages_read": rows[-1][2] - rows[0][2], "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s,
         "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside), "writes": (omni.writes if omni else 0),
         "handed_back": (omni.handed_back if omni else True), "foreign_writer": (omni.foreign if omni else False), "failups": (omni.failups if omni else 0)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    print(f"   {arm} rep {rep}: {n} operations, inside the line {g['work_inside_line_ops']:.0f}/s, p95 {g['p95_ms']:.2f} ms, cache {g['cache_mb_mean']:.0f} MB, "
          f"in cache {g['cache_used_mb_mean']:.0f} MB, pages read {g['pages_read']:,}, CPU {cpu_s:.1f} s, handed back {g['handed_back']}", flush=True)
    return g


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


def server_version():
    try:
        import pymongo
        return pymongo.MongoClient(URL).server_info().get("version", "?")
    except Exception:
        return "?"


def run_workload(name, out: Path, reps, step_s, line_ms):
    workload_file, base, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"ycsb-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    ver = server_version()
    top = max(int(s) for s in steps.split())
    print(f"== {name}: YCSB {workload_file}, {base:,} records x notch (loaded to notch {top}: {base * top:,}), steps {steps}, {step_s} s a notch, MongoDB {ver}", flush=True)
    fresh_server(NATIVE_MB)
    load_dataset(workload_file, base * top, wl_dir / "load.log")
    rec = {"workload": name, "tuning": tuning, "ycsb_workload": workload_file, "base_records": base, "steps": steps, "step_s": step_s,
           "line_ms": line_ms, "rate_ops": RATE, "threads": THREADS, "record_bytes": RECORD_BYTES, "native_mb": NATIVE_MB, "cover_mb": list(COVER_MB),
           "mongodb_version": ver, "ycsb_version": YCSB_VERSION, "ycsb_sha256": YCSB_SHA256, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, workload_file, base, steps, step_s, line_ms, seed=1000 + rep)
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
    L = ["# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size", "",
         f"MongoDB as shipped with the operator's WiredTiger cache ({NATIVE_MB} MB) is native; omni is the compass law on the cache size "
         f"through the server's own console inside [{COVER_MB[0]}, {COVER_MB[1]}] MB, holding the server's own read latency at {CENTER:.0%} of "
         f"the {LINE_MS:.0f} ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the "
         "cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, "
         "losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: YCSB {rec['ycsb_workload']}, {rec['base_records']:,} records × notch, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"MongoDB {rec['mongodb_version']}, YCSB {rec['ycsb_version']}; {rec['rate_ops']:,} operations a second offered from {rec['threads']} threads; "
              f"{len(rec['reps'])} paired repetitions; engine {rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"]); fw = any(r["omni"]["foreign_writer"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to the operator's cache size: {'yes' if hb else 'NO'}; another writer seen: {'yes' if fw else 'no'}; "
              f"fail-ups: {sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "YCSB.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "YCSB.md"


def setup():
    """YCSB fetched from the project's release and checked against the SHA-256 recorded before any run; the server pointed at
    the operator's cache (its configuration file) and restarted. MongoDB itself is installed by the workflow from its publisher's
    repository, signed by the publisher's key."""
    tgz = YCSB_HOME.parent / f"ycsb-mongodb-binding-{YCSB_VERSION}.tar.gz"
    if not tgz.exists():
        urllib.request.urlretrieve(YCSB_URL, tgz)
    got = hashlib.sha256(tgz.read_bytes()).hexdigest()
    if got != YCSB_SHA256:
        print(f"YCSB checksum mismatch: {got} (expected {YCSB_SHA256})", file=sys.stderr); return 1
    if not YCSB_HOME.exists():
        subprocess.run(["tar", "xzf", str(tgz), "-C", str(YCSB_HOME.parent)], check=True)
    conf = Path("/etc/mongod.conf")
    if conf.exists():
        txt = conf.read_text()
        if "cacheSizeGB" not in txt:
            txt = txt.replace("storage:\n", f"storage:\n  wiredTiger:\n    engineConfig:\n      cacheSizeGB: {NATIVE_MB / 1024:.3f}\n", 1)
            subprocess.run(["sudo", "tee", str(conf)], input=txt, text=True, check=True, capture_output=True)
        subprocess.run(["sudo", "systemctl", "restart", "mongod"], check=True)
    print(f"YCSB {YCSB_VERSION} at {YCSB_HOME} (sha256 {got[:16]}...); MongoDB {server_version()} at the operator's {NATIVE_MB} MB cache")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--out", default="ycsb-out")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("ycsb-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.line_ms) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
