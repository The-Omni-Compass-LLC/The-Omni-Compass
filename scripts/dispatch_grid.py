#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The full grid, every square, filled to 1,000 runs: each of the six organisms at 1, 10, 100 and 1,000 copies clustered
on one clock, each size at 1, 10, 100 and 1,000 runs, native and Omni side by side (96 squares), twice: modelled
(six.yml) and with the real Kubernetes cluster inside (six-kube.yml). A square's runs are nested (its first 1, 10, 100 and
1,000 runs), so a size needs its 1,000 runs once.

The conductor (tick) starts the grid and keeps every runner GitHub gives this repository busy without flooding the queue:
it finds which runs of each square are already started (the dispatches named by their squares, plus the manifest of the
first night's runs), and starts the next ones (the 10-run squares of every size first, then 100, then 1,000) until the
repository's queued and running jobs reach what GitHub is running now plus a margin. grid.yml runs it every 15 minutes;
the six and six-kube buttons run it once when started with their defaults. Nothing is started twice: a started run is
read back from its own name.

Shards are cut from run times measured on the max (12 Oct, work waiting in line, GitHub's own machines) so that no job
nears GitHub's six-hour limit; each shard also stops starting runs at its deadline and hands in every run it finished.
Where a square cannot run on GitHub at all, it says where it runs instead (NOT_HERE).

  python3 scripts/dispatch_grid.py plan                 every square, how many of its runs are started, what is left
  python3 scripts/dispatch_grid.py tick [--dry]         start what fits now (GITHUB_TOKEN, or Claude Code's gh api)
  python3 scripts/dispatch_grid.py matrix ...           six.yml's shards for one dispatch (used by the workflow)
  python3 scripts/dispatch_grid.py kube-matrix ...      six-kube.yml's cells for one dispatch (used by the workflow)
"""
from __future__ import annotations

import argparse
import calendar
import contextlib
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "grid_v5" / "DISPATCHED.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "the-omni-compass-llc/the-omni-compass")
SINCE = "2026-10-12T06:00:00Z"     # the max's grid: runs started before belong to other engines or settings
ENGINE = "omni-v5"                 # the engine whose grid this is (tools/omni_version.py)
SIZES = (1, 10, 100, 1000)
RUNS = 1000                        # every square to 1,000 runs (the founder's order)
TIERS = (10, 100, 1000)            # the 10-run squares of every size first, then 100, then 1,000
MAX_JOBS = 250                     # GitHub: at most 256 jobs in one run's matrix (a few kept for the plan and the receipt)
ORGS = ["1", "2", "3", "4", "5", "6"]   # tools/run_scale.py: the four realms, the four stacked, the whole tower
KUBE = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
        "stack", "tower"]          # tools/run_kil.py names of the same six, in the same order (5 the four stacked, 6 the tower)
LOAD = "line"                      # the founder's order: work waiting in line in every organism (six.yml)

# Seconds per paired run (native then Omni on one seed), measured on the max with work waiting in line (12 Oct): 1 copy
# on GitHub's machines (the night's shards), 10 copies of every organism and 100 copies of the compute realm and the tower
# on a 4-core machine that runs as fast as GitHub's, and 1,000 copies of the compute realm stepped by the max (17.5 s a
# step, 6.8 GB); the other figures are scaled from those (a run grows 9 to 11 times per tenfold size) and the 1,000-copy
# shards are held at their first ten runs until those runs' own times are read back (CAP). CAL: the calibration run each
# worker makes once per organism (a native run on the calibration seed). MEM: a worker's peak memory (GB).
SEC = {1: {"1": 7.2, "2": 6.5, "3": 5.1, "4": 5.0, "5": 28.8, "6": 17.4},
       10: {"1": 77, "2": 95, "3": 79, "4": 67, "5": 359, "6": 250},
       100: {"1": 660, "2": 850, "3": 710, "4": 600, "5": 2820, "6": 1780},
       1000: {"1": 6100, "2": 8100, "3": 6750, "4": 5700, "5": 26700, "6": 16800}}
CAL = {1: {o: 2 for o in ORGS}, 10: {o: 15 for o in ORGS},
       100: {"1": 150, "2": 200, "3": 170, "4": 150, "5": 670, "6": 500},
       1000: {"1": 1650, "2": 2000, "3": 1700, "4": 1450, "5": 6800, "6": 4800}}
MEM = {1: {o: 0.2 for o in ORGS}, 10: {o: 0.4 for o in ORGS},
       100: {"1": 0.9, "2": 0.9, "3": 0.9, "4": 0.9, "5": 3.2, "6": 1.8},
       1000: {"1": 7.5, "2": 7.5, "3": 7.5, "4": 7.5, "5": 30.0, "6": 15.0}}
RUNNER_GB, RUNNER_CPUS = 14.0, 4   # GitHub's machine for a public repository: 4 cores, 16 GB (2 kept for the system)
JOB_S = 4 * 3600                   # a shard's planned work (a single run that needs more gets up to LONG_S)
LONG_S = 5 * 3600
DEADLINE_MIN = 320                 # run_scale starts no run that would end after this; the job is cut at 355 minutes
NOT_HERE = {("six", 1000, "5"): "joined from the four realms' runs on the same seeds (tools/pool_scale.py): its four "
                                "bodies share nothing on the clock, and whole it needs 32 GB, past a GitHub machine",
            ("six", 1000, "6"): "on a rented Azure machine (big-organism-detached, test scale): one run takes about 6 "
                                "hours and 15 GB, past a GitHub machine",
            ("kube", 1000, "tower"): "on a rented Azure machine (big-organism-detached): one repetition takes about 17 "
                                     "hours with the cluster inside",
            ("kube", 1000, "stack"): "on a rented Azure machine (big-organism-detached): one repetition takes about 22 "
                                     "hours and 32 GB with the cluster inside"}
# with the real cluster inside, the organism steps on the window's clock (240 steps), so the window must be long enough
# for the max's arm to make each step in time (tools/six_kube_report.py marks a repetition more than 5% late OFF THE
# CLOCK): seconds per arm by size, and by organism where the default is too short
KUBE_WINDOW = {1: 960, 10: 960, 100: 1440, 1000: 7200}
KUBE_WINDOW_ORG = {(100, "tower"): 2400, (100, "stack"): 3600}
KUBE_BUILD = {1: 1, 10: 1, 100: 8, 1000: 35}       # minutes to build the organism (calibration, plants, the max's bone)
KUBE_SPLIT = {1000}                # sizes whose two arms run on separate runners (together they pass six hours)
# a size whose runs past the first CAP are held until its first runs' times are read back (the 1,000-copy shards are
# cut from scaled figures; the first ten runs of each organism measure them before the rest are started)
CAP = {("six", 1000): 10, ("kube", 1000): 10}


# ------------------------------------------------------------------------------------------------- shard shapes
def shape(size, org):
    """(runs per shard, workers per runner) for a modelled square, or None where it cannot run on GitHub."""
    if ("six", size, org) in NOT_HERE:
        return None
    workers = max(1, min(RUNNER_CPUS, int(RUNNER_GB // MEM[size][org])))
    cal, sec = CAL[size][org], SEC[size][org]
    budget = JOB_S if cal + sec <= JOB_S else LONG_S
    per_worker = int((budget - cal) // sec)
    if per_worker < 1:
        return None
    return min(100, per_worker * workers), workers


def kube_minutes(size, org, split):
    """Planned minutes of one six-kube job: each arm builds a fresh cluster, builds the organism, warms up and runs its
    window."""
    win = KUBE_WINDOW_ORG.get((size, org), KUBE_WINDOW[size])
    arm = 6 + KUBE_BUILD[size] + 2 + win / 60.0 + 2
    return arm if split else 2 * arm


def matrix(scale, orgs, first, runs, per=None, workers=None):
    """six.yml's shards for one dispatch: each organism's runs first .. first+runs-1 cut into shards of its shape."""
    inc = []
    for o in orgs:
        sh = shape(scale, o)
        n = int((per or {}).get(o) or (sh[0] if sh else 1))
        w = int((workers or {}).get(o) or (sh[1] if sh else 1))
        for f in range(first, first + runs, n):
            inc.append({"org": o, "first": f, "n": min(n, first + runs - f), "w": w})
    return {"include": inc}


def kube_matrix(sizes, organisms, rep_first, reps, durations, split):
    cells = []
    for i, sz in enumerate(sizes):
        dur = durations[min(i, len(durations) - 1)]
        for o in organisms:
            for r in range(rep_first, rep_first + reps):
                for arm in (("native", "compass") if split else ("native compass",)):
                    cells.append({"organism": o, "size": sz, "rep": r, "duration": dur, "arms": arm,
                                  "tag": f"-{arm}" if split else ""})
    return cells


# ------------------------------------------------------------------------------------------------- what is started
SIX_NAME = re.compile(r"^six x(\d+) (\w+) orgs ([\d,]+) runs (\d+)\+(\d+)$")
KUBE_NAME = re.compile(r"^six-kube x(\d+) orgs ([\w,]+) reps (\d+)\+(\d+) arms ([\w ]+?) split (\w+) window (\d+)$")


def six_title(size, org, first, n):
    return f"six x{size} {LOAD} orgs {org} runs {first}+{n}"


def kube_title(size, orgs, r0, reps, split, window):
    return f"six-kube x{size} orgs {','.join(orgs)} reps {r0}+{reps} arms native compass split {'yes' if split else 'no'} window {window}"


def coverage(runs, manifest):
    """Which runs of each square are started (in flight or finished, not cancelled): {("six", size, org): set of run
    indices 0..999, ("kube", size, organism): set of repetitions 1..1000 with both arms}."""
    cov = {}
    add = lambda key, xs: cov.setdefault(key, set()).update(xs)
    for d in manifest.get("dispatches", []):
        if d.get("status") != "kept":
            continue
        if d["grid"] == "six" and d.get("load", "normal") == LOAD:
            for o in d["orgs"]:
                add(("six", d["size"], o), range(d["first"], d["first"] + d["runs"]))
        elif d["grid"] == "six-kube":
            for o in KUBE:
                add(("kube", d["size"], o), range(d["rep_first"], d["rep_first"] + d["reps"]))
    for r in runs:
        if r.get("conclusion") == "cancelled":
            continue
        t = r.get("display_title") or ""
        m = SIX_NAME.match(t)
        if m and m.group(2) == LOAD:
            size, first, n = int(m.group(1)), int(m.group(4)), int(m.group(5))
            for o in m.group(3).split(","):
                add(("six", size, o), range(first, first + n))
            continue
        m = KUBE_NAME.match(t)
        if m:
            size, r0, n = int(m.group(1)), int(m.group(3)), int(m.group(4))
            for o in m.group(2).split(","):
                add(("kube", size, o), range(r0, r0 + n))
    return cov


def gaps(have, lo, hi):
    """Runs lo..hi-1 not yet started, as (first, count) stretches."""
    out, i = [], lo
    while i < hi:
        if i in have:
            i += 1
            continue
        j = i
        while j < hi and j not in have:
            j += 1
        out.append((i, j - i))
        i = j
    return out


def next_dispatches(cov, caps=CAP):
    """Every dispatch still to start, in order: tier by tier (10, 100, 1,000 runs), small sizes first, modelled then
    with the cluster inside."""
    out, cov = [], {k: set(v) for k, v in cov.items()}      # what is planned here counts as started for the next tier
    for tier in TIERS:
        for size in SIZES:
            for o in ORGS:
                sh = shape(size, o)
                if sh is None:
                    continue
                hi = min(tier, caps.get(("six", size), RUNS))
                for f, n in gaps(cov.get(("six", size, o), set()), 0, hi):
                    step = sh[0] * MAX_JOBS
                    for f2 in range(f, f + n, step):
                        k = min(step, f + n - f2)
                        out.append({"grid": "six", "size": size, "orgs": [o], "first": f2, "runs": k,
                                    "jobs": math.ceil(k / sh[0]), "per": sh[0], "workers": sh[1],
                                    "hours": round(k * SEC[size][o] / sh[1] / 3600.0 + math.ceil(k / sh[0]) * CAL[size][o] / 3600.0, 1),
                                    "title": six_title(size, o, f2, k)})
                        cov.setdefault(("six", size, o), set()).update(range(f2, f2 + k))
            # with the cluster inside: organisms that share a window and the same runs still to start go in one dispatch
            split, hi = size in KUBE_SPLIT, min(tier, caps.get(("kube", size), RUNS)) + 1
            groups = {}
            for o in KUBE:
                if ("kube", size, o) in NOT_HERE:
                    continue
                win = KUBE_WINDOW_ORG.get((size, o), KUBE_WINDOW[size])
                groups.setdefault((win, tuple(gaps(cov.get(("kube", size, o), set()), 1, hi))), []).append(o)
            for (win, todo), orgs in groups.items():
                for r0, n in todo:
                    step = MAX_JOBS // (len(orgs) * (2 if split else 1))
                    for r in range(r0, r0 + n, step):
                        k = min(step, r0 + n - r)
                        jobs = k * len(orgs) * (2 if split else 1)
                        out.append({"grid": "six-kube", "size": size, "orgs": orgs, "rep_first": r, "reps": k,
                                    "split": split, "window": win, "jobs": jobs,
                                    "hours": round(jobs * kube_minutes(size, orgs[0], split) / 60.0, 1),
                                    "title": kube_title(size, orgs, r, k, split, win)})
                        for o in orgs:
                            cov.setdefault(("kube", size, o), set()).update(range(r, r + k))
    return out


# ------------------------------------------------------------------------------------------------- GitHub
def engine():
    """The engine of this checkout, by its fingerprint; a partial checkout without the engine's files reads it from git."""
    try:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", "HEAD"], cwd=ROOT,
                           capture_output=True, text=True, timeout=120)
        return r.stdout.split()[0] if r.stdout.strip() else "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def api(path, method="GET", data=None, tries=4):
    """GitHub's REST API with the workflow's token, or Claude Code's gh api where there is none; a server error or a
    dropped connection is tried again (2, 4 and 8 seconds apart)."""
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    for i in range(tries):
        try:
            if tok:
                req = urllib.request.Request(f"https://api.github.com/{path}", method=method,
                                             data=json.dumps(data).encode() if data is not None else None,
                                             headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                                                      "X-GitHub-Api-Version": "2022-11-28"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    body = r.read()
                return json.loads(body) if body else {}
            cmd = ["gh", "api", "-X", method, path] + (["--input", "-"] if data is not None else [])
            r = subprocess.run(cmd, input=json.dumps(data) if data is not None else None, capture_output=True, text=True)
            if r.returncode != 0:
                raise RuntimeError(f"gh api {path}: {r.stderr.strip()[:300]}")
            return json.loads(r.stdout) if r.stdout.strip() else {}
        except urllib.error.HTTPError as e:
            if e.code < 500 or i == tries - 1:
                raise
        except (urllib.error.URLError, TimeoutError, RuntimeError) as e:
            if i == tries - 1 or (isinstance(e, RuntimeError) and "HTTP 5" not in str(e) and "timeout" not in str(e).lower()):
                raise
        time.sleep(2 ** (i + 1))


def grid_runs():
    """Every run of six.yml and six-kube.yml started since the max's grid began."""
    out = []
    for wf in ("six.yml", "six-kube.yml"):
        page = 1
        while True:
            d = api(f"repos/{REPO}/actions/workflows/{wf}/runs?per_page=100&page={page}&created=>={SINCE}")
            out += d.get("workflow_runs", [])
            if len(d.get("workflow_runs", [])) < 100:
                break
            page += 1
    return out


def jobs_in_flight():
    """(queued, running) jobs across every workflow of the repository right now."""
    queued = running = 0
    for st in ("queued", "in_progress", "waiting", "pending", "requested"):
        d = api(f"repos/{REPO}/actions/runs?status={st}&per_page=100")
        for r in d.get("workflow_runs", []):
            page = 1
            while True:
                try:
                    j = api(f"repos/{REPO}/actions/runs/{r['id']}/jobs?filter=latest&per_page=100&page={page}")
                except (RuntimeError, urllib.error.URLError) as e:   # a run being cancelled can refuse its list
                    print(f"run {r['id']}: jobs not readable ({str(e)[:80]}); not counted", file=sys.stderr)
                    break
                for x in j.get("jobs", []):
                    queued += x["status"] in ("queued", "waiting", "pending", "requested")
                    running += x["status"] == "in_progress"
                if len(j.get("jobs", [])) < 100:
                    break
                page += 1
    return queued, running


def dispatch(d, ref):
    if d["grid"] == "six":
        o = d["orgs"][0]
        inputs = {"what": "runs", "scale": str(d["size"]), "orgs": ",".join(d["orgs"]), "first": str(d["first"]),
                  "runs": str(d["runs"]), "per_shard": json.dumps({o: d["per"]}), "workers": json.dumps({o: d["workers"]}),
                  "arm": "v5", "load": LOAD, "deadline_min": str(DEADLINE_MIN)}
        wf = "six.yml"
    else:
        inputs = {"what": "runs", "sizes": str(d["size"]), "organisms": ",".join(d["orgs"]), "reps": str(d["reps"]),
                  "rep_first": str(d["rep_first"]), "durations_s": str(d["window"]), "arms": "native compass",
                  "split": "yes" if d["split"] else "no"}
        wf = "six-kube.yml"
    api(f"repos/{REPO}/actions/workflows/{wf}/dispatches", method="POST", data={"ref": ref, "inputs": inputs})


# ------------------------------------------------------------------------------------------------- rented machines
# The squares too big for a GitHub machine run on rented Azure machines (big-organism-detached), each machine a batch of
# repetitions (runs, for the modelled tower) one after another: the machine asked for (the start job falls back through
# the sizes it may rent), machine-hours per repetition and list price (eastus, Linux, pay as you go), and the window that
# keeps the organism's clock with the cluster inside (the max steps the tower at 1,000 copies in about 33 s, the four
# stacked in about 60 s, on Azure's v7 machines). Machines are started up to the number the quota holds and never past
# the budget the founder set; the estimate of every machine started counts against it.
AZURE = {("kube", 1000, "tower"): {"test": "organism", "org": "tower", "per": 4, "window": 10800, "vm": "Standard_D8as_v7",
                                   "run_h": 8.5, "workers": 1, "cal_h": 0.0, "usd_h": 0.45},
         ("kube", 1000, "stack"): {"test": "organism", "org": "stack", "per": 3, "window": 19800, "vm": "Standard_E8as_v7",
                                   "run_h": 14.0, "workers": 1, "cal_h": 0.0, "usd_h": 0.52},
         ("six", 1000, "6"): {"test": "scale", "org": "6", "per": 24, "window": 0, "vm": "Standard_E8as_v7", "run_h": 3.6,
                              "workers": 3, "cal_h": 1.0, "usd_h": 0.52}}


def azure_hours(sq, reps):
    """A machine's hours for a batch: its calibration, then its repetitions, as many at once as it has workers."""
    a = AZURE[sq]
    return a["cal_h"] + math.ceil(reps / a["workers"]) * a["run_h"]
AZURE_NAME = re.compile(r"^big-organism-detached start (\w+) (\w+) x(\d+) reps (\d+)\+(\d+) window (\d+)$")
BUDGET_USD = 5000                  # the founder's figure for the big squares on rented machines (12 Oct)
AZURE_CAP = 10                     # repetitions per square started before the first ones' own times are read back


def azure_runs():
    d = api(f"repos/{REPO}/actions/workflows/big-organism-detached.yml/runs?per_page=100&created=>={SINCE}")
    return d.get("workflow_runs", [])


def azure_coverage(runs, manifest):
    """{square: set of repetitions (runs) started on a rented machine}, and the squares whose last start failed within
    two hours (no machine of that kind to be had right now: tried again later)."""
    cov, failing = {}, set()
    by = {(a["test"], a["org"]): k for k, a in AZURE.items()}
    for d in manifest.get("dispatches", []):
        if d["grid"] == "azure" and d.get("status") == "kept":
            cov.setdefault(tuple(d["square"]), set()).update(range(d["rep_first"], d["rep_first"] + d["reps"]))
    now = time.time()
    for r in runs:
        m = AZURE_NAME.match(r.get("display_title") or "")
        if not m or (m.group(1), m.group(2)) not in by:
            continue
        sq, r0, n = by[(m.group(1), m.group(2))], int(m.group(4)), int(m.group(5))
        if r.get("conclusion") in (None, "success"):        # rented, or being rented
            cov.setdefault(sq, set()).update(range(r0, r0 + n))
        elif r.get("conclusion") == "failure":
            t = calendar.timegm(time.strptime(r["created_at"], "%Y-%m-%dT%H:%M:%SZ"))
            if now - t < 2 * 3600:
                failing.add(sq)
    return cov, failing


def azure_spent(cov):
    """The estimated bill of every machine started: its hours at list price (whole batches of the square's size)."""
    tot = 0.0
    for k, v in cov.items():
        if k in AZURE and v:
            full, rest = divmod(len(v), AZURE[k]["per"])
            tot += (full * azure_hours(k, AZURE[k]["per"]) + (azure_hours(k, rest) if rest else 0.0)) * AZURE[k]["usd_h"]
    return tot


def azure_next(cov, cap=AZURE_CAP):
    """Machine batches still to start, tier by tier (10, 100, 1,000), the squares in turn within a tier, none past the
    cap until the first repetitions' own times are read back."""
    out, cov = [], {k: set(v) for k, v in cov.items()}
    for tier in sorted({min(t, cap or RUNS) for t in TIERS}):
        pending = True
        while pending:
            pending = False
            for sq, a in AZURE.items():
                lo = 0 if sq[0] == "six" else 1
                todo = gaps(cov.get(sq, set()), lo, lo + tier)
                if not todo:
                    continue
                r0, n = todo[0][0], min(a["per"], todo[0][1])
                out.append({"square": sq, "rep_first": r0, "reps": n, "usd": round(azure_hours(sq, n) * a["usd_h"], 2),
                            "title": f"big-organism-detached start {a['test']} {a['org']} x{sq[1]} reps {r0}+{n} window {a['window']}"})
                cov.setdefault(sq, set()).update(range(r0, r0 + n))
                pending = True
    return out


def azure_start(b, ref):
    a = AZURE[b["square"]]
    hours = azure_hours(b["square"], b["reps"])
    inputs = {"mode": "start", "test": a["test"], "organisms": a["org"], "size": str(b["square"][1]), "reps": str(b["reps"]),
              "rep_first": str(b["rep_first"]), "duration_s": str(a["window"]), "vm_size": a["vm"], "location": "eastus",
              "max_hours": str(int(hours * 1.3 + 6))}
    api(f"repos/{REPO}/actions/workflows/big-organism-detached.yml/dispatches", method="POST", data={"ref": ref, "inputs": inputs})


def squares(cov):
    """The 96 squares by organism and size: runs started of 1,000 (modelled; with the cluster inside)."""
    rows = []
    for size in SIZES:
        for o, k in zip(ORGS, KUBE):
            six = ("six", size, o)
            kube = ("kube", size, k)
            rows.append((size, o, len({x for x in cov.get(six, ()) if x < RUNS}), NOT_HERE.get(six),
                         len({x for x in cov.get(kube, ()) if 1 <= x <= RUNS}), NOT_HERE.get(kube)))
    return rows


def report(cov, started, queued, running, target, out=sys.stdout):
    names = {"1": "Compute / AI / Cloud", "2": "Physics / Robotics / Autonomous", "3": "Energy / Facility / Industrial",
             "4": "Distribution / Specialized", "5": "The four stacked", "6": "The whole tower"}
    print("| Size | Organism | Modelled: runs started of 1,000 | With the real cluster inside: runs started of 1,000 |", file=out)
    print("|---:|---|---|---|", file=out)
    for size, o, six, six_else, kube, kube_else in squares(cov):
        a = f"{six:,}" + (f" (the rest {six_else})" if six_else and six < RUNS else "")
        b = f"{kube:,}" + (f" (the rest {kube_else})" if kube_else and kube < RUNS else "")
        print(f"| {size:,} | {names[o]} | {a} | {b} |", file=out)
    print(f"\nJobs now: {running} running, {queued} queued; target {target}. Started this time: {len(started)} dispatches, "
          f"{sum(d['jobs'] for d in started)} jobs.", file=out)
    for d in started:
        print(f"- {d['title']} ({d['jobs']} jobs, about {d['hours']} runner-hours)", file=out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="what", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--offline", action="store_true", help="from the manifest alone (no GitHub calls)")
    t = sub.add_parser("tick")
    t.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "main"))
    t.add_argument("--dry", action="store_true", help="say what would start; start nothing")
    t.add_argument("--extra", type=int, default=60, help="jobs kept queued beyond what GitHub is running")
    t.add_argument("--floor", type=int, default=150, help="the least jobs kept in flight")
    t.add_argument("--max-dispatches", type=int, default=40)
    t.add_argument("--grid", choices=("six", "six-kube", "all"), default="all", help="which grid to start (the buttons: their own)")
    m = sub.add_parser("matrix")
    m.add_argument("--scale", type=int, required=True); m.add_argument("--orgs", required=True)
    m.add_argument("--first", type=int, default=0); m.add_argument("--runs", type=int, default=RUNS)
    m.add_argument("--per-shard", default=""); m.add_argument("--workers", default="")
    k = sub.add_parser("kube-matrix")
    k.add_argument("--sizes", required=True); k.add_argument("--organisms", default=",".join(KUBE))
    k.add_argument("--reps", required=True); k.add_argument("--rep-first", type=int, default=1)
    k.add_argument("--durations", required=True); k.add_argument("--split", default="no")
    z = sub.add_parser("azure-tick", help="the biggest squares on rented machines, within the quota and the budget")
    z.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "main"))
    z.add_argument("--machines-now", type=int, required=True, help="rented machines standing now (az group list)")
    z.add_argument("--max-machines", type=int, default=6, help="machines the quota holds at once")
    z.add_argument("--budget", type=float, default=BUDGET_USD)
    z.add_argument("--dry", action="store_true")
    a = ap.parse_args(argv)

    if a.what == "azure-tick":
        manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"dispatches": []}
        zr = azure_runs()
        cov, failing = azure_coverage(zr, manifest)
        spent, started, why = azure_spent(cov), [], "every batch is started"
        # a start still waiting for a runner has no machine yet: it counts as one, so the quota is never asked twice
        waiting = sum(1 for r in zr if r.get("status") in ("queued", "waiting", "pending", "requested")
                      and AZURE_NAME.match(r.get("display_title") or ""))
        if engine() != ENGINE:
            why = f"this checkout is not {ENGINE}"
        else:
            now = a.machines_now + waiting
            for b in azure_next(cov):
                if b["square"] in failing:
                    continue
                if now >= a.max_machines:
                    why = f"the quota's {a.max_machines} machines are all running"; break
                if spent + b["usd"] > a.budget:
                    why = f"the budget: ${spent:,.0f} of ${a.budget:,.0f} committed, the next machine would pass it"; break
                if not a.dry:
                    azure_start(b, a.ref); time.sleep(3)
                started.append(b); spent += b["usd"]; now += 1
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        with (open(summary, "a") if summary else contextlib.nullcontext(sys.stdout)) as out:
            print("## The biggest squares on rented machines" + (" (dry run)" if a.dry else ""), file=out)
            print("", file=out)
            for sq, al in AZURE.items():
                n = len({x for x in cov.get(sq, ()) if (x >= 1 if sq[0] == "kube" else x >= 0)})
                print(f"- {'with the cluster inside' if sq[0] == 'kube' else 'modelled'}, {al['org']} at {sq[1]:,} copies: "
                      f"{n:,} of 1,000 started" + (" (its last start found no machine; tried again later)" if sq in failing else ""), file=out)
            print(f"\nStarted now: {len(started)} machines; estimated bill of every machine started ${spent:,.0f} of the "
                  f"${a.budget:,.0f} budget; stopped because {why}.", file=out)
            for b in started:
                print(f"- {b['title']} (about ${b['usd']:,.0f})", file=out)
        for b in started:
            print(f"started: {b['title']} (about ${b['usd']:,.0f})")
        print(f"estimated bill committed ${spent:,.0f} of ${a.budget:,.0f}; {why}")
        return 0

    if a.what == "matrix":
        js = lambda s: json.loads(s) if s.strip().startswith("{") else ({} if not s.strip() else None)
        per, wk = js(a.per_shard), js(a.workers)
        if wk is None:                                   # one number for every organism
            wk = {o: int(a.workers) for o in ORGS}
        print(json.dumps(matrix(a.scale, json.loads(a.orgs) if a.orgs.startswith("[") else a.orgs.split(","),
                                a.first, a.runs, per, wk)))
        return 0
    if a.what == "kube-matrix":
        sizes = [int(x) for x in a.sizes.split(",")]
        reps = [int(x) for x in a.reps.split(",")]          # one count for every size, or one per size
        durs = [int(x) for x in a.durations.split(",")]      # likewise
        pick = lambda xs, i: xs[min(i, len(xs) - 1)]
        cells = [c for i, sz in enumerate(sizes)
                 for c in kube_matrix([sz], a.organisms.split(","), a.rep_first, pick(reps, i), [pick(durs, i)], a.split == "yes")]
        print(json.dumps(cells))
        return 0

    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"dispatches": []}
    runs = [] if getattr(a, "offline", False) else grid_runs()
    cov = coverage(runs, manifest)
    todo = next_dispatches(cov)
    if a.what == "plan":
        report(cov, [], 0, 0, 0)
        left_jobs = sum(d["jobs"] for d in next_dispatches(cov, caps={}))
        left_h = sum(d["hours"] for d in next_dispatches(cov, caps={}))
        print(f"\nStill to start on GitHub: {left_jobs:,} jobs, about {left_h:,.0f} runner-hours "
              f"(about {left_h / 180 / 24:.1f} days at the 180 jobs GitHub ran at once on 12 Oct; free for this public repository).")
        return 0
    eng = engine()
    if eng != ENGINE:                                  # a grid belongs to one engine: never start its runs on another
        print(f"this checkout runs {eng}, the grid is {ENGINE}'s: nothing started (a new engine gets its own grid)")
        return 0
    queued, running = jobs_in_flight()
    target = max(a.floor, running + a.extra)
    inflight, started = queued + running, []
    for d in todo:
        if a.grid != "all" and d["grid"] != a.grid:
            continue
        if len(started) >= a.max_dispatches or inflight + d["jobs"] > target:
            break
        if not a.dry:
            dispatch(d, a.ref)
            time.sleep(2)
        started.append(d)
        inflight += d["jobs"]
    for d in started:
        print(f"started: {d['title']} ({d['jobs']} jobs)")
    print(f"jobs now {running} running, {queued} queued; target {target}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    with (open(summary, "a") if summary else contextlib.nullcontext(sys.stdout)) as out:
        print("## The grid on the max: every square to 1,000 runs" + (" (dry run: nothing started)" if a.dry else ""), file=out)
        print("", file=out)
        report(cov, started, queued, running, target, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
