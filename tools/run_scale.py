#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Six organisms, native and Omni, over many runs and at many sizes (evidence class S: the realm models).

  1 Compute / AI / Cloud
  2 Physics / Robotics / Autonomous
  3 Energy / Facility / Industrial
  4 Distribution / Specialized
  5 the four stacked, every duplicate kept, one body on one clock
  6 the whole tower, every muscle once
  (sizes: realms/catalog_provenance.json)

Every organism runs native (its own controllers) and native with Omni on top on the same seed: --arm v5 (the engine's
law, realms/compass_arm_v5.py, on the v5 catalog) or --arm compass (the v3 law, realms/compass_arm.py, on v3's catalog,
for v3's stored grid); --runs paired seeds (7000 on); --scale copies of the organism on one clock (each copy its own
seeds), so 10x is ten clusters of that organism governed together. Receipts: per organism, work per energy, work, energy
and violations with their 95% intervals over runs, the label by the round-3 rule, and the raw per-run contrasts.

The four stacked (5), two ways (--stack): "realms" (the v5 default) keeps each realm's own body on the one clock, so
every muscle in the stack runs exactly the native it runs in its own realm, plant by plant (the founder's order: the
native identical in all six); "body" (v3's stored grid) puts all four realms in one body, each copy its own series.

  python3 tools/run_scale.py --runs 100 --scale 1 --out results/scale/r100-x1 [--arm v5] [--workers N] [--organisms 1,2,5]
"""
from __future__ import annotations

import argparse

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import (catalog, run_organism_arm, run_bodies, Body, paired_organism, summarize, label, STACK,  # noqa: E402
                            TOWER, organism_name)

ARM, CATALOG, STACK_MODE = "compass", None, "body"       # set by main() (and passed to each worker)
CATALOGS = {"compass": str(ROOT / "realms" / "catalog.csv"), "v5": str(ROOT / "realms" / "catalog_v5.csv")}

REALMS = ("compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized")
ORGS = {"1": ("compute_ai_cloud", "Compute / AI / Cloud"), "2": ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
        "3": ("energy_facility_industrial", "Energy / Facility / Industrial"), "4": ("distribution_specialized", "Distribution / Specialized"),
        "5": (STACK, "The four stacked, duplicates kept"), "6": (TOWER, "The whole tower, every muscle once")}
SEED0 = 7000


def rows_for(key, scale, cat=None):
    rows = catalog(cat or CATALOG) if (cat or CATALOG) else catalog()
    key = organism_name(key)
    if key == STACK:
        base = [dict(r, muscle_id=f"{r['muscle_id']}@{realm}") for realm in REALMS for r in rows if realm in r["realms"].split(";")]
    elif key == TOWER:
        base = rows
    else:
        base = [r for r in rows if key in r["realms"].split(";")]
    return [dict(r, muscle_id=r["muscle_id"] + (f"~{c}" if c else "")) for c in range(scale) for r in base]


def run_arm(key, scale, seed, arm, cat, stack_mode):
    if organism_name(key) == STACK and stack_mode == "realms":
        bodies = [Body(rows_for(realm, scale, cat), seed) for realm in REALMS]
        return run_bodies(bodies, arm, [list(range(len(bodies)))])
    return run_organism_arm(rows_for(key, scale, cat), seed, arm)


def job(args):
    key, scale, seed, arm, cat, stack_mode = args
    nat = run_arm(key, scale, seed, "native", cat, stack_mode)
    om = run_arm(key, scale, seed, arm, cat, stack_mode)
    c = paired_organism(om, nat)
    c["restore_ok"] = om["restore_ok"]
    c["energy_native_j"] = sum(p["energy_j"] for p in nat["plants"])
    c["energy_omni_j"] = sum(p["energy_j"] for p in om["plants"])
    return key, seed, c


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=int, default=100)
    ap.add_argument("--scale", type=int, default=1)
    ap.add_argument("--organisms", default="1,2,3,4,5,6")
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--out", required=True)
    ap.add_argument("--first", type=int, default=0, help="first run index (a shard of a larger run starts here)")
    ap.add_argument("--arm", choices=("v5", "compass"), default="v5",
                    help="v5: the engine's law on the v5 catalog; compass: the v3 law on v3's catalog (its stored grid)")
    ap.add_argument("--catalog", default="", help="a muscle catalog (default: the arm's own)")
    ap.add_argument("--stack", choices=("realms", "body"), default="",
                    help="the four stacked: each realm's own body (v5 default) or one body (v3's stored grid)")
    a = ap.parse_args(argv)
    cat = a.catalog or CATALOGS[a.arm]
    stack_mode = a.stack or ("realms" if a.arm == "v5" else "body")
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    keys = [ORGS[k][0] for k in a.organisms.split(",")]
    jobs = [(k, a.scale, SEED0 + a.first + i, a.arm, cat, stack_mode) for i in range(a.runs) for k in keys]
    t0 = time.time()
    res = {k: {} for k in keys}
    with ProcessPoolExecutor(a.workers) as ex:
        for n, (k, seed, c) in enumerate(ex.map(job, jobs, chunksize=1), 1):
            res[k][seed] = c
            if n % max(1, len(jobs) // 20) == 0:
                print(f"{n}/{len(jobs)} done, {time.time() - t0:.0f} s", flush=True)
    commit = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    names = {v[0]: v[1] for v in ORGS.values()}
    L = [f"# Six organisms, {a.runs} runs, {a.scale}x size", "",
         f"Evidence class **S** (models). Commit `{commit[:12]}`, seeds {SEED0}-{SEED0 + a.runs - 1}, {a.scale} cop{'y' if a.scale == 1 else 'ies'} "
         f"of each organism on one clock, {time.time() - t0:.0f} s on {a.workers} workers. Native: each organism's own "
         "controllers. Omni: " + ("the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5)" if a.arm == "v5" else
                                  "the v3 compass law on every muscle (`realms/compass_arm.py`)")
         + f", catalog `{Path(cat).relative_to(ROOT)}`, the four stacked as "
         + ("each realm's own body on one clock (the native identical to each realm's)" if stack_mode == "realms" else "one body")
         + ". Harness `tools/run_scale.py`.", "",
         "Band first (the founder's rule): no win unless the time over the service line is no higher than native's "
         "(violations, mean over runs, at or under 0 pp).", "",
         "| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |",
         "|---|---|---:|---|---|---:|---:|---:|---:|---|"]
    summary = {}
    for num, (k, nm) in ORGS.items():
        if k not in res:
            continue
        per = [res[k][s] for s in sorted(res[k])]
        sm = summarize(per)
        lab = label(per, valid=all(c["restore_ok"] for c in per))
        summary[k] = {"label": lab, **{q: list(v) for q, v in sm.items()}, "runs": len(per)}
        f = lambda q, s=100.0, u="%": f"{s * sm[q][0]:+.3f}{u} ({s * sm[q][1]:+.3f} to {s * sm[q][2]:+.3f})"
        band = "held" if sm["viol_pp"][0] <= 0.0 else "NOT held"
        summary[k]["band_first"] = band
        L.append(f"| {num} | {nm} | {sum(len(rows_for(r, a.scale, cat)) for r in REALMS) if organism_name(k) == STACK else len(rows_for(k, a.scale, cat))} | **{lab}** | {band} | {f('primary')} | {f('work')} | {f('energy')} | "
                 f"{f('viol_pp', 1.0, '')} | {all(c['restore_ok'] for c in per)} |")
    (out / "SCALE.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    (out / "SCALE.json").write_text(json.dumps({"runs": a.runs, "scale": a.scale, "commit": commit, "arm": a.arm,
                                                "catalog": str(Path(cat).relative_to(ROOT)), "stack": stack_mode, "summary": summary,
                                                "per_run": {k: {str(s): c for s, c in v.items()} for k, v in res.items()}}) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
