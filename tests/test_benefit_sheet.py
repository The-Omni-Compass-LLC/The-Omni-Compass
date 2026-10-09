# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The benefit sheet (tools/benefit_sheet.py): one number per benchmark, plus always good for Omni, read from the tables."""
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

    def test_a_fall_in_a_lower_is_better_gauge_reads_plus(self):
        rows = [["Gauge", "native (A)", "omni (A)", "A", "B", "C", "Reading"],
                ["energy (J)", "100", "80", "-20.0%", "-20.0%", "-20.0%", "**confirmed better**"],
                ["work (units)", "100", "110", "+10.0%", "+10.0%", "+10.0%", "**confirmed better**"],
                ["taps", "4", "8", "+100.0%", "+100.0%", "+100.0%", "**confirmed WORSE**"],
                ["noise", "1", "1", "+1.0%", "-1.0%", "+0.5%", "no difference beyond the noise (3 of 3 runs)"]]
        r, better, worse = bs.sim_case_ratio(rows)
        self.assertEqual((better, worse), (2, 1))
        self.assertAlmostEqual(r, (1.25 * 1.10 * 0.5 * 1.0) ** 0.25, places=9, msg="less energy is plus, more work is plus, more taps is minus, noise is one")

    def test_the_published_sheet_is_what_the_tables_give(self):
        self.assertEqual(bs.main(check=True), 0)


if __name__ == "__main__":
    unittest.main()
