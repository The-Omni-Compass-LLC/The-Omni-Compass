# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The decision period (the founder's orders of 14 October, night: faster than every native controller, but only where it
hurts nothing). The fast checks run every 5 s, three times as fast as the HPA's own 15-second check; the full decision
stays at the tested 60 s, because the give-back trial counts its phase in decisions: at a period too short the phase ends
before it has measured the response times it needs, every trial is abandoned, and no machine is ever given back."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE_CHECK_S = 15.0          # the HPA's own sync period on a managed cluster (fixed by the provider)
PROBE_MAX_PER_S = 1.0          # scripts/latency_probe.py: 5 requests, then a 5 s pause: at most one response time a second


def fast_checks_per_decision(interval, floor):
    """The controller's own spacing (omni_controller/controller.py, main): it sleeps in steps of the floor interval and runs
    a fast check after every step that ends before the next decision."""
    waited, n = 0.0, 0
    while waited + 1e-9 < interval:
        waited += min(floor, interval - waited)
        if waited + 1e-9 < interval:
            n += 1
    return n


def trial_phase_s(interval):
    """A give-back trial's phase in seconds: max_trial decisions (written in the controller) at this period."""
    src = (ROOT / "omni_controller" / "controller.py").read_text()
    return int(re.search(r"max_trial=(\d+)", src).group(1)) * interval


def samples_needed():
    src = (ROOT / "omni_controller" / "controller.py").read_text()
    return int(re.search(r'getattr\(a, "verdict_samples", (\d+)\)', src).group(1))


def periods(env):
    """The periods a run hands the governor: the run's own, else the rig's defaults (scripts/kind_bench.sh)."""
    rig = (ROOT / "scripts" / "kind_bench.sh").read_text()
    d_i = float(re.search(r'OMNI_INTERVAL="\$\{OMNI_INTERVAL:-([0-9.]+)\}"', rig).group(1))
    d_f = float(re.search(r'OMNI_FLOOR_INTERVAL="\$\{OMNI_FLOOR_INTERVAL:-([0-9.]+)\}"', rig).group(1))
    i = re.search(r"OMNI_INTERVAL: '([0-9.]+)'", env); f = re.search(r"OMNI_FLOOR_INTERVAL: '([0-9.]+)'", env)
    return (float(i.group(1)) if i else d_i), (float(f.group(1)) if f else d_f)


class DecisionPeriod(unittest.TestCase):
    def setUp(self):
        self.interval, self.floor = periods((ROOT / ".github" / "workflows" / "aks-metered.yml").read_text())

    def test_the_fast_checks_run_faster_than_native_and_between_every_decision(self):
        self.assertLess(self.floor, NATIVE_CHECK_S)
        self.assertGreaterEqual(fast_checks_per_decision(self.interval, self.floor), 1)

    def test_a_give_back_trial_has_time_to_measure_what_it_needs(self):
        need_s = samples_needed() / PROBE_MAX_PER_S
        self.assertGreaterEqual(trial_phase_s(self.interval), need_s)
        # the trap found before any run (14 October): at 5 s a phase lasts 100 s, every trial would be abandoned, the
        # bill could never fall; and a 5 s decision with 5 s checks would run no fast check at all
        self.assertLess(trial_phase_s(5.0), need_s)
        self.assertEqual(fast_checks_per_decision(5.0, 5.0), 0)

    def test_the_rig_passes_both_periods_to_the_governor(self):
        s = (ROOT / "scripts" / "kind_bench.sh").read_text()
        self.assertIn('--interval "$OMNI_INTERVAL" --floor-interval "$OMNI_FLOOR_INTERVAL"', s)
        self.assertIn("want=$(( DURATION / 60 - 1 ))", s)          # a silent window still needs a decision a minute


if __name__ == "__main__":
    unittest.main()
