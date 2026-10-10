# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""docs/REALM_MUSCLES.md from realms/catalog.csv: the shared spine, then each realm's own families, then the tower.

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
OUT = ROOT / "docs" / "REALM_MUSCLES.md"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
BANNER = f"> {_LEGAL_TOP}"                 # the one notice (tools/legal.py); stamp() keeps one copy of it


def families(rows):
    out = OrderedDict()
    for r in rows:
        out.setdefault(r["family"], []).append(r)
    return out


def section(fams):
    L = []
    for f, rs in sorted(fams.items()):
        L += [f"### {f} ({len(rs)}; plant: {rs[0]['template']}, {rs[0]['preset']})",
              ", ".join(f"{r['muscle']} [{r['knob']}]" for r in rs), ""]
    return L


def main():
    rows = list(csv.DictReader(open(ROOT / "realms" / "catalog.csv", encoding="utf-8")))
    spine = [r for r in rows if len(r["realms"].split(";")) == 4]
    L = [f"# The {len(rows)} muscles, realm by realm", "", BANNER, "",
         "Generated from `realms/catalog.csv` (rules: `tools/realms_catalog.py`; the v2 build: `tools/realms_catalog_v2.py`). Every "
         "realm's organism is its own families plus the **shared spine** (the infrastructure every real stack runs on), so the realm "
         "counts add to more than the tower. Each muscle is followed by the one knob Omni may hold on it.", "",
         f"## The shared spine: {len(spine)} muscles, in all four realms", ""] + section(families(spine))
    for i, (k, name) in enumerate(REALMS.items(), 1):
        own = [r for r in rows if r["realm"] == k and len(r["realms"].split(";")) == 1]
        total = sum(1 for r in rows if k in r["realms"].split(";"))
        L += [f"## Realm {i}: {name}: {len(own)} own muscles + the spine = {total} in its organism", ""] + section(families(own))
    stack = sum(sum(1 for r in rows if k in r["realms"].split(";")) for k in REALMS)
    L += [f"## Organism 5: the four stacked, every duplicate kept, {stack:,} muscles", "",
          f"## Organism 6: the whole tower, all {len(rows)} muscles once", ""]
    OUT.write_text("\n".join(_legal_stamp(L)) + "\n", encoding="utf-8")
    print(f"{OUT} {len(rows)} muscles, spine {len(spine)}")


if __name__ == "__main__":
    main()
