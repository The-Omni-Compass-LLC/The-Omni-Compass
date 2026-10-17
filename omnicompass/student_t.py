# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The two-sided 95% point of Student's t distribution, for any number of degrees of freedom, computed (no table).

t95(ν) is the t with P(|T| ≤ t) = 0.95 for T ~ Student's t with ν degrees of freedom. It is found by bisection on the
distribution's own CDF, P(|T| ≤ t) = 1 − I_x(ν/2, 1/2) with x = ν/(ν + t²), where I is the regularized incomplete beta
function (continued fraction, Numerical Recipes 6.4), and rounded to three decimals, as the printed tables were: 12.706 at
ν = 1, 4.303, 3.182, …, 2.262 at 9, 2.228 at 10, 2.086 at 20, 1.984 at 100, 1.960 as ν grows without bound. So every
interval printed before (all on 9 or fewer degrees of freedom) reads the same to the last digit. The hand-copied tables it
replaces fell back to the normal 1.96 past their last row, which narrows an interval of 11 to 30 repetitions by 2% to 14%.

  python3 -m omnicompass.student_t 9 10 20 100   prints each ν and its t95
"""
from __future__ import annotations

import math
import sys
from functools import lru_cache


def _betacf(a: float, b: float, x: float) -> float:
    """The continued fraction of the incomplete beta function (modified Lentz)."""
    tiny, qab, qap, qam = 1e-300, a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 10000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d; d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c; c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d; d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c; c = c if abs(c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    return h


def ibeta(a: float, b: float, x: float) -> float:
    """The regularized incomplete beta function I_x(a, b), 0 ≤ x ≤ 1."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_front = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(ln_front) * _betacf(a, b, x) / a
    return 1.0 - math.exp(ln_front) * _betacf(b, a, 1.0 - x) / b


def coverage(t: float, df: float) -> float:
    """P(|T| ≤ t) for Student's t with df degrees of freedom."""
    return 1.0 - ibeta(df / 2.0, 0.5, df / (df + t * t))


@lru_cache(maxsize=None)
def t95(df: int) -> float:
    """The two-sided 95% point for df degrees of freedom (df ≥ 1), to three decimals; NaN below one."""
    if df < 1:
        return float("nan")
    lo, hi = 0.0, 64.0                                     # t95(1) = 12.706 is the largest
    for _ in range(80):
        mid = (lo + hi) / 2.0
        lo, hi = (mid, hi) if coverage(mid, df) < 0.95 else (lo, mid)
    return round((lo + hi) / 2.0, 3)


class _T95:
    """t95 read as the tables were read, T95.get(ν, fallback) and T95[ν], so every caller stays as written; the fallback
    answers only below one degree of freedom, where no interval exists."""

    def get(self, df: int, default: float = float("nan")) -> float:
        return t95(df) if df >= 1 else default

    def __getitem__(self, df: int) -> float:
        return t95(df)


T95 = _T95()


if __name__ == "__main__":
    for arg in sys.argv[1:] or ["1", "2", "9", "10", "20", "100", "1000"]:
        print(arg, f"{t95(int(arg)):.3f}")
