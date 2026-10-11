# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The compass: one smooth law for every muscle.

A muscle is plugged in with one wire in and one wire out (omnicompass/wire.py: snapshot once, write only from the body's
tick, read back, one writer, restore). All the thinking is here, in the brain, written once for every muscle.

Two bands
  cover     the outer band, the lever's hard range (the device's or the buyer's lowest and highest setting); every
            write is clipped to it, so nothing the math does can set the lever outside
  compass      the service reading as a position in its band, 0 to 1 (0: calm, 1: the service line); the brain pulls it
            to the bottom of the compass, the center (0.5 by default); the walls run to 0.05 and 0.95, and the last 5% on
            each side is cushion (10% in all) before the line

The force (CompassLaw.force), the physics of a ball in a compass with the right friction
  pull      K_P x (position - center): gentle near the bottom, harder up the walls
  push      K_D x velocity: whatever is shoving the position (a load rising, heat building) is met by an equal and
            opposite push; it is also the friction that stops the ball sloshing past the bottom (with K_D chosen for
            critical damping it glides to the center and stops, no overshoot, no ringing)
  smooth    the force is A x tanh(raw / A): a spring near the center that bends over and flattens into its maximum A,
            never a corner, never a hammer; the same shape the engine already uses for v_eff (omnicompass/core.py)
  fail up   past the 0.95 wall the up side goes to its full force at once, and the down side may not act until the
            position is back inside the compass

Two forces (antagonist pairs)
  up        a positive force adds capacity, power, cooling or speed (scale out, raise a clock, start a chiller)
  down      a negative force takes it back (scale in, lower a limit, warm a setpoint)
  each side has its own gain (lever units per unit of force), because adding and taking back do not cost the same;
  a muscle with two wires (a GPU's clock range and power limit) gives each side its own lever; a one-wire muscle
  carries both directions on its one lever

The frozen engine (omnicompass/core.py) and its proofs are untouched; this is a separate law, run as its own arm.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional


def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v


@dataclass
class Band:
    """A reading's band: lo is calm (position 0), hi is the line (position 1)."""
    lo: float
    hi: float
    center: float = 0.5
    cushion: float = 0.05

    def position(self, x: float) -> float:
        return (x - self.lo) / (self.hi - self.lo)

    @property
    def wall_low(self) -> float:
        return self.cushion

    @property
    def wall_high(self) -> float:
        return 1.0 - self.cushion


@dataclass
class CompassLaw:
    """The brain's law for one muscle. dt: seconds between decisions; tau: the muscle's response time in seconds
    (how long the service reading takes to follow the lever); kd defaults to critical damping for that response."""
    band: Band
    dt: float
    tau: float
    kp: float = 1.0
    kd: Optional[float] = None
    authority: float = 1.0
    smooth: float = 0.5          # the velocity estimate's smoothing (0: raw difference, near 1: heavily smoothed)
    p: Optional[float] = field(default=None, init=False)
    v: float = field(default=0.0, init=False)

    def __post_init__(self):
        if self.kd is None:
            # a first-order muscle with response tau under a P-D pull: critical damping when kd = 2 sqrt(kp tau) - 1
            # scaled to the decision period; never negative
            self.kd = max(0.0, 2.0 * math.sqrt(self.kp * self.tau / self.dt) - 1.0) * self.dt

    def sense(self, reading: float) -> float:
        p = self.band.position(reading)
        if self.p is not None:
            self.v = self.smooth * self.v + (1.0 - self.smooth) * (p - self.p) / self.dt
        self.p = p
        return p

    def force(self, reading: float) -> float:
        """Positive: the up side (add capacity); negative: the down side (take it back). Bounded by the authority."""
        p = self.sense(reading)
        if p >= self.band.wall_high:
            return self.authority                                  # fail up: past the wall, full force up at once
        raw = self.kp * (p - self.band.center) + self.kd * self.v
        f = self.authority * math.tanh(raw / self.authority)
        if f < 0.0 and self.v > 0.0 and p > self.band.center:
            f = 0.0                                                # never take back while it climbs above the center
        return f


# The plug every muscle is wired through lives in omnicompass/wire.py (Omni v4: the wire belongs to the body); its v3 names
# are kept here for the harnesses that import them.
from omnicompass.wire import ForeignWriter, Plug, Wire  # noqa: E402,F401
