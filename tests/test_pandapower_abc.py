# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""The power grid's A/B/C rule (tools/pandapower_abc.py, docs/OMNI_V1.md): a deterministic simulator, so the three runs must
reproduce; a gauge reads confirmed better or WORSE by its sign when they do, same under one part in a million, and "the
runs differ" when they do not; any increase in voltage violations is WORSE; more tap operations is WORSE (the declared
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
    assert P.verdict([same] * 3, "zip", "load_energy_mwh", "lower") == "**confirmed better**"
    assert P.verdict([same] * 3, "zip", "losses_mwh", "lower") == "**confirmed WORSE**", "more losses in all three is shown as WORSE"
    assert P.verdict([same] * 3, "zip", "tap_operations", "lower") == "**confirmed WORSE**", "the declared cost still reads WORSE"
    assert P.verdict([same] * 3, "zip", "violation_bus_share", "never more") == "**confirmed WORSE**", "any increase in violations is WORSE"
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
        assert "confirmed WORSE" in txt and "confirmed better" in txt and "Not a v1 confirmation" in txt and "ZIP loads" in txt
    print("PASS  power-grid A/B/C rule: reproduced runs read by sign, a run that differs is a finding, any added violation and "
          "every extra tap read WORSE, shown-only gauges never judged")


if __name__ == "__main__":
    main()
