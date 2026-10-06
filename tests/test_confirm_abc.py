# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The A/B/C confirmation rule (tools/confirm_abc.py, docs/OMNI_V1.md): confirmed better or WORSE only when all three
runs move the same way with every 95% interval clear of zero; an interval that includes zero reads no difference beyond
the noise, with the count of such runs; runs clear of the noise that point different ways read as a disagreement; a
rounding-level change reads same; unjudged rows stay unjudged."""
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
    better = r(300, -150, -200, -100)
    assert C.verdict(P95, [better] * 3) == "**confirmed better**"
    assert C.verdict(P95, [r(300, 30, 10, 50)] * 3) == "**confirmed WORSE**", "a loss in all three is shown as WORSE"
    assert C.verdict(P95, [better, better, r(300, -20, -60, 5)]) == "no difference beyond the noise in 1 of 3 runs", "one interval crosses zero"
    assert C.verdict(P95, [r(300, -5, -40, 30), r(300, 8, -20, 36), r(300, -2, -30, 26)]) == "no difference beyond the noise (all three runs)"
    assert C.verdict(P95, [better, better, r(300, 40, 10, 70)]) == "**the runs disagree**", "one run flips the sign, clear of the noise"
    assert C.verdict(P95, [better, r(300, -20, -60, 5), r(300, 40, 10, 70)]) == "**the runs disagree**", "a disagreement outranks a noisy run"
    assert C.verdict(P95, [better, better, r(300, 20, -5, 45)]) == "no difference beyond the noise in 1 of 3 runs", "a flipped sign inside the noise is noise"
    assert C.verdict(P95, [r(300, 1e-7, 5e-8, 2e-7)] * 3) == "same", "a change under one part in a million"
    assert C.verdict("CPU used (cores), mean", [r(2.0, -0.5, -0.7, -0.3)] * 3) == "shown, not judged"
    assert C.cell(better) == "-50.0% (-66.7 to -33.3)"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-123" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1", "2", "3"], "compass": ["1", "2"]},
                                                       "means": {}, "paired": {"compass": {P95: better}}}))
        run, paired, n = C.load(d.parent)
        assert (run, n, paired[P95]["diff"]) == ("123", 2, -150), (run, n)
    assert C.verdict(C.CAPACITY, [r(18.6, 9.0, 6.0, 12.0)] * 3) == "**confirmed better**", "more work inside the line is better"
    assert C.verdict(C.CAPACITY, [r(18.6, -3.0, -5.0, -1.0)] * 3) == "**confirmed WORSE**"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-124" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1"], "compass": ["1"]}, "means": {}, "paired": {"compass": {}},
                                                       "capacity": {"native": {"capacity_rps": 18.6}, "compass": {"capacity_rps": 27.6, "change_pct": 48.4, "ci95": [6.0, 12.0]}}}))
        _, paired, _ = C.load(d.parent)
        assert paired[C.CAPACITY]["diff"] == 9.0 and paired[C.CAPACITY]["significant"], "the capacity block becomes a judged row"
    print("PASS  A/B/C confirmation rule: confirmed only with the same sign and every interval clear of zero in all three; "
          "an interval over zero reads no difference beyond the noise; clear runs pointing different ways read as a disagreement")


if __name__ == "__main__":
    main()
