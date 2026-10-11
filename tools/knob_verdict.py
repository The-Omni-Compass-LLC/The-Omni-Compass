# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The brain's own verdict on one live knob, in real time (the founder's order of 9 October 2026).

Every knob starts in watch: one wire out, nothing written. It is written only between native and the deepest step a paired
trial on the stack itself has allowed under the declared objective, and a step that fails its trial is not taken. The
trial, the judgement, the line and the recheck are the engine's (omnicompass/verdict.py: no fixed percentage, the knob's own
wobble as the line, one sureness of 99.9% for the whole engine); this module gives that Verdict the knob's notch, the cost
it judges and the condition under which a trial of this knob is fair. Nothing in the engine changes.

  two directions   spend (more of the resource: a bigger ceiling, more consumers, more connections) and give back (less:
                   fewer connections, a smaller pool or cache), each its own Verdict with its own steps outward from native.
                   Restoring native is never a step: the knob may always be moved back toward the operator's setting.
  the condition    a give-back step is tried while the service is calm and the stack's own give-back condition holds (the
                   engine's rule: a trial is never run under stress); a spend step is tried while the compass asks to spend
                   and the stack's own spend condition holds (a cache full and missing, messages waiting, clients queued),
                   because that is the only time a spend can show what it buys. A give-back trial once started runs on
                   until its samples are in unless the service leaves calm, when it is abandoned (the engine's rule). A
                   spend trial runs to its samples whatever the compass's force: the spend's own effect calms the service
                   within seconds, and a trial ended on that calm could never be judged (the first counted set of 10
                   October 2026 abandoned every Kafka spend trial that way; amendment 3 in the five preregistrations). Only
                   the wall (a fail-up) or the engine's own time limit ends a spend trial early.
  the cost         one sample a second from the stack's own readings. Under the resource objective, the preregistered
                   reading of the Omni index, cost = resource held x host CPU busy share x latency / work: a step passes only
                   if the service gained outweighs the resource and CPU spent, by the index's own arithmetic (a geometric mean
                   of the four ratios no lower than one is the same statement). Under the service objective cost = latency /
                   work: the resources are shown and not judged. Lower is better; a step passes when the engine is 99.9% sure
                   its cost stays inside the knob's own wobble, which is the engine's judge, so a step that costs more than it
                   buys is refused and nothing unproven is taken.
  the hold         during a trial the knob stands at the phase's value whatever the compass asks: the reference at the
                   deepest step already allowed (native at first), then the trial step one notch further. Between trials the
                   compass moves the knob by its own law, clamped to the allowance. A fail-up never spends beyond the
                   allowance; toward native it is always free.
  the record       every trial, allowance, refusal and abandonment is kept for the audit, with the counts and the state:
                   "left native" (no step allowed in either direction) or "acting" with the allowance.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omnicompass.body import Body, Muscle, SPEND, GIVE  # noqa: E402  (the engine's body, Omni v4)

RESOURCE, SERVICE, PER_WORK = "resource", "service", "per-work"
OBJECTIVES = (RESOURCE, SERVICE, PER_WORK)


def sample_cost(objective, work, latency, resource, cpu_share):
    """One second's cost under the objective, lower is better; None when nothing worked (nothing was measured).

    resource   the index's reading: resource x host CPU busy share x latency / work (declared 9 October)
    service    latency / work: the resources shown, not judged (declared 9 October)
    per-work   resource / work: the resource spent per unit of work inside the line, the speed left to the compass's own line
               as the guardrail (the card's reading, work per energy; added 10 October for the machine's own power, where the
               resource is the energy the processor's meter reads)"""
    if work is None or latency is None or work <= 0 or latency < 0:
        return None
    if objective == SERVICE:
        return latency / work
    if objective == PER_WORK:
        return max(float(resource), 1e-9) / work
    cpu = 1.0 if cpu_share is None else max(float(cpu_share), 1e-3)
    return max(float(resource), 1e-9) * cpu * latency / work


class KnobVerdict:
    """One live knob as a body of one muscle (omnicompass/body.py, Omni v4): the engine's body does the granting, the
    reflex rule, the wall and the clamping; this adapter gives it the knob's notch, the settle and the harness's words."""

    def __init__(self, native, notch, cover, objective=RESOURCE, min_samples=8, probe_every=20, recheck=60,
                 max_trial=40, settle_s=2.0):
        if objective not in OBJECTIVES:
            raise ValueError(f"objective must be one of {OBJECTIVES}, not {objective!r}")
        lo, hi = cover
        self.native, self.notch, self.lo, self.hi = native, notch, lo, hi
        self.objective = objective
        self.settle_s = settle_s
        self.muscle = Muscle("knob", native, notch, cover, min_samples=min_samples, probe_every=probe_every,
                             recheck=recheck, max_trial=max_trial, incremental=True)
        self.body = Body([self.muscle], name="knob")
        self.verdicts = self.muscle.verdicts
        self.events = []
        self.counts = {"trials": 0, "allowed": 0, "refused": 0, "abandoned": 0, "clamped": 0, "held": 0, "samples": 0,
                       "proven_again": 0, "taken_back": 0}
        self.last_value, self.changed_at, self.t = native, None, 0.0

    # ---------------------------------------------------------------------------------------------- the steps
    def value_of(self, direction, step):
        return self.muscle.value_of(direction, step)

    @property
    def phase_dir(self):
        """The direction whose trial holds the knob, or None."""
        f = self.muscle.in_flight()
        return f[0] if f else None

    @property
    def allowed_low(self):
        return self.muscle.allowed_low

    @property
    def allowed_high(self):
        return self.muscle.allowed_high

    @property
    def state(self):
        return self.muscle.state

    # ---------------------------------------------------------------------------------------------- the samples
    def observe(self, cost, t, settled=True):
        """This second's cost sample, measured under the value the knob stood at. Fed to the trial in flight, once the
        knob has settled after its last change; nothing else is kept."""
        if cost is None or not settled or self.phase_dir is None:
            return False
        if self.changed_at is not None and t - self.changed_at < self.settle_s:
            return False
        if self.body.observe([cost], at={"knob": self.last_value}):
            self.counts["samples"] += 1
            return True
        return False

    # ---------------------------------------------------------------------------------------------- the decision
    def decide(self, wanted, spend_ok, give_ok, t, why="", stress=None, calm=None, fail_up=False):
        """The compass's wanted value becomes the knob's target: the block's value while a trial holds the knob, the wanted
        value clamped to the allowance otherwise. spend_ok / give_ok: the stack's own conditions for a step in each direction
        this second (the compass asking to spend with the stack full and missing; calm with the stack holding its demand).
        stress / calm: the service past the cushion toward the line / inside the calm cushion (the compass's force): a
        give-back trial is abandoned when the service leaves calm; a spend trial runs to its samples whatever the force (the
        reflex rule, now the engine's own). fail_up: the service at the wall: every trial is abandoned and the knob goes
        where the fail-up says, native always free, never beyond the allowance.
        Returns (target, why, info)."""
        self.t = t
        stress = bool(spend_ok) if stress is None else bool(stress)
        force = 1.0 if spend_ok else (-1.0 if give_ok else 0.0)
        n0 = len(self.body.events)
        out = self.body.tick({"knob": {"force": force, "spend_ok": bool(spend_ok), "give_ok": bool(give_ok),
                                       "wanted": wanted}}, wall=bool(fail_up), calm=not stress)
        for ev in self.body.events[n0:]:
            e = {k: v for k, v in ev.items() if k not in ("muscle",)}
            e["t"] = round(t, 1)
            self.events.append(e)
            self._count(e)
        target = out.get("knob", self.last_value)
        info = {"verdict_phase": None, "verdict_direction": self.phase_dir, "allowed_low": self.allowed_low,
                "allowed_high": self.allowed_high}
        f = self.muscle.in_flight()
        if f is not None:
            info["verdict_phase"] = f[1].phase
            if target != wanted:
                self.counts["held"] += 1
            why = f"{why}; held by the verdict: {f[0]} {'reference' if f[1].phase == 'ref' else 'trial'} at {target}"
        elif target != wanted:
            self.counts["clamped"] += 1
            why = f"{why}; the verdict allows {self.allowed_low} to {self.allowed_high}: held at {target}"
        if target != self.last_value:
            self.changed_at, self.last_value = t, target
        return target, why, info

    def _count(self, ev):
        s = ev.get("verdict", "")
        if s == "trial":
            self.counts["trials"] += 1
        elif s == "step allowed":
            self.counts["allowed"] += 1
        elif s.startswith("step refused"):
            self.counts["refused"] += 1
        elif s.startswith("trial abandoned"):
            self.counts["abandoned"] += 1
        elif s.startswith("step kept"):
            self.counts["proven_again"] += 1
        if "back_to" in ev:
            self.counts["taken_back"] += 1

    # ---------------------------------------------------------------------------------------------- the record
    def record(self, keep_events=400):
        return {"objective": self.objective, "state": self.state, "native": self.native, "notch": self.notch,
                "spend_allowed_steps": self.verdicts[SPEND].allowed, "give_back_allowed_steps": self.verdicts[GIVE].allowed,
                "allowed_low": self.allowed_low, "allowed_high": self.allowed_high, "counts": dict(self.counts),
                "events": self.events[:keep_events], "events_total": len(self.events)}


def summarize(records):
    """One line for a table from the omni arms' verdict records of one workload: the state of each arm and the allowance."""
    if not records:
        return "no verdict record"
    parts = []
    for r in records:
        c = r.get("counts", {})
        parts.append(f"{r.get('state', '?')} ({c.get('trials', 0)} trials, {c.get('allowed', 0)} allowed, {c.get('refused', 0)} refused)")
    return "; ".join(parts)
