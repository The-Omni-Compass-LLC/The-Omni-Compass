#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Pool the shards of a six-organism run (tools/run_scale.py, one SCALE.json per shard) into one receipt.

  python3 tools/pool_scale.py OUT.md parts/*/SCALE.json
"""
import glob, json, sys

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import summarize, label  # noqa: E402
from tools.run_scale import ORGS, REALMS, CATALOGS, rows_for  # noqa: E402
from realms.harness import STACK, organism_name  # noqa: E402


def main(out, *paths):
    files = [p for g in paths for p in glob.glob(g)]
    per, scale, commits, arms = {}, None, set(), set()
    cat, stack = None, "body"
    for f in files:
        d = json.loads(Path(f).read_text())
        scale = d["scale"]; commits.add(d["commit"][:12])
        arms.add(d.get("arm", "compass")); stack = d.get("stack", "body")
        cat = str(ROOT / d["catalog"]) if d.get("catalog") else None
        for k, runs in d["per_run"].items():
            per.setdefault(k, {}).update(runs)
    total = max(len(v) for v in per.values())
    assert len(arms) == 1, f"shards from different arms cannot be pooled: {sorted(arms)}"
    arm = arms.pop()
    law = ("the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5)" if arm == "v5" else
           "the v3 compass law on every muscle (`realms/compass_arm.py`)")
    count = lambda k: (sum(len(rows_for(r, scale, cat)) for r in REALMS) if organism_name(k) == STACK and stack == "realms"
                       else len(rows_for(k, scale, cat)))
    L = [f"# Six organisms at {scale}x size, up to {total} runs (pooled from {len(files)} shards)", "",
         f"Evidence class **S** (models). Commit(s) {', '.join(sorted(commits))}. Native: each organism's own controllers. "
         f"Omni: {law}. Each block is the first N runs (seeds 7000 on), so 1, 10, 100 and 1,000 "
         "are nested. Band first: no win unless the time over the service line is no higher than native's.", ""]
    summ = {}
    for n in [x for x in (1, 10, 100, 1000) if x <= total]:
        L += [f"## {n} run{'s' if n > 1 else ''}", "",
              "| # | Organism | Muscles | Runs | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |",
              "|---|---|---:|---:|---|---|---:|---:|---:|---:|---|"]
        for num, (k, nm) in ORGS.items():
            if k not in per:
                continue
            xs = [per[k][s] for s in sorted(per[k], key=int)][:n]
            ok = all(c["restore_ok"] for c in xs)
            if len(xs) >= 2:
                sm = summarize(xs); lab = label(xs, valid=ok)
            else:
                sm = {q: (xs[0][q], xs[0][q], xs[0][q]) for q in ("primary", "work", "energy", "viol_pp")}; lab = "ONE RUN (no label)"
            band = "held" if sm["viol_pp"][0] <= 0 else "NOT held"
            summ.setdefault(str(n), {})[k] = {"runs": len(xs), "label": lab, "band_first": band, **{q: list(v) for q, v in sm.items()}}
            f = lambda q, s=100.0, u="%": f"{s * sm[q][0]:+.3f}{u}" + (f" ({s * sm[q][1]:+.3f} to {s * sm[q][2]:+.3f})" if len(xs) > 1 else "")
            L.append(f"| {num} | {nm} | {count(k)} | {len(xs)} | **{lab}** | {band} | {f('primary')} | {f('work')} | "
                     f"{f('energy')} | {f('viol_pp', 1.0, '')} | {ok} |")
        L.append("")
    Path(out).write_text("\n".join(_legal_stamp(L)) + "\n")
    Path(out).with_suffix(".json").write_text(json.dumps({"scale": scale, "arm": arm, "stack": stack, "summary": summ}, indent=1) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(*sys.argv[1:])
