// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/student_t.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/student_t.hpp"
#include "omnicompass/verdict.hpp"
#include <cmath>
#include <limits>
namespace omnicompass {

// CPython's lanczos_sum and m_lgamma (Modules/mathmodule.c), which math.lgamma runs on every platform
static constexpr int LANCZOS_N = 13;
static constexpr double lanczos_g = 6.024680040776729583740234375;
static const double lanczos_num_coeffs[LANCZOS_N] = {
    23531376880.410759688572007674451636754734846804940, 42919803642.649098768957899047001988850926355848959,
    35711959237.355668049440185451547166705960488635843, 17921034426.037209699919755754458931112671403265390,
    6039542586.3520280050642916443072979210699388420708, 1439720407.3117216736632230727949123939715485786772,
    248874557.86205415651146038641322942321632125127801, 31426415.585400194380614231628318205362874684987640,
    2876370.6289353724412254090516208496135991145378768, 186056.26539522349504029498971604569928220784236328,
    8071.6720023658162106380029022722506138218516325024, 210.82427775157934587250973392071336271166969580291,
    2.5066282746310002701649081771338373386264310793408};
static const double lanczos_den_coeffs[LANCZOS_N] = {0.0, 39916800.0, 120543840.0, 150917976.0, 105258076.0, 45995730.0,
                                                     13339535.0, 2637558.0, 357423.0, 32670.0, 1925.0, 66.0, 1.0};

static double lanczos_sum(double x) {
  double num = 0.0, den = 0.0;
  if (x < 5.0) {
    for (int i = LANCZOS_N; --i >= 0;) { num = num * x + lanczos_num_coeffs[i]; den = den * x + lanczos_den_coeffs[i]; }
  } else {
    for (int i = 0; i < LANCZOS_N; i++) { num = num / x + lanczos_num_coeffs[i]; den = den / x + lanczos_den_coeffs[i]; }
  }
  return num / den;
}

double py_lgamma(double x) {
  if (!std::isfinite(x)) return std::isnan(x) ? x : std::numeric_limits<double>::infinity();
  if (x == std::floor(x) && x <= 2.0) return x <= 0.0 ? std::numeric_limits<double>::infinity() : 0.0;
  const double absx = std::fabs(x);
  if (absx < 1e-20) return -std::log(absx);
  double r = std::log(lanczos_sum(absx)) - lanczos_g;
  r += (absx - 0.5) * (std::log(absx + lanczos_g - 0.5) - 1);
  if (x < 0.0) {   // the reflection formula (not reached here: every argument is a positive half-integer or more)
    const double pi = 3.141592653589793238462643383279502884197;
    r = std::log(pi) - std::log(std::fabs(std::sin(pi * absx))) - std::log(absx) - r;
  }
  return r;
}

static double betacf(double a, double b, double x) {   // the continued fraction (modified Lentz)
  const double tiny = 1e-300, qab = a + b, qap = a + 1.0, qam = a - 1.0;
  double c = 1.0, d = 1.0 - qab * x / qap;
  d = 1.0 / (std::fabs(d) > tiny ? d : tiny);
  double h = d;
  for (int m = 1; m < 10000; ++m) {
    const int m2 = 2 * m;
    double aa = m * (b - m) * x / ((qam + m2) * (a + m2));
    d = 1.0 + aa * d; d = 1.0 / (std::fabs(d) > tiny ? d : tiny);
    c = 1.0 + aa / c; c = std::fabs(c) > tiny ? c : tiny;
    h *= d * c;
    aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2));
    d = 1.0 + aa * d; d = 1.0 / (std::fabs(d) > tiny ? d : tiny);
    c = 1.0 + aa / c; c = std::fabs(c) > tiny ? c : tiny;
    const double delta = d * c;
    h *= delta;
    if (std::fabs(delta - 1.0) < 1e-15) break;
  }
  return h;
}

double ibeta(double a, double b, double x) {
  if (x <= 0.0) return 0.0;
  if (x >= 1.0) return 1.0;
  const double ln_front = py_lgamma(a + b) - py_lgamma(a) - py_lgamma(b) + a * std::log(x) + b * std::log1p(-x);
  if (x < (a + 1.0) / (a + b + 2.0)) return std::exp(ln_front) * betacf(a, b, x) / a;
  return 1.0 - std::exp(ln_front) * betacf(b, a, 1.0 - x) / b;
}

double t_coverage(double t, double df) { return 1.0 - ibeta(df / 2.0, 0.5, df / (df + t * t)); }

double t95(int df) {
  if (df < 1) return std::numeric_limits<double>::quiet_NaN();
  double lo = 0.0, hi = 64.0;                            // t95(1) = 12.706 is the largest
  for (int i = 0; i < 80; ++i) {
    const double mid = (lo + hi) / 2.0;
    if (t_coverage(mid, df) < 0.95) lo = mid; else hi = mid;
  }
  return py_round((lo + hi) / 2.0, 3);
}

}  // namespace omnicompass
