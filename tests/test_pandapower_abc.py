# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The power grid's A/B/C rule (tools/pandapower_abc.py, docs/OMNI_V1.md): a deterministic simulator, so the three runs must
reproduce; a gauge reads lower or higher in all three of our runs by its sign when they do, same under one part in a million, and "the
runs differ" when they do not; any increase in voltage violations reads higher; more tap operations reads higher (the declared
cost); the shown-only gauges are never judged."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import pandapower_abc as P


def arm(**kw):
    base = {"steps": 8784, "energy_in_mwh": 29000.0, "losses_mwh": 540.0, "load_energy_mwh": 57000.0, "violation_bus_share": 0.0,
            "tap_operations": 4, "vmin": 0.977, "vmax": 1.061}
    base.update(kw); return base


def rec(**omni):
    return {"zip": {"native": arm(), "omni": arm(**omni)}, "constant_power": {"native": arm(), "omni": arm(**omni)}}


def main():
    same = rec(load_energy_mwh=56200.0, losses_mwh=548.0, tap_operations=8, violation_bus_share=1e-5, vmin=0.962)
    assert P.verdict([same] * 3, "zip", "load_energy_mwh", "lower") == "**lower in all three of our runs**"
    assert P.verdict([same] * 3, "zip", "losses_mwh", "lower") == "**higher in all three of our runs**", "more losses in all three reads higher"
    assert P.verdict([same] * 3, "zip", "tap_operations", "lower") == "**higher in all three of our runs**", "the declared cost reads higher"
    assert P.verdict([same] * 3, "zip", "violation_bus_share", "never more") == "**higher in all three of our runs**", "any increase in violations reads higher"
    assert P.verdict([same] * 3, "zip", "energy_in_mwh", "lower") == "same"
    assert P.verdict([same] * 3, "zip", "vmin", "shown") == "shown, not judged"
    other = rec(load_energy_mwh=56300.0, losses_mwh=548.0, tap_operations=8)
    assert P.verdict([same, same, other], "zip", "load_energy_mwh", "lower") == "**the runs differ**", "a run that does not reproduce is a finding"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}" / "pandapower-1-MV-test--0-sw"; d.mkdir(parents=True)
            (d / "1-MV-test--0-sw.json").write_text(json.dumps(same)); dirs.append(str(d.parent))
        out = Path(t) / "V1.md"
        assert P.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "higher in all three of our runs" in txt and "lower in all three of our runs" in txt and "Not one engine's three runs" in txt and "ZIP loads" in txt
    print("PASS  power-grid A/B/C rule: reproduced runs read by sign, a run that differs is a finding, any added violation and "
          "every extra tap read higher, shown-only gauges never judged")


if __name__ == "__main__":
    main()
