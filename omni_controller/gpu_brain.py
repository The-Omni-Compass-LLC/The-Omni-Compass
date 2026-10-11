# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The card's brain without wires: every decision Omni-Compass makes on a GPU, as plain logic, the same object on a real
card (omni_controller/gpu_compass.py) and in the card model (realms/gpu_card.py).

What the paid A10 run of 2 October 2026 measured (results/gpu/run-20261002T082232Z, read in docs/GPU_PREREGISTRATION.md,
amendment 13), and what the brain does about it:
  busy      work on a card held by its own power limit runs at the clock that limit allows, and running it slower costs
            MORE energy per request (a third of the busy draw does not scale with the clock: a 105 W lid made each request
            twice as slow and 40% dearer). So while work is on the card the lid stays at the start limit and the clock
            ceiling stays at the top: race. Slower only where a measured trial shows the work loses nothing and the card
            draws less (memory-bound work: the verdict below)
  idle      with a model loaded the firmware holds the top clock while nothing runs: 66 W at 1695 MHz against 46 W at
            700 MHz, and the card was idle 58% of the time. So when the work stops the brain parks the clock, and the
            moment work arrives it races back to the top
  heat      a hot chip leaks: 16 C hotter, the same request took 14% longer under the same limit. A parked card runs
            cooler, which gives its busy work a little more clock under the same limit

The pedals, on the card's one up wire (the clock ceiling) and its down wire (the power limit):
  idle (park)   no work for hold_ms: the ceiling to the park level the verdict allows
  gas (race)    work arrives on an idle card: the ceiling to the top at once (the arrival signal, not the next decision)
  cruise        work queued behind work: the ceiling at the busy level the verdict allows (the top unless proven free)
  brake         a power target (an operator's or the grid's): the lid to the target, the park and cruise levels as above
  reset         past the wall, blind meters, or the chip hot: every wire to native at once (fail up)

The verdict (omnicompass/verdict.py), on the card's own time per request, decides both depths, one trial at a time:
  park    paired trials on the first request after a rest: rests at the top (the reference: the card as it is alone),
          then rests parked one level deeper; that request's own time may rise at most `allow` (2%), or the level is
          refused and not tried again for recheck_s. A card whose clock answers slowly is held at a shallow level by its
          own measurements, never by a setting
  cruise  paired trials on requests served behind other work: the ceiling one busy step lower while work is queued; the
          request's own time may rise at most `allow` AND the card must draw at least `busy_gain` less while busy, or the
          step is refused (a card held by its own limit draws the same watts under a lower ceiling: no gain, refused)
A trial runs to its full measurement; only the wall ends it early (the reflex rule, docs/OMNI_V4_PLAN.md). Without an
arrival signal the brain cannot race in time, so it never parks (nothing that cannot work is switched on).
"""
from __future__ import annotations

from omnicompass.verdict import Verdict


def park_levels(top, floor, shares=(0.88, 0.77, 0.65, 0.53, 0.41, 0.30, 0.18), step=15.0):
    """The park levels from the top down: shares of the top clock in whole clock steps, never under the card's floor."""
    out = [float(top)]
    for s in shares:
        v = max(float(floor), round(top * s / step) * step)
        if v < out[-1] - step / 2:
            out.append(v)
    if out[-1] > floor + step / 2:
        out.append(float(floor))
    return out


class CardBrain:
    def __init__(self, top, floor, start_w, allow=0.005, samples=30, decision_s=0.25, hold_ms=20.0, rest_ms=80.0,
                 busy_step_mhz=60.0, busy_gain=0.02, probe_every_s=8.0, recheck_s=900.0, trial_s=120.0,
                 learn_samples=15, signal=True, park=True, cruise=True, power_target_w=None):
        self.top, self.floor, self.start_w = float(top), float(floor), float(start_w)
        self.levels = park_levels(top, floor)
        self.hold_s, self.rest_s = hold_ms / 1000.0, rest_ms / 1000.0
        self.busy_step = float(busy_step_mhz)
        d = lambda s: max(1, int(round(s / decision_s)))
        self.park_on = bool(park and signal)                 # parking needs a race in time: only with the arrival signal
        self.cruise_on = bool(cruise)
        self.park_vd = Verdict(tolerance=allow, min_samples=samples, probe_every=d(probe_every_s), recheck=d(recheck_s),
                               max_steps=len(self.levels) - 1, max_trial=d(trial_s), bisect=True)
        self.busy_vd = Verdict(tolerance=allow, min_samples=samples, probe_every=d(probe_every_s), recheck=d(recheck_s),
                               max_steps=max(1, int((self.top - self.floor) // self.busy_step)), max_trial=d(trial_s),
                               gain=busy_gain)
        self.park_step = 0                                   # the step the verdict lets idle rests use now (0: the top)
        self.busy_step_now = 0
        self.power_target = power_target_w
        self.learn_n = learn_samples
        self.busy_clk, self.busy_draw = [], []
        self.inflight = {}                                   # request id -> its tag (which verdict may count it)
        self.last_done = -1e9
        self.idle_since = 0.0
        self.parked = False
        self.ceiling = self.top
        self.lid = self.start_w if power_target_w is None else min(self.start_w, float(power_target_w))
        self.fail = None                                     # None, or why every wire is at native ("wall", "blind", "heat")
        self.events = []                                     # audit events since the caller last took them
        self.counts = {"arrivals": 0, "races": 0, "parks": 0, "cruise_sets": 0}

    # ---- the levels -----------------------------------------------------------------------------------------------
    def park_clock(self):
        return self.levels[min(self.park_step, len(self.levels) - 1)]

    def cruise_clock(self):
        return max(self.floor, self.top - self.busy_step_now * self.busy_step)

    def _set(self, c, why):
        c = float(c)
        if abs(c - self.ceiling) >= 0.5:
            self.ceiling = c
            return (c, why)
        return None

    # ---- events: what the workload (or the proxy in front of it) tells the brain --------------------------------------
    def arrival(self, t, rid):
        """Work arrives. On an idle card: race to the top now. Returns a ceiling write (mhz, why) or None."""
        self.counts["arrivals"] += 1
        idle = not self.inflight
        if idle:
            from_rest = t - self.last_done >= self.rest_s
            tag = ("park", self.park_vd.phase, self.park_vd.trial) if (from_rest and self.park_on and self.fail is None) else None
            self.inflight[rid] = tag
            self.parked = False
            w = self._set(self.top, "race")
            if w:
                self.counts["races"] += 1
            return w
        # work already on the card: this request will be served behind it, under the cruise level
        self.inflight[rid] = ("busy", self.busy_vd.phase, self.busy_vd.trial) if (self.cruise_on and self.fail is None) else None
        return None

    def done(self, t, rid, cost_ms):
        """A request finished; cost_ms is the card's own time on it (or the workload's per-token time). Feeds the verdict
        it belongs to when the verdict still stands where it stood when the request arrived; returns a ceiling write."""
        tag = self.inflight.pop(rid, None)
        if tag is not None and cost_ms is not None:
            vd = self.park_vd if tag[0] == "park" else self.busy_vd
            if vd.phase is not None and (vd.phase, vd.trial) == (tag[1], tag[2]):
                vd.observe([float(cost_ms)])
        self.last_done = t
        if self.inflight:
            if self.fail is None and self.cruise_on:
                w = self._set(self.cruise_clock(), "cruise")
                if w:
                    self.counts["cruise_sets"] += 1
                return w
            return None
        self.idle_since = t
        return None

    def idle_due(self, t):
        """Called when the card has had no work for hold_ms: park. Returns a ceiling write or None."""
        if self.inflight or self.parked or not self.park_on or self.fail is not None:
            return None
        if t - self.idle_since < self.hold_s - 1e-9:
            return None
        self.parked = True
        w = self._set(self.park_clock(), "park")
        if w:
            self.counts["parks"] += 1
        return w

    def next_idle_check(self):
        """When idle_due should next be called (seconds, absolute), or None."""
        if self.inflight or self.parked or not self.park_on or self.fail is not None:
            return None
        return self.idle_since + self.hold_s

    # ---- the decision, every decision_s ---------------------------------------------------------------------------
    def decide(self, t, tele, position=None, heat=False, wall=0.95):
        """tele: the card's own readings (util 0-1, draw_w, clock_mhz, limit_w) or None when the meters are unreadable.
        position: where the service stands in its compass (0 calm .. 1 the line); None when the response feed is blind
        (the caller passes 0.0 where no feed is wired, or where the arrival signal shows the card simply idle).
        Returns (ceiling, lid, why) to hold now; event-driven writes (race, park, cruise) happen between decisions."""
        blind = tele is None or position is None
        past = position is not None and position >= wall
        why = None
        if blind:
            why = "blind_fail_up"
        elif past:
            why = "fail_up"
        elif heat:
            why = "thermal_fail_up"
        prev = self.fail
        self.fail = why
        if why:
            self.parked = False
            self.ceiling = self.top
            self.lid = self.start_w if self.power_target is None else min(self.start_w, float(self.power_target))
            # the wall ends the trials in flight (and undoes their step): calm False aborts them
            for vd, name in ((self.park_vd, "park"), (self.busy_vd, "cruise")):
                _, _, ev = vd.tick(False)
                if ev:
                    self.events.append({"verdict": ev, "of": name})
            return self.ceiling, self.lid, why
        if prev is not None:
            self.events.append({"recovered_from": prev})
        # the card on its own: while the ceiling is at the top and the card is busy, its clock and draw are native's
        if tele is not None and self.ceiling >= self.top - 0.5 and tele.get("util", 0) >= 0.9:
            self.busy_clk = (self.busy_clk + [tele.get("clock_mhz", self.top)])[-200:]
            self.busy_draw = (self.busy_draw + [tele.get("draw_w", 0.0)])[-200:]
        # the cruise verdict's second reading: the watts drawn while busy under the step in force
        if tele is not None and tele.get("util", 0) >= 0.9 and self.busy_vd.phase is not None:
            self.busy_vd.observe([], benefit=[float(tele.get("draw_w", 0.0))])
        # one trial at a time inside the body: a verdict may open a trial only while the other has none in flight
        p_ev = b_ev = None
        if self.park_on:
            step, _, p_ev = self.park_vd.tick(self.busy_vd.phase is None)
            self.park_step = step
        if self.cruise_on:
            # a card held by its own power limit while busy draws the limit under any ceiling above the clock that
            # limit allows: nothing to buy, so no cruise trial opens (one already open runs to its measurement)
            headroom = self.busy_headroom()
            open_ok = self.park_vd.phase is None and (self.busy_vd.phase is not None or headroom)
            step, _, b_ev = self.busy_vd.tick(open_ok)
            self.busy_step_now = step
        for ev, name in ((p_ev, "park"), (b_ev, "cruise")):
            if ev:
                self.events.append({"verdict": ev, "of": name})
        self.lid = self.start_w if self.power_target is None else min(self.start_w, float(self.power_target))
        # hold what the work calls for now (the events move it between decisions)
        if self.inflight:
            want, why = (self.top, "race") if self.ceiling >= self.top - 0.5 else (self.cruise_clock(), "cruise")
        elif self.parked:
            want, why = self.park_clock(), "park"
        else:
            want, why = self.top, "idle_unparked"
        self.ceiling = want
        return self.ceiling, self.lid, why

    def busy_headroom(self):
        """True when the card, busy on its own, draws clearly under its power limit (memory-bound work): only then can
        a lower ceiling under queued work save watts. Unknown until the card's own busy draw is learned."""
        n_clk, n_draw = self.native()
        return n_draw is not None and n_draw < 0.92 * self.lid

    def native(self):
        """(busy clock, busy draw) of the card on its own, or (None, None) until enough busy readings are in."""
        if len(self.busy_clk) < self.learn_n:
            return None, None
        c, d = sorted(self.busy_clk), sorted(self.busy_draw)
        return c[len(c) // 2], d[int(0.9 * (len(d) - 1))]

    def take_events(self):
        ev, self.events = self.events, []
        return ev

    def state(self):
        return {"park_step": self.park_step, "park_mhz": self.park_clock(), "park_verdict": self.park_vd.phase or self.park_vd.state,
                "park_allowed": self.park_vd.allowed, "cruise_step": self.busy_step_now, "cruise_mhz": self.cruise_clock(),
                "cruise_verdict": self.busy_vd.phase or self.busy_vd.state, "cruise_allowed": self.busy_vd.allowed,
                "inflight": len(self.inflight), "parked": self.parked, "fail": self.fail, **self.counts}
