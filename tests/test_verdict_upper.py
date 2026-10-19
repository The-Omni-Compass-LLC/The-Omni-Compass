# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict's upper end (v12, judge="upper"): a step is kept only when the upper end of its 95% interval is inside the
allowance; each phase measures as many pieces of work as a free step needs to show that; a trial that could not be read
in its time is never started."""
import math
import random
import unittest

from omnicompass.verdict import Verdict, pieces_needed, Z95, Z_FREE


def trial(rise, rate, seed, tol=0.02, spread=0.25, max_trial=40, decisions=120):
    """One give-back trial on lognormal work: (the verdict's last event, the steps the knob stood at)."""
    rng = random.Random(seed)
    v = Verdict(tolerance=tol, min_samples=60, probe_every=1, recheck=10 ** 6, max_trial=max_trial)
    step, ev, stood = 0, None, []
    for _ in range(decisions):
        v.observe([10.0 * (1.0 + rise * step) * rng.lognormvariate(0.0, spread) for _ in range(rate)])
        step, _, ev = v.tick(True)
        stood.append(step)
        if ev and str(ev.get("verdict", "")).startswith(("step", "trial not started")):
            return ev, stood, v
    return ev, stood, v


class Upper(unittest.TestCase):
    def test_the_pieces_a_free_step_needs(self):
        rng = random.Random(1)
        xs = [math.exp(rng.gauss(0.0, 0.25)) for _ in range(5000)]
        s2 = (0.25 ** 2)
        want = 2 * s2 * (Z95 + Z_FREE) ** 2 / math.log(1.02) ** 2
        self.assertAlmostEqual(pieces_needed(xs, 0.02, 60) / want, 1.0, delta=0.06)
        self.assertEqual(pieces_needed([1.0] * 100, 0.02, 60), 60)          # no spread: never fewer than min_samples
        self.assertEqual(pieces_needed([1.0], 0.02, 60), math.inf)          # one piece: no spread known

    def test_fast_work_keeps_a_free_step_and_refuses_a_step_past_the_allowance(self):
        kept = {rise: sum(trial(rise, 200, s)[0]["verdict"] == "step allowed" for s in range(100)) for rise in (0.0, 0.03)}
        self.assertGreaterEqual(kept[0.0], 90)
        self.assertLessEqual(kept[0.03], 2)

    def test_a_step_is_read_once_at_its_pieces(self):
        ev, _, v = trial(0.0, 200, 3)
        self.assertTrue(ev["verdict"].startswith("step "))
        self.assertGreaterEqual(ev["pieces"], v.min_n)
        self.assertLess(ev["pieces"], 200 * 40)

    def test_slow_work_never_starts_a_trial_and_the_knob_stays_where_it_is_allowed(self):
        ev, stood, v = trial(0.0, 20, 1)
        self.assertEqual(ev["verdict"], "trial not started: the work too noisy to read the step in a trial's time")
        self.assertGreater(ev["pieces_needed"], 20 * 40)
        self.assertEqual(v.allowed, 0)
        self.assertEqual(v.phase, None)
        self.assertEqual(set(stood), {0})                                   # the knob never left native

    def test_the_interval_judge_is_kept_by_name(self):
        rng = random.Random(2)
        v = Verdict(tolerance=0.02, min_samples=60, probe_every=1, recheck=10 ** 6, max_trial=40, judge="interval")
        for _ in range(10):
            v.observe([10.0 * rng.lognormvariate(0.0, 0.25) for _ in range(20)])
            _, _, ev = v.tick(True)
            self.assertFalse(ev and str(ev.get("verdict", "")).startswith("trial not started"))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
