# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The v5 edge: the compass's balance point is not a fixed middle, it moves with each muscle's own risk.

One Edge per knob. Every decision it reads the service position (0 calm, 1 the service line) and keeps the cushion the
knob needs in front of the line:

    cushion = climb x reaction + z x wobble

  climb     the largest rise of the position seen within one reaction time, per decision (how fast the service has been
            climbing lately); times the reaction, it is the rise that can land before the knob's own action does
  reaction  the decisions the knob takes to act: its own, not the plant's (a power cap answers in one decision; a machine
            pool only once its machines have started)
  wobble    the step-to-step spread of the position over the window (divided by root 2: the spread of one step)
  z         3.09: 99.9% of steps inside the cushion

It widens at once when the need rises and narrows slowly when it falls (a driver doubles the following distance the
moment rain starts, and closes it slowly after). A fall (the service over its line) while, or soon after, Omni held
something back teaches the knob a floor under its cushion, forgotten slowly. With memory, the worst climb and wobble the
knob has shown are kept as long as its own physics carries them.

The balance point is 1 - cushion; the wall (where the law fails up at once) moves with the reaction part of it. The
realms use this through realms/compass_arm_v5.py; the live controllers through omni_controller/ (--law v5). Pure math,
no I/O; the frozen engine (omnicompass/core.py) is untouched.
"""
from __future__ import annotations

import math


class Edge:
    def __init__(self, react: float, z: float = 3.09, window: int = 20, narrow: float = 0.05, start: float = 0.5,
                 memory: float = 0.0, fall_decay: float = 0.9995, est: int = 2):
        self.react = max(1.0, float(react))
        self.z, self.window, self.narrow, self.est = z, int(window), narrow, est
        self.mem = memory
        self.fall_decay = fall_decay
        self.hist = []
        self.cushion = 1.0 - start
        self.react_part = 0.05
        self.climb_mem = 0.0
        self.wob_mem = 0.0
        self.floor = 0.0                      # learned from a fall: the least cushion this knob needs

    def learn_fall(self, step: float) -> None:
        """A fall while, or soon after, Omni held something back: this knob needs more room than its statistics said."""
        self.floor = min(1.0, max(self.floor, self.cushion) + step)

    def update(self, p: float) -> float:
        """Read one position; return the balance point (1 - cushion)."""
        self.hist.append(min(p, 1.0))
        if len(self.hist) > self.window + 1:
            self.hist.pop(0)
        h = self.hist
        if len(h) >= 3 and self.est == 2:
            r = max(1, int(round(self.react)))
            d = [b - a for a, b in zip(h, h[1:])]
            md = sum(d) / len(d)
            wob = math.sqrt(sum((x - md) ** 2 for x in d) / max(1, len(d) - 1)) / math.sqrt(2.0)
            if r < len(h):
                rise = max(h[i + r] - h[i] for i in range(len(h) - r))
            else:
                rise = max(0.0, max(d)) * r                       # longer than the window: the steepest climb, extrapolated
            climb = max(0.0, rise) / r                            # per decision, so climb x reaction is the rise
        elif len(h) >= 3:
            climb = max(max(0.0, b - a) for a, b in zip(h, h[1:]))
            m = sum(h) / len(h)
            wob = math.sqrt(sum((x - m) ** 2 for x in h) / (len(h) - 1))
        else:
            climb, wob = 0.05, 0.05
        if self.mem > 0:
            # held longer: the worst climb and spread this knob has shown, forgotten slowly
            self.climb_mem = max(climb, self.climb_mem * self.mem)
            self.wob_mem = max(wob, self.wob_mem * self.mem)
            climb, wob = self.climb_mem, self.wob_mem
        react_part = min(1.0, climb * self.react)
        need = min(1.0, max(react_part + self.z * wob, self.floor))
        self.floor *= self.fall_decay
        if need >= self.cushion:
            self.cushion = need                                   # widen at once
        else:
            self.cushion = max(need, self.cushion * (1.0 - self.narrow))   # narrow slowly
        self.react_part = max(0.005, react_part)
        return 1.0 - self.cushion


def physics_memory(horizon: float, window: int) -> float:
    """The forgetting factor for a knob whose risks last `horizon` decisions (its own slowest physics): none if that is
    inside the window, else 1 - 1 / horizon per decision."""
    return (1.0 - 1.0 / horizon) if horizon > window else 0.0
