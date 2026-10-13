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
                "stack@10": {"arm": "compass", "repetitions": 10, "verdict": "better on 3, worse on 0, inside the noise on 9", "rows": {}},
                "tower@10": {"arm": "compass", "repetitions": 10, "verdict": "better on 2, worse on 1 (energy), inside the noise "
                             "on 9; OFF THE CLOCK in 2 of 10 repetitions", "rows": {}}}}))
            out = t / "GRID.md"
            self.assertEqual(grid_v5.main(["--modelled", str(t / "run-111"), "--kube", str(t / "run-222"), "--out", str(out)]), 0)
            text = out.read_text()
            self.assertIn("10 copies: run 111", text)
            self.assertIn("10 copies: run 222", text)
            self.assertIn("FEWER MISSES: misses -0.100 pp, work +0.000%, power given +0.050% (10 of 10 runs)", text)
            self.assertIn("not in the receipt", text)                            # the tower at 100 runs
            self.assertIn("| 10 repetitions: better on 3, worse on 0, inside the noise on 9 |", text)
            self.assertIn("not in the report", text)
            # the one line the front page reads, counted from the squares (17 modelled: 11 of 10 and 100 runs, 6 single)
            self.assertIn("**Across the grid: modelled, 11 of 11 squares of 10 and 100 runs FEWER MISSES; the 6 single runs: "
                          "6 with fewer misses; work +0.000%; power given +0.050%; with the cluster "
                          "inside, 2 squares: 0 single repetitions (no reading); of the 2 of 10 and 100 repetitions, worse on "
                          "no gauge in 1, the gauges read worse: \"energy\" in 1; off the clock in 1; invalid in 0.**", text)
            self.assertEqual(grid_v5.worse_gauges("better on 5, worse on 2 (HPA replicas, mean; response time (ms), 95th "
                                                  "percentile), inside the noise on 2; OFF THE CLOCK in 1 of 100 repetitions"),
                             ["HPA replicas, mean", "response time (ms), 95th percentile"])
            self.assertEqual(grid_v5.worse_gauges("better on 4, worse on 0, inside the noise on 5"), [])
            self.assertIsNone(grid_v5.worse_gauges("ONE REPETITION"))
            self.assertIn("No outside party has reviewed or approved these results.", text)
            # every receipt's page linked from the grid page's own folder (a relative link resolves from the page)
            self.assertIn("](run-111/six-pooled-v5-x10/SIX_v5-x10.md)", text)
            self.assertIn("](run-222/six-kube-pooled-v5-x10/SIX_KUBE_v5-x10_r10.md)", text)
            data = json.loads(out.with_suffix(".json").read_text())
            self.assertIsNone(data["modelled"]["tower@10"]["100"])
            self.assertEqual(data["kube"]["stack@10"]["10"]["repetitions"], 10)


if __name__ == "__main__":
    unittest.main()
