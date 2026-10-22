// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The verdict (C++ twin of omnicompass/verdict.py: median, log_stats, change_interval, Verdict). Read the two side by side:
// every line here has its Python line, in the same order of operations, so the same costs give the same trials, the same
// readings and the same steps allowed or refused to the last bit (tests/test_cpp_verdict_parity.py). A sum over a list is
// the Python's own sum() (Neumaier's compensated sum, as CPython 3.12 adds floats), so the means match it bit for bit.
#pragma once
#include <map>
#include <optional>
#include <string>
#include <utility>
#include <vector>
namespace omnicompass {

inline constexpr double Z95 = 1.96;              // the two-sided 95% interval every report reads (tools/readings.py)

double py_sum(const std::vector<double>& xs);    // sum(xs) as CPython 3.12 computes it
std::optional<double> median(std::vector<double> xs);
struct LogStats { double mean, var; long n; };
std::optional<LogStats> log_stats(const std::vector<double>& xs);
std::optional<std::pair<double, double>> change_interval(const std::vector<double>& ref, const std::vector<double>& got,
                                                         double z = Z95);
double py_round(double x, int digits);           // round(x, digits) as Python rounds (correctly rounded decimal)

// What a decision tells the audit (Python: the event dict, or None).
struct VerdictEvent {
  std::string verdict;                           // "trial", "step allowed", "step refused: ...", "trial abandoned (...)"
  long step{};
  std::optional<double> cost_native, cost_step;  // the medians, on a judged trial
  std::string reading;                           // judge="interval": GAIN, EVEN, LOSS or "past the allowance"
  std::vector<std::pair<double, double>> intervals;   // judge="interval": the intervals, rounded to five decimals
};
struct Tick { long step{}; bool is_trial{}; std::optional<VerdictEvent> event; };

class Verdict {
 public:
  explicit Verdict(double tolerance = 0.005, long min_samples = 30, long probe_every = 120, long recheck = 1800,
                   long max_steps = 60, long max_trial = 30, bool incremental = false, std::string judge = "interval");
  std::string state() const { return allowed == 0 ? "left native" : "acting"; }
  void observe(const std::vector<double>& costs);
  Tick tick(bool calm);

  double tol; std::string judge; std::optional<std::vector<double>> native_ref;
  long min_n, probe_every, recheck, max_steps, max_trial; bool incremental;
  std::optional<double> native_cost;
  long allowed{0};
  std::map<long, long> refused_until;
  std::string phase;                             // "", "ref" (knob at native) or "trial" (knob at the trial step)
  long trial{0}; bool has_trial{false};
  std::vector<double> ref, got;
  long phase_t{0}, t{0}, last_probe{-1000000000};

 private:
  void end_();
  struct Reading { std::string reading; std::vector<std::pair<double, double>> ivs; bool wide; double d_max; };
  Reading reading_() const;
};
}  // namespace omnicompass
