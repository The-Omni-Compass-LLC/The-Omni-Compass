// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The compass law and the two-way plug (C++ twin of omnicompass/compass_law.py: Band, CompassLaw, Plug). Read the two
// side by side: every line here has its Python line, in the same order of operations, so the same readings give the
// same forces and the same writes to the last bit (tests/test_cpp_compass_law_parity.py; the live engine page's C++
// twin panel replays every organism muscle's and every live controller's own readings through it).
#pragma once
#include <functional>
#include <optional>
#include <stdexcept>
#include <string>
namespace omnicompass {

// A reading's band: lo is calm (position 0), hi is the line (position 1).
struct Band {
  double lo, hi, center = 0.5, cushion = 0.05;
  double position(double x) const { return (x - lo) / (hi - lo); }
  double wall_low() const { return cushion; }
  double wall_high() const { return 1.0 - cushion; }
};

// The brain's law for one muscle. dt: seconds between decisions; tau: the muscle's response time in seconds; kd defaults
// to critical damping for that response. ref_dt (omni-v16): the period the lever's rate and the smoothing are stated at,
// where the caller moves its lever at a rate in time (the live governor: 60 s); none, or 0, is dt itself.
class CompassLaw {
 public:
  CompassLaw(Band band, double dt, double tau, double kp = 1.0, std::optional<double> kd = std::nullopt,
             double authority = 1.0, double smooth = 0.5, std::optional<double> ref_dt = std::nullopt);
  double sense(double reading);
  double force(double reading);   // positive: the up side (add capacity); negative: the down side; bounded by authority
  Band band;
  double dt, tau, kp, kd, authority, smooth;
  std::optional<double> ref_dt;
  std::optional<double> p;
  double v = 0.0;
};

struct ForeignWriter : std::runtime_error { using std::runtime_error::runtime_error; };

// One wire in, one wire out. The three wires are given as functions; everything else is here, as in the Python.
class Plug {
 public:
  Plug(double lo, double hi, double tolerance, std::function<double()> read_service, std::function<double()> read_lever,
       std::function<void(double)> send);
  double attach();                              // read the lever once, before any write: the restore point
  double read() { return read_service_(); }
  double lever() { return read_lever_(); }
  std::optional<double> write(double value);    // nullopt: not written (not owned); throws ForeignWriter
  bool restore();
  double lo, hi, tol;
  std::optional<double> snapshot, last_written;
  bool owned = true;
  long writes = 0, clipped = 0;
 private:
  std::function<double()> read_service_, read_lever_;
  std::function<void(double)> send_;
};

inline double cover_clip(double v, double lo, double hi) { return v < lo ? lo : v > hi ? hi : v; }
}  // namespace omnicompass
