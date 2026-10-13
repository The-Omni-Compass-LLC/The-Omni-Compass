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
import sys
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


def modelled(dirs):
    """{size: (receipt, run id)} from every SIX_v5-x<size>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_v5-x*.json"):
            rec = json.loads(f.read_text())
            out[int(rec["scale"])] = (rec, run_of(f))
    return out


def kube(dirs):
    """{(size, runs): (report, run id)} from every SIX_KUBE_v5-x<size>_r<n>.json under the given folders."""
    out = {}
    for d in dirs:
        for f in Path(d).rglob("SIX_KUBE_v5-x*_r*.json"):
            size, n = f.stem.split("-x", 1)[1].split("_r")
            out[(int(size), n)] = (json.loads(f.read_text()), run_of(f))
    return out


def model_cell(s):
    if not s:
        return "not in the receipt"
    m, w, e = s["viol_pp"][0], 100 * s["work"][0], 100 * s["energy"][0]
    lab = s["label"].replace("**", "")
    return f"{lab}: misses {m:+.3f} pp, work {w:+.3f}%, power given {e:+.3f}% ({s['runs']} of {s['of']} runs)"


def kube_key(org, size):
    return org if size == 1 else f"{org}@{size}"


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
    L += ["## Modelled (six.yml; evidence class S, our own models)", "",
          "Pooled receipts: " + ", ".join(f"{copies(s)}: run {mod[s][1]}" for s in sorted(mod)) + ".", ""]
    data = {"modelled": {}, "kube": {}}
    for size in SIZES:
        rec = mod.get(size, (None, None))[0]
        L += [f"### {copies(size)}", "", "| Organism | 1 run | 10 runs | 100 runs |", "|---|---|---|---|"]
        for org in ORGS:
            cells = [model_cell((rec or {}).get("summary", {}).get(n, {}).get(org)) for n in RUNS]
            data["modelled"][f"{org}@{size}"] = {n: (rec or {}).get("summary", {}).get(n, {}).get(org) for n in RUNS}
            L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
        L.append("")
    if kub:
        L += ["## With the real Kubernetes cluster inside (six-kube.yml; the cluster measured, class L; the organism "
              "modelled, class S)", "",
              "Pooled reports: " + ", ".join(f"{copies(s)}: run {r}" for s, r in sorted({(s, r) for (s, _), (_, r) in kub.items()})) + ".", ""]
        for size in SIZES:
            L += [f"### {copies(size)}", "", "| Organism | 1 run | 10 runs | 100 runs |", "|---|---|---|---|"]
            for org in ORGS:
                cells = []
                for n in RUNS:
                    rep = kub.get((size, n), (None, None))[0]
                    o = ((rep or {}).get("organisms") or {}).get(kube_key(org, size))
                    data["kube"].setdefault(f"{org}@{size}", {})[n] = o and {"repetitions": o["repetitions"], "verdict": o["verdict"]}
                    cells.append(f"{o['verdict']} ({o['repetitions']} repetitions)" if o else "not in the report")
                L.append(f"| {NAMES[org]} | " + " | ".join(cells) + " |")
            L.append("")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps(data, indent=1) + "\n")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
