// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/verdict.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/verdict.hpp"
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <limits>
namespace omnicompass {

double py_sum(const std::vector<double>& xs) {
  // CPython 3.12 builtin sum() over floats: Neumaier's improvement of Kahan-Babuska, the compensation added at the end
  double f = 0.0, c = 0.0;
  for (const double x : xs) {
    const double t = f + x;
    if (std::fabs(f) >= std::fabs(x)) c += (f - t) + x;
    else c += (x - t) + f;
    f = t;
  }
  if (c != 0.0 && std::isfinite(c)) f += c;
  return f;
}

double py_round(double x, int digits) {
  if (!std::isfinite(x)) return x;
  char b[512];
  std::snprintf(b, sizeof b, "%.*f", digits, x);                  // correctly rounded, as Python's dtoa mode 3
  return std::strtod(b, nullptr);
}

std::optional<double> median(std::vector<double> s) {
  std::sort(s.begin(), s.end());
  const size_t n = s.size();
  if (n == 0) return std::nullopt;
  return n % 2 ? s[n / 2] : 0.5 * (s[n / 2 - 1] + s[n / 2]);
}

std::optional<LogStats> log_stats(const std::vector<double>& xs) {
  std::vector<double> ls;
  for (const double x : xs) if (x > 0) ls.push_back(std::log(x));
  const long n = static_cast<long>(ls.size());
  if (n == 0) return std::nullopt;
  const double m = py_sum(ls) / n;
  double var = std::numeric_limits<double>::infinity();
  if (n > 1) {
    std::vector<double> sq; sq.reserve(ls.size());
    for (const double x : ls) sq.push_back(std::pow(x - m, 2.0));
    var = py_sum(sq) / (n - 1);
  }
  return LogStats{m, var, n};
}

std::optional<std::pair<double, double>> change_interval(const std::vector<double>& ref, const std::vector<double>& got, double z) {
  const auto a = log_stats(ref), b = log_stats(got);
  if (!a || !b) return std::nullopt;
  const double d = b->mean - a->mean;
  const double se = std::isfinite(a->var) && std::isfinite(b->var) ? std::sqrt(a->var / a->n + b->var / b->n)
                                                                   : std::numeric_limits<double>::infinity();
  return std::make_pair(d - z * se, d + z * se);
}

Verdict::Verdict(double tolerance, long min_samples, long probe_every_, long recheck_, long max_steps_, long max_trial_,
                 bool incremental_, std::string judge_)
    : tol(tolerance), judge(std::move(judge_)), min_n(min_samples), probe_every(probe_every_), recheck(recheck_),
      max_steps(max_steps_), max_trial(max_trial_), incremental(incremental_) {}

void Verdict::observe(const std::vector<double>& costs) {
  if (phase == "ref") ref.insert(ref.end(), costs.begin(), costs.end());
  else if (phase == "trial") got.insert(got.end(), costs.begin(), costs.end());
}

void Verdict::end_() { phase.clear(); has_trial = false; trial = 0; ref.clear(); got.clear(); }

Tick Verdict::tick(bool calm) {
  t += 1;
  std::optional<VerdictEvent> event;
  if (!phase.empty() && (!calm || t - phase_t > max_trial)) {
    event = VerdictEvent{!calm ? "trial abandoned (service not calm)" : "trial abandoned (too little work)", trial};
    end_();
  } else if (phase == "ref" && static_cast<long>(ref.size()) >= min_n) {
    phase = "trial"; phase_t = t;
  } else if (phase == "trial" && static_cast<long>(got.size()) >= min_n) {
    const double m0 = *median(ref), mk = *median(got);
    if (incremental && allowed == 0) {
      native_cost = m0;
      native_ref = ref;
    }
    const double bound = !native_cost ? m0 : (*native_cost < m0 ? *native_cost : m0);   // min(m0, self.native_cost)
    const bool within = mk <= bound * (1.0 + tol);
    if (judge == "interval") {
      const Reading r = reading_();
      if (r.reading != "LOSS" && r.wide && static_cast<long>(got.size()) < 3 * min_n)
        return Tick{trial, true, std::nullopt};                  // the evidence is wider than the allowance: it measures on
      if (r.reading != "LOSS" && within && r.d_max <= std::log(1.0 + tol)) {
        allowed = trial;
        event = VerdictEvent{"step allowed", trial, m0, mk, r.reading, r.ivs};
      } else {
        refused_until[trial] = t + recheck;
        event = VerdictEvent{"step refused: the muscle is slower there", trial, m0, mk,
                             r.reading == "LOSS" ? "LOSS" : "past the allowance", r.ivs};
      }
    } else if (within) {
      allowed = trial;
      event = VerdictEvent{"step allowed", trial, m0, mk};
    } else {
      refused_until[trial] = t + recheck;
      event = VerdictEvent{"step refused: the muscle is slower there", trial, m0, mk};
    }
    end_();
  } else if (phase.empty() && calm && t - last_probe >= probe_every && allowed < max_steps &&
             (refused_until.count(allowed + 1) ? refused_until.at(allowed + 1) : -1) <= t) {
    phase = "ref"; trial = allowed + 1; has_trial = true; phase_t = t; last_probe = t;
    ref.clear(); got.clear();
    event = VerdictEvent{"trial", trial};
  }
  if (phase == "ref") return Tick{incremental ? allowed : 0, true, event};
  if (phase == "trial") return Tick{trial, true, event};
  return Tick{allowed, false, event};
}

Verdict::Reading Verdict::reading_() const {
  const double tau = std::log(1.0 + tol);
  std::vector<std::pair<double, double>> ivs;
  if (const auto iv = change_interval(ref, got)) ivs.push_back(*iv);
  if (incremental && native_ref && !native_ref->empty())
    if (const auto iv = change_interval(*native_ref, got)) ivs.push_back(*iv);
  if (ivs.empty()) return {"EVEN", {}, true, std::numeric_limits<double>::infinity()};
  std::string reading;
  if (std::any_of(ivs.begin(), ivs.end(), [](const auto& iv) { return iv.first > 0.0; })) reading = "LOSS";
  else if (std::all_of(ivs.begin(), ivs.end(), [](const auto& iv) { return iv.second < 0.0; })) reading = "GAIN";
  else reading = "EVEN";
  bool wide = false;
  for (const auto& [lo, hi] : ivs) wide = wide || (hi - lo) / 2.0 > tau;
  double d_max = (ivs[0].first + ivs[0].second) / 2.0;            // Python's max(): the first, replaced by any larger
  for (size_t i = 1; i < ivs.size(); ++i) {
    const double d = (ivs[i].first + ivs[i].second) / 2.0;
    if (d > d_max) d_max = d;
  }
  std::vector<std::pair<double, double>> shown;
  for (const auto& [lo, hi] : ivs) shown.emplace_back(py_round(lo, 5), py_round(hi, 5));
  return {reading, shown, wide, d_max};
}
}  // namespace omnicompass
