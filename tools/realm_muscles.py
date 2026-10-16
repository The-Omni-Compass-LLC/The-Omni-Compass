# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""docs/REALM_MUSCLES.md from realms/catalog_v5.csv: every organism written out, muscle by muscle.

The shared spine (the muscles every realm's organism carries), then each realm's own families, then the two whole-catalog
organisms: the four stacked (every realm's organism on one clock, every duplicate of the spine kept) and the tower (every
muscle once). Each muscle is followed by the one knob Omni-Compass may hold on it; what the engine does with that knob, how
it is wired and its own card are in docs/MUSCLE_CATALOG.md (tools/muscle_catalog.py), family by family.

    python3 tools/realm_muscles.py
"""
from __future__ import annotations

import csv
from collections import OrderedDict
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "realms" / "catalog_v5.csv"
OUT = ROOT / "docs" / "REALM_MUSCLES.md"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
BANNER = f"> {_LEGAL_TOP}"                 # the one notice (tools/legal.py); stamp() keeps one copy of it


def families(rows):
    """The rows grouped by family, in the catalog's family order (family_id)."""
    out = OrderedDict()
    def key(r):                               # family order, then the muscle's id (numbers first, then the audited "AUDIT-nnnn" ids)
        mid = r["muscle_id"]
        return (int(r["family_id"]), (0, int(mid)) if mid.isdigit() else (1, mid))
    for r in sorted(rows, key=key):
        out.setdefault(r["family"], []).append(r)
    return out


def section(fams):
    L = []
    for f, rs in fams.items():
        L += [f"### {f} ({len(rs)}; plant: {rs[0]['template']}, {rs[0]['preset']})",
              ", ".join(f"{r['muscle']} [{r['knob']}]" for r in rs), ""]
    return L


def build(rows):
    spine = [r for r in rows if len(r["realms"].split(";")) == 4]
    in_realm = {k: [r for r in rows if k in r["realms"].split(";")] for k in REALMS}
    stack = sum(len(v) for v in in_realm.values())
    L = [f"# The {len(rows):,} muscles, organism by organism", "", BANNER, "",
         f"Generated from `realms/catalog_v5.csv` (the catalog the engine that stands carries: {len(rows):,} distinct muscles in "
         f"{len({r['family'] for r in rows})} families) by `tools/realm_muscles.py`. A **muscle** is one setting on one machine that already has "
         "its own control; the one knob Omni-Compass may hold on it stands in brackets after its name. Every realm's organism is its "
         "own families plus the **shared spine** (the infrastructure every real stack runs on), so the realm counts add to more than "
         "the tower. What the engine does with each knob, which native controller owns it, where the reading is tapped and the "
         "setting written, how it is restored and its own card are written family by family in `docs/MUSCLE_CATALOG.md` (the "
         "manuals' muscle appendix); the organisms' results are in `results/realms_v5/REALMS_V5.md` and the grid in "
         "`results/grid_v5/GRID.md`, each named for the engine it ran on.", "",
         "## The six organisms", "",
         "| Organism | Muscles | What it is |", "|---|---:|---|"]
    for i, (k, name) in enumerate(REALMS.items(), 1):
        own = [r for r in rows if r["realm"] == k and len(r["realms"].split(";")) == 1]
        L.append(f"| {i}. {name} | {len(in_realm[k]):,} | its {len(own)} own muscles and the spine of {len(spine)} |")
    L += [f"| 5. The four stacked (`stack`) | {stack:,} | the four realms' organisms on one clock, every duplicate of the spine kept |",
          f"| 6. The whole tower (`tower`) | {len(rows):,} | every muscle of the catalog once |", "",
          f"## The shared spine: {len(spine)} muscles, in all four realms", ""] + section(families(spine))
    for i, (k, name) in enumerate(REALMS.items(), 1):
        own = [r for r in rows if r["realm"] == k and len(r["realms"].split(";")) == 1]
        L += [f"## Organism {i}: {name}: {len(own)} own muscles + the spine of {len(spine)} = {len(in_realm[k]):,} in its organism", ""] + section(families(own))
    L += [f"## Organism 5: the four stacked, every duplicate kept, {stack:,} muscles", "",
          "The four realms' organisms above, run on one clock as one body (`stack`; the older name `stack_1226` is read as an alias): "
          f"every muscle listed under organisms 1 to 4, the spine counted once in each, {stack:,} in all.", "",
          f"## Organism 6: the whole tower, all {len(rows):,} muscles once", "",
          "Every muscle of the catalog once (`tower`; the older name `organism_656` is read as an alias): the spine and every realm's own "
          f"families, {len(rows):,} in all.", ""]
    return L, len(spine)


def main():
    rows = list(csv.DictReader(open(CATALOG, encoding="utf-8")))
    L, spine = build(rows)
    OUT.write_text("\n".join(_legal_stamp(L)) + "\n", encoding="utf-8")
    print(f"{OUT} {len(rows)} muscles, spine {spine}")


if __name__ == "__main__":
    main()
