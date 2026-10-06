# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The CityLearn A/B/C rule (tools/citylearn_abc.py, docs/OMNI_V1.md): a deterministic simulator, so the three runs must
reproduce each other; a score reads confirmed better or WORSE by its sign when they do, same under one part in a million,
and "the runs differ" when they do not; a district with no electric battery is listed as nothing for Omni to move, and a
district CityLearn cannot run is listed with its error, never dropped."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import citylearn_abc as C
from tools.run_citylearn import KPIS

COST, PEAK = "cost_total", "daily_peak_average"


def arm(name, batteries, **kpis):
    base = {k: 1.0 for k in KPIS}; base.update(kpis)
    return {"arm": name, "buildings": 3, "steps": 720, "batteries": batteries, "thermal_stores_left_native": 1,
            "seconds": 1.0, "moved_hours": 100, "handed_back": True, "kpis": base}


def rec(batteries, omni_cost, omni_peak):
    return {"native": arm("native", batteries), "omni": arm("omni", batteries, **{COST: omni_cost, PEAK: omni_peak}),
            "citylearn_version": "3.0.2", "settings": {}}


def write(root, run, districts):
    d = Path(root) / f"run-{run}"
    for name, r in districts.items():
        (d / f"citylearn-{name}").mkdir(parents=True)
        (d / f"citylearn-{name}" / f"{name}.json").write_text(json.dumps(r))
    return d


def main():
    same = rec(3, 0.98, 1.03)                               # cost 2% lower, daily peak 3% higher, every run alike
    assert C.verdict([same] * 3, COST) == "**confirmed better**"
    assert C.verdict([same] * 3, PEAK) == "**confirmed WORSE**", "a loss in all three is shown as WORSE"
    assert C.verdict([same] * 3, "carbon_emissions_total") == "same"
    other = rec(3, 0.98, 1.03); other["omni"]["kpis"][COST] = 0.97
    assert C.verdict([same, same, other], COST) == "**the runs differ**", "a run that does not reproduce is a finding"
    tiny = rec(3, 1.0 + 1e-7, 1.0)
    assert C.verdict([tiny] * 3, COST) == "same", "a change under one part in a million"
    with tempfile.TemporaryDirectory() as t:
        broken = {"native": {"error": "ValueError: needs interface='entity'"}, "omni": {"error": "ValueError: needs interface='entity'"}}
        dirs = [write(t, i, {"d_bat": same, "d_nobat": rec(0, 1.0, 1.0), "d_broken": broken}) for i in (1, 2, 3)]
        out = Path(t) / "V1.md"
        assert C.main([str(d) for d in dirs] + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "| d_nobat | 3 | 1 | none | yes |" in txt, "no battery: nothing for Omni to move"
        assert "| d_broken | `ValueError: needs interface='entity'` |" in txt, "a district CityLearn cannot run is listed"
        assert "confirmed WORSE" in txt and "confirmed better" in txt and "Not a v1 confirmation" in txt
    print("PASS  CityLearn A/B/C rule: reproduced runs read by sign, a run that differs is a finding, no battery means nothing to move, "
          "a district CityLearn cannot run is listed")


if __name__ == "__main__":
    main()
