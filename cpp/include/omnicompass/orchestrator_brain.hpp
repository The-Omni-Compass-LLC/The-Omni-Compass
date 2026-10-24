// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omni_orchestrator/brain.py and omni_orchestrator/scheduler.py, Omni direct's brain and room rule (omni-v18):
// the yardstick (Kubernetes' published autoscaling rule, written by us as the measure), Omni's own brain (the reflex, the
// compass, the twin and the verdict's depth), the conveyed CPU walls, the machines the units need, and where a unit goes
// (the room on each machine; Omni's pack and the yardstick's spread). Every answer is the Python's to the last bit
// (tests/test_cpp_orchestrator_brain_parity.py).
#pragma once
#include "omnicompass/compass_law.hpp"
#include <map>
#include <optional>
#include <string>
#include <utility>
#include <vector>
namespace omnicompass {

class Yardstick {
 public:
  Yardstick(int mn, int mx, double target = 0.5, double tolerance = 0.1, double window_s = 300.0);
  int recommend(double now, int units, std::optional<double> busy);
  int mn, mx;
  double target, tolerance, window_s;
  std::vector<std::pair<double, int>> hist;
};

struct BrainInfo {
  double force, position;
  int twin, floor, depth;
  bool trial;
  double p95_ms;
  std::optional<double> busy;
  int waiting;
};

class OmniBrain {
 public:
  OmniBrain(double line_ms, double beat_s, int mn, int mx, int max_step = 3, int hold = 3);
  std::pair<int, BrainInfo> decide(double now, int units, std::optional<double> busy, double p95_ms, int waiting, int depth = 0,
                                   bool trial = false, std::optional<int> twin = std::nullopt,
                                   std::optional<int> anchor = std::nullopt);
  CompassLaw law;
  Yardstick yard;
  int mn, mx, max_step, hold, calm = 0;
};

struct Unit { std::string id; double req_m; };
// nullopt: nothing changes; otherwise each unit's CPU wall in millicores
std::optional<std::map<std::string, double>> conveyed_limits(double cpu_m, std::optional<double> busy_m, const std::vector<Unit>& ours,
                                                             double others_m, bool others_room = false);
int machines_needed(int units, double req_m, double room_m, int step_units, int floor, double extra_m = 0.0);

// the room rule (omni_orchestrator/scheduler.py)
struct Machine { std::string name; double cpu_m; std::optional<double> busy_m; std::string state; };
struct Placed { std::string machine; double req_m; std::optional<std::string> service; };
double room(const Machine& m, const std::vector<Placed>& units, const std::string& rule = "requests");
// the machine's name, or nullopt when no machine awake has the room
std::optional<std::string> place(double req_m, const std::string& service, const std::vector<Machine>& machines,
                                 const std::vector<Placed>& units, const std::string& how = "pack", const std::string& rule = "requests");

}  // namespace omnicompass
