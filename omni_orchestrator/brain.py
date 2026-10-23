# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How many units, and how many machines.

Yardstick   the Kubernetes Horizontal Pod Autoscaler's published rule, written here from its documentation as the
            measure Omni is read against (it is not Kubernetes' code): every 15 s the units become
            ceil(units × busy ÷ target), busy being the processor the units used over their requests, target 50%;
            no move inside a 10% tolerance; a rise at most to max(2 × units, units + 4) at once; a fall only to the
            highest count it recommended over the last 300 s.

OmniBrain   Omni-Compass's own: the compass law (omnicompass/compass_law.py) on the service's 95th percentile response
            time in the band from 0 to the service's line. A force up adds units at once in proportion to it (past
            the wall, the most it may add); a force down gives back one unit, only after it has held down for three
            beats with no request waiting. It never holds fewer units than its native twin, the yardstick's rule
            computed on the same readings: whatever Kubernetes would have held, Omni holds at least that.

machines    how many machines the units need: their requests, plus room for the most units the brain may add at once,
            so a unit never waits for a machine; never fewer than the floor (two).
"""
from __future__ import annotations

import math

from omnicompass.compass_law import Band, CompassLaw


def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v


class Yardstick:
    def __init__(self, mn: int, mx: int, target: float = 0.5, tolerance: float = 0.1, window_s: float = 300.0):
        self.mn, self.mx, self.target, self.tolerance, self.window_s = mn, mx, target, tolerance, window_s
        self.hist: list[tuple[float, int]] = []

    def recommend(self, now: float, units: int, busy: float | None) -> int:
        if busy is None or units <= 0:
            rec = max(units, self.mn)
        else:
            ratio = busy / self.target
            rec = units if abs(ratio - 1.0) <= self.tolerance else math.ceil(units * ratio)
        rec = clamp(rec, self.mn, self.mx)
        self.hist = [(t, r) for t, r in self.hist if now - t <= self.window_s] + [(now, rec)]
        if rec < units:
            rec = max(r for _, r in self.hist)           # a fall only to the highest of the window
        if rec > units:
            rec = min(rec, max(2 * units, units + 4))
        return clamp(rec, self.mn, self.mx)


class OmniBrain:
    def __init__(self, line_ms: float, beat_s: float, mn: int, mx: int, max_step: int = 3, hold: int = 3):
        self.law = CompassLaw(Band(0.0, line_ms), dt=beat_s, tau=2.0 * beat_s)
        self.twin = Yardstick(mn, mx)
        self.mn, self.mx, self.max_step, self.hold = mn, mx, max_step, hold
        self.calm = 0

    def decide(self, now: float, units: int, busy: float | None, p95_ms: float, waiting: int) -> tuple[int, dict]:
        twin = self.twin.recommend(now, units, busy)
        f = self.law.force(p95_ms)
        if f > 0.05:
            self.calm = 0
            want = units + max(1, round(f * self.max_step))
        elif f < -0.05 and waiting == 0:
            self.calm += 1
            want = units - 1 if self.calm >= self.hold else units
        else:
            self.calm = 0
            want = units
        want = clamp(max(want, twin), self.mn, self.mx)
        return want, {"force": round(f, 3), "position": round(self.law.p or 0.0, 3), "twin": twin,
                      "p95_ms": round(p95_ms, 1), "busy": None if busy is None else round(busy, 3), "waiting": waiting}


def machines_needed(units: int, req_m: float, room_m: float, step_units: int, floor: int, extra_m: float = 0.0) -> int:
    return max(floor, math.ceil((units * req_m + step_units * req_m + extra_m) / room_m - 1e-9))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
