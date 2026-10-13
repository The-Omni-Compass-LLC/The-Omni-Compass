# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The benefit sheet (tools/benefit_sheet.py): one number per benchmark, plus always toward the system's declared aims, read
from the tables."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import benefit_sheet as bs  # noqa: E402


class TheSheet(unittest.TestCase):
    def test_the_words_and_the_numbers(self):
        self.assertEqual(bs.benefit_word(3, 0), "yes")
        self.assertEqual(bs.benefit_word(0, 2), "no")
        self.assertEqual(bs.benefit_word(0, 0), "none")
        self.assertEqual(bs.benefit_word(2, 1), "trade")
        self.assertEqual(bs.fmt_pct(0.02), "0%")
        self.assertEqual(bs.fmt_pct(-24.9), "-25%")
        self.assertEqual(bs.fmt_pct(4.04), "+4.0%")
        self.assertEqual(bs.fmt_pct(None), "no number")

    def test_a_fall_in_a_gauge_that_aims_lower_reads_plus(self):
        rows = [["Gauge", "native (A)", "omni (A)", "A", "B", "C", "Reading"],
                ["energy (J)", "100", "80", "-20.0%", "-20.0%", "-20.0%", "**lower in all three of our runs**"],
                ["work (units)", "100", "110", "+10.0%", "+10.0%", "+10.0%", "**higher in all three of our runs**"],
                ["taps", "4", "8", "+100.0%", "+100.0%", "+100.0%", "**higher in all three of our runs**"],
                ["noise", "1", "1", "+1.0%", "-1.0%", "+0.5%", "no difference beyond the noise (3 of 3 runs)"]]
        aims = {"energy (J)": True, "work (units)": False, "taps": True, "noise": True}   # True: the gauge aims lower
        r, toward, away = bs.sim_case_ratio(rows, aims)
        self.assertEqual((toward, away), (2, 1))
        self.assertAlmostEqual(r, (1.25 * 1.10 * 0.5 * 1.0) ** 0.25, places=9, msg="less energy is plus, more work is plus, more taps is minus, noise is one")
        self.assertEqual(bs.in_words([("p95", "toward", "-65% to -71%"), ("memory", "away", "+215%")]),
                         "p95 lower 65% to 71% (toward its aim); memory higher 215% (away from its aim)")
        self.assertEqual(bs.fmt_pct_words(31.0), "+31% toward the aims")
        self.assertEqual(bs.fmt_pct_words(-25.0), "-25% away from the aims")

    def test_the_published_sheet_is_what_the_tables_give(self):
        self.assertEqual(bs.main(check=True), 0)


if __name__ == "__main__":
    unittest.main()
