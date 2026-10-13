# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words rule (tools/readings.py): GAIN, EVEN and LOSS, set by what the gauge is for and never by its sign."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import readings as R  # noqa: E402


class Words(unittest.TestCase):
    def test_word_by_aim_not_sign(self):
        self.assertEqual(R.word(True, R.LOWER), R.GAIN)        # a response time that fell
        self.assertEqual(R.word(False, R.LOWER), R.LOSS)       # a response time that rose
        self.assertEqual(R.word(False, R.HIGHER), R.GAIN)      # work that rose
        self.assertEqual(R.word(True, R.HIGHER), R.LOSS)       # work that fell
        self.assertEqual(R.word(True, R.SPENT), R.GAIN)        # a resource cut
        self.assertEqual(R.word(False, R.SPENT), R.GIVEN)      # a resource that rose: power given, never a loss

    def test_aim_of_a_resource(self):
        self.assertEqual(R.aim("lower", "node-hours"), R.SPENT)
        self.assertEqual(R.aim("lower", "response time (ms), mean"), R.LOWER)
        self.assertIsNone(R.aim("shown"))

    def test_classify_new_and_old_words(self):
        self.assertEqual(R.classify("**GAIN in all three of our runs**", R.LOWER), "gain")
        self.assertEqual(R.classify("**power given in all three of our runs**", R.SPENT), "given")
        self.assertEqual(R.classify("**LOSS in all three of our runs**", R.HIGHER), "loss")
        self.assertEqual(R.classify("EVEN, no difference beyond the noise (all three runs)", R.LOWER), "noise")
        self.assertEqual(R.classify("**the runs disagree**", R.LOWER), "disagree")
        # older recorded tables read back the same way
        self.assertEqual(R.classify("**lower in all three of our runs**", R.LOWER), "gain")
        self.assertEqual(R.classify("**higher in all three of our runs**", R.SPENT), "given")
        self.assertEqual(R.classify("no difference beyond the noise (3 of 3 runs)", R.LOWER), "noise")

    def test_labels_word_first(self):
        self.assertEqual(R.labelled("SUPERIOR WITHIN GUARDRAILS"), "GAIN (within the guardrails)")
        self.assertTrue(R.labelled("AT ITS LIMIT ON NATIVE").startswith(R.EVEN))
        self.assertEqual(R.labelled("AWAY FROM ITS AIMS"), R.LOSS)

    def test_the_key(self):
        text = "\n".join(R.key_lines())
        for w in ("Growth", "Advantage", "Improvement", "Net-positive", "Equalized", "Verified baseline", "Equilibrium",
                  "Neutral", "Leakage", "Off-track", "Setback", "Subpar", "power given", "Disclosure and disclaimer",
                  R.OWN_RUNS):
            self.assertIn(w, text)
        self.assertEqual(R.check_pages(), [], "a page lacks the key word for word: python3 tools/readings.py --fix")


if __name__ == "__main__":
    unittest.main()
