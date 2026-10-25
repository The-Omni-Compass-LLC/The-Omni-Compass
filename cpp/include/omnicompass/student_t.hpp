// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/student_t.py: the two-sided 95% point of Student's t for any degrees of freedom, found by bisection
// on the distribution's own CDF (the regularized incomplete beta function, continued fraction), rounded to three decimals as
// Python's round() rounds. Its log-gamma is CPython's own (Lanczos, mathmodule.c m_lgamma), so every value is the Python's to
// the last bit (tests/test_cpp_student_t_parity.py).
#pragma once
namespace omnicompass {

double py_lgamma(double x);                       // math.lgamma as CPython computes it
double ibeta(double a, double b, double x);       // I_x(a, b), 0 <= x <= 1
double t_coverage(double t, double df);           // P(|T| <= t), T ~ Student's t with df degrees of freedom
double t95(int df);                               // the two-sided 95% point, three decimals; NaN below one

}  // namespace omnicompass
