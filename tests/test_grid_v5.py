# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid's one page (tools/grid_v5.py): every square from the pooled receipts, nothing recomputed, a missing square
said, and the runs each half was pooled from named."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import grid_v5  # noqa: E402


def square(m, label="FEWER MISSES", runs=10):
    return {"runs": runs, "of": runs, "label": label, "band_first": "held", "viol_pp": [m, m - 0.01, m + 0.01],
            "work": [0.0, 0.0, 0.0], "energy": [0.0005, 0.0004, 0.0006], "primary": [0, 0, 0]}


class Grid(unittest.TestCase):
    def test_every_square_from_the_receipts(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            m = t / "run-111" / "six-pooled-v5-x10"; m.mkdir(parents=True)
            summary = {n: {o: square(-0.1, runs=int(n)) for o in grid_v5.ORGS} for n in grid_v5.RUNS}
            del summary["100"]["tower"]                                         # a square the receipt lacks
            (m / "SIX_v5-x10.json").write_text(json.dumps({"scale": 10, "summary": summary}))
            k = t / "run-222" / "six-kube-pooled-v5-x10"; k.mkdir(parents=True)
            (k / "SIX_KUBE_v5-x10_r10.json").write_text(json.dumps({"organisms": {
                "stack@10": {"arm": "compass", "repetitions": 10, "verdict": "better: p95 (inside the noise)", "rows": {}}}}))
            out = t / "GRID.md"
            self.assertEqual(grid_v5.main(["--modelled", str(t / "run-111"), "--kube", str(t / "run-222"), "--out", str(out)]), 0)
            text = out.read_text()
            self.assertIn("10 copies: run 111", text)
            self.assertIn("10 copies: run 222", text)
            self.assertIn("FEWER MISSES: misses -0.100 pp, work +0.000%, power given +0.050% (10 of 10 runs)", text)
            self.assertIn("not in the receipt", text)                            # the tower at 100 runs
            self.assertIn("better: p95 (inside the noise) (10 repetitions)", text)
            self.assertIn("not in the report", text)
            self.assertIn("No outside party has reviewed or approved these results.", text)
            data = json.loads(out.with_suffix(".json").read_text())
            self.assertIsNone(data["modelled"]["tower@10"]["100"])
            self.assertEqual(data["kube"]["stack@10"]["10"]["repetitions"], 10)


if __name__ == "__main__":
    unittest.main()
