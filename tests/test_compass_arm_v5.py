# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Tests for the Omni v5 law (realms/compass_arm_v5.py), the engine change that makes this tree omni-v5.

The default is the max (V5CFG): for EVERY muscle alone in the catalog, on a development seed, the omni arm does no less
work than native and is over its line no more often, hands every knob back to native before the run ends (the lease),
and acts somewhere; its energy may rise (power given). Inside an organism the bone grants the max only the power the body
can carry, and a pool never has fewer machines than its twin. The tune-down (V5SAVE, the dial turned to save) keeps its
own promise: no more energy than native, no less work, no more time over the line, on every muscle. Run directly or under
pytest. The preregistered seeds 3000-3009 are never used here.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import realms.harness as H                                   # noqa: E402
import realms.compass_arm_v5 as L                            # noqa: E402

SEED = 7100
ETOL = 1e-6          # energy may not exceed native beyond rounding (the tune-down)
WTOL = 1e-4          # work may not fall below native beyond rounding
CAT = str(ROOT / "realms" / "catalog_v5.csv")


def _harms(row, arm):
    nat = H.run_muscle_arm(row, SEED, "native")
    got = H.run_muscle_arm(row, SEED, arm)
    harms = []
    if arm == "v5save" and got["energy_j"] > nat["energy_j"] * (1 + ETOL) + 1e-9:
        harms.append(f"energy +{got['energy_j'] / nat['energy_j'] - 1:.4%}")
    if nat["work"] > 0 and got["work"] < nat["work"] * (1 - WTOL) - 1e-9:
        harms.append(f"work {got['work'] / nat['work'] - 1:.4%}")
    if got["viol"] > nat["viol"]:
        harms.append(f"over the line {got['viol'] - nat['viol']:+d}")
    if not got["restore_ok"]:
        harms.append("not handed back by the lease")
    return harms, got["writes"]


def _all_muscles(arm):
    bad, acted = [], 0
    for row in H.catalog(CAT):
        harms, writes = _harms(row, arm)
        acted += int(writes > 0)
        if harms:
            bad.append(f"{row['muscle_id']} {row['family']}/{row['muscle']} ({row['knob']}): {', '.join(harms)}")
    return bad, acted


def test_max_does_no_harm_to_any_muscle_alone():
    bad, acted = _all_muscles("v5")
    assert not bad, "the max harmed muscles vs native:\n" + "\n".join(bad[:30])
    assert acted > 0, "the max never acted on any muscle (silent no-op)"


def test_save_dial_does_no_harm_to_any_muscle_alone():
    bad, acted = _all_muscles("v5save")
    assert not bad, "the tune-down harmed muscles vs native:\n" + "\n".join(bad[:30])
    assert acted > 0


def test_max_is_the_default_and_never_shaves():
    assert L.V5CFG.dial == "max", "the engine's default brain is the max"
    assert L.V5SAVE.dial == "save"
    # a muscle native already runs flat out asks the max for nothing
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    loop = H.make_plant(rows["2121"], SEED)                  # a generating unit's steam pressure: full actuator natively
    assert L.max_ask(loop, "setpoint", L.V5CFG) is None
    assert L.max_apply(loop, "setpoint", L.V5CFG) == {}


def test_bone_never_leaves_a_pool_below_its_twin():
    # inside an organism, every pool the max holds has at least the machines its twin (native) runs, every decision
    rows = [r for r in H.catalog(CAT) if "compute_ai_cloud" in r["realms"].split(";")]
    b = H.scale_load(H.Body(rows, SEED), "climb")
    bone = L.Bone(b, L.V5CFG)
    kill = int(H.KILL_AT * H.ORGANISM_STEPS)
    for k in range(kill):
        b.couple()
        bone.advance_twin()
        L.max_body_step(b, L.V5CFG, bone)
        b.step()
        for i, tw in bone.twins.items():
            p = b.plants[i]
            assert L.machines(p) >= min(L.machines(tw), p.P["n_max"]), f"pool {rows[i]['muscle_id']} below its twin at {k}"


def test_tower_max_does_no_less_work_and_hands_back():
    rows = H.catalog(CAT)
    nat = H.run_organism_arm(rows, SEED, "native")
    mx = H.run_organism_arm(rows, SEED, "v5")
    assert sum(p["work"] for p in mx["plants"]) >= sum(p["work"] for p in nat["plants"]) * (1 - WTOL), "tower work below native"
    assert mx["restore_ok"], "the tower's knobs were not all handed back by the lease"


def test_walk_back_is_gradual_and_complete():
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    zone = H.make_plant(rows["547"], SEED)                   # a data hall's setpoint
    zone.override = {"setpoint": zone.P["t_set"] - 2.0}
    seen = []
    for left in range(H.WALK, 0, -1):
        H.walk_back(zone, left)
        seen.append(zone.override.get("setpoint", zone.P["t_set"]))
    assert seen[0] < zone.P["t_set"] and seen[-1] == zone.P["t_set"] and zone.override == {}
    assert all(b >= a - 1e-12 for a, b in zip(seen, seen[1:])), "the walk back moves one way, toward native"


if __name__ == "__main__":
    test_max_does_no_harm_to_any_muscle_alone()
    test_save_dial_does_no_harm_to_any_muscle_alone()
    test_max_is_the_default_and_never_shaves()
    test_bone_never_leaves_a_pool_below_its_twin()
    test_tower_max_does_no_less_work_and_hands_back()
    test_walk_back_is_gradual_and_complete()
    print("test_compass_arm_v5: OK")
