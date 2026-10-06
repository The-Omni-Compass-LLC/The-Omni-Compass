# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""docs/REALM_MUSCLES.md from realms/catalog.csv: the shared spine, then each realm's own families, then the tower.

    python3 tools/realm_muscles.py
"""
from __future__ import annotations

import csv
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "REALM_MUSCLES.md"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
BANNER = ("> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not "
          "open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, "
          "commercialization, monetization, production use, redistribution, hosted service or incorporation into a product "
          "requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, "
          "copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its "
          "software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).")
END = ("*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or\n"
       "monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.\n"
       "Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE` and `NOTICE` at the root of\n"
       "this repository.*")


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
          f"## Organism 6: the whole tower, all {len(rows)} muscles once", "", "---", "", END, ""]
    OUT.write_text("\n".join(L))
    print(f"{OUT} {len(rows)} muscles, spine {len(spine)}")


if __name__ == "__main__":
    main()
