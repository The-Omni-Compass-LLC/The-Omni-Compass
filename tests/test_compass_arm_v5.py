# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Smoke and do-no-harm test for the Omni v5 compass law (realms/compass_arm_v5.py), additive beside frozen v3.

Not part of verify.py --quick yet (the v5 engine is not frozen); run directly or under pytest. It proves the v5 module
imports and runs in-repo on real presets, produces finite meters, and on a fixed seed does no harm to the modelled
organism against native: work is not materially below native and energy is not above it."""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import realms.harness as H                                    # noqa: E402
from realms.compass_arm_v5 import compass_apply_v5, Cfg       # noqa: E402
from tools.run_scale import rows_for, ORGS                    # noqa: E402

CFG = dict(target_free=False, est=2, learn_fall=0.1, hybrid=True, physics_memory=True,
           motion_safe=True, band=True, drop_guard=True, hole_guard=True)


def _run(rows, seed, arm, cfg):
    b = H.Body(rows, seed)
    kill_at = int(H.KILL_AT * H.ORGANISM_STEPS)
    acted = False
    for k in range(H.ORGANISM_STEPS):
        b.couple()
        if arm == "v5":
            for p, knob in zip(b.plants, b.knobs):
                if k >= kill_at:
                    p.override = {}
                    continue
                compass_apply_v5(p, knob, cfg)
                acted = acted or bool(p.override)
        b.step()
    for p in b.plants:
        p.finalize()
    return b.plants, acted


def main(organisms=("1", "2"), seed=7000):
    cfg = Cfg(**CFG)
    for o in organisms:
        rows = rows_for(ORGS[o][0], 1)
        nat, _ = _run(rows, seed, "native", cfg)
        v5, acted = _run(rows, seed, "v5", cfg)
        assert all(math.isfinite(p.m["energy_j"]) and math.isfinite(p.m["work"]) for p in v5), "v5 produced non-finite meters"
        ne = sum(p.m["energy_j"] for p in nat); e = sum(p.m["energy_j"] for p in v5)
        nw = sum(p.m["work"] for p in nat); w = sum(p.m["work"] for p in v5)
        assert e <= ne * (1 + 1e-6), f"{o}: v5 energy above native ({e:.1f} > {ne:.1f})"
        assert w >= nw * (1 - 1e-4), f"{o}: v5 work materially below native ({w:.1f} < {nw:.1f})"
        assert acted, f"{o}: v5 never acted"
    return True


def test_compass_arm_v5_no_harm():
    assert main()


if __name__ == "__main__":
    main()
    print("test_compass_arm_v5: OK")
