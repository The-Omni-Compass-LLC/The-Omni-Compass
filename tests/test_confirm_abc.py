# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C three-run table rule (tools/confirm_abc.py, the one rule in tools/readings.py judge_runs, the founder's order of
24 October 2026): EVEN only when every run's change is under 0.5% (EVEN, under the floor) or rounding-level (EVEN, the same);
otherwise the runs that moved 0.5% or more decide. All the same way: the word by what the gauge is for (a response time that
fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given), "in all three of our runs" when
all three moved 0.5% or more with every 95% interval clear of zero, else with its qualifier and the count of runs clear of the
noise; pointing different ways: the runs disagree; unjudged rows stay unjudged."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import confirm_abc as C

P95 = "response time (ms), 95th percentile"


def r(native, diff, lo, hi):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "significant": lo > 0 or hi < 0}


def main():
    fell = r(300, -150, -200, -100)
    assert C.verdict(P95, [fell] * 3) == "**GAIN in all three of our runs**", "a response time cut in all three is a GAIN (a minus that reads GAIN)"
    assert C.verdict(P95, [r(300, 30, 10, 50)] * 3) == "**LOSS in all three of our runs**", "a slower response in all three is a LOSS"
    assert C.verdict(P95, [fell, fell, r(300, -20, -60, 5)]) == "**GAIN** (the same way in all three runs; 2 of 3 clear of the noise)", "one interval crosses zero: the word stands, with its count"
    # the founder's own case (24 October): a latency row at -3.0%, -2.3% and -3.7%, one interval across zero, is a GAIN
    assert C.verdict(P95, [r(100, -3.0, -3.6, -2.5), r(100, -2.3, -5.4, 0.8), r(100, -3.7, -4.3, -3.1)]) == \
        "**GAIN** (the same way in all three runs; 2 of 3 clear of the noise)"
    assert C.verdict(P95, [r(300, -5, -40, 30), r(300, 8, -20, 36), r(300, -2, -30, 26)]) == "**the runs disagree**", "runs past the floor pointing different ways"
    assert C.verdict(P95, [r(100, 0.3, -1, 1.6), r(100, -0.4, -2, 1.2), r(100, 0.2, 0.1, 0.3)]) == \
        "EVEN, under the floor (every run under 0.5%; the largest 0.40%)", "every run under 0.5%: EVEN, whatever the intervals"
    assert C.verdict(P95, [r(100, 2.0, -1, 5), r(100, -2.0, -5, 1), r(100, 2.0, -1, 5)]) == "**the runs disagree**", "+2% and -2%"
    assert C.verdict(P95, [r(100, 2.0, -1, 5), r(100, 0.2, -1, 1.4), r(100, 1.0, 0.5, 1.5)]) == \
        "**LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise)"
    assert C.verdict(P95, [fell, fell, r(300, 40, 10, 70)]) == "**the runs disagree**", "one run flips the sign, clear of the noise"
    assert C.verdict(P95, [fell, r(300, -20, -60, 5), r(300, 40, 10, 70)]) == "**the runs disagree**", "a disagreement outranks a noisy run"
    assert C.verdict(P95, [fell, fell, r(300, 20, -5, 45)]) == "**the runs disagree**", "a run past the floor the other way disagrees, inside the noise or not"
    assert C.verdict(P95, [fell, fell, r(300, 1, -5, 7)]) == "**GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 2 of 3 clear of the noise)", \
        "a run under the floor does not decide the direction"
    assert C.verdict("energy (Wh)", [r(100.0, 1.0, -0.5, 2.5)] * 3) == "**power given** (the same way in all three runs; 0 of 3 clear of the noise)", "energy +1% in all three: power given"
    assert C.verdict("failed requests (%)", [r(0.0, 0.0, 0.0, 0.0), r(0.0, 0.0, 0.0, 0.0), r(0.0, 1.0, -1.0, 3.0)]) == \
        "**LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise)", "failed requests up from none in one run: LOSS"
    assert C.verdict(P95, [r(300, 1e-7, 5e-8, 2e-7)] * 3) == "EVEN, the same", "a change under one part in a million"
    assert C.verdict("CPU used (cores), mean", [r(2.0, -0.5, -0.7, -0.3)] * 3) == "shown, not judged"
    # one pair a run (the 24-hour robustness run on rented machines): no interval, read by sign alone, never a confirmation
    nan = float("nan")
    single = {"native": 300.0, "omni": 150.0, "diff": -150.0, "ci95": [nan, nan], "significant": False}
    assert C.verdict(P95, [single] * 3) == "three single pairs agree: GAIN (one pair a run, no interval, so the noise cannot be judged)"
    assert C.verdict(P95, [single, single, dict(single, diff=20.0, omni=320.0)]) == "single pairs point different ways (one pair a run, no interval)"
    assert C.verdict(C.CAPACITY, [single] * 3).startswith("three single pairs agree: LOSS"), "less work inside the line from three single pairs reads LOSS, and still not a reading of all three of our runs"
    # the number beside a word carries the word's sign (tools/readings.py, 20 October); with no word, its own direction
    assert C.cell(fell) == "−50.0% (−66.7 to −33.3)", C.cell(fell)
    assert C.cell(fell, "GAIN") == "+50.0% (+33.3 to +66.7)", C.cell(fell, "GAIN")
    assert C.cell(fell, "LOSS") == "−50.0% (−33.3 to −66.7)", C.cell(fell, "LOSS")
    assert C.cell(r(300, -5, -40, 30), "EVEN, no difference beyond the noise") == "=1.7% (−13.3 to +10.0)", "EVEN: the size with =, the interval as it lies"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-123" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1", "2", "3"], "compass": ["1", "2"]},
                                                       "means": {}, "paired": {"compass": {P95: fell}}}))
        run, paired, n, _ = C.load(d.parent)
        assert (run, n, paired[P95]["diff"]) == ("123", 2, -150), (run, n)
    assert C.engine("1")[1] == "unknown", "a run whose commit cannot be read is never called v1 (GitHub's gh prints nothing for it)"
    assert C.verdict(C.CAPACITY, [r(18.6, 9.0, 6.0, 12.0)] * 3) == "**GAIN in all three of our runs**", "more work inside the line is a GAIN"
    assert C.verdict(C.CAPACITY, [r(18.6, -3.0, -5.0, -1.0)] * 3) == "**LOSS in all three of our runs**", "less work is a LOSS"
    assert C.verdict("batch: worker machines in service after the queue finished, mean", [r(6.0, -2.0, -2.5, -1.5)] * 3) == "**GAIN in all three of our runs**", "machines cut"
    assert C.verdict("batch: worker machines in service after the queue finished, mean", [r(6.0, 2.0, 1.5, 2.5)] * 3) == "**power given in all three of our runs**", "machines up: power given, never a LOSS"
    assert C.verdict("batch: queue finished (s)", [r(575.0, 5.0, 2.0, 8.0)] * 3) == "**LOSS in all three of our runs**", "a later finish is a LOSS"
    assert C.verdict("compute bill at list price ($)", [r(1.0, -0.1, -0.15, -0.05)] * 3) == "**GAIN in all three of our runs**", "a bill cut is a GAIN"
    assert C.verdict("energy (Wh)", [r(10.0, 1.0, 0.5, 1.5)] * 3) == "**power given in all three of our runs**", "energy up is power given"
    assert C.verdict("failed requests (%)", [r(1.0, 0.5, 0.2, 0.8)] * 3) == "**LOSS in all three of our runs**", "more failed requests is a LOSS"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-124" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1"], "compass": ["1"]}, "means": {}, "paired": {"compass": {}},
                                                       "capacity": {"native": {"capacity_rps": 18.6}, "compass": {"capacity_rps": 27.6, "change_pct": 48.4, "ci95": [6.0, 12.0]}}}))
        _, paired, _, _ = C.load(d.parent)
        assert paired[C.CAPACITY]["diff"] == 9.0 and paired[C.CAPACITY]["significant"], "the capacity block becomes a judged row"
    with tempfile.TemporaryDirectory() as t:                # the rig each run ran on (amendment of 18 October): never two in one table
        old, new = Path(t) / "run-1", Path(t) / "run-2"
        for d, line in ((old, ""), (new, "images=pre-pulled on every worker before the arm (deploy/kind/prepull.yaml)\n")):
            for arm in ("native", "compass"):
                (d / f"bench-{arm}-1").mkdir(parents=True)
                (d / f"bench-{arm}-1" / "preflight.txt").write_text("arm=" + arm + "\n" + line)
        assert C.rig(old) == "pulled by each node at each start", C.rig(old)
        assert C.rig(new) == "pre-pulled on every worker before the arm (deploy/kind/prepull.yaml)", C.rig(new)
        assert C.rig(Path(t) / "none") == "not recorded"
    print("PASS  A/B/C three-run table rule (24 October): EVEN only under the 0.5% floor in every run or the same; from 0.5% up the word by what the gauge "
          "is for, in all three of our runs or with its count of runs clear of the noise; runs past the floor pointing different ways disagree")


if __name__ == "__main__":
    main()
