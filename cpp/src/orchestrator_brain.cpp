// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omni_orchestrator/brain.py and scheduler.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/orchestrator_brain.hpp"
#include "omnicompass/verdict.hpp"
#include <algorithm>
#include <cmath>
namespace omnicompass {

static constexpr double CONVEY_TOP = 0.75, CONVEY_BACK = 0.70;   // the engine's own lines on a machine's busy share
static constexpr double BUSY_TOP = 0.75;     // no unit onto a machine this busy (omni_controller/capacity.py, omni-v7)

template <class T> static T clampv(T v, T lo, T hi) { return v < lo ? lo : v > hi ? hi : v; }
static int py_round_int(double x) { return static_cast<int>(std::nearbyint(x)); }   // round(x): half to even

Yardstick::Yardstick(int mn_, int mx_, double target_, double tolerance_, double window_s_)
    : mn(mn_), mx(mx_), target(target_), tolerance(tolerance_), window_s(window_s_) {}

int Yardstick::recommend(double now, int units, std::optional<double> busy) {
  int rec;
  if (!busy || units <= 0) {
    rec = std::max(units, mn);
  } else {
    const double ratio = *busy / target;
    rec = std::fabs(ratio - 1.0) <= tolerance ? units : static_cast<int>(std::ceil(units * ratio));
  }
  rec = clampv(rec, mn, mx);
  std::vector<std::pair<double, int>> kept;
  for (const auto& tr : hist) if (now - tr.first <= window_s) kept.push_back(tr);
  kept.emplace_back(now, rec);
  hist = kept;
  if (rec < units) {                                   // a fall only to the highest of the window
    int hi = hist.front().second;
    for (const auto& tr : hist) hi = std::max(hi, tr.second);
    rec = hi;
  }
  if (rec > units) rec = std::min(rec, std::max(2 * units, units + 4));
  return clampv(rec, mn, mx);
}

OmniBrain::OmniBrain(double line_ms, double beat_s, int mn_, int mx_, int max_step_, int hold_)
    : law(Band{0.0, line_ms}, beat_s, 2.0 * beat_s), yard(mn_, mx_), mn(mn_), mx(mx_), max_step(max_step_), hold(hold_) {}

std::pair<int, BrainInfo> OmniBrain::decide(double now, int units, std::optional<double> busy, double p95_ms, int waiting, int depth,
                                            bool trial, std::optional<int> twin, std::optional<int> anchor) {
  const int tw = twin ? *twin : yard.recommend(now, units, busy);
  // during a phase the step is counted from the higher of the twin as the phase found it and the twin now
  const int floor = std::max(mn, (anchor ? std::max(*anchor, tw) : tw) - std::max(0, depth));
  const double f = law.force(p95_ms);
  const int reflex = waiting > 0 ? std::min(max_step, waiting) : 0;
  int want;
  if (reflex || f > 0.05) {
    calm = 0;
    want = units + std::max({reflex, f > 0.05 ? py_round_int(f * max_step) : 0, 1});
  } else if (trial) {
    calm = 0;
    want = std::max(floor, units - 1);                 // a trial walks to its step one unit a beat and stands there
  } else if (f < -0.05) {
    calm += 1;
    want = calm >= hold ? units - 1 : units;
  } else {
    calm = 0;
    want = units;
  }
  want = clampv(std::max(want, floor), mn, mx);
  const BrainInfo info{py_round(f, 3), py_round(law.p ? *law.p : 0.0, 3), tw, floor, depth, trial,
                       py_round(p95_ms, 1), busy ? std::optional<double>(py_round(*busy, 3)) : std::nullopt, waiting};
  return {want, info};
}

std::optional<std::map<std::string, double>> conveyed_limits(double cpu_m, std::optional<double> busy_m, const std::vector<Unit>& ours,
                                                             double others_m, bool others_room) {
  if (!busy_m || ours.empty()) return std::nullopt;
  if (*busy_m >= CONVEY_TOP * cpu_m) {
    if (!others_room) return std::nullopt;
    std::map<std::string, double> out;
    for (const auto& u : ours) out[u.id] = u.req_m;
    return out;
  }
  if (*busy_m >= CONVEY_BACK * cpu_m) return std::nullopt;
  const double share = (CONVEY_TOP * cpu_m - others_m) / static_cast<double>(ours.size());
  std::map<std::string, double> out;
  for (const auto& u : ours) out[u.id] = std::min(cpu_m, std::max(u.req_m, std::floor(share / 10.0) * 10.0));
  return out;
}

int machines_needed(int units, double req_m, double room_m, int step_units, int floor, double extra_m) {
  return std::max(floor, static_cast<int>(std::ceil((units * req_m + step_units * req_m + extra_m) / room_m - 1e-9)));
}

double room(const Machine& m, const std::vector<Placed>& units, const std::string& rule) {
  std::vector<double> on;
  for (const auto& u : units) if (u.machine == m.name) on.push_back(u.req_m);
  const double by_req = m.cpu_m - py_sum(on);
  if (rule == "busy" && m.busy_m) return std::min(by_req, BUSY_TOP * m.cpu_m - *m.busy_m);
  return by_req;
}

std::optional<std::string> place(double req_m, const std::string& service, const std::vector<Machine>& machines,
                                 const std::vector<Placed>& units, const std::string& how, const std::string& rule) {
  std::vector<const Machine*> awake, fits;
  for (const auto& m : machines) if (m.state == "awake") awake.push_back(&m);
  for (const auto* m : awake) if (room(*m, units, rule) >= req_m) fits.push_back(m);
  if (fits.empty()) return std::nullopt;
  std::map<std::string, int> mine;
  for (const auto* m : awake) {
    int n = 0;
    for (const auto& u : units) n += u.machine == m->name && u.service && *u.service == service;
    mine[m->name] = n;
  }
  if (how == "spread") {   // the fewest units of the service, then the most room left, then the name
    const Machine* best = nullptr; int bn = 0; double br = 0.0;
    for (const auto* m : fits) {
      const int n = mine[m->name]; const double r = -room(*m, units, rule);
      if (!best || n < bn || (n == bn && (r < br || (r == br && m->name < best->name)))) { best = m; bn = n; br = r; }
    }
    return best->name;
  }
  std::vector<std::string> on;
  for (const auto& [name, n] : mine) if (n > 0) on.push_back(name);
  if (on.size() == 1) {   // the service stands on one machine: its next unit goes to another where one has the room
    std::vector<const Machine*> others;
    for (const auto* m : fits) if (m->name != on[0]) others.push_back(m);
    if (!others.empty()) fits = others;
  }
  const Machine* best = nullptr; double br = 0.0;   // the best fit: the least room left, then the name
  for (const auto* m : fits) {
    const double r = room(*m, units, rule) - req_m;
    if (!best || r < br || (r == br && m->name < best->name)) { best = m; br = r; }
  }
  return best->name;
}

}  // namespace omnicompass
