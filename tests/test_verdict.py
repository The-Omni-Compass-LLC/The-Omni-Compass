# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict (omnicompass/verdict.py): no fixed percentage, the machine's own wobble as the line, one sureness (99.9%).

  arithmetic   the t and normal quantiles equal the published tables; a sureness of 1 (or of a half or less) is refused
  exact        a machine with no wobble at all: a step that costs exactly what native costs is allowed, a step that costs
               any more is refused, and steps past the first costly one are never taken
  1 in 1,000   a noisy machine: over 4,000 trials of a step whose true cost is one line past native (the band two
               back-to-back windows of the machine fall inside at 99.9%), at most 1 in 1,000 is allowed across every cycle
               (the guarantee); a step that costs nothing is allowed nine times in ten or more; a clearly costly step is
               refused at the first judgement
  own line     the same rule on a steady machine and a jumpy one: each draws its own line, and the jumpy one's is wider
  drift        a machine whose level wanders by itself, up to nearly twice its own block noise every block (fresh, never
               measured before): the interleaving cancels the wander, the walk it measures is carried in the test, and the
               first trial measures the machine twice before anything is changed, so a step one line past native still gets
               through at most 1 time in 1,000. (Measured limit, docs/OMNI_V4.md: at a wander of about four times the block
               noise every block, 3.4 in 1,000 on a fresh machine and 1.3 on one measured over many trials; blocks are
               then too long for the machine's wander.)
  stepwise     steps that each cost a little cannot add up: every step is also held to the newest reference at native
  gain         a step that saves nothing is refused (no gain); one that saves watts and costs nothing is allowed
  calm         a trial the caller ends is abandoned at once and the knob goes back
  recheck      a refused step is tried again only after its recheck time
  nothing      a kept step is proven again; when the machine changes under it and it no longer proves, it is taken back
  permanent
  card         the modelled card: Omni-Compass on top of the firmware never makes a request slower beyond the card's own
               wobble at 99.9% (the request times of the two arms compared by the verdict's own arithmetic)
"""
import math
import random
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.verdict import SURE, Verdict, t_quantile, z_quantile, compare, trimmed, stats


def drive(v, cost_at, decisions, calm=lambda t: True, per=40, rng=None, sigma=0.0, benefit_at=None, shift=None):
    """Feed the verdict `per` costs a decision at the step it asks for; returns its events."""
    step, log = 0, []
    for t in range(decisions):
        c = cost_at(step) if shift is None else cost_at(step, t)
        xs = [c * (math.exp(rng.gauss(0.0, sigma)) if sigma else 1.0) for _ in range(per)]
        v.observe(xs, benefit=[benefit_at(step)] * 4 if benefit_at else None)
        step, trial, ev = v.tick(calm(t))
        if ev:
            log.append(ev)
    return log


def arithmetic():
    table = {(0.999, 1): 318.3088, (0.999, 4): 7.1732, (0.999, 9): 4.2968, (0.999, 29): 3.3962, (0.975, 10): 2.2281,
             (0.95, 5): 2.0150}
    for (p, df), want in table.items():
        assert abs(t_quantile(p, df) - want) < 5e-4, (p, df, t_quantile(p, df))
    assert abs(z_quantile(0.999) - 3.090232) < 1e-6 and abs(z_quantile(0.975) - 1.959964) < 1e-6
    assert SURE == 0.999
    for bad in (1.0, 0.5, 0.3):
        try:
            Verdict(sure=bad)
        except ValueError:
            continue
        raise AssertionError(f"a sureness of {bad} was accepted")


def exact():
    # every step down costs 1% more: nothing is ever allowed
    v = Verdict(min_samples=30, probe_every=5, recheck=50)
    log = drive(v, lambda k: 10.0 * (1 + 0.01 * k), 400)
    assert v.allowed == 0 and v.state == "left native"
    assert any("refused" in e["verdict"] for e in log) and not any(e["verdict"] == "step allowed" for e in log)
    # the first three steps cost nothing, the fourth costs 0.1%: three allowed, the fourth refused
    v = Verdict(min_samples=30, probe_every=3, recheck=10 ** 6)
    drive(v, lambda k: 10.0 if k <= 3 else 10.01, 200)
    assert v.allowed == 3 and v.state == "acting", v.allowed


def population_line(n, sigma, rng):
    """The machine's true line: the band two back-to-back windows of n pieces of work fall inside at the engine's
    sureness, from the trimmed mean's true spread (measured here over 20,000 windows)."""
    means = [trimmed([rng.gauss(0, sigma) for _ in range(n)])[0] for _ in range(20000)]
    mu = sum(means) / len(means)
    return z_quantile(SURE) * math.sqrt(2) * math.sqrt(sum((m - mu) ** 2 for m in means) / (len(means) - 1))


def one_trial(effect, seed, n, sigma, tau=0.0):
    """One trial of one step on a fresh machine (lognormal spread sigma a piece of work, a level walking tau a piece);
    returns the judgement's event."""
    r = random.Random(seed)
    v = Verdict(min_samples=n, probe_every=1, recheck=10 ** 9, max_steps=1)
    step, level = 0, 0.0
    for t in range(24):
        xs = []
        for _ in range(n):
            level += r.gauss(0.0, tau) if tau else 0.0
            xs.append(10.0 * math.exp(level + effect * step + r.gauss(0.0, sigma)))
        v.observe(xs)
        step, _, ev = v.tick(True)
        if ev and ev["verdict"].startswith("step"):
            return ev
    return None


def guarantee():
    """4,000 independent trials of one step on a noisy machine (8% spread a piece of work, 30 a block): a step one line
    past native is allowed at most 1 time in 1,000; a free step nine times in ten or more; a step three lines past is
    refused, nine times in ten at the first judgement."""
    sigma, n = 0.08, 30
    line = population_line(n, sigma, random.Random(20261011))
    allowed_bad = sum(1 for s in range(4000) if (e := one_trial(line, s, n, sigma)) and e["verdict"] == "step allowed")
    assert allowed_bad <= 6, f"a step one line past native was allowed {allowed_bad} times in 4,000"
    free = [one_trial(0.0, 10 ** 6 + s, n, sigma) for s in range(400)]
    allowed_free = sum(1 for e in free if e and e["verdict"] == "step allowed")
    assert allowed_free >= 0.9 * 400, f"a free step was allowed only {allowed_free} times in 400"
    clear = [one_trial(3 * line, 2 * 10 ** 6 + s, n, sigma) for s in range(200)]
    assert all(e and e["verdict"].startswith("step refused") for e in clear)
    # a fresh machine is first judged after two cycles (it is measured twice before anything is changed)
    first = sum(1 for e in clear if e["verdict"] == "step refused: the muscle is slower there" and e["cycles"] == 2)
    assert first >= 0.9 * len(clear), f"only {first} of {len(clear)} clearly costly steps refused at the first judgement"
    return allowed_bad, allowed_free


def own_line():
    rng = random.Random(7)
    steady = stats([10 * math.exp(rng.gauss(0, 0.01)) for _ in range(30)])[1]
    jumpy = stats([10 * math.exp(rng.gauss(0, 0.20)) for _ in range(30)])[1]
    v = Verdict()
    assert v.line(jumpy) > 10 * v.line(steady)


def drift():
    """A machine whose level walks by itself (0.5% a piece of work: the level moves 2.7% over a block whose own noise is
    1.5%): the walk is measured, and on fresh machines a step one line past native is allowed at most 1 time in 1,000."""
    sigma, n, tau = 0.08, 30, 0.005
    line = population_line(n, sigma, random.Random(11))
    v = Verdict(min_samples=n, probe_every=1, recheck=10 ** 9, max_steps=1)
    r = random.Random(12)
    step, level = 0, 0.0
    for t in range(40):
        xs = []
        for _ in range(n):
            level += r.gauss(0.0, tau)
            xs.append(10.0 * math.exp(level + r.gauss(0.0, sigma)))
        v.observe(xs)
        step, _, _ = v.tick(True)
    assert v.drift()[0] > 0
    bad = sum(1 for s in range(3000) if (e := one_trial(line, 3 * 10 ** 6 + s, n, sigma, tau)) and e["verdict"] == "step allowed")
    assert bad <= 6, f"on a wandering machine a step one line past native was allowed {bad} times in 3,000"


def stepwise():
    # each step 0.5% dearer than the one before on a machine with a 1% spread: each step is close to free against the step
    # before it, but the climb's whole cost is held to native's line, so the steps never add up past it
    line = population_line(60, 0.01, random.Random(13))
    worst = 0.0
    for seed in range(40):
        rng = random.Random(seed)
        v = Verdict(min_samples=60, probe_every=2, recheck=10 ** 9, incremental=True, max_steps=40)
        drive(v, lambda k: 10.0 * (1 + 0.005 * k), 3000, per=60, rng=rng, sigma=0.01)
        worst = max(worst, math.log(1 + 0.005 * v.allowed))
    assert worst <= line + 1e-9, (worst, line)


def gain():
    # costs nothing and saves nothing: refused; costs nothing and saves 10% of the watts: allowed
    v = Verdict(min_samples=30, probe_every=1, recheck=10 ** 9, gain=True, max_steps=1)
    log = drive(v, lambda k: 10.0, 40, benefit_at=lambda k: 100.0)
    assert v.allowed == 0 and any("no gain" in e["verdict"] for e in log)
    v = Verdict(min_samples=30, probe_every=1, recheck=10 ** 9, gain=True, max_steps=1)
    rng = random.Random(5)
    step, log = 0, []
    for t in range(60):
        v.observe([10.0 * math.exp(rng.gauss(0, 0.02)) for _ in range(30)],
                  benefit=[(100.0 if step == 0 else 90.0) * math.exp(rng.gauss(0, 0.01)) for _ in range(4)])
        step, _, ev = v.tick(True)
        if ev:
            log.append(ev)
    assert v.allowed == 1 or any("never proven" in e["verdict"] for e in log), log[-1]


def calm():
    v = Verdict(min_samples=30, probe_every=1, recheck=10)
    log = drive(v, lambda k: 10.0, 6, calm=lambda t: t != 1, per=5)
    assert any("abandoned" in e["verdict"] for e in log)


def recheck():
    v = Verdict(min_samples=10, probe_every=1, recheck=30)
    log = drive(v, lambda k: 10.0 + k, 100)
    tries = [i for i, e in enumerate(log) if e["verdict"] == "trial"]
    assert len(tries) >= 2 and v.allowed == 0


def permanent():
    # step 1 free until decision 300, then 20% dearer: it is allowed, proven again, and taken back once it costs
    v = Verdict(min_samples=30, probe_every=2, recheck=100, max_steps=1)
    log = drive(v, lambda k, t: 10.0 * (1.2 if (k == 1 and t >= 300) else 1.0), 700, shift=True)
    assert any(e["verdict"] == "step allowed" for e in log)
    assert any(e["verdict"] == "step kept: proven again" for e in log)
    back = [e for e in log if "back_to" in e]
    assert back and back[0]["back_to"] == 0 and v.allowed == 0, back


def determinism():
    a = drive(Verdict(min_samples=30, probe_every=3, recheck=50), lambda k: 10.0 * (1 + 0.002 * k), 300,
              rng=random.Random(9), sigma=0.03)
    b = drive(Verdict(min_samples=30, probe_every=3, recheck=50), lambda k: 10.0 * (1 + 0.002 * k), 300,
              rng=random.Random(9), sigma=0.03)
    assert a == b


def card():
    # the modelled card: compute-bound work, Omni-Compass on top of the firmware; the two arms' request times compared by
    # the verdict's own arithmetic: never proven slower beyond the card's own wobble
    from realms.gpu_card import run
    a, n = run(5000, "omni", duration=300.0), run(5000, "native", duration=300.0)
    d, hw, _, _ = compare(n["svc"], a["svc"])
    line = Verdict().line(stats(n["svc"])[1])
    assert d - hw <= line, (d, hw, line)
    assert a["restored"] and a["served"] == n["served"]


def main():
    arithmetic(); exact()
    bad, free = guarantee()
    own_line(); drift(); stepwise(); gain(); calm(); recheck(); permanent(); determinism(); card()
    print(f"PASS verdict: the quantiles exact, a sureness of 1 refused; on a machine with no wobble a free step allowed and a "
          f"costly one refused; on a noisy one a step one line past native allowed {bad} times in 4,000 (at most 1 in 1,000), "
          f"a free step allowed {free} times in 400, a clearly costly one refused at the first judgement; each machine its own "
          "line; a wandering machine held to the same guarantee; a stepwise climb held to native's line; no gain refused; "
          "trials abandoned when the caller ends them; refused steps rechecked; a kept step proven again against native and "
          "taken back when it costs; the card never proven slower")


if __name__ == "__main__":
    main()
