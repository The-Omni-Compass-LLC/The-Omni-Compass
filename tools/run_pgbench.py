# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of a database's own connection pooler (docs/POSTGRES_PREREGISTRATION.md).

PostgreSQL (the PostgreSQL Global Development Group) runs as the distribution ships it; PgBouncer (its own project) sits
in front of it in transaction pooling with the pool size it ships with, 20 server connections; pgbench (PostgreSQL's own
benchmark) offers the load. That is native: the pooler's fixed pool is the DBA's one setting, made once.

omni is the same database, the same pooler and the same load, with the compass law (omnicompass/compass_law.py) on
one knob: the pooler's pool size, written through its own admin console (SET default_pool_size), inside the cover
[2, 90]. The reading is the service time the pooler itself reports every second (transaction time plus the time clients
waited for a server, per transaction), or the share of its clients queued for a server scaled to the line, whichever is
worse (amendment 1), on a band from 0 to the response line. Past the wall the knob is handed back to
the pooler's own setting at once (fail up). At the end it is handed back and read back.

Load: pgbench at a fixed client count, rate-limited, the rate stepping one notch at a time (1 2 3 2 3 4 5 6 5 4 3 2 1 2
1) with the base rate set before the counted runs by one native-only run with no rate limit (the peak notch offers
native's own unlimited capacity). Both arms run the same steps, paired, the order alternating between repetitions.

Gauges (from pgbench's per-transaction log, PgBouncer's SHOW POOLS and the host's /proc/stat): work inside the
response line (transactions a second whose latency, lag included, was within the line), throughput, p50/p95/p99
latency, failed transactions, server connections alive (the "machines"), the host's CPU busy share and CPU-seconds.
There is no watt-meter on a GitHub runner: nothing here is an energy claim.

Usage:
  python tools/run_pgbench.py --setup                      # create the bench role and database (needs the postgres user)
  python tools/run_pgbench.py --workloads tpcb --reps 3 --out out
  python tools/run_pgbench.py --report-only all --out all  # re-read finished <workload>.json files and write PGBENCH.md
"""
from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, Plug, clamp  # noqa: E402
from tools.legal import stamp as _legal_stamp  # noqa: E402

# --- the frozen rule -----------------------------------------------------------------------------------------------
LINE_MS = 50.0            # the response line: a transaction answered within 50 ms, lag included
CENTER = 0.4              # the compass pulls the service to 40% of the line (the service profile of the Kubernetes adapter)
DT = 1.0                  # one decision a second
TAU = 2.0                 # the pool's response time: a slot added or removed shows in the reading within a couple of seconds
SMOOTH = 0.5
DEAD = 0.05               # a force inside the cushion moves nothing
UP = 0.10                 # adding: ceil(force / UP) slots a second (full force adds ten); taking back: one idle server a second
PEAK = 0.9                # the peak notch offers nine tenths of native's unlimited capacity: native at its knee, not past it
DWELL_S = 5.0             # after adding, no taking back within five seconds (no hunting); adding is never held (amendment 1)
FLOOR, CEILING = 2, 90    # the cover: never under two server connections; never within ten of PostgreSQL's 100 connections
NATIVE_POOL = 20          # PgBouncer's shipped default_pool_size: native's setting and Omni's snapshot
WAIT_SHARE = 0.5          # where the time goes decides the direction: waiting for a server (add one) or inside it (take one)


def service_reading(latency_s, waiting_share, line_s=LINE_MS / 1000.0):
    """The reading the compass sees (amendment 1, docs/POSTGRES_PREREGISTRATION.md): the pooler's service time per
    transaction, or the share of its clients queued for a server scaled to the line, whichever is worse. A pool too small
    for the offered rate shows at the pooler as clients waiting, not as a long transaction: its own clock cannot see the
    backlog that piles up in the clients' schedules, and the first untouched run proved it."""
    return max(latency_s, waiting_share * line_s)

STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
WORKLOADS = {             # name: (pgbench script flag, scale factor)
    "tpcb": ("", 20),             # the tuning workload: pgbench's TPC-B-like default script, 20 branches
    "select": ("-S", 20),         # untouched: select-only, read-heavy
    "simple_update": ("-N", 20),  # untouched: the default script without the branch and teller updates
    "tpcb_hot": ("", 2),          # untouched: two branches, every transaction fights for the same rows
}
GAUGES = [  # key, label, direction
    ("work_inside_line_tps", "work inside the response line (transactions a second answered within the line)", "higher"),
    ("tps", "throughput (transactions a second)", "higher"),
    ("p95_ms", "latency, 95th percentile (ms, lag included)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("p50_ms", "latency, median (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed transactions", "never more"),
    ("servers_alive_mean", "server connections alive, mean (the machines)", "lower"),
    ("servers_alive_max", "server connections alive, most at once", "lower"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "lower"),
    ("cpu_seconds", "host CPU-seconds", "lower"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 transactions inside the line", "lower"),
    ("pool_mean", "pool size, mean (the knob)", "shown"),
]
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262}
SAME_REL = 1e-6


# --- pure pieces (tested without a database) -----------------------------------------------------------------------
def decide(p, force, wait_share, idle, cur, snapshot, last_dir, since_change_s, wall=0.95):
    """The pool size the brain wants this second, by the frozen rule. Returns (target, direction, reason)."""
    if p >= wall:
        return snapshot, 0, "fail up: handed back to the pooler's own setting"
    if force > DEAD:
        d = math.ceil(force / UP) if wait_share >= WAIT_SHARE else -1
        why = f"slow, clients waiting for a server: {d} more" if d > 0 else "slow inside the server: one fewer"
    elif force < -DEAD:
        if idle < 1:
            return cur, 0, "calm, but no idle server to give back"
        d, why = -1, "calm, an idle server given back"
    else:
        return cur, 0, "inside the cushion"
    sign = 1 if d > 0 else -1
    if sign < 0 and last_dir > 0 and since_change_s < DWELL_S:
        return cur, 0, "dwell: no taking back within five seconds of adding"   # gas is never held; only the brake dwells (amendment 1)
    target = int(clamp(cur + d, FLOOR, CEILING))
    if target == cur:
        return cur, 0, "at the cover"
    return target, sign, why


def parse_latencies(files):
    """Latencies (microseconds) from pgbench's per-transaction log files (-l): client transaction time script epoch us lag."""
    out = []
    for f in files:
        with open(f) as fh:
            for line in fh:
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        out.append(int(parts[2]))
                    except ValueError:
                        continue
    return out


def latency_gauges(lat_us, seconds, line_ms=LINE_MS):
    """The gauges one arm's transactions give over `seconds` of offered load."""
    n = len(lat_us)
    if n == 0:
        return {"transactions": 0, "tps": 0.0, "work_inside_line_tps": 0.0, "inside_line_share": 0.0,
                "p50_ms": float("nan"), "p95_ms": float("nan"), "p99_ms": float("nan"), "mean_ms": float("nan")}
    s = sorted(lat_us)
    q = lambda f: s[min(n - 1, int(math.ceil(f * n)) - 1)] / 1000.0  # noqa: E731
    inside = sum(1 for x in lat_us if x <= line_ms * 1000)
    return {"transactions": n, "tps": n / seconds, "work_inside_line_tps": inside / seconds,
            "inside_line_share": inside / n, "p50_ms": q(0.5), "p95_ms": q(0.95), "p99_ms": q(0.99),
            "mean_ms": sum(lat_us) / n / 1000.0}


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
        reading = "**WORSE**"                                     # any increase, in any repetition, whatever the noise
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


# --- the wires -----------------------------------------------------------------------------------------------------
class Bouncer:
    """PgBouncer as a child process with its own ini, admin console through psql."""

    def __init__(self, workdir: Path, port: int, pg: str, dbname: str, user: str, password: str):
        self.dir, self.port, self.user = workdir, port, user
        self.dir.mkdir(parents=True, exist_ok=True)
        self.as_postgres = os.geteuid() == 0           # PgBouncer refuses to run as root
        if self.as_postgres:
            os.chmod(self.dir, 0o777)
        (self.dir / "userlist.txt").write_text(f'"{user}" "{password}"\n')
        self.ini = self.dir / "pgbouncer.ini"
        self.ini.write_text("\n".join([
            "[databases]", f"{dbname} = {pg} dbname={dbname} user={user} password={password}", "", "[pgbouncer]",
            "listen_addr = 127.0.0.1", f"listen_port = {port}", f"unix_socket_dir = {self.dir}", "auth_type = trust",
            f"auth_file = {self.dir / 'userlist.txt'}", f"admin_users = {user}", "pool_mode = transaction",
            f"default_pool_size = {NATIVE_POOL}", "max_client_conn = 1000", f"logfile = {self.dir / 'pgbouncer.log'}",
            f"pidfile = {self.dir / 'pgbouncer.pid'}", ""]))
        self.proc = None

    def start(self):
        cmd = ["pgbouncer", "-d", str(self.ini)]
        if self.as_postgres:
            cmd = ["runuser", "-u", "postgres", "--"] + cmd
        subprocess.run(cmd, check=True)
        for _ in range(50):
            time.sleep(0.1)
            if self.admin("SHOW VERSION", quiet=True) is not None:
                return
        raise RuntimeError("PgBouncer did not come up")

    def admin(self, sql, quiet=False):
        r = subprocess.run(["psql", "-h", "127.0.0.1", "-p", str(self.port), "-U", self.user, "pgbouncer", "--csv", "-c", sql],
                           capture_output=True, text=True, env={**os.environ, "PGPASSWORD": "x", "PGCONNECT_TIMEOUT": "3"})
        if r.returncode != 0:
            if not quiet:
                sys.stderr.write(r.stderr)
            return None
        return r.stdout

    def rows(self, sql):
        out = self.admin(sql)
        if not out:
            return []
        lines = [l for l in out.splitlines() if l.strip()]
        head = lines[0].split(",")
        return [dict(zip(head, l.split(","))) for l in lines[1:]]

    def pool_size(self):
        for r in self.rows("SHOW CONFIG"):
            if r.get("key") == "default_pool_size":
                return int(r["value"])
        raise RuntimeError("SHOW CONFIG gave no default_pool_size")

    def set_pool_size(self, n):
        self.admin(f"SET default_pool_size = {int(n)}")

    def pools(self, dbname):
        for r in self.rows("SHOW POOLS"):
            if r.get("database") == dbname:
                return {k: int(v) for k, v in r.items() if k.startswith(("cl_", "sv_", "maxwait"))}
        return {}

    def stats(self, dbname):
        for r in self.rows("SHOW STATS"):
            if r.get("database") == dbname:
                return {k: int(v) for k, v in r.items() if k.startswith("total_")}
        return {}

    def stop(self):
        self.admin("SHUTDOWN", quiet=True)
        pid = self.dir / "pgbouncer.pid"
        for _ in range(30):
            if not pid.exists():
                return
            time.sleep(0.1)


class PoolPlug(Plug):
    """One wire in (the pooler's own service time per transaction), one wire out (its pool size)."""

    def __init__(self, b: Bouncer, dbname: str, line_ms=LINE_MS):
        super().__init__(FLOOR, CEILING, tolerance=0.5)
        self.b, self.db, self.line_s = b, dbname, line_ms / 1000.0
        self.prev = None
        self.wait_share = 0.0
        self.waiting_share = 0.0
        self.last_latency_s = 0.0

    def _read_service(self):
        s = self.b.stats(self.db)
        p = self.b.pools(self.db)
        clients = p.get("cl_active", 0) + p.get("cl_waiting", 0)
        self.waiting_share = p.get("cl_waiting", 0) / clients if clients else 0.0   # clients queued for a server (amendment 1)
        if not s:
            return service_reading(self.last_latency_s, self.waiting_share, self.line_s)
        if self.prev is None:
            self.prev = s
            return service_reading(0.0, self.waiting_share, self.line_s)
        dx = s["total_xact_count"] - self.prev["total_xact_count"]
        dt = s["total_xact_time"] - self.prev["total_xact_time"]
        dw = s["total_wait_time"] - self.prev["total_wait_time"]
        self.prev = s
        if dx <= 0:
            self.wait_share, self.last_latency_s = self.waiting_share, 0.0       # nothing served: calm unless clients are queued
            return service_reading(0.0, self.waiting_share, self.line_s)
        self.wait_share = max(dw / (dt + dw) if (dt + dw) > 0 else 0.0, self.waiting_share)
        self.last_latency_s = (dt + dw) / dx / 1e6
        return service_reading(self.last_latency_s, self.waiting_share, self.line_s)

    def _read_lever(self):
        return float(self.b.pool_size())

    def _send(self, value):
        self.b.set_pool_size(int(round(value)))


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit."""

    def __init__(self, plug: PoolPlug, audit_path: Path, line_ms=LINE_MS):
        super().__init__(daemon=True)
        self.plug, self.audit = plug, audit_path
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event()
        self.last_dir, self.last_change = 0, -1e9
        self.writes, self.failups = 0, 0
        self.foreign, self.handed_back = False, False

    def run(self):
        snapshot = self.plug.attach()
        t0 = time.monotonic()
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    reading = self.plug.read()
                    f = self.law.force(reading)
                    idle = self.plug.b.pools(self.plug.db).get("sv_idle", 0)
                    cur = int(self.plug.lever())
                    target, d, why = decide(self.law.p, f, self.plug.wait_share, idle, cur, int(snapshot), self.last_dir,
                                            tick - self.last_change, wall=self.law.band.wall_high)
                    wrote = None
                    if target != cur:
                        wrote = self.plug.write(target)
                        self.writes += 1
                        if d:
                            self.last_dir, self.last_change = d, tick
                        else:
                            self.failups += 1
                            self.last_dir, self.last_change = 0, tick
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "latency_ms": round(self.plug.last_latency_s * 1000, 3),
                                         "waiting_share": round(self.plug.waiting_share, 3), "p": round(self.law.p, 4),
                                         "force": round(f, 4), "wait_share": round(self.plug.wait_share, 3), "idle": idle,
                                         "pool": cur, "target": target, "wrote": wrote, "why": why}) + "\n")
                except Exception as e:  # a foreign writer or a lost console: say so, stop writing
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """Server connections alive, once a second, in both arms."""

    def __init__(self, b: Bouncer, dbname: str):
        super().__init__(daemon=True)
        self.b, self.db, self.stop_flag, self.alive, self.pool = b, dbname, threading.Event(), [], []

    def run(self):
        while not self.stop_flag.is_set():
            p = self.b.pools(self.db)
            if p:
                self.alive.append(sum(p.get(k, 0) for k in ("sv_active", "sv_idle", "sv_used", "sv_tested", "sv_login")))
            try:
                self.pool.append(self.b.pool_size())
            except Exception:
                pass
            time.sleep(DT)


def cpu_times():
    """(busy, total) jiffies of the whole host from /proc/stat."""
    with open("/proc/stat") as fh:
        parts = fh.readline().split()
    v = [int(x) for x in parts[1:]]
    idle = v[3] + (v[4] if len(v) > 4 else 0)
    return sum(v) - idle, sum(v)


def pgbench(args, env, log=None):
    r = subprocess.run(["pgbench"] + args, capture_output=True, text=True, env=env)
    if log is not None:
        log.write_text(r.stdout + r.stderr)
    return r


def parse_summary(text):
    out = {"tps": None, "failed": 0}
    for line in text.splitlines():
        if line.startswith("tps = "):
            out["tps"] = float(line.split("=")[1].split("(")[0])
        if line.startswith("number of failed transactions:"):
            out["failed"] = int(line.split(":")[1].split("(")[0])
    return out


# --- one workload --------------------------------------------------------------------------------------------------
def run_arm(arm, b, wl_dir, rep, dbname, user, port, script, steps, step_s, base, clients, jobs, line_ms):
    d = wl_dir / f"rep-{rep}" / arm
    d.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PGPASSWORD": "x"}
    conn = ["-h", "127.0.0.1", "-p", str(port), "-U", user]
    assert b.pool_size() == NATIVE_POOL, "every arm starts from the pooler's own setting"
    # an uncounted warm-up at the base rate, both arms alike
    pgbench(conn + ["-c", str(clients), "-j", str(jobs), "-T", "5", "-R", f"{base:.1f}", "-n"] + script + [dbname], env)
    sampler = Sampler(b, dbname); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(PoolPlug(b, dbname, line_ms), d / "audit.jsonl", line_ms); omni.start()
    cpu0, t0 = cpu_times(), time.monotonic()
    lat, failed, per_step = [], 0, []
    for k, notch in enumerate(steps):
        rate = base * notch
        prefix = d / f"step-{k:02d}"
        r = pgbench(conn + ["-c", str(clients), "-j", str(jobs), "-T", str(step_s), "-R", f"{rate:.1f}", "-n", "-l",
                           f"--log-prefix={prefix}"] + script + [dbname], env, d / f"step-{k:02d}.txt")
        s = parse_summary(r.stdout)
        files = sorted(d.glob(f"step-{k:02d}.*[0-9]"))
        l = parse_latencies(files)
        g = latency_gauges(l, step_s, line_ms)
        per_step.append({"step": k, "notch": notch, "offered_tps": rate, **g, "failed": s["failed"], "exit": r.returncode})
        lat += l; failed += s["failed"]
        for f in files:
            f.unlink()                                             # the per-step gauges are kept; the raw log is large
    seconds = time.monotonic() - t0
    cpu1 = cpu_times()
    sampler.stop_flag.set(); sampler.join(timeout=5)
    g = latency_gauges(lat, step_s * len(steps), line_ms)
    g.update({"failed": failed, "seconds": seconds,
              "servers_alive_mean": sum(sampler.alive) / len(sampler.alive) if sampler.alive else float("nan"),
              "servers_alive_max": max(sampler.alive) if sampler.alive else float("nan"),
              "cpu_busy_share": (cpu1[0] - cpu0[0]) / max(1, cpu1[1] - cpu0[1]),
              "cpu_seconds": (cpu1[0] - cpu0[0]) / os.sysconf("SC_CLK_TCK"),
              "pool_mean": sum(sampler.pool) / len(sampler.pool) if sampler.pool else float("nan"),
              "pool_min": min(sampler.pool) if sampler.pool else None, "pool_max": max(sampler.pool) if sampler.pool else None,
              "steps": per_step})
    inside = g["work_inside_line_tps"] * step_s * len(steps)
    g["cpu_s_per_1k_inside"] = g["cpu_seconds"] / inside * 1000 if inside else float("nan")
    if omni is not None:
        omni.stop_flag.set(); omni.join(timeout=10)
        g.update({"writes": omni.writes, "fail_ups": omni.failups, "handed_back": bool(omni.handed_back),
                  "foreign_writer": omni.foreign, "pool_read_back": b.pool_size()})
    else:
        g.update({"writes": 0, "handed_back": True, "pool_read_back": b.pool_size()})
    if b.pool_size() != NATIVE_POOL:                             # belt and braces: the next arm starts native
        b.set_pool_size(NATIVE_POOL)
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    return g


def run_workload(name, out, pg, dbname, user, password, port, reps, steps, step_s, clients, jobs, calib_s, line_ms):
    script_flag, scale = WORKLOADS[name]
    script = [script_flag] if script_flag else []
    wl_dir = out / f"pgbench-{name}"
    wl_dir.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PGPASSWORD": password}
    direct = ["-h", pg_host(pg), "-p", pg_port(pg), "-U", user]
    r = pgbench(direct + ["-i", "-s", str(scale), "-q", dbname], env, wl_dir / "init.txt")
    if r.returncode != 0:
        raise SystemExit(f"pgbench -i failed: {r.stderr[-400:]}")
    b = Bouncer(wl_dir / "pgb", port, pg, dbname, user, password)
    b.start()
    try:
        snapshot = b.pool_size()
        assert snapshot == NATIVE_POOL
        # the base rate: native's own unlimited capacity, found once before the counted runs, over the peak notch
        cal = pgbench(["-h", "127.0.0.1", "-p", str(port), "-U", user, "-c", str(clients), "-j", str(jobs), "-T", str(calib_s), "-n"]
                      + script + [dbname], {**os.environ, "PGPASSWORD": "x"}, wl_dir / "calibration.txt")
        cap = parse_summary(cal.stdout)["tps"]
        if not cap:
            raise SystemExit(f"calibration gave no tps: {cal.stderr[-300:]}")
        base = PEAK * cap / max(steps)
        print(f"== {name}: native capacity {cap:.0f} tps unlimited; base rate {base:.0f} tps (peak notch {100 * PEAK:.0f}% of it); steps {steps}", flush=True)
        rec = {"workload": name, "script": script_flag or "tpcb (default)", "scale": scale, "line_ms": line_ms, "steps": steps,
               "step_s": step_s, "clients": clients, "jobs": jobs, "native_capacity_tps": cap, "base_tps": base,
               "snapshot_pool": snapshot, "cover": [FLOOR, CEILING], "center": CENTER, "engine": engine(), "reps": []}
        for rep in range(1, reps + 1):
            order = ["native", "omni"] if rep % 2 else ["omni", "native"]
            one = {"rep": rep, "order": order}
            for arm in order:
                one[arm] = run_arm(arm, b, wl_dir, rep, dbname, user, port, script, steps, step_s, base, clients, jobs, line_ms)
                print(f"== {name} rep {rep} {arm}: inside the line {one[arm]['work_inside_line_tps']:.0f} tps, p95 {one[arm]['p95_ms']:.1f} ms, "
                      f"servers {one[arm]['servers_alive_mean']:.1f}, pool {one[arm]['pool_mean']:.1f}, CPU {100 * one[arm]['cpu_busy_share']:.0f}%", flush=True)
            rec["reps"].append(one)
            (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
        rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
        return rec
    finally:
        b.stop()


def pg_host(pg):
    return dict(kv.split("=", 1) for kv in pg.split()).get("host", "127.0.0.1")


def pg_port(pg):
    return dict(kv.split("=", 1) for kv in pg.split()).get("port", "5432")


def engine():
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except Exception:
        sha = ""
    try:
        v = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], cwd=ROOT, capture_output=True, text=True)
        ver = v.stdout.strip().splitlines()[0] if v.stdout.strip() else "unknown"
    except Exception:
        ver = "unknown"
    return {"commit": sha, "version": ver}


# --- the report ----------------------------------------------------------------------------------------------------
def pct(r, key):
    if r is None:
        return "no value"
    nat, diff, lo, hi = r["native"], r["diff"], r["ci95"][0], r["ci95"][1]
    if key in ("failed",) or not nat:
        return f"{diff:+.3g} ({lo:+.3g} to {hi:+.3g})"
    return f"{100 * diff / abs(nat):+.1f}% ({100 * lo / abs(nat):+.1f} to {100 * hi / abs(nat):+.1f})"


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:.3g}" if abs(v) < 10 else f"{v:,.1f}" if abs(v) < 1000 else f"{v:,.0f}"


def report(recs, out: Path):
    L = ["# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)", "",
         "Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law "
         f"writing the pool size through PgBouncer's own console inside [{FLOOR}, {CEILING}], handed back at the end. The load is pgbench, "
         "rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses "
         "included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the "
         "noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed "
         "(`docs/POSTGRES_PREREGISTRATION.md`).", ""]
    for rec in recs:
        e = rec.get("engine", {})
        L += [f"## {rec['workload']} ({rec['script']}, scale {rec['scale']}): line {rec['line_ms']:.0f} ms, {len(rec['reps'])} paired repetitions", "",
              f"Native capacity, unlimited: {rec['native_capacity_tps']:,.0f} tps; base rate {rec['base_tps']:,.0f} tps; steps {rec['steps']} × {rec['step_s']} s; "
              f"{rec['clients']} clients. Engine {e.get('version', 'unknown')} at `{e.get('commit', '')[:12]}`.", "",
              "| Gauge | native | omni | change (95% interval) | reading |", "|---|---:|---:|---|---|"]
        for k, label, dr in GAUGES:
            r = (rec.get("paired") or {}).get(k)
            if r is None:
                continue
            L.append(f"| {label} | {fmt(r['native'])} | {fmt(r['omni'])} | {pct(r, k)} | {r['reading']} |")
        hb = all(x["omni"].get("handed_back") for x in rec["reps"])
        fw = any(x["omni"].get("foreign_writer") for x in rec["reps"])
        L += ["", f"The knob handed back and read back at the end of every omni arm: {'yes' if hb else '**NO**'}; "
              f"a foreign writer seen: {'**yes**' if fw else 'no'}; Omni's writes per arm: "
              + ", ".join(str(x["omni"].get("writes", 0)) for x in rec["reps"])
              + "; fail-ups per arm: " + ", ".join(str(x["omni"].get("fail_ups", 0)) for x in rec["reps"]) + ".", "",
              "Per repetition (inside the line tps / p95 ms / servers alive / pool mean):", ""]
        for x in rec["reps"]:
            n, o = x["native"], x["omni"]
            L.append(f"- rep {x['rep']} ({' then '.join(x['order'])}): native {n['work_inside_line_tps']:.0f} / {n['p95_ms']:.1f} / "
                     f"{n['servers_alive_mean']:.1f} / {n['pool_mean']:.1f}; omni {o['work_inside_line_tps']:.0f} / {o['p95_ms']:.1f} / "
                     f"{o['servers_alive_mean']:.1f} / {o['pool_mean']:.1f}")
        L.append("")
    (out / "PGBENCH.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def setup(pg, dbname, user, password):
    """The bench role and database, through the postgres superuser."""
    pre = ["runuser", "-u", "postgres", "--"] if os.geteuid() == 0 else ["sudo", "-u", "postgres"]
    sql = (f"DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='{user}') THEN CREATE ROLE {user} LOGIN PASSWORD '{password}'; "
           f"END IF; END $$;")
    subprocess.run(pre + ["psql", "-qc", sql], check=True)
    have = subprocess.run(pre + ["psql", "-tAc", f"SELECT 1 FROM pg_database WHERE datname='{dbname}'"], capture_output=True, text=True).stdout.strip()
    if have != "1":
        subprocess.run(pre + ["createdb", "-O", user, dbname], check=True)
    print(f"role {user} and database {dbname} ready")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workloads", default="tpcb")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--steps", default=STEPS)
    ap.add_argument("--step-s", type=int, default=20)
    ap.add_argument("--clients", type=int, default=64)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--calib-s", type=int, default=20)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--pg", default="host=127.0.0.1 port=5432")
    ap.add_argument("--dbname", default="bench")
    ap.add_argument("--user", default="bench")
    ap.add_argument("--password", default="bench")
    ap.add_argument("--port", type=int, default=6543, help="the port our PgBouncer listens on")
    ap.add_argument("--out", default="out")
    ap.add_argument("--report-only", default="")
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="a one-minute pass: short steps, one repetition")
    a = ap.parse_args(argv)
    if a.setup:
        setup(a.pg, a.dbname, a.user, a.password)
        return 0
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).glob("pgbench-*/*.json"))]
        recs = [r for r in recs if "reps" in r]
        for r in recs:
            r["paired"] = {k: paired(r["reps"], k, dr) for k, _, dr in GAUGES}
        report(recs, out)
        return 0
    for tool in ("pgbench", "psql", "pgbouncer"):
        if shutil.which(tool) is None:
            raise SystemExit(f"{tool} not found")
    steps = [int(x) for x in a.steps.split()]
    if a.smoke:
        a.reps, a.step_s, a.calib_s, steps = 1, 4, 4, [1, 2, 3, 2, 1]
    recs = []
    for name in a.workloads.split(","):
        if name not in WORKLOADS:
            raise SystemExit(f"unknown workload {name}; one of {sorted(WORKLOADS)}")
        recs.append(run_workload(name, out, a.pg, a.dbname, a.user, a.password, a.port, a.reps, steps, a.step_s, a.clients, a.jobs,
                                 a.calib_s, a.line_ms))
    report(recs, out)
    print(f"report: {out / 'PGBENCH.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
