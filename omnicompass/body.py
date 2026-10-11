# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The body: one body, one brain, one tick (Omni v4, docs/OMNI_V4_PLAN.md, sections 1 and 3).

A body is every knob that acts on the same service: a cluster's machines and its pods' targets, a card's park and cruise
clocks, one database's cache or pool. It holds every one of those muscles and decides for all of them at once, every tick.

  read first   every muscle's reading and the whole body's state come in before anything is decided: each muscle's compass
               force (the law's urge from where its service sits in its band, smooth, never a hammer), what the law wants
               for it, and its own conditions (something to buy for a spend: messages waiting, a cache missing, clients
               queued; the whole body calm for a give-back)
  no forcing   a spend is tried only when the muscle's own reading says there is something to buy; a give-back only when the
               whole body is calm. The brain never moves a muscle because it wants to
  one trial    at most one new trial a tick, and one in flight at a time: two muscles moved together could not be told apart.
               The trial goes to the muscle asking loudest (the largest force) whose own condition holds; every other muscle
               keeps acting inside what it has already proven. Nothing is frozen; only new trials wait their turn
  the reflex   a trial runs to its full measurement and is never ended by the calm it causes: a spend trial runs on whatever
  rule         the force; a give-back trial ends when the body leaves calm; both end at the wall or at the verdict's own time
               limit, and nothing else ends them
  the body's   the samples the body is judged on are the body's own cost (all its work, speed, machines and resources: the
  cost         Omni index's own arithmetic), with each part of the body (each service) guarded too: a step that makes any part
               worse is refused even when the whole improves (omnicompass/verdict.py, the guard for every part)
  the wall     a service of the body at its line ends the trial in flight, undoes its step, and turns every muscle to the law's
               brake: the law's fail-up, clamped to what each muscle has proven (never a spend beyond its proof; native is
               always free)
  nothing      every kept step is proven again against native (the verdict's recheck) and taken back when it no longer pays;
  permanent    a muscle at native is asked again whenever its signal returns
  the wire     every muscle's wire is plugged into the body (omnicompass/wire.py): written only from the body's tick, with the
               body's key; the hand-back restores every snapshot

The verdict (omnicompass/verdict.py) gives each muscle its steps from native in two directions, spend (more capacity, power,
memory, consumers) and give back (less), each proven on the body before the law may use it.
"""
from __future__ import annotations

from omnicompass.verdict import Verdict
from omnicompass.wire import ForeignWriter, clamp

SPEND, GIVE = "spend", "give back"


class Muscle:
    """One knob of a body: native, its notch, its cover, its two verdicts and, on a real system, its wire. values: the
    settings each direction's steps stand at, when they are not whole notches ({direction: [step 1, step 2, ...]}, a
    card's park levels); kw: options for one direction's verdict ({direction: {...}}: coarse to fine, a gain to prove)."""

    def __init__(self, name, native, notch, cover, wire=None, values=None, kw=None, **verdict_kw):
        lo, hi = cover
        self.name, self.native, self.notch, self.lo, self.hi = name, native, notch, lo, hi
        self.wire = wire
        self.values = {d: list(v) for d, v in (values or {}).items()}
        base = dict(verdict_kw)
        base.setdefault("incremental", True)
        self.verdicts = {}
        for d, n in ((SPEND, int((hi - native) // notch)), (GIVE, int((native - lo) // notch))):
            k = dict(base, **(kw or {}).get(d, {}))
            self.verdicts[d] = Verdict(max_steps=max(0, len(self.values[d]) if d in self.values else n), **k)
        self.handed_over = False                         # someone else wrote the lever: it is theirs, the body stops

    def value_of(self, direction, step):
        if step <= 0:
            return self.native
        if direction in self.values:
            return self.values[direction][min(step, len(self.values[direction])) - 1]
        v = self.native + step * self.notch if direction == SPEND else self.native - step * self.notch
        return clamp(v, self.lo, self.hi)

    @property
    def allowed_low(self):
        return self.value_of(GIVE, self.verdicts[GIVE].allowed)

    @property
    def allowed_high(self):
        return self.value_of(SPEND, self.verdicts[SPEND].allowed)

    def in_flight(self):
        """(direction, verdict) of this muscle's trial in flight, or None."""
        for d, v in self.verdicts.items():
            if v.phase is not None:
                return d, v
        return None

    @property
    def state(self):
        if self.verdicts[SPEND].allowed == 0 and self.verdicts[GIVE].allowed == 0:
            return "left native"
        return f"acting: {self.allowed_low} to {self.allowed_high}"


class Body:
    def __init__(self, muscles, name="body"):
        self.name = name
        self.muscles = {m.name: m for m in muscles}
        self.key = object()                               # the body's key: its wires are written only from its tick
        for m in muscles:
            if m.wire is not None:
                m.wire.plug(self.key)
                m.wire.attach()
        self.t = 0
        self.events = []
        self.targets = {m.name: m.native for m in muscles}
        self.counts = {"trials": 0, "allowed": 0, "refused": 0, "abandoned": 0, "walls": 0, "held": 0, "clamped": 0}

    # ---- the trial in flight -------------------------------------------------------------------------------------
    def in_flight(self):
        """(muscle, direction, verdict) of the one trial in flight, or None."""
        for m in self.muscles.values():
            f = m.in_flight()
            if f is not None:
                return m, f[0], f[1]
        return None

    def observe(self, costs, benefit=None, parts=None, at=None):
        """The body's cost (one sample per piece of work or per second, the index's arithmetic over the whole body), its
        second reading where the trial asks for a gain, and each part's own cost, measured since the last tick. They count
        only for the trial in flight, and only if its muscle stood where the trial's block holds it (at: {muscle: value}
        as the muscle reports it; by default the targets the body last handed out)."""
        f = self.in_flight()
        if f is None:
            return False
        m, d, v = f
        pos = v.position()
        if pos is None:
            return False
        stood = (at or {}).get(m.name, self.targets.get(m.name))
        if stood is None or abs(stood - m.value_of(d, pos)) > 1e-9 * max(1.0, abs(stood)):
            return False
        v.observe(costs, benefit, parts)
        return True

    # ---- the tick ------------------------------------------------------------------------------------------------
    def tick(self, readings, wall=False, calm=True):
        """One decision for the whole body.

        readings: {muscle: {"force": the compass force (positive asks to spend, negative to give back),
                            "wanted": the value the law wants now, "spend_ok": the muscle's own reading says there is
                            something to buy, "give_ok": its own condition to give back}}; a muscle without a reading
                  holds where it stands.
        wall: a service of the body at its line. calm: the whole body inside its compasses.
        Returns {muscle: target}; with wires, the targets are written through them with the body's key."""
        self.t += 1
        flight = self.in_flight()
        ended = False
        if flight is not None:
            m, d, v = flight
            # the reflex rule: a spend trial runs on whatever the force; a give-back trial needs the body calm; the wall
            # ends either
            go_on = (not wall) and (calm if d == GIVE else True)
            _, _, ev = v.tick(go_on)
            if ev:
                if wall and "abandoned" in ev["verdict"]:
                    ev = dict(ev, verdict="trial abandoned (the wall)")
                self._event(m, d, ev)
            ended = v.phase is None
        granted = None
        if not wall and not ended and self.in_flight() is None:
            asking = []
            for m in self.muscles.values():
                if m.handed_over:
                    continue
                r = readings.get(m.name) or {}
                f = float(r.get("force", 0.0) or 0.0)
                if f > 0 and r.get("spend_ok") and m.verdicts[SPEND].ready():
                    asking.append((-abs(f), m.name, SPEND))
                elif f < 0 and r.get("give_ok") and calm and m.verdicts[GIVE].ready():
                    asking.append((-abs(f), m.name, GIVE))
            if asking:
                asking.sort()
                granted = (asking[0][1], asking[0][2])
        for m in self.muscles.values():
            for d, v in m.verdicts.items():
                if flight is not None and v is flight[2]:
                    continue                              # ticked above
                _, _, ev = v.tick(granted == (m.name, d))
                if ev:
                    self._event(m, d, ev)
        # every muscle's target: the trial's block for the muscle on trial; the law's value, clamped to what the muscle
        # has proven, for every other (at the wall the law's own fail-up, clamped the same way)
        f = self.in_flight()
        out = {}
        for m in self.muscles.values():
            if m.handed_over:
                continue
            r = readings.get(m.name) or {}
            if f is not None and m is f[0]:
                target = m.value_of(f[1], f[2].position())
                if r.get("wanted") is not None and target != r["wanted"]:
                    self.counts["held"] += 1
            else:
                wanted = r.get("wanted", self.targets.get(m.name, m.native))
                target = clamp(wanted, m.allowed_low, m.allowed_high)
                if target != wanted:
                    self.counts["clamped"] += 1
            out[m.name] = target
        if wall:
            self.counts["walls"] += 1
        self.targets.update(out)
        self._write(out)
        return out

    def _write(self, targets):
        for name, value in targets.items():
            m = self.muscles[name]
            if m.wire is None:
                continue
            try:
                m.wire.write(value, key=self.key)
            except ForeignWriter as e:
                # one writer: the lever is someone else's now; every trial of this muscle ends, and it is left alone
                m.handed_over = True
                for d, v in m.verdicts.items():
                    if v.phase is not None:
                        v.tick(False)
                self.events.append({"t": self.t, "muscle": name, "verdict": f"handed over: {e}"})

    def _event(self, m, d, ev):
        self.events.append({"t": self.t, "muscle": m.name, "direction": d, **ev})
        s = ev.get("verdict", "")
        if s.startswith("trial") and not s.startswith("trial abandoned"):
            self.counts["trials"] += 1
        elif s == "step allowed":
            self.counts["allowed"] += 1
        elif s.startswith("step refused"):
            self.counts["refused"] += 1
        elif s.startswith("trial abandoned"):
            self.counts["abandoned"] += 1

    # ---- the hand-back -------------------------------------------------------------------------------------------
    def hand_back(self):
        """Every trial ended and every wire back at its snapshot (the kill switch, the end of a run). True: all restored."""
        for m in self.muscles.values():
            for v in m.verdicts.values():
                if v.phase is not None:
                    v.tick(False)
        ok = True
        for m in self.muscles.values():
            self.targets[m.name] = m.native
            if m.wire is not None:
                ok = m.wire.restore() and ok
        return ok

    def record(self, keep_events=400):
        return {"name": self.name, "counts": dict(self.counts), "events": self.events[:keep_events],
                "events_total": len(self.events),
                "muscles": {n: {"state": m.state, "native": m.native, "allowed_low": m.allowed_low,
                                "allowed_high": m.allowed_high, "handed_over": m.handed_over}
                            for n, m in self.muscles.items()}}
