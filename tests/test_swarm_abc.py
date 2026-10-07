# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The drone swarms' A/B/C rule (tools/swarm_abc.py): a deterministic simulator, so the three runs must reproduce; a gauge
reads confirmed better or WORSE by its own direction when they do (lower, higher, never more, never less), same under one
part in a million, "the runs differ" when they do not; a late mission, a reserve breach or a near miss added is WORSE; a
cell the paired trial left native is nothing for Omni to move; a cell with a collision is void; the tuning cell is shown
and not counted."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import swarm_abc as M


def arm(**kw):
    base = {"energy_per_mission_j": 450.0, "fleet_energy_j": 9000.0, "missions_per_charge": 5.9, "late_share": 0.0, "reserve_breaches": 0,
            "near_miss_ticks": 0, "min_separation_m": 0.37, "tracking_rms_m": 0.07, "mission_s": 20.0, "airborne_s": 19.0, "override_mean": 1.0,
            "collisions": 0, "handed_back": True, "missions_flown": 20}
    base.update(kw); return base


def rec(cell="mixed", moves=True, void=False, tuning=False, **omni):
    o = arm(**omni)
    return {"cell": cell, "drones": 20, "missions_per_drone": 4, "distance_m": [3.0, 8.0], "tuning": tuning, "omni_moves": moves, "void": void,
            "physics_trial": {"planner_cruise": arm(), "override_1.25": arm(energy_per_mission_j=400.0), "faster_is_cheaper": moves},
            "native": arm(collisions=1 if void else 0), "omni": o}


def main():
    better = rec(energy_per_mission_j=380.0, fleet_energy_j=7700.0, missions_per_charge=7.0, tracking_rms_m=0.14, min_separation_m=0.18, override_mean=1.5, mission_s=15.0)
    assert M.verdict([better] * 3, "energy_per_mission_j", "lower") == "**confirmed better**"
    assert M.verdict([better] * 3, "missions_per_charge", "higher") == "**confirmed better**", "more missions a charge is better"
    assert M.verdict([better] * 3, "late_share", "never more") == "same"
    assert M.verdict([better] * 3, "min_separation_m", "shown") == "shown, not judged"
    worse = rec(late_share=0.05, reserve_breaches=1, near_miss_ticks=3, missions_per_charge=5.0)
    assert M.verdict([worse] * 3, "late_share", "never more") == "**confirmed WORSE**", "a late mission added is WORSE"
    assert M.verdict([worse] * 3, "reserve_breaches", "never more") == "**confirmed WORSE**"
    assert M.verdict([worse] * 3, "near_miss_ticks", "never more") == "**confirmed WORSE**"
    assert M.verdict([worse] * 3, "missions_per_charge", "higher") == "**confirmed WORSE**", "fewer missions a charge is WORSE"
    other = rec(energy_per_mission_j=381.0)
    assert M.verdict([better, better, other], "energy_per_mission_j", "lower") == "**the runs differ**"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("mixed", better), ("tuning", rec("tuning", tuning=True, energy_per_mission_j=390.0)),
                            ("short", rec("short", moves=False)), ("long", rec("long", void=True))):
                (d / f"swarm-{name}").mkdir(parents=True); (d / f"swarm-{name}" / f"swarm-{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V3.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "### mixed" in txt and "### tuning" in txt and "confirmed better" in txt
        assert "| short | 450.0 | 400.0 | yes |" in txt, "the cell the trial left native is listed as nothing to move"
        assert "| long | a collision in an arm" in txt, "a collision voids the cell"
        across = txt[txt.index("## Across the untouched cells"):txt.index("## Cells where the paired trial")]
        assert "| energy per mission (J, declared model: motors and avionics over the fleet window) | 1 | 0 | 0 | 0 |" in across, "the tuning cell is not counted"
        assert "Not a confirmation on one frozen engine" in txt
    print("PASS  drone swarms A/B/C rule: reproduced runs read by each gauge's direction, a run that differs is a finding, a late mission, "
          "a reserve breach or a near miss added reads WORSE, a cell left native is nothing to move, a collision voids the cell, the tuning cell is not counted")


if __name__ == "__main__":
    main()
