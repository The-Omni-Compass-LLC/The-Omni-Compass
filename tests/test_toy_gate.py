# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The toy gate (tools/toy_gate.py) runs on this checkout: each toy's workers run the shipped code against the toy, write
every gauge, and the reading of a candidate against the standing engine follows the words rule (a resource spent that
rose is power given, never a LOSS; an interval across zero is EVEN)."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import toy_gate as tg  # noqa: E402


def captured(fn, *a):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*a)
    return json.loads(buf.getvalue().strip().splitlines()[-1])


class ToyGate(unittest.TestCase):
    def test_cluster_toy_runs_both_arms(self):
        d = tempfile.mkdtemp()
        for arm in ("native", "omni"):
            r = captured(tg.worker, arm, 3, 0.1, 60.0, os.path.join(d, arm))
            for g in tg.GAUGES:
                self.assertIn(g, r)
            self.assertGreater(r["machine_hours"], 0.0)
        self.assertIn("steps_allowed", r)
        self.assertEqual(r["errors"], 0)

    def test_convey_toy_runs_both_arms(self):
        d = tempfile.mkdtemp()
        nat = captured(tg.worker_convey, "native", 2, os.path.join(d, "n"))
        omni = captured(tg.worker_convey, "omni", 2, os.path.join(d, "o"))
        for g in tg.CONVEY_GAUGES:
            self.assertIn(g, nat); self.assertIn(g, omni)
        self.assertGreaterEqual(omni["limit_given_m"], nat["limit_given_m"])    # conveyance never lowers under native

    def test_reading_follows_the_words_rule(self):
        self.assertEqual(tg.reading("machine_hours", [1.0, 1.1, 0.9, 1.2], [10.0] * 4)["word"], "power given")
        self.assertEqual(tg.reading("p95_ms", [1.0, 1.1, 0.9, 1.2], [10.0] * 4)["word"], "LOSS")
        self.assertEqual(tg.reading("p95_ms", [-1.0, -1.1, -0.9, -1.2], [10.0] * 4)["word"], "GAIN")
        self.assertEqual(tg.reading("p95_ms", [-1.0, 1.1, -0.9, 1.2], [10.0] * 4)["word"], "EVEN")
        self.assertEqual(tg.reading("requests_served", [1.0, 1.1, 0.9, 1.2], [10.0] * 4, tg.CONVEY_GAUGES)["word"], "GAIN")


if __name__ == "__main__":
    unittest.main()
