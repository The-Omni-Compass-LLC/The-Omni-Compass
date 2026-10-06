# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The database benchmark's A/B/C rule (tools/pgbench_abc.py, docs/OMNI_V1.md): confirmed better or WORSE only when all
three runs move the same way with every interval clear of zero; a run whose interval includes zero reads no difference
beyond the noise with the count; clear runs pointing different ways read as a disagreement; any added failed transaction
in any run is WORSE; the pool size is shown, never judged."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import pgbench_abc as P


def r(diff, lo, hi, nat=100.0):
    return {"native": nat, "omni": nat + diff, "diff": diff, "ci95": [lo, hi], "significant": lo > 0 or hi < 0}


def main():
    assert P.verdict([r(10, 5, 15)] * 3, "higher") == "**confirmed better**"
    assert P.verdict([r(10, 5, 15)] * 3, "lower") == "**confirmed WORSE**", "a higher value where lower is better, clear in all three, is WORSE"
    assert P.verdict([r(-10, -15, -5)] * 3, "lower") == "**confirmed better**"
    assert P.verdict([r(10, 5, 15), r(10, -2, 22), r(10, 5, 15)], "higher") == "no difference beyond the noise (1 of 3 runs)"
    assert P.verdict([r(10, 5, 15), r(-10, -15, -5), r(10, 5, 15)], "higher") == "**the runs disagree**"
    assert P.verdict([r(0.0, -1e-9, 1e-9)] * 3, "higher") == "same"
    assert P.verdict([r(0, 0, 0, nat=0), r(1, 1, 1, nat=0), r(0, 0, 0, nat=0)], "never more") == "**confirmed WORSE**", "one more failed transaction in one run is WORSE"
    assert P.verdict([r(0, 0, 0, nat=0)] * 3, "never more") == "same"
    assert P.verdict([r(-5, -8, -2)] * 3, "shown") == "shown, not judged"
    assert P.verdict([r(1, 0, 2), None, r(1, 0, 2)], "higher") == "no value"
    print("PASS  database A/B/C rule: confirmed only with the same sign and every interval clear of zero in all three runs; an interval "
          "over zero reads no difference beyond the noise with its count; clear runs pointing different ways read as a disagreement; "
          "any added failed transaction is WORSE; the pool size is shown, never judged")


if __name__ == "__main__":
    main()
