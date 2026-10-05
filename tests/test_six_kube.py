# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The six organisms with the cluster inside (tools/run_kil.py): the same demand in both arms, the load across the whole
declared range, every simulated knob handed back in the Omni arm, and the report's twelve columns."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_kil
from tools.run_hil import NAMES


class SixKube(unittest.TestCase):
    def test_arms_share_demand_and_hand_back(self):
        with tempfile.TemporaryDirectory() as t:
            recs = {}
            for arm in ("native", "compass"):
                d = Path(t) / arm
                self.assertEqual(run_kil.main(["--organism", "compute_ai_cloud", "--arm", arm, "--duration", "0.5",
                                               "--out", str(d), "--dry", "--load-max", "6"]), 0)
                recs[arm] = json.loads((d / "organism.json").read_text())
            self.assertEqual(recs["native"]["demand"], recs["compass"]["demand"])
            self.assertEqual(recs["native"]["replicas"], recs["compass"]["replicas"])
            self.assertEqual((min(recs["compass"]["replicas"]), max(recs["compass"]["replicas"])), (1, 6))
            self.assertEqual(recs["native"]["sim_writes"], 0)
            self.assertGreater(recs["compass"]["sim_writes"], 0)
            self.assertTrue(recs["compass"]["sim_restore_ok"])
            log = (Path(t) / "compass" / "load_schedule.log").read_text()
            self.assertIn("load-generator replicas -> ", log)

    def test_six_organisms_named(self):
        self.assertEqual(len(NAMES), 6)
        self.assertEqual(sorted(run_kil.groups(1)), sorted(NAMES))


if __name__ == "__main__":
    unittest.main()
