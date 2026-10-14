# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The cloud's decision period (the founder's orders of 14 October, night): the governor decides every 5 s on Azure, never
slower than the native controller's own 15-second check, and its fast checks (the scheduling floor, the pod reflex,
conveyance on every third) still run between decisions, with conveyance no slower than at the 60-second decision."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE_CHECK_S = 15.0          # the HPA's own sync period on a managed cluster (fixed by the provider)


def fast_checks_per_decision(interval, floor):
    """The controller's own spacing (omni_controller/controller.py, main): it sleeps in steps of the floor interval and runs
    a fast check after every step that ends before the next decision."""
    waited, n = 0.0, 0
    while waited + 1e-9 < interval:
        waited += min(floor, interval - waited)
        if waited + 1e-9 < interval:
            n += 1
    return n


def convey_period(interval, floor):
    """Conveyance runs on every third fast check (controller.py, floor_step)."""
    n = fast_checks_per_decision(interval, floor)
    return float("inf") if n == 0 else 3 * interval / n


class CloudCadence(unittest.TestCase):
    def setUp(self):
        y = (ROOT / ".github" / "workflows" / "aks-metered.yml").read_text()
        self.interval = float(re.search(r"OMNI_INTERVAL: '([0-9.]+)'", y).group(1))
        self.floor = float(re.search(r"OMNI_FLOOR_INTERVAL: '([0-9.]+)'", y).group(1))

    def test_the_cloud_decides_every_five_seconds_never_slower_than_native(self):
        self.assertEqual(self.interval, 5.0)
        self.assertLessEqual(self.interval, NATIVE_CHECK_S)

    def test_the_fast_checks_still_run_and_conveyance_is_no_slower_than_at_sixty_seconds(self):
        self.assertLess(self.floor, self.interval)
        self.assertGreaterEqual(fast_checks_per_decision(self.interval, self.floor), 1)
        self.assertLessEqual(convey_period(self.interval, self.floor), convey_period(60.0, 5.0))
        # the trap the 2.5 s checks avoid: a 5 s decision with 5 s checks runs none, a 10 s decision conveys every 30 s
        self.assertEqual(fast_checks_per_decision(5.0, 5.0), 0)
        self.assertEqual(convey_period(10.0, 5.0), 30.0)

    def test_the_rig_passes_both_periods_to_the_governor(self):
        s = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('--interval "$OMNI_INTERVAL" --floor-interval "$OMNI_FLOOR_INTERVAL"', s)
        self.assertIn("want=$(( DURATION / 60 - 1 ))", s)          # a silent window still needs a decision a minute


if __name__ == "__main__":
    unittest.main()
