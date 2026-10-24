# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words rule (tools/readings.py): GAIN, EVEN and LOSS, set by what the gauge is for and never by its sign."""
import math
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


class TheFloor(unittest.TestCase):
    """The founder's order of 24 October 2026: "Any gauge that gives anything over a 0.5 percent change either way is a
    change ... it has to show its loss or gain." One rule, judge_runs, every tool calling it."""

    def test_a_latency_row_with_one_interval_across_zero_reads_gain(self):
        # -3.0% (-3.6 to -2.5), -2.3% (-5.4 to +0.8), -3.7% (-4.3 to -3.1)
        self.assertEqual(R.judge_runs([-0.030, -0.023, -0.037], [True, False, True], R.LOWER),
                         "**GAIN** (the same way in all three runs; 2 of 3 clear of the noise)")

    def test_every_run_under_the_floor_is_even(self):
        self.assertEqual(R.judge_runs([0.004, -0.003, 0.001], [True, True, False], R.LOWER),
                         "EVEN, under the floor (every run under 0.5%; the largest 0.40%)")

    def test_runs_past_the_floor_pointing_different_ways_disagree(self):
        self.assertEqual(R.judge_runs([0.02, -0.02, 0.02], [False, False, False], R.LOWER), "**the runs disagree**")

    def test_energy_up_one_percent_in_all_three_is_power_given(self):
        self.assertEqual(R.judge_runs([0.01, 0.01, 0.01], [True, True, True], R.SPENT), "**power given in all three of our runs**")
        self.assertEqual(R.judge_runs([0.01, 0.01, 0.01], [False, True, False], R.SPENT),
                         "**power given** (the same way in all three runs; 1 of 3 clear of the noise)")
        self.assertEqual(R.judge_runs([-0.01, -0.01, -0.01], [False, False, False], R.SPENT),
                         "**GAIN** (the same way in all three runs; 0 of 3 clear of the noise)", "a cut of a resource spent is a GAIN")

    def test_a_failed_request_in_one_run_is_loss(self):
        self.assertEqual(R.judge_runs([0.0, math.inf, 0.0], [False, False, False], R.NEVER_MORE), "**LOSS in at least one of our runs**")
        rs = [{"native": 0.0, "diff": 0.0, "significant": False}, {"native": 0.0, "diff": 1.0, "significant": False},
              {"native": 0.0, "diff": 0.0, "significant": False}]
        self.assertEqual(R.stack_reading(rs, R.NEVER_MORE, 1e-6), "**LOSS in at least one of our runs**")
        self.assertEqual(R.judge_runs([0.0, math.inf, 0.0], [False, False, False], R.LOWER),
                         "**LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise)")

    def test_a_run_under_the_floor_never_decides_the_direction(self):
        self.assertEqual(R.judge_runs([0.02, 0.03, -0.004], [True, False, True], R.HIGHER),
                         "**GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise)")

    def test_the_word_comes_from_the_aim_never_the_sign(self):
        self.assertTrue(R.judge_runs([0.02] * 3, [False] * 3, R.HIGHER).startswith("**GAIN**"))
        self.assertTrue(R.judge_runs([0.02] * 3, [False] * 3, R.LOWER).startswith("**LOSS**"))
        self.assertTrue(R.judge_runs([-0.02] * 3, [False] * 3, R.WORK_PER).startswith("**power given**"))
        self.assertEqual(R.judge_runs([0.02] * 3, [False] * 3, None), R.SHOWN)

    def test_a_deterministic_simulator_reads_in_all_three(self):
        self.assertEqual(R.judge_runs([-0.02] * 3, None, R.SPENT), "**GAIN in all three of our runs**")
        self.assertEqual(R.judge_runs([0.003] * 3, None, R.SPENT), "EVEN, under the floor (every run under 0.5%; the largest 0.30%)")
        self.assertEqual(R.judge_runs([0.003] * 3, None, R.NEVER_MORE), "**LOSS in all three of our runs**", "never more: any rise, floor or not")

    def test_one_paired_comparison(self):
        self.assertEqual(R.judge_one(0.012, False, R.LOWER), "LOSS (not clear of the noise)")
        self.assertEqual(R.judge_one(-0.012, True, R.LOWER), "GAIN")
        self.assertEqual(R.judge_one(0.003, True, R.LOWER), "EVEN, under the floor (0.30%, under 0.5%)")

    def test_the_tally_counts_every_word_and_the_strict_ones(self):
        t = R.Tally()
        t.add("**GAIN** (the same way in all three runs; 2 of 3 clear of the noise)", R.LOWER)
        t.add("**GAIN in all three of our runs**", R.LOWER)
        t.add("**LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise)", R.LOWER)
        t.add("EVEN, under the floor (every run under 0.5%; the largest 0.10%)", R.LOWER)
        t.add("**the runs disagree**", R.LOWER)
        self.assertEqual(t.sentence(2), "**Across 2 workloads: 2 gauge-rows GAIN (1 in all three of our runs), 1 LOSS (0 in all three of our "
                                        "runs), 0 power given (0 in all three of our runs), 1 EVEN, 1 where the runs disagree.**")

    def test_every_published_table_is_read_by_the_rule(self):
        from tools import reread_key
        self.assertEqual(reread_key.run(write=False), [], "a table not yet read by the rule of 24 October 2026 (python3 tools/reread_key.py)")


class Landed(unittest.TestCase):
    """A newer engine's table takes its benchmark's place only once its three runs share a reading (20 October: the three
    omni-v12 YCSB runs each failed partway, their table held no workload in all three, and the benchmark fell off the
    benefit sheet and the Omni index instead of omni-v11's table standing)."""

    def test_a_table_whose_runs_share_no_workload_has_not_landed(self):
        import json, tempfile
        from tools import benefit_sheet, omni_index
        run = {"native": 1.0, "omni": 0.9, "diff": -0.1, "ci95": [-0.2, -0.05]}
        with tempfile.TemporaryDirectory() as td:
            live = Path(td)
            (live / "V11_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"f": {"g": {"reading": "x", "runs": [run, run, run]}}}}))
            (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {}}))
            (live / "V12_DEMO.md").write_text("# demo\n")
            self.assertTrue(R.landed(live / "V11_DEMO.json"))
            self.assertFalse(R.landed(live / "V12_DEMO.json"))
            self.assertFalse(R.landed(live / "V12_DEMO.md"))          # read through its JSON twin
            keep = (benefit_sheet.LIVE, omni_index.LIVE)
            benefit_sheet.LIVE = omni_index.LIVE = live
            try:
                self.assertEqual(benefit_sheet.newest_table("V7_DEMO.json"), "V11_DEMO.json")
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V11_DEMO.json")
                (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"tuning": {"g": {"runs": [run, run, run]}}}}))
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V11_DEMO.json")   # the tuning workload alone reads nothing
                (live / "V12_ORG.json").write_text(json.dumps({"organisms": {"spine": {}}}))
                self.assertTrue(R.landed(live / "V12_ORG.json"))                       # another table's shape: its writer decides
                (live / "V12_DEMO.json").write_text(json.dumps({"runs": [{}, {}, {}], "workloads": {"f": {"g": {"runs": [run, run, run]}}}}))
                self.assertEqual(benefit_sheet.newest_table("V7_DEMO.json"), "V12_DEMO.json")
                self.assertEqual(omni_index.newest("V7_DEMO.json"), "V12_DEMO.json")
            finally:
                benefit_sheet.LIVE, omni_index.LIVE = keep


if __name__ == "__main__":
    unittest.main()
