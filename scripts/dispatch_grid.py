#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The full grid, every square: each of the six organisms at 1, 10, 100 and 1,000 copies clustered on one clock, each at
1, 10, 100 and 1,000 runs, native and Omni side by side (96 squares). One square's runs are nested (the first 1, 10, 100
and 1,000 runs), so a size needs its 1,000 runs once; GitHub allows 256 jobs in one run, so each size's runs are cut into
dispatches of six.yml (the modelled organisms) and six-kube.yml (the organisms with the real Kubernetes cluster inside),
in waves so the small squares land first.

  python3 scripts/dispatch_grid.py plan                       the dispatches, their jobs and runner-hours (nothing started)
  python3 scripts/dispatch_grid.py go --ref v5 [--grid six] [--load line] [--wave 1]   start them; run ids appended to the manifest

The manifest (results/grid_v5/DISPATCHED.json) lists every run id by grid, size and wave; six-pool.yml pools a size's runs
into one receipt. Uses Claude Code's GitHub client (gh api) or GITHUB_TOKEN with curl."""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "grid_v5" / "DISPATCHED.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "the-omni-compass-llc/the-omni-compass")
MAX_JOBS = 250                    # GitHub: at most 256 jobs in one run's matrix (a few kept for the plan and the receipt)
ORGS = ["1", "2", "3", "4", "5", "6"]      # the four realms, the four stacked, the whole tower (tools/run_scale.py)
# runs per job and processes per runner, by size and organism (a job ends at 6 hours; the four stacked at 1,000 copies
# runs alone on its runner for the memory, one run of it takes 2 to 3 hours)
PER = {1: {o: 100 for o in ORGS}, 10: {o: 100 for o in ORGS},
       100: {"1": 50, "2": 50, "3": 50, "4": 50, "5": 15, "6": 40},
       1000: {"1": 6, "2": 6, "3": 6, "4": 6, "5": 1, "6": 3}}
WORKERS = {1: {o: 4 for o in ORGS}, 10: {o: 4 for o in ORGS},
           100: {"1": 2, "2": 2, "3": 2, "4": 2, "5": 1, "6": 2}, 1000: {"1": 2, "2": 2, "3": 2, "4": 2, "5": 1, "6": 2}}
# runner-minutes per run (from the 12 Oct runs on GitHub's machines), for the plan's estimate
MIN_PER_RUN = {1: 0.4, 10: 1.3, 100: {"1": 4, "2": 4, "3": 4, "4": 4, "5": 17, "6": 6},
               1000: {"1": 40, "2": 40, "3": 40, "4": 40, "5": 165, "6": 60}}
WAVES = [(0, 100), (100, 1000)]   # runs 1-100 first (the 1-, 10- and 100-run squares), then 101-1,000
KUBE_WAVES = [(1, 10), (11, 100), (101, 1000)]
KUBE_DUR = {1: 960, 10: 960, 100: 1440, 1000: 2880}
KUBE_MIN = {1: 44, 10: 44, 100: 60, 1000: 110}
KUBE_ORGS = 6


def six_plan():
    """Dispatches of six.yml: (size, wave, organisms, first, runs, jobs, runner-hours)."""
    out = []
    for size in (1, 10, 100, 1000):
        waves = [(0, 1000)] if size in (1, 10) else WAVES
        for wi, (a, b) in enumerate(waves, 1):
            groups, cur, cur_jobs = [], [], 0
            for o in ORGS:
                jobs = math.ceil((b - a) / PER[size][o])
                if jobs > MAX_JOBS:                      # one organism alone: cut its runs
                    n = PER[size][o]
                    step = MAX_JOBS * n
                    for f in range(a, b, step):
                        groups.append(([o], f, min(step, b - f)))
                    continue
                if cur_jobs + jobs > MAX_JOBS:
                    groups.append((cur, a, b - a)); cur, cur_jobs = [], 0
                cur.append(o); cur_jobs += jobs
            if cur:
                groups.append((cur, a, b - a))
            for orgs, f, n in groups:
                jobs = sum(math.ceil(n / PER[size][o]) for o in orgs)
                mins = MIN_PER_RUN[size]
                hours = sum(n * (mins[o] if isinstance(mins, dict) else mins) / WORKERS[size][o] for o in orgs) / 60.0
                out.append({"grid": "six", "size": size, "wave": wi, "orgs": orgs, "first": f, "runs": n, "jobs": jobs,
                            "runner_hours": round(hours, 1)})
    return out


def kube_plan():
    """Dispatches of six-kube.yml: (sizes, wave, rep_first, reps, jobs, runner-hours); one job per paired repetition."""
    out = []
    for wi, (a, b) in enumerate(KUBE_WAVES, 1):
        for size in (1, 10, 100, 1000):
            per = MAX_JOBS // KUBE_ORGS                   # repetitions of one size that fit in one dispatch
            for r0 in range(a, b + 1, per):
                n = min(per, b + 1 - r0)
                out.append({"grid": "six-kube", "size": size, "wave": wi, "rep_first": r0, "reps": n,
                            "jobs": n * KUBE_ORGS, "runner_hours": round(n * KUBE_ORGS * KUBE_MIN[size] / 60.0, 1)})
    return out


def inputs_of(d):
    if d["grid"] == "six":
        s = d["size"]
        return {"scale": str(s), "arm": "v5", "orgs": json.dumps(d["orgs"]), "first": str(d["first"]),
                "runs": str(d["runs"]), "per_shard": json.dumps({o: PER[s][o] for o in d["orgs"]}),
                "workers": json.dumps({o: WORKERS[s][o] for o in d["orgs"]}), "load": d.get("load", "normal")}
    return {"sizes": str(d["size"]), "reps": str(d["reps"]), "rep_first": str(d["rep_first"]),
            "durations_s": str(KUBE_DUR[d["size"]])}


def gh(*args, data=None):
    cmd = ["gh", "api", *args]
    r = subprocess.run(cmd, input=json.dumps(data) if data is not None else None, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gh api {' '.join(args)}: {r.stderr.strip()[:300]}")
    return r.stdout


def dispatch(d, ref):
    wf = "six.yml" if d["grid"] == "six" else "six-kube.yml"
    before = {r["id"] for r in json.loads(gh(f"repos/{REPO}/actions/workflows/{wf}/runs?branch={ref}&per_page=20"))["workflow_runs"]}
    gh("-X", "POST", f"repos/{REPO}/actions/workflows/{wf}/dispatches", "--input", "-",
       data={"ref": ref, "inputs": inputs_of(d)})
    for _ in range(30):                                  # the new run's id (it appears within seconds)
        time.sleep(3)
        runs = json.loads(gh(f"repos/{REPO}/actions/workflows/{wf}/runs?branch={ref}&per_page=20"))["workflow_runs"]
        new = [r["id"] for r in runs if r["id"] not in before and r["event"] == "workflow_dispatch"]
        if new:
            return max(new)
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("what", choices=["plan", "go"])
    ap.add_argument("--ref", default="v5")
    ap.add_argument("--grid", choices=["six", "six-kube", "all"], default="all")
    ap.add_argument("--wave", type=int, default=0, help="only this wave (0: every wave)")
    ap.add_argument("--size", type=int, default=0, help="only this size (0: every size)")
    ap.add_argument("--load", choices=("normal", "climb", "line"), default="line",
                    help="the modelled organisms' load (six.yml): work waiting in line by default (the founder's order)")
    a = ap.parse_args(argv)
    plan = (six_plan() if a.grid in ("six", "all") else []) + (kube_plan() if a.grid in ("six-kube", "all") else [])
    for d in plan:
        if d["grid"] == "six":
            d["load"] = a.load
    plan = [d for d in plan if (not a.wave or d["wave"] == a.wave) and (not a.size or d["size"] == a.size)]
    tot_jobs = sum(d["jobs"] for d in plan); tot_h = sum(d["runner_hours"] for d in plan)
    for d in plan:
        print(json.dumps(d))
    print(f"{len(plan)} dispatches, {tot_jobs} jobs, about {tot_h:,.0f} runner-hours "
          f"(about {tot_h / 80 / 24:.1f} days at 80 runners at once; GitHub's machines cost this repository nothing)")
    if a.what == "plan":
        return 0
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {"dispatches": []}
    for d in plan:
        rid = dispatch(d, a.ref)
        d.update(run_id=rid, ref=a.ref, at=time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()))
        man["dispatches"].append(d)
        MANIFEST.write_text(json.dumps(man, indent=1) + "\n")
        print(f"started {d['grid']} x{d['size']} wave {d['wave']}: run {rid}", flush=True)
        time.sleep(2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
