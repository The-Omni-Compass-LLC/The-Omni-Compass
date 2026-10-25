// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/edge.py: the balance point every muscle's compass moves by, its cushion the rise that can land before
// the knob acts plus z times the step-to-step spread, widened at once and narrowed slowly, with a floor learned from a fall.
// Its sums are CPython 3.12's (py_sum, verdict.hpp) and its rounding Python's round half to even, so it is the Python's to the
// last bit (tests/test_cpp_edge_parity.py).
#pragma once
#include <deque>
namespace omnicompass {

class Edge {
 public:
  Edge(double react, double z = 3.09, int window = 20, double narrow = 0.05, double start = 0.5, double memory = 0.0,
       double fall_decay = 0.9995, int est = 2, double pace = 1.0);
  void learn_fall(double step);         // a fall while, or soon after, Omni held something back
  double update(double p);              // read one position; the balance point (1 - cushion)
  double cushion() const noexcept { return cushion_; }
  double react_part() const noexcept { return react_part_; }
  double floor_() const noexcept { return floor__; }

 private:
  double react_, z_, narrow_, mem_, fall_decay_;
  int window_, est_, lag_ = 1;
  std::deque<double> hist_;
  double cushion_, react_part_ = 0.05, climb_mem_ = 0.0, wob_mem_ = 0.0, floor__ = 0.0;
};

}  // namespace omnicompass
