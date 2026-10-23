// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/compass_law.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/compass_law.hpp"
#include <algorithm>
#include <cmath>
#include <cstdio>
namespace omnicompass {

CompassLaw::CompassLaw(Band band_, double dt_, double tau_, double kp_, std::optional<double> kd_, double authority_,
                       double smooth_)
    : band(band_), dt(dt_), tau(tau_), kp(kp_), kd(0.0), authority(authority_), smooth(smooth_) {
  // __post_init__: a first-order muscle with response tau under a P-D pull: critical damping when
  // kd = 2 sqrt(kp tau) - 1 scaled to the decision period; never negative
  kd = kd_ ? *kd_ : std::max(0.0, 2.0 * std::sqrt(kp * tau / dt) - 1.0) * dt;
}

double CompassLaw::sense(double reading) {
  const double pos = band.position(reading);
  if (p) v = smooth * v + (1.0 - smooth) * (pos - *p) / dt;
  p = pos;
  return pos;
}

double CompassLaw::force(double reading) {
  const double pos = sense(reading);
  if (pos >= band.wall_high()) return authority;                 // fail up: past the wall, full force up at once
  const double raw = kp * (pos - band.center) + kd * v;
  double f = authority * std::tanh(raw / authority);
  if (f < 0.0 && v > 0.0 && pos > band.center) f = 0.0;          // never take back while it climbs above the center
  return f;
}

Plug::Plug(double lo_, double hi_, double tolerance, std::function<double()> read_service, std::function<double()> read_lever,
           std::function<void(double)> send)
    : lo(lo_), hi(hi_), tol(tolerance), read_service_(std::move(read_service)), read_lever_(std::move(read_lever)),
      send_(std::move(send)) {}

double Plug::attach() {
  snapshot = read_lever_();
  return *snapshot;
}

std::optional<double> Plug::write(double value) {
  if (!owned) return std::nullopt;
  const double now = read_lever_();
  const std::optional<double> expected = last_written ? last_written : snapshot;
  if (expected && std::fabs(now - *expected) > tol) {
    owned = false;                                               // someone else moved it: it is theirs now
    char msg[96];
    std::snprintf(msg, sizeof msg, "lever at %.17g, last written %.17g", now, *expected);
    throw ForeignWriter(msg);
  }
  const double v = cover_clip(value, lo, hi);       // clamp(value, self.lo, self.hi)
  clipped += (v != value);
  if (std::fabs(v - now) <= tol) return now;
  send_(v);
  last_written = read_lever_();
  writes += 1;
  return last_written;
}

bool Plug::restore() {
  if (!owned || !snapshot) return true;
  if (std::fabs(read_lever_() - *snapshot) > tol) send_(*snapshot);
  last_written.reset();
  return std::fabs(read_lever_() - *snapshot) <= tol;
}
}  // namespace omnicompass
