# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The capacity test's A/B/C three-run table (docs/CAPACITY_PREREGISTRATION.md): the same test run three times as separate
GitHub runs on the same engine, each run's own table built by tools/capacity_report.py (CAPACITY.json in each archived run,
results/live/raw/capacity-run-<id>/). Each cap level gets two judged rows, completed work and capacity, each with the three
readings every three-run table uses (tools/confirm_abc.py's rule: better or WORSE in all three of our runs, no difference
beyond the noise, or the runs disagree). Every row is shown, losses included.

  python3 tools/capacity_abc.py A_DIR B_DIR C_DIR --out results/live/V5_CAPACITY.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.confirm_abc import CAPACITY, cell, engine, verdict   # noqa: E402
from tools.legal import stamp                                   # noqa: E402
from tools.readings import OWN_RUNS                             # noqa: E402

WORK = "completed work (requests answered within the line over the window; higher is better)"


def load(d):
    """One run: its GitHub run id (from the folder's name), its label and its rows by cap level."""
    d = Path(d)
    run = d.name.rsplit("-", 1)[-1]
    rows = {r["cap_m"]: r for r in json.loads((d / "CAPACITY.json").read_text())["rows"]}
    meta = dict(line.split("=", 1) for line in (d / "RUN.txt").read_text().splitlines() if "=" in line) if (d / "RUN.txt").exists() else {}
    return run, meta, rows


def pair(r, key):
    """A cap row's paired difference in the shape confirm_abc reads (native, omni, diff, ci95)."""
    if key == "work":
        return {"native": r["work_native"], "omni": r["work_omni"], "diff": r["work_diff"], "ci95": [r["work_lo"], r["work_hi"]]}
    return {"native": r["capacity_native"], "omni": r["capacity_omni"], "diff": r["capacity_diff"],
            "ci95": [r["capacity_lo"], r["capacity_hi"]]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table (Omni v5)", "",
         "Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the "
         "replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the "
         "load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change "
         "with its 95% interval (completed work in percent of native; capacity in requests a second). Every judged row gets "
         "one of three readings. **Better** or **WORSE in all three of our runs**: all three runs move the same way and every "
         "interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero; that "
         "is the result. **The runs disagree**: runs clear of the noise point different ways. Every row is shown, losses "
         "included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).", "",
         OWN_RUNS, "", "| Run | GitHub run | Label | Commit | Engine | Pairs per cap |", "|---|---|---|---|---|---:|"]
    engines = []
    for tag, (run, meta, rows) in zip("ABC", runs):
        sha, ver = engine(run)
        engines.append(ver.split(" ")[0])
        pairs = sorted({r["pairs"] for r in rows.values()})
        L.append(f"| {tag} | {run} | {meta.get('label', '?')} | `{sha}` | {ver} | {', '.join(map(str, pairs))} |")
    if len(set(engines)) > 1 or len({r for r, _, _ in runs}) < 3:
        L[2:2] = ["**Not one engine's three separate runs: " + ", ".join(engines) + ".** The readings below compare runs on "
                  "different engines.", ""]
    caps = sorted(set.intersection(*(set(rows) for _, _, rows in runs)))
    L += ["", "| Cap (cores) | Measure | A | B | C | Reading |", "|---:|---|---|---|---|---|"]
    tally, data = {}, {}
    for cap in caps:
        for key, label in (("work", WORK), ("capacity", CAPACITY)):
            rs = [pair(rows[cap], key) for _, _, rows in runs]
            v = verdict(CAPACITY, rs)               # both measures: higher is better
            tally[v] = tally.get(v, 0) + 1
            data[f"{cap}:{key}"] = {"reading": v.strip("*"), "runs": rs}
            cells = [cell(r) if key == "work" else f"{r['diff']:+.2f} req/s ({r['ci95'][0]:+.2f} to {r['ci95'][1]:+.2f})"
                     for r in rs]
            L.append(f"| {cap / 1000:g} | {label} | {cells[0]} | {cells[1]} | {cells[2]} | {v} |")
    L += ["", "Readings: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())) + ".", "",
          "How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work "
          "from the same capacity; where neither arm can do more under the cap, the rows show no difference beyond the noise, "
          "and that is the result. Each run's own table, with its audit lines and what each step up in the cap gives each "
          "arm: `CAPACITY.md` in its archived folder."]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps({"runs": [r for r, _, _ in runs], "engines": engines, "rows": data},
                                                   indent=1) + "\n")
    print(f"{out}: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
