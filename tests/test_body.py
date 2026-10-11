# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The body (omnicompass/body.py) and its wires (omnicompass/wire.py): the test set every wire must pass before it is plugged
in (docs/OMNI_V4_PLAN.md, section 3).

  (a) calm it causes   a muscle whose spend calms the service at once (the Kafka case) is judged, never cut off
  (b) a neighbour      a spend that helps its own service and hurts a neighbour is refused, though the whole body improves
  (c) in turn          two muscles asking at once are taken in turn, the louder first; never two trials in flight
  (d) the wall         the wall ends the trial, undoes its step and brakes the body, never past what is proven
  (e) asked again      a refused muscle is asked again only when its own signal returns (and its recheck has passed)
  (f) the hand-back    every wire back at its snapshot; a lever someone else moved is left to them
  the key              a body's wire is written only from the body's tick
"""
import math
import random
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.body import Body, Muscle, SPEND, GIVE
from omnicompass.wire import Wire, NotTheBody, ForeignWriter

KW = dict(min_samples=5, probe_every=2, recheck=60, max_trial=20)


def run(body, seconds, readings_of, cost_of, wall_of=lambda t, at: False, calm_of=lambda t, at: True, per=6, rng=None):
    """Drive a body: each second the samples measured at where the knobs stood, then the body's tick."""
    at = dict(body.targets)
    trace = []
    for t in range(seconds):
        costs, parts = cost_of(at, t)
        r = rng or random.Random(t)
        body.observe([c * math.exp(r.gauss(0, 0.01)) for c in costs] if costs else [],
                     parts={k: [x * math.exp(r.gauss(0, 0.01)) for x in v] for k, v in (parts or {}).items()}, at=at)
        out = body.tick(readings_of(at, t), wall=wall_of(t, at), calm=calm_of(t, at))
        f = body.in_flight()
        n_flight = sum(1 for m in body.muscles.values() for v in m.verdicts.values() if v.phase is not None)
        assert n_flight <= 1, f"{n_flight} trials in flight at once"
        trace.append((t, dict(at), dict(out), (f[0].name, f[1], f[2].phase) if f else None))
        at = dict(out)
    return trace


def calm_it_causes():
    m = Muscle("consumers", 2, 1, (1, 8), **KW)
    b = Body([m])
    # the spend drains the queue: once a third consumer is on, the service is calm and the force asks for nothing more
    readings = lambda at, t: {"consumers": {"force": 0.8 if at["consumers"] <= 2 else -0.1, "spend_ok": at["consumers"] <= 2,
                                            "wanted": 8 if at["consumers"] <= 2 else at["consumers"]}}
    cost = lambda at, t: ([10.0 / at["consumers"] ** 2] * 6, None)
    run(b, 120, readings, cost, calm_of=lambda t, at: at["consumers"] > 2)
    assert b.counts["abandoned"] == 0, b.events
    assert b.counts["allowed"] >= 1 and m.verdicts[SPEND].allowed >= 1, b.events


def a_neighbour():
    m = Muscle("cache_a", 64, 8, (16, 512), **KW)
    b = Body([m])
    # each notch of A's memory makes A 20% cheaper and B, its neighbour, 10% dearer: the body's whole cost (the geometric
    # mean of the two) falls, but B is made worse, so the step is refused
    readings = lambda at, t: {"cache_a": {"force": 0.6, "spend_ok": True, "wanted": 512}}

    def cost(at, t):
        k = (at["cache_a"] - 64) / 8
        a, bb = 10.0 * 0.8 ** k, 10.0 * 1.1 ** k
        return [math.sqrt(a * bb)] * 6, {"a": [a] * 6, "b": [bb] * 6}
    run(b, 80, readings, cost)
    assert m.verdicts[SPEND].allowed == 0, b.record()
    hurt = [e for e in b.events if e["verdict"].startswith("step refused: it makes a part worse")]
    assert hurt and hurt[0]["parts_hurt"] == ["b"], b.events


def in_turn():
    x, y = Muscle("x", 10, 1, (1, 20), **KW), Muscle("y", 10, 1, (1, 20), **KW)
    b = Body([x, y])
    readings = lambda at, t: {"x": {"force": 0.9, "spend_ok": True, "wanted": 20}, "y": {"force": 0.4, "spend_ok": True, "wanted": 20}}
    cost = lambda at, t: ([5.0] * 6, None)
    trace = run(b, 200, readings, cost)
    flights = [f for *_, f in trace if f]                          # run() asserts never two in flight at any second
    first = next(f for f in flights)
    assert first[0] == "x", first                                  # the louder first
    # never two at once, and both had their turn
    assert {f[0] for f in flights} == {"x", "y"}
    assert x.verdicts[SPEND].allowed >= 1 and y.verdicts[SPEND].allowed >= 1


def the_wall():
    m = Muscle("machines", 6, 1, (2, 6), **KW)
    b = Body([m])
    # a give-back trial (one machine fewer) under way when a service hits its line: the trial ends, the step is undone,
    # and the law's fail-up is clamped to what is proven (nothing yet: native, all six machines)
    readings = lambda at, t: {"machines": {"force": -0.7, "give_ok": True, "wanted": 2}}
    cost = lambda at, t: ([3.0] * 6, None)
    wall_at = {}

    def wall(t, at):
        if at["machines"] < 6 and "t" not in wall_at:
            wall_at["t"] = t                                       # the trial's block holds a machine back: the wall
        return "t" in wall_at and t == wall_at["t"]
    trace = run(b, 30, readings, cost, wall_of=wall)
    assert "t" in wall_at, trace[:12]
    t0 = wall_at["t"]
    assert any(e["verdict"] == "trial abandoned (the wall)" for e in b.events), b.events
    after = trace[t0][2]["machines"]
    assert after == 6, (after, trace[t0])                         # the step undone: native, no give-back proven yet
    assert b.counts["walls"] == 1


def asked_again():
    m = Muscle("pool", 20, 1, (2, 90), min_samples=5, probe_every=2, recheck=15, max_trial=20)
    b = Body([m])
    # every give-back costs 50% more: refused; afterwards the pool's own condition is off for a while: no trial; when the
    # condition returns and the recheck has passed, it is asked again
    signal = lambda t: t < 40 or t >= 90
    readings = lambda at, t: {"pool": {"force": -0.5, "give_ok": signal(t), "wanted": 2}}
    cost = lambda at, t: ([4.0 * (1.5 ** (20 - at["pool"]))] * 6, None)
    run(b, 150, readings, cost)
    trials = [e["t"] for e in b.events if e["verdict"] == "trial"]
    assert trials and any(t > 90 for t in trials), trials
    assert not any(40 < t < 90 for t in trials), trials          # no trial while its own signal is off
    assert m.verdicts[GIVE].allowed == 0 and b.counts["refused"] >= 2


class Knob(Wire):
    def __init__(self, value, lo, hi, name):
        super().__init__(lo, hi, name=name)
        self.value = value

    def _read_service(self):
        return 0.0

    def _read_lever(self):
        return self.value

    def _send(self, v):
        self.value = v


def hand_back_and_key():
    a, c = Knob(64, 16, 512, "a"), Knob(20, 2, 90, "c")
    ma, mc = Muscle("a", 64, 8, (16, 512), wire=a, **KW), Muscle("c", 20, 1, (2, 90), wire=c, **KW)
    b = Body([ma, mc])
    try:
        a.write(72)
        raise AssertionError("a write from outside the body's tick was accepted")
    except NotTheBody:
        pass
    readings = lambda at, t: {"a": {"force": 0.5, "spend_ok": True, "wanted": 512}, "c": {"force": -0.5, "give_ok": True, "wanted": 2}}
    cost = lambda at, t: ([2.0] * 6, None)
    run(b, 60, readings, cost)
    assert a.writes + c.writes > 0
    assert b.hand_back() and a.value == 64 and c.value == 20
    # a lever someone else moved is theirs: the body stops writing it and does not restore over it
    a2 = Knob(64, 16, 512, "a2")
    m2 = Muscle("a2", 64, 8, (16, 512), wire=a2, **KW)
    b2 = Body([m2])
    run(b2, 10, lambda at, t: {"a2": {"force": 0.5, "spend_ok": True, "wanted": 512}}, cost)
    a2.value = 300                                                # the operator takes it
    b2.tick({"a2": {"force": 0.5, "spend_ok": True, "wanted": 512}})
    assert m2.handed_over and a2.value == 300
    assert b2.hand_back() and a2.value == 300


def main():
    calm_it_causes(); a_neighbour(); in_turn(); the_wall(); asked_again(); hand_back_and_key()
    print("PASS body: a spend that calms its own service judged, never cut off; a spend that hurts a neighbour refused though "
          "the whole improved; two muscles taken in turn, the louder first; the wall ends the trial, undoes the step and "
          "brakes to what is proven; a refused muscle asked again only when its own signal returns; every wire handed back, "
          "a lever someone else took left to them; a body's wire written only from its tick")


if __name__ == "__main__":
    main()
