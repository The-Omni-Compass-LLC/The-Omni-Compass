# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The core's Monte Carlo from the jump generator: every record reproduces its digest, and the live engine's port of the core gives the same."""
import json
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import tools.core_runs as R  # noqa: E402
from omnicompass import core as C  # noqa: E402


class CoreRuns(unittest.TestCase):
    def test_the_draws_are_the_ranges(self):
        """Run k's state and parameters come from its own stream, inside the ranges benchmarks/core_evidence.py draws."""
        for k in range(20):
            seed, x0, p = R.draw(k, 20261024)
            self.assertEqual(seed, (20261024 + k * 0x9E3779B9) % 2 ** 32)
            for v, (lo, hi) in zip(x0.as_tuple(), R.STATE_RANGES):
                self.assertTrue(lo <= v <= hi)
            for name, (lo, hi) in C.PARAMETER_RANGES.items():
                self.assertTrue(lo <= getattr(p, name) <= hi, name)
        self.assertEqual(R.draw(3, 7)[1], R.draw(3, 7)[1])

    def test_a_run_is_the_core(self):
        """Each way of a run is omnicompass/core.simulate itself, its convey and cert steps as the core counts them."""
        r = R.one(0, 20261024)
        seed, x0, p = R.draw(0, 20261024)
        s = C.simulate(x0, p)
        self.assertEqual(r["controlled"]["U"], [float(u) for u in s.U_hist])
        self.assertEqual(r["controlled"]["convey"], s.convey_confirm if s.convey else 0)
        self.assertEqual(len(r["uncontrolled"]["U"]), C.MACRO_STEPS + 1)
        self.assertEqual(R.canonical([r]).count("\n") + 1, len(R.WAYS))

    def test_every_record_reproduces(self):
        recs = sorted((ROOT / "results" / "core_runs").glob("CORE_RUNS_*.json"))
        self.assertTrue(recs, "no record of the core's Monte Carlo")
        rec = json.loads(recs[-1].read_text(encoding="utf-8"))
        runs = [R.one(k, rec["base"]) for k in range(rec["runs"])]
        self.assertEqual(R.digest(runs), rec["digest"])
        self.assertEqual(R.summary(runs), rec["summary"])

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_the_pages_port_is_the_pythons(self):
        self.assertEqual(R.verify(ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html", 60, 1369407155), 0)


if __name__ == "__main__":
    unittest.main()
