# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Do-no-harm test for the Omni v5 compass law (realms/compass_arm_v5.py), the engine change that makes this tree omni-v5.

The v5 law's default (V5CFG) must make the no-harm promise true: on a fixed seed, for EVERY muscle in the catalog, the v5
arm uses no more energy than native, does no less work, and is in violation no more often; it hands every knob back to
native on the kill (the dead-man lease); and it acts somewhere (it is not a silent no-op). The whole tower, as one
organism, is no worse than native on energy and work. Run directly or under pytest.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import realms.harness as H                                   # noqa: E402
from realms.compass_arm_v5 import V5CFG, apply_v5            # noqa: E402  (the in-engine v5 law and its default config)

SEED = 3000
ETOL = 1e-6          # energy may not exceed native beyond rounding
WTOL = 1e-4          # work may not fall below native beyond rounding


def _muscle_harms(row):
    nat = H.run_muscle_arm(row, SEED, "native")
    v5 = H.run_muscle_arm(row, SEED, "v5")
    harms = []
    if v5["energy_j"] > nat["energy_j"] * (1 + ETOL) + 1e-9:
        harms.append(f"energy +{v5['energy_j'] / nat['energy_j'] - 1:.4%}")
    if nat["work"] > 0 and v5["work"] < nat["work"] * (1 - WTOL) - 1e-9:
        harms.append(f"work {v5['work'] / nat['work'] - 1:.4%}")
    if v5["viol"] / max(1, v5["steps"]) > nat["viol"] / max(1, nat["steps"]) + 1e-9:
        harms.append("violations up")
    if not v5["restore_ok"]:
        harms.append("did not hand back on kill")
    return harms, v5["writes"]


def test_v5_default_does_no_harm_to_any_muscle():
    rows = H.catalog(str(ROOT / "realms" / "catalog_v5.csv"))   # the v5 muscle set (1,002)
    bad, acted = [], 0
    for row in rows:
        harms, writes = _muscle_harms(row)
        acted += int(writes > 0)
        if harms:
            bad.append(f"{row['muscle_id']} {row['family']}/{row['muscle']} ({row['knob']}): {', '.join(harms)}")
    assert not bad, "v5 default harmed muscles vs native:\n" + "\n".join(bad[:30])
    assert acted > 0, "v5 default never acted on any muscle (silent no-op)"


def test_v5_tower_is_no_worse_than_native():
    rows = H.catalog(str(ROOT / "realms" / "catalog_v5.csv"))
    nat = H.run_organism_arm(rows, SEED, "native")
    v5 = H.run_organism_arm(rows, SEED, "v5")
    assert sum(v5["plants"][i]["energy_j"] for i in range(len(v5["plants"]))) <= \
        sum(nat["plants"][i]["energy_j"] for i in range(len(nat["plants"]))) * (1 + 1e-6), "v5 tower energy above native"
    assert sum(p["work"] for p in v5["plants"]) >= sum(p["work"] for p in nat["plants"]) * (1 - 1e-4), \
        "v5 tower work below native"
    assert v5["restore_ok"], "v5 tower did not hand every knob back on the kill"


def test_v5_default_config_present():
    # the engine default is the no-harm configuration, and apply_v5 uses it: every process loop free under its own reach,
    # the power cap only where a pool's response line outlasts a decision, the battery shave and a cloud pool's machine
    # hand-back held native
    assert V5CFG.loop_reach is True, "a process loop's setpoint must be held by its own reach"
    assert V5CFG.storage_shave is False, "the battery shave trades round-trip energy for service: native in the default"
    assert V5CFG.ca_release is False, "a cloud pool's machine hand-back is permanent: the autoscaler's own in the default"
    assert callable(apply_v5)


def test_v5_power_cap_only_on_long_line_pools():
    # a pool whose response line is shorter than one decision keeps its own power cap; a batch pool's cap may move
    from realms.compass_arm_v5 import lever_v5
    rows = {r["muscle_id"]: r for r in H.catalog(str(ROOT / "realms" / "catalog_v5.csv"))}
    interactive = H.make_plant(rows["130"], SEED)          # gpu_power_limit: a 2 s line, 15 s decisions
    batch = H.make_plant(rows["1070"], SEED)               # node_power_saving on a batch queue: a 300 s line
    assert lever_v5(interactive, "power", V5CFG) is None, "an interactive pool's cap must stay native"
    assert lever_v5(batch, "power", V5CFG) is not None, "a batch pool's cap is free under the drop and latency floors"


def test_v5_every_generation_loop_is_free():
    # no blanket gate: a generating unit's steam/speed/gate loop moves inside its band like any loop, held by its reach
    from realms.compass_arm_v5 import lever_v5
    rows = {r["muscle_id"]: r for r in H.catalog(str(ROOT / "realms" / "catalog_v5.csv"))}
    turbine = H.make_plant(rows["2121"], SEED)             # boiler_steam_pressure_setpoint
    assert lever_v5(turbine, "setpoint", V5CFG) is not None


if __name__ == "__main__":
    test_v5_default_does_no_harm_to_any_muscle()
    test_v5_tower_is_no_worse_than_native()
    test_v5_default_config_present()
    test_v5_power_cap_only_on_long_line_pools()
    test_v5_every_generation_loop_is_free()
    print("test_compass_arm_v5: OK")
