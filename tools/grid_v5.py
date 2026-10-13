# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid of the card version, every square in one page (results/grid_v5/GRID.md), built from the pooled receipts the
archive keeps: the six organisms at 1, 10 and 100 copies on one clock, each at its first 1, 10 and 100 runs (nested),
native against Omni-Compass on top, twice: modelled (six.yml, pooled by six-pool: SIX_v5-x<size>.json) and with the real
Kubernetes cluster inside (six-kube.yml, pooled by six-kube-pool: SIX_KUBE_v5-x<size>_r<n>.json). Nothing is
recomputed here: every cell is the pooled receipt's own reading, and each half names the runs it was pooled from.

  python3 tools/grid_v5.py --modelled DIR [DIR ...] [--kube DIR [DIR ...]] --out results/grid_v5/GRID.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp                                   # noqa: E402
from tools.readings import OWN_RUNS                             # noqa: E402

ORGS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
        "stack", "tower"]
NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         "stack": "The four stacked", "tower": "The whole tower"}
SIZES, RUNS = (1, 10, 100), ("1", "10", "100")
copies = lambda n: f"{n} cop{'y' if int(n) == 1 else 'ies'}"


def run_of(path):
    """The GitHub run an archived receipt came from (results/live/raw/run-<id>/...)."""
    return next((p.name[4:] for p in Path(path).resolve().parents if p.name.startswith("run-")), "?")


def where(f):
    """A receipt's page (its .md beside the .json), as the repository names it."""
    f = Path(f).resolve().with_suffix(".md")
    return f.relative_to(ROOT).as_posix() if f.is_relative_to(ROOT) else f.name


def modelled(dirs):
    """{size: (receipt, run id, page)} from every SIX_v5-x<size>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_v5-x*.json"):
            rec = json.loads(f.read_text())
            out[int(rec["scale"])] = (rec, run_of(f), where(f))
    return out


def kube(dirs):
    """{(size, runs): (report, run id, page)} from every SIX_KUBE_v5-x<size>_r<n>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_KUBE_v5-x*_r*.json"):
            size, n = f.stem.split("-x", 1)[1].split("_r")
            out[(int(size), n)] = (json.loads(f.read_text()), run_of(f), where(f))
    return out


def model_cell(s):
    if not s:
        return "not in the receipt"
    m, w, e = s["viol_pp"][0], 100 * s["work"][0], 100 * s["energy"][0]
    lab = s["label"].replace("**", "")
    return f"{lab}: misses {m:+.3f} pp, work {w:+.3f}%, power given {e:+.3f}% ({s['runs']} of {s['of']} runs)"


def kube_cell(o):
    if not o:
        return "not in the report"
    if o["verdict"].startswith("ONE REPETITION"):
        return o["verdict"]
    return f"{o['repetitions']} repetitions: {o['verdict']}"


def kube_key(org, size):
    return org if size == 1 else f"{org}@{size}"


def rng(xs):
    lo, hi = f"{min(xs):+.3f}%", f"{max(xs):+.3f}%"
    return lo if lo == hi else f"{lo} to {hi}"


WORSE = re.compile(r"worse on (\d+)(?: \((.*)\))?, inside the noise on")


def worse_gauges(verdict):
    """The gauges a square's verdict reads worse, in its own words (tools/six_kube_report.py: "better on 3, worse on 2
    (a; b), inside the noise on 6"); None for a verdict with no such count (one repetition)."""
    m = WORSE.search(verdict)
    return None if not m else (m.group(2).split("; ") if m.group(2) else [])


def across(data):
    """The grid in one line, counted from the squares themselves (the front page's reading of this table)."""
    sq = [s for cells in data["modelled"].values() for n, s in cells.items() if s]
    labs = Counter(s["label"].replace("**", "") for s in sq if s["runs"] >= 2)
    one = [s for s in sq if s["runs"] < 2]
    pg = [100 * s["energy"][0] for s in sq]
    parts = []
    if sq:
        parts.append("modelled, " + ", ".join(f"{c} of {sum(labs.values())} squares of 10 and 100 runs {lab}"
                                               for lab, c in labs.most_common())
                     + f"; the {len(one)} single runs: {sum(1 for s in one if s['viol_pp'][0] < 0)} with fewer misses"
                     + f"; work {rng([100 * s['work'][0] for s in sq])}; power given {rng(pg)}")
    ks = [o for cells in data["kube"].values() for o in cells.values() if o]
    if ks:
        judged = [w for o in ks if (w := worse_gauges(o["verdict"])) is not None]
        single = sum(1 for o in ks if o["verdict"].startswith("ONE REPETITION"))
        by = Counter(g for w in judged for g in w)
        other = len(ks) - len(judged) - single
        parts.append(f"with the cluster inside, {len(ks)} squares: {single} single repetitions (no reading)"
                     + (f", {other} with a verdict of another form" if other else "")
                     + f"; of the {len(judged)} of 10 and 100 repetitions, worse on no gauge in {sum(1 for w in judged if not w)}"
                     + (", the gauges read worse: " + ", ".join(f'"{g}" in {c}' for g, c in by.most_common()) if by else "")
                     + f"; off the clock in {sum(1 for o in ks if 'OFF THE CLOCK' in o['verdict'])}"
                     + f"; invalid in {sum(1 for o in ks if 'INVALID' in o['verdict'])}")
    return "**Across the grid: " + ("; ".join(parts) or "no squares") + ".**"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--modelled", nargs="+", required=True)
    ap.add_argument("--kube", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    mod, kub = modelled(a.modelled), kube(a.kube)
    L = ["# The grid of the card version: six organisms at 1, 10 and 100 copies, each at 1, 10 and 100 runs", "",
         "Native against Omni-Compass on top of native, engine omni-v5 (digest 5648f290, every muscle its own card), work "
         "waiting in line in every organism. Each square is the pooled receipt's own reading; the 1-, 10- and 100-run "
         "squares of a size are nested (the first N runs). Every square is shown.", "",
         "How to read a modelled square: its reading (one run carries no label; at 10 and 100 runs the receipt's own word), "
         "then the change Omni-Compass made against native, averaged over the runs: misses, the share of time the plants "
         "were over their own line, in percentage points (negative is fewer); work done, in percent; power given, the "
         "energy the max took for it, in percent. A square with the cluster inside carries the report's verdict and the "
         "repetitions it pooled.", "", OWN_RUNS, ""]
    top = len(L)                                                 # the grid in one line goes here, once every square is read
    L += ["## Modelled (six.yml; evidence class S, our own models)", "",
          "Pooled receipts: " + ", ".join(f"{copies(s)}: run {mod[s][1]}" for s in sorted(mod)) + ". Every column of every "
          "square (the intervals, the band, the knobs handed back): " + ", ".join(f"[`{mod[s][2]}`]({mod[s][2]})" for s in sorted(mod))
          + ".", ""]
    data = {"modelled": {}, "kube": {}}
    for size in SIZES:
        rec = mod.get(size, (None,))[0]
        L += [f"### {copies(size)}", "", "| Organism | 1 run | 10 runs | 100 runs |", "|---|---|---|---|"]
        for org in ORGS:
            cells = [model_cell((rec or {}).get("summary", {}).get(n, {}).get(org)) for n in RUNS]
            data["modelled"][f"{org}@{size}"] = {n: (rec or {}).get("summary", {}).get(n, {}).get(org) for n in RUNS}
            L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
        L.append("")
    if kub:
        L += ["## With the real Kubernetes cluster inside (six-kube.yml; the cluster measured, class L; the organism "
              "modelled, class S)", "",
              "Pooled reports: " + ", ".join(f"{copies(s)}: run {r}" for s, r in sorted({(s, r) for (s, _), (_, r, _) in kub.items()}))
              + ". Every gauge of every square, with its interval: " + ", ".join(f"[`{kub[k][2]}`]({kub[k][2]})" for k in sorted(kub, key=lambda k: (k[0], int(k[1]))))
              + ".", "",
              "How to read a square with the cluster inside: the report's own verdict (`tools/six_kube_report.py`) over its judged "
              "gauges, the cluster's response times, time over the response line, failed requests, pods started, replicas, "
              "machines and declared energy, and the organism's work, energy, work per energy and time over its line; a gauge "
              "counts better or worse only when its 95% interval is clear of zero, and the rest are inside the noise. That "
              "report judges the organism's modelled energy and its work per energy as lower-better, as it did before the max; "
              "the modelled receipts above show the same energy as the power given, beside the work. OFF THE CLOCK marks the "
              "repetitions where the organism ended more than 5% of the window late, its last steps seeing a cluster whose load "
              "schedule had ended: the runner could not step that many muscles in time.", ""]
        for size in SIZES:
            L += [f"### {copies(size)}", "", "| Organism | 1 run | 10 runs | 100 runs |", "|---|---|---|---|"]
            for org in ORGS:
                cells = []
                for n in RUNS:
                    rep = kub.get((size, n), (None,))[0]
                    o = ((rep or {}).get("organisms") or {}).get(kube_key(org, size))
                    data["kube"].setdefault(f"{org}@{size}", {})[n] = o and {"repetitions": o["repetitions"], "verdict": o["verdict"]}
                    cells.append(kube_cell(o))
                L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
            L.append("")
    L[top:top] = [across(data), ""]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps(data, indent=1) + "\n")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
