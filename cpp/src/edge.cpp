// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/edge.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/edge.hpp"
#include "omnicompass/verdict.hpp"
#include <algorithm>
#include <cmath>
#include <vector>
namespace omnicompass {

static int py_round_int(double x) { return static_cast<int>(std::nearbyint(x)); }   // int(round(x)): half to even
// x ** 2 as CPython computes it: libm's pow, which can differ from x * x in the last bit; the exponent is read through a
// volatile so the compiler cannot turn the call into a multiplication
static double py_square(double x) { volatile double two = 2.0; return std::pow(x, two); }

Edge::Edge(double react, double z, int window, double narrow, double start, double memory, double fall_decay, int est,
           double pace)
    : react_(std::max(1.0, react)), z_(z), narrow_(narrow), mem_(memory), fall_decay_(fall_decay), window_(window), est_(est),
      cushion_(1.0 - start) {
  if (pace != 1.0) {
    // every count and rate given per reference step, kept in time at this pace (omni-v16)
    window_ = std::max(window, py_round_int(window / pace));
    narrow_ = 1.0 - std::pow(1.0 - narrow, pace);
    fall_decay_ = std::pow(fall_decay, pace);
    mem_ = memory > 0 ? std::pow(memory, pace) : 0.0;
    lag_ = std::max(1, py_round_int(1.0 / pace));
  }
}

void Edge::learn_fall(double step) { floor__ = std::min(1.0, std::max(floor__, cushion_) + step); }

double Edge::update(double p) {
  hist_.push_back(std::min(p, 1.0));
  if (static_cast<int>(hist_.size()) > window_ + 1) hist_.pop_front();
  const std::vector<double> h(hist_.begin(), hist_.end());
  const int lag = lag_, n = static_cast<int>(h.size());
  double climb, wob;
  if (n >= lag + 2 && est_ == 2) {
    const int r = std::max(1, py_round_int(react_));
    std::vector<double> d;                                     // the change over one reference step
    for (int i = 0; i + lag < n; ++i) d.push_back(h[i + lag] - h[i]);
    const double md = py_sum(d) / static_cast<double>(d.size());
    std::vector<double> sq;
    for (const double x : d) sq.push_back(py_square(x - md));
    wob = std::sqrt(py_sum(sq) / std::max(1, static_cast<int>(d.size()) - 1)) / std::sqrt(2.0);
    double rise;
    if (r < n) {
      rise = h[r] - h[0];
      for (int i = 1; i < n - r; ++i) rise = std::max(rise, h[i + r] - h[i]);
    } else {
      rise = std::max(0.0, *std::max_element(d.begin(), d.end())) / lag * r;   // longer than the window: extrapolated
    }
    climb = std::max(0.0, rise) / r;                           // per reading, so climb x reaction is the rise
  } else if (n >= lag + 2) {
    climb = 0.0;
    for (int i = 0; i + lag < n; ++i) climb = std::max(climb, std::max(0.0, h[i + lag] - h[i]));
    climb = climb / lag;
    const double m = py_sum(h) / n;
    std::vector<double> sq;
    for (const double x : h) sq.push_back(py_square(x - m));
    wob = std::sqrt(py_sum(sq) / (n - 1));
  } else {
    climb = 0.05; wob = 0.05;
  }
  if (mem_ > 0) {
    // held longer: the worst climb and spread this knob has shown, forgotten slowly
    climb_mem_ = std::max(climb, climb_mem_ * mem_);
    wob_mem_ = std::max(wob, wob_mem_ * mem_);
    climb = climb_mem_; wob = wob_mem_;
  }
  const double react_part = std::min(1.0, climb * react_);
  const double need = std::min(1.0, std::max(react_part + z_ * wob, floor__));
  floor__ *= fall_decay_;
  if (need >= cushion_) cushion_ = need;                                       // widen at once
  else cushion_ = std::max(need, cushion_ * (1.0 - narrow_));                 // narrow slowly
  react_part_ = std::max(0.005, react_part);
  return 1.0 - cushion_;
}

}  // namespace omnicompass
