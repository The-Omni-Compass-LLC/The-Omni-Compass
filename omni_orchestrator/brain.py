# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How many units, how many machines, and how much processor each unit may use.

Yardstick   the Kubernetes Horizontal Pod Autoscaler's published rule, written here from its documentation as the
            measure Omni is read against (it is not Kubernetes' code): every 15 s the units become
            ceil(units × busy ÷ target), busy being the processor the units used over their requests (a pod never uses
            more than its limit, here its request, so busy is read capped at the request), target 50%; no move inside a
            10% tolerance; a rise at most to max(2 × units, units + 4) at once; a fall only to the highest count it
            recommended over the last 300 s.

OmniBrain   Omni-Compass's own, the max riding the edge of the organism:
            the reflex    work waiting in line at the front (every hand busy) adds units now, one for each request
                          waiting, up to the step; a request in line is the organism's own signal, read in the beat;
            the compass   the compass law (omnicompass/compass_law.py) on the service's 95th percentile response time in
                          the band from 0 to the service's line: a force up adds units at once in proportion to it (past
                          the wall, the most it may add); a force down gives back one unit, only after it has held down
                          for three beats with no request waiting;
            the twin      the yardstick's rule computed on the same readings, what Kubernetes would hold for this work:
                          Omni holds at least that, less only the depth the verdict has allowed (omnicompass/verdict.py,
                          the engine's own trigger): one unit fewer than the twin is tried on the service itself and kept
                          only where the response time measured under it reads no LOSS against the count before, within
                          the 2% allowance; a trial walks to its step one unit a beat, stands there while it measures,
                          and is abandoned the moment work waits or the wall is reached. Work waiting in line hands one
                          allowed step back (the immune reaction: harm seen, the knob steps toward native).

conveyance  the processor each unit may use (its CPU wall), the engine's own rule (omni_controller/muscles.py, omni-v7
            and omni-v13): the room under 75% of its machine, less the other workloads' units on it counted by their
            limits, shared equally among the service's units there, never under a unit's request and never over the
            machine; no new raise while the machine is 75% busy or its busy share is unread; at the top beside another
            workload's room every limit goes back to the request, conveyed again under 70%. A unit whose wall stands
            above its request answers at its machine's own speed instead of its paper quota's: faster, with no unit and
            no machine added. Kubernetes' autoscaler never moves a limit; it adds pods.

machines    how many machines the units need: their requests, plus room for the most units the brain may add at once,
            so a unit never waits for a machine; never fewer than the floor (two).
"""
from __future__ import annotations

import math

from omnicompass.compass_law import Band, CompassLaw

CONVEY_TOP, CONVEY_BACK = 0.75, 0.70     # the engine's own lines on a machine's busy share (omni-v7, omni-v13)


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

    def decide(self, now: float, units: int, busy: float | None, p95_ms: float, waiting: int,
               depth: int = 0, trial: bool = False, twin: int | None = None, anchor: int | None = None) -> tuple[int, dict]:
        """One beat. depth: how many units below the twin the verdict allows (a trial's own step included); trial: a
        verdict phase is on, so the count walks to that depth one unit a beat and stands there while it measures.
        anchor: the twin the depth is counted from during a phase (the twin as it stood when the phase began, so the
        step does not follow the count down: inside its 10% tolerance the yardstick's rule holds whatever stands)."""
        if twin is None:
            twin = self.twin.recommend(now, units, busy)
        # during a phase the step is counted from the higher of the twin as the phase found it and the twin now: the floor
        # never follows the count down (the twin's tolerance would accept the cut) and never stays below a twin the
        # traffic has raised since the phase began
        floor = max(self.mn, (twin if anchor is None else max(anchor, twin)) - max(0, int(depth)))
        f = self.law.force(p95_ms)
        reflex = min(self.max_step, int(waiting)) if waiting > 0 else 0
        if reflex or f > 0.05:
            self.calm = 0
            want = units + max(reflex, round(f * self.max_step) if f > 0.05 else 0, 1)
        elif trial:
            self.calm = 0
            want = max(floor, units - 1)                 # a trial walks to its step one unit a beat and stands there
        elif f < -0.05:
            self.calm += 1
            want = units - 1 if self.calm >= self.hold else units
        else:
            self.calm = 0
            want = units
        want = clamp(max(want, floor), self.mn, self.mx)
        return want, {"force": round(f, 3), "position": round(self.law.p or 0.0, 3), "twin": twin, "floor": floor,
                      "depth": int(depth), "trial": bool(trial), "p95_ms": round(p95_ms, 1),
                      "busy": None if busy is None else round(busy, 3), "waiting": waiting}


def conveyed_limits(cpu_m: float, busy_m: float | None, ours: list[dict], others_m: float,
                    others_room: bool = False) -> dict[str, float] | None:
    """The CPU wall (millicores) each of the service's units on one machine may have, by the engine's rule: the room
    under 75% of the machine, less the other workloads' units counted by their limits (others_m), shared equally among
    ours; never under a unit's request, never over the machine, in steps of 10 m. None: nothing changes (the machine's
    busy share unread, or between 70% and 75%, where what stands is held). At 75% or over: no new raise; and beside
    another workload's room (others_room) every wall goes back to the request."""
    if busy_m is None or not ours:
        return None
    if busy_m >= CONVEY_TOP * cpu_m:
        return {u["id"]: float(u["req_m"]) for u in ours} if others_room else None
    if busy_m >= CONVEY_BACK * cpu_m:
        return None
    share = (CONVEY_TOP * cpu_m - others_m) / len(ours)
    return {u["id"]: float(min(cpu_m, max(u["req_m"], math.floor(share / 10.0) * 10.0))) for u in ours}


def machines_needed(units: int, req_m: float, room_m: float, step_units: int, floor: int, extra_m: float = 0.0) -> int:
    return max(floor, math.ceil((units * req_m + step_units * req_m + extra_m) / room_m - 1e-9))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
