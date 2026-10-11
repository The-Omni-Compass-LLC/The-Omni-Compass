# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The YCSB A/B/C rule (tools/ycsb_abc.py): confirmed only with the same sign and every interval clear of zero in all three
runs; an interval over zero reads no difference beyond the noise with the count of such runs; clear runs pointing different
ways read as a disagreement; a failed operation added in any run is WORSE; the resource held reads WORSE when it grows."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import ycsb_abc as A


def r(diff, lo, hi, native=100.0):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "n": 3, "significant": lo > 0 or hi < 0}


def main():
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "higher") == "**confirmed better**"
    assert A.verdict([r(5, 2, 8), r(6, 3, 9), r(4, 1, 7)], "lower") == "**confirmed WORSE**", "a resource that grows reads WORSE"
    assert A.verdict([r(5, 2, 8), r(1, -2, 4), r(4, 1, 7)], "higher") == "no difference beyond the noise (1 of 3 runs)"
    assert A.verdict([r(5, 2, 8), r(-6, -9, -3), r(4, 1, 7)], "higher") == "**the runs disagree**"
    assert A.verdict([r(0, -1, 1), r(0, -1, 1), r(0, -1, 1)], "higher") == "same"
    assert A.verdict([r(0, 0, 0), r(1, 1, 1), r(0, 0, 0)], "never more") == "**confirmed WORSE**", "one failed operation more in any run is WORSE"
    assert A.verdict([r(0, 0, 0), r(0, 0, 0), r(0, 0, 0)], "never more") == "same"
    assert A.verdict([r(1, 0, 2), None, r(1, 0, 2)], "higher") == "no value"
    assert A.verdict([r(9, 1, 2)], "shown") == "shown, not judged"
    assert A.cell(r(5, 2, 8), "ops") == "+5.0% (+2.0 to +8.0)" and A.cell(r(2, 1, 3, native=0.0), "failed") == "+2 (+1 to +3)"
    print("PASS  YCSB A/B/C rule: confirmed only with the same sign and every interval clear of zero in all three runs; an interval over zero reads no "
          "difference beyond the noise with the count; clear runs pointing different ways read as a disagreement; a failed operation added is WORSE")


if __name__ == "__main__":
    main()
