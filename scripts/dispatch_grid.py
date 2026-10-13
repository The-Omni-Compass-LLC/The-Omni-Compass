#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid, every square filled to 100 runs: each of the six organisms at 1, 10 and 100 copies clustered on one clock,
each size at 1, 10 and 100 runs, native and Omni side by side (54 squares), twice: modelled (six.yml) and with the real
Kubernetes cluster inside (six-kube.yml). A square's runs are nested (its first 1, 10 and 100 runs), so a size needs its
100 runs once. 1, 10 and 100 only, the founder's order of 12 October: no 1,000 copies and no 1,000 runs, to cut the time
and the bill; the whole grid runs on GitHub's own machines.

The conductor (tick) starts the grid and keeps every runner GitHub gives this repository busy without flooding the queue:
it finds which runs of each square are already started (the dispatches named by their squares, plus the manifest of the
first night's runs), and starts the next ones (the 10-run squares of every size first, then 100) until the repository's
queued and running jobs reach what GitHub is running now plus a margin. grid.yml runs it every 15 minutes; the six and
six-kube buttons run it once when started with their defaults. Nothing is started twice: a started run is read back from
its own name.

Shards are cut from run times measured on the max (12 Oct, work waiting in line, GitHub's own machines) so that no job
nears GitHub's six-hour limit; each shard also stops starting runs at its deadline and hands in every run it finished.

  python3 scripts/dispatch_grid.py plan                 every square, how many of its runs are started, what is left
  python3 scripts/dispatch_grid.py tick [--dry]         start what fits now (GITHUB_TOKEN, or Claude Code's gh api)
  python3 scripts/dispatch_grid.py matrix ...           six.yml's shards for one dispatch (used by the workflow)
  python3 scripts/dispatch_grid.py kube-matrix ...      six-kube.yml's cells for one dispatch (used by the workflow)
"""
from __future__ import annotations

import argparse
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
SINCE = "2026-10-13T02:50:00Z"     # the grid of omni-v5 as re-declared on 13 Oct (digest 5648f290, every muscle its own
                                   # card): runs started before belong to other engines or settings (results/grid_v5/history)
ENGINE = "omni-v5"                 # the engine whose grid this is (tools/omni_version.py)
SIZES = (1, 10, 100)               # 1, 10 and 100 copies only (the founder's order, 12 Oct)
RUNS = 100                         # every square to 100 runs: 1, 10 and 100 runs only (the founder's order, 12 Oct)
TIERS = (10, 100)                  # the 10-run squares of every size first, then 100
MAX_JOBS = 250                     # GitHub: at most 256 jobs in one run's matrix (a few kept for the plan and the receipt)
ORGS = ["1", "2", "3", "4", "5", "6"]   # tools/run_scale.py: the four realms, the four stacked, the whole tower
KUBE = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
        "stack", "tower"]          # tools/run_kil.py names of the same six, in the same order (5 the four stacked, 6 the tower)
LOAD = "line"                      # the founder's order: work waiting in line in every organism (six.yml)

# Seconds per paired run (native then Omni on one seed), measured on the max with work waiting in line (12 Oct): 1 copy
# on GitHub's machines (the night's shards), 10 copies of every organism and 100 copies of the compute realm and the tower
# on a 4-core machine that runs as fast as GitHub's; the other figures are scaled from those (a run grows 9 to 11 times
# per tenfold size). CAL: the calibration run each worker makes once per organism (a native run on the calibration seed).
# MEM: a worker's peak memory (GB).
SEC = {1: {"1": 7.2, "2": 6.5, "3": 5.1, "4": 5.0, "5": 28.8, "6": 17.4},
       10: {"1": 77, "2": 95, "3": 79, "4": 67, "5": 359, "6": 250},
       100: {"1": 660, "2": 850, "3": 710, "4": 600, "5": 2820, "6": 1780}}
CAL = {1: {o: 2 for o in ORGS}, 10: {o: 15 for o in ORGS},
       100: {"1": 150, "2": 200, "3": 170, "4": 150, "5": 670, "6": 500}}
MEM = {1: {o: 0.2 for o in ORGS}, 10: {o: 0.4 for o in ORGS},
       100: {"1": 0.9, "2": 0.9, "3": 0.9, "4": 0.9, "5": 3.2, "6": 1.8}}
RUNNER_GB, RUNNER_CPUS = 14.0, 4   # GitHub's machine for a public repository: 4 cores, 16 GB (2 kept for the system)
JOB_S = 4 * 3600                   # a shard's planned work (a single run that needs more gets up to LONG_S)
LONG_S = 5 * 3600
DEADLINE_MIN = 320                 # run_scale starts no run that would end after this; the job is cut at 355 minutes
# with the real cluster inside, the organism steps on the window's clock (240 steps), so the window must be long enough
# for the max's arm to make each step in time (tools/six_kube_report.py marks a repetition more than 5% late OFF THE
# CLOCK): seconds per arm by size, and by organism where the default is too short
KUBE_WINDOW = {1: 960, 10: 960, 100: 1440}
KUBE_WINDOW_ORG = {(100, "tower"): 2400, (100, "stack"): 3600}
KUBE_BUILD = {1: 1, 10: 1, 100: 8}         # minutes to build the organism (calibration, plants, the max's bone)
# the test rig's protocol with the real cluster inside (scripts/kind_bench.sh), carried in each run's name. Protocol 2 (12
# Oct): the governor at the organism's own CPU priority, never below the rig beside it; its decisions counted inside the
# measured window; kind, kubectl and the metrics-server manifest tried again when a download is refused. The runs of
# protocol 1 (before it: their names carry no protocol) are kept as they stand and counted in no square, so every square
# with the cluster inside is filled on protocol 2 alone
KUBE_PROTOCOL = "2"
MAX_TRIES = 3                      # a repetition whose job failed this many times is started no more (the report lists it)


# ------------------------------------------------------------------------------------------------- shard shapes
def shape(size, org):
    """(runs per shard, workers per runner) for a modelled square, or None where it cannot run on GitHub."""
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
KUBE_NAME = re.compile(r"^six-kube x(\d+) orgs ([\w,]+) reps (\d+)\+(\d+) arms ([\w ]+?) split (\w+) window (\d+)"
                       r"(?: protocol (\w+))?$")
JOB_NAME = re.compile(r"^run \((\w+), (\d+), (\d+), \d+, [\w ]+?(?:, -\w+)?\)$")   # six-kube's cell: organism, size, rep


def six_title(size, org, first, n):
    return f"six x{size} {LOAD} orgs {org} runs {first}+{n}"


def kube_title(size, orgs, r0, reps, split, window):
    return (f"six-kube x{size} orgs {','.join(orgs)} reps {r0}+{reps} arms native compass split {'yes' if split else 'no'} "
            f"window {window} protocol {KUBE_PROTOCOL}")


def coverage(runs, manifest, failed=None):
    """Which runs of each square are started (in flight or finished, not cancelled): {("six", size, org): set of run
    indices from 0, ("kube", size, organism): set of repetitions from 1 with both arms}. With the cluster inside only
    runs of protocol KUBE_PROTOCOL count, and a repetition whose job failed counts as not started (failed: {run id: set of
    (organism, rep)}, read from the runs' own job lists by failed_reps), so it is started again."""
    cov, failed = {}, failed or {}
    add = lambda key, xs: cov.setdefault(key, set()).update(xs)
    for d in manifest.get("dispatches", []):
        if d.get("status") != "kept":
            continue
        if d["grid"] == "six" and d.get("load", "normal") == LOAD:
            for o in d["orgs"]:
                add(("six", d["size"], o), range(d["first"], d["first"] + d["runs"]))
        elif d["grid"] == "six-kube" and str(d.get("protocol", "1")) == KUBE_PROTOCOL:
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
        if m and m.group(8) == KUBE_PROTOCOL and r.get("conclusion") in (None, "success", "failure"):
            size, r0, n = int(m.group(1)), int(m.group(3)), int(m.group(4))
            bad = failed.get(r.get("id"), set())
            for o in m.group(2).split(","):
                add(("kube", size, o), [x for x in range(r0, r0 + n) if (o, x) not in bad])
    return cov


def kube_failures(runs, failed):
    """{(size, organism, rep): how many runs of protocol KUBE_PROTOCOL failed that repetition's job}."""
    out = {}
    for r in runs:
        m = KUBE_NAME.match(r.get("display_title") or "")
        if m and m.group(8) == KUBE_PROTOCOL:
            for o, x in failed.get(r.get("id"), ()):
                out[(int(m.group(1)), o, x)] = out.get((int(m.group(1)), o, x), 0) + 1
    return out


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


def next_dispatches(cov):
    """Every dispatch still to start, in order: tier by tier (10, then 100 runs), small sizes first, modelled then with
    the cluster inside."""
    out, cov = [], {k: set(v) for k, v in cov.items()}      # what is planned here counts as started for the next tier
    for tier in TIERS:
        for size in SIZES:
            for o in ORGS:
                sh = shape(size, o)
                if sh is None:
                    continue
                for f, n in gaps(cov.get(("six", size, o), set()), 0, tier):
                    step = sh[0] * MAX_JOBS
                    for f2 in range(f, f + n, step):
                        k = min(step, f + n - f2)
                        out.append({"grid": "six", "size": size, "orgs": [o], "first": f2, "runs": k,
                                    "jobs": math.ceil(k / sh[0]), "per": sh[0], "workers": sh[1],
                                    "hours": round(k * SEC[size][o] / sh[1] / 3600.0 + math.ceil(k / sh[0]) * CAL[size][o] / 3600.0, 1),
                                    "title": six_title(size, o, f2, k)})
                        cov.setdefault(("six", size, o), set()).update(range(f2, f2 + k))
            # with the cluster inside: organisms that share a window and the same runs still to start go in one dispatch
            split, hi = False, tier + 1          # both arms of a repetition on one runner (paired)
            groups = {}
            for o in KUBE:
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


def failed_reps(runs):
    """{run id: set of (organism, rep)}: the repetitions whose job did not succeed, in every finished run of protocol
    KUBE_PROTOCOL that failed. A finished run's jobs do not change, so each is read once per conductor (a file in the
    runner's temporary folder); a list GitHub does not give now is read again at the next tick, its run counted as started
    meanwhile (nothing is started twice)."""
    path = Path(os.environ.get("RUNNER_TEMP") or "/tmp") / "omni_grid_failed_jobs.json"
    try:
        cache = json.loads(path.read_text())
    except (OSError, ValueError):
        cache = {}
    out = {}
    for r in runs:
        m = KUBE_NAME.match(r.get("display_title") or "")
        if not m or m.group(8) != KUBE_PROTOCOL or r.get("conclusion") != "failure":
            continue
        rid = str(r["id"])
        if rid not in cache:
            bad, page = set(), 1
            try:
                while True:
                    j = api(f"repos/{REPO}/actions/runs/{rid}/jobs?filter=latest&per_page=100&page={page}")
                    for x in j.get("jobs", []):
                        mm = JOB_NAME.match(x.get("name") or "")
                        if mm and x.get("conclusion") not in ("success", "skipped"):
                            bad.add((mm.group(1), int(mm.group(3))))
                    if len(j.get("jobs", [])) < 100:
                        break
                    page += 1
            except (RuntimeError, urllib.error.URLError) as e:
                print(f"run {rid}: jobs not readable now ({str(e)[:80]}); counted as started until the next tick", file=sys.stderr)
                continue
            cache[rid] = sorted(bad)
        out[r["id"]] = {(o, int(x)) for o, x in cache[rid]}
    try:
        path.write_text(json.dumps(cache))
    except OSError:
        pass
    return out


def give_up(cov, runs, failed):
    """The repetitions whose job failed MAX_TRIES times in runs of protocol KUBE_PROTOCOL: counted as started from now on
    (never started again) and returned, {(size, organism, rep): failures}, for the report to name."""
    out = {}
    for (size, o, x), n in sorted(kube_failures(runs, failed).items()):
        if n >= MAX_TRIES and x not in cov.get(("kube", size, o), set()):
            cov.setdefault(("kube", size, o), set()).add(x)
            out[(size, o, x)] = n
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


def squares(cov):
    """The squares by organism and size: runs started of 100 (modelled; with the cluster inside)."""
    rows = []
    for size in SIZES:
        for o, k in zip(ORGS, KUBE):
            rows.append((size, o, len({x for x in cov.get(("six", size, o), ()) if x < RUNS}),
                         len({x for x in cov.get(("kube", size, k), ()) if 1 <= x <= RUNS})))
    return rows


def report(cov, started, queued, running, target, out=sys.stdout, gave_up=None):
    names = {"1": "Compute / AI / Cloud", "2": "Physics / Robotics / Autonomous", "3": "Energy / Facility / Industrial",
             "4": "Distribution / Specialized", "5": "The four stacked", "6": "The whole tower"}
    print(f"| Size | Organism | Modelled: runs started of {RUNS} | With the real cluster inside: runs started of {RUNS} |", file=out)
    print("|---:|---|---|---|", file=out)
    for size, o, six, kube in squares(cov):
        print(f"| {size:,} | {names[o]} | {six:,} | {kube:,} |", file=out)
    print(f"\nJobs now: {running} running, {queued} queued; target {target}. Started this time: {len(started)} dispatches, "
          f"{sum(d['jobs'] for d in started)} jobs.", file=out)
    for d in started:
        print(f"- {d['title']} ({d['jobs']} jobs, about {d['hours']} runner-hours)", file=out)
    print(f"\nWith the cluster inside, only runs of protocol {KUBE_PROTOCOL} count (12 Oct: the governor never below the "
          "organism's priority, its decisions counted inside the window); a repetition whose job failed is started again, up "
          f"to {MAX_TRIES} times.", file=out)
    for (size, o, x), n in sorted((gave_up or {}).items()):
        print(f"- not started again: {o} at {size:,} copies, repetition {x} (its job failed {n} times; listed, never "
              "dropped silently)", file=out)


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
    a = ap.parse_args(argv)

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
    failed = failed_reps(runs) if runs else {}
    cov = coverage(runs, manifest, failed)
    gave_up = give_up(cov, runs, failed)
    todo = next_dispatches(cov)
    if a.what == "plan":
        report(cov, [], 0, 0, 0, gave_up=gave_up)
        left_jobs = sum(d["jobs"] for d in todo)
        left_h = sum(d["hours"] for d in todo)
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
        if len(started) >= a.max_dispatches or inflight >= target:   # a dispatch bigger than the margin still starts
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
        print("## The grid on the max: 1, 10 and 100 copies, every square to 100 runs" + (" (dry run: nothing started)" if a.dry else ""), file=out)
        print("", file=out)
        report(cov, started, queued, running, target, out, gave_up=gave_up)
    return 0


if __name__ == "__main__":
    sys.exit(main())
