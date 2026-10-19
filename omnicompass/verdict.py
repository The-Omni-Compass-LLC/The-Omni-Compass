# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict: Omni-Compass moves a knob only where it measures that the muscle loses nothing by it.

Omni-Compass sits on top of a muscle that already works (a card's firmware, an autoscaler, a chiller's loop). It does not
replace that muscle, and it has no reason to move the muscle's knob unless moving it costs the muscle nothing. The
verdict is how the brain finds that out, on the muscle itself, before it acts and again from time to time:

  steps     the knob's settings from native outward, in whole steps (step 0 is native: the muscle as it runs alone)
  cost      what each setting costs the muscle's own work, measured per piece of work (a card: the milliseconds it spends
            on one request, the wait in the queue left out, so more traffic is never mistaken for a slower card)
  probe     while the service is calm, a paired trial: first the knob at native until min_samples pieces of work are
            measured (the reference, fresh, under the same traffic), then at one step past the deepest step already
            allowed until min_samples more are measured
  judge     the trial step's median cost against the reference's: no higher (within the measurement's resolution,
            tolerance) and the step is allowed; higher and it is refused, the knob goes back, and that step is not tried
            again until recheck decisions have passed (the work may have changed). A trial that sees the service leave
            calm is abandoned, and the knob goes back at once
  allowed   the compass may move the knob only between native and the deepest allowed step; where no step is allowed, the
            verdict is "left native" and the knob is never moved

  stepwise  for a knob that is slow to move back (a machine given back takes minutes to return), incremental=True runs
            the reference at the deepest step already allowed instead of at native, and judges the trial step against
            both that reference and the cost first measured at native, so steps can never add up past the allowance

The verdict never makes the knob more aggressive than the law: it only narrows where the law may go. Every probe and
every judgement is returned to the caller for the audit.

  in words  (Omni v7, judge="interval": the reports' own words, GAIN, EVEN and LOSS, as the code that steers the knob,
            docs/omni_v5/NEXT_VERSION_PLAN.md section 1) the trial step is read exactly as a report reads a row: the 95%
            interval of its change in cost, on the logarithm of each piece of work's cost (so a heavy tail does not
            decide it), d = mean ln c_trial − mean ln c_ref ± 1.96 se. The interval wholly above zero is a LOSS: the step
            is refused and undone, whatever the allowance says. Wholly below zero is a GAIN, and across zero is EVEN.
            While the interval is wider than the allowance (its half-width over τ = ln(1 + tolerance)) the trial measures
            on, up to three times min_samples. A GAIN or an EVEN step is allowed only if both estimates of its change
            are within the allowance: the median (the guard of the engines before v7, kept) and the mean of the log
            costs, d ≤ τ. A stepwise step is read, the same way, against the costs first measured at native. On noisy
            work this refuses a step that truly costs 3% more against a 2% allowance about a quarter less often than the
            medians alone allowed it, and one that costs 5% more about half as often, while a free step is kept almost
            as often (tests/test_verdict_interval.py). judge="median" keeps the engines before v7 (the medians alone).

  upper end (Omni v12, judge="upper", the default) a step is kept only when the upper end of every 95% interval of its
            change in cost is inside the allowance, d + 1.96 se ≤ τ, so a step whose cost could reach past the allowance is
            never kept on its estimate alone (judge="interval" kept it when d ≤ τ, and at the noise of the omni-v10 data-store
            tables a step that truly costs 3% was kept about 31% of the time). The reference is measured long enough, from its
            own spread s (the standard deviation of its log costs), that a step costing nothing shows its whole interval inside
            the allowance at least 95% of the time: n ≥ 2 s² (1.96 + 1.645)² / τ² pieces of work in each phase, never fewer than
            min_samples. When the work arrives too slowly for both phases to measure that many inside the trial's time
            (max_trial decisions each, at the rate the reference measured), the trial is not started: the knob stays where it
            is allowed, the event says why, and it is tried again after probe_every decisions. The trial step is read once, at
            its n, never measured on until it passes. A step that truly costs the whole allowance is kept at most 2.5% of the
            time, one that costs more less often (tests/test_verdict_upper.py).
"""
from __future__ import annotations

import math

Z95 = 1.96                       # the two-sided 95% interval every report reads (tools/readings.py)
Z_FREE = 1.645                   # judge="upper": a step that costs nothing is kept at least 95% of the time (v12)


def median(xs):
    s = sorted(xs)
    n = len(s)
    return None if n == 0 else (s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2]))


def log_stats(xs):
    """(mean, variance, n) of the logarithms of the positive costs; the variance is infinite with fewer than two."""
    ls = [math.log(x) for x in xs if x is not None and x > 0]
    n = len(ls)
    if n == 0:
        return None
    m = sum(ls) / n
    var = sum((x - m) ** 2 for x in ls) / (n - 1) if n > 1 else math.inf
    return m, var, n


def change_interval(ref, got, z=Z95):
    """The 95% interval of the change in log cost from ref to got (Welch's standard error), or None if either is empty."""
    a, b = log_stats(ref), log_stats(got)
    if a is None or b is None:
        return None
    d = b[0] - a[0]
    se = math.sqrt(a[1] / a[2] + b[1] / b[2]) if math.isfinite(a[1]) and math.isfinite(b[1]) else math.inf
    return d - z * se, d + z * se


def pieces_needed(xs, tolerance, min_samples, z=Z95, z_free=Z_FREE):
    """judge="upper": the pieces of work each phase needs, from the spread of xs, for a step that costs nothing to show
    its whole 95% interval inside the allowance at least 95% of the time: n ≥ 2 s² (z + z_free)² / τ² (equal phases)."""
    st = log_stats(xs)
    tau = math.log(1.0 + tolerance)
    if st is None or not math.isfinite(st[1]) or tau <= 0.0:
        return math.inf
    return max(int(min_samples), math.ceil(2.0 * st[1] * (z + z_free) ** 2 / tau ** 2))


class Verdict:
    def __init__(self, tolerance=0.005, min_samples=30, probe_every=120, recheck=1800, max_steps=60, max_trial=30,
                 incremental=False, judge="upper"):
        self.tol = tolerance
        self.judge = judge
        self.native_ref = None            # the costs measured at native (incremental, judge="interval")
        self.min_n = min_samples
        self.probe_every = probe_every
        self.recheck = recheck
        self.max_steps = max_steps
        self.max_trial = max_trial        # decisions a trial phase may take before it is abandoned
        self.incremental = incremental
        self.native_cost = None           # the cost measured at native (incremental: the bound every step is held to)
        self.allowed = 0                  # deepest step allowed (0: native only)
        self.refused_until = {}           # step -> decision index before which it is not tried again
        self.phase = None                 # None, "ref" (knob at native) or "trial" (knob at the trial step)
        self.trial = None
        self.ref, self.got = [], []
        self.need = None                  # judge="upper": the pieces of work each phase measures, from the reference's spread
        self.phase_t = 0
        self.t = 0
        self.last_probe = -10 ** 9

    @property
    def state(self):
        return "left native" if self.allowed == 0 else "acting"

    def observe(self, costs):
        """Costs (one per piece of work) measured since the last decision, under the step tick() last returned."""
        if self.phase == "ref":
            self.ref.extend(costs)
        elif self.phase == "trial":
            self.got.extend(costs)

    def _end(self):
        self.phase, self.trial, self.ref, self.got, self.need = None, None, [], [], None

    def tick(self, calm):
        """One decision. calm: the service is inside its compass and nothing waits (a trial is never run under stress).
        Returns (the step the knob must stand at during a trial, or the deepest step the law may use; is_trial; event).
        The event, if any, is for the audit."""
        self.t += 1
        event = None
        if self.phase is not None and (not calm or self.t - self.phase_t > self.max_trial):
            event = {"verdict": "trial abandoned (service not calm)" if not calm else "trial abandoned (too little work)",
                     "step": self.trial}
            self._end()
        elif self.phase == "ref" and self.judge == "upper" and len(self.ref) >= max(self.min_n, self.need or 0):
            need = pieces_needed(self.ref, self.tol, self.min_n)
            rate = len(self.ref) / max(1, self.t - self.phase_t)          # pieces of work a decision, as the reference saw
            if need > rate * self.max_trial:
                event = {"verdict": "trial not started: the work too noisy to read the step in a trial's time",
                         "step": self.trial, "pieces_needed": need if math.isfinite(need) else None,
                         "pieces_a_decision": round(rate, 3)}
                self._end()
            elif len(self.ref) >= need:
                self.need, self.phase, self.phase_t = need, "trial", self.t
            else:
                self.need = need                                          # the reference measures on to its n
        elif self.phase == "ref" and self.judge != "upper" and len(self.ref) >= self.min_n:
            self.phase, self.phase_t = "trial", self.t
        elif self.phase == "trial" and len(self.got) >= (self.need or self.min_n):
            m0, mk = median(self.ref), median(self.got)
            if self.incremental and self.allowed == 0:
                self.native_cost = m0
                self.native_ref = list(self.ref)
            bound = m0 if self.native_cost is None else min(m0, self.native_cost)
            within = mk <= bound * (1.0 + self.tol)
            if self.judge == "upper":
                reading, ivs, _, _ = self._reading()
                upper = self._upper()
                if reading != "LOSS" and within and upper <= math.log(1.0 + self.tol):
                    self.allowed = self.trial
                    event = {"verdict": "step allowed", "step": self.trial, "cost_native": m0, "cost_step": mk,
                             "reading": reading, "interval_ln": ivs, "pieces": len(self.got)}
                else:
                    self.refused_until[self.trial] = self.t + self.recheck
                    event = {"verdict": "step refused: the muscle is slower there", "step": self.trial,
                             "cost_native": m0, "cost_step": mk, "pieces": len(self.got),
                             "reading": "LOSS" if reading == "LOSS" else "past the allowance", "interval_ln": ivs}
            elif self.judge == "interval":
                reading, ivs, wide, d_max = self._reading()
                if reading != "LOSS" and wide and len(self.got) < 3 * self.min_n:
                    return self._stand()                         # the evidence is wider than the allowance: it measures on
                if reading != "LOSS" and within and d_max <= math.log(1.0 + self.tol):
                    self.allowed = self.trial
                    event = {"verdict": "step allowed", "step": self.trial, "cost_native": m0, "cost_step": mk,
                             "reading": reading, "interval_ln": ivs}
                else:
                    self.refused_until[self.trial] = self.t + self.recheck
                    event = {"verdict": "step refused: the muscle is slower there", "step": self.trial,
                             "cost_native": m0, "cost_step": mk,
                             "reading": "LOSS" if reading == "LOSS" else "past the allowance", "interval_ln": ivs}
            elif within:
                self.allowed = self.trial
                event = {"verdict": "step allowed", "step": self.trial, "cost_native": m0, "cost_step": mk}
            else:
                self.refused_until[self.trial] = self.t + self.recheck
                event = {"verdict": "step refused: the muscle is slower there", "step": self.trial,
                         "cost_native": m0, "cost_step": mk}
            self._end()
        elif (self.phase is None and calm and self.t - self.last_probe >= self.probe_every
              and self.allowed < self.max_steps and self.refused_until.get(self.allowed + 1, -1) <= self.t):
            self.phase, self.trial, self.phase_t, self.last_probe = "ref", self.allowed + 1, self.t, self.t
            self.ref, self.got = [], []
            event = {"verdict": "trial", "step": self.trial}
        if self.phase == "ref":
            return (self.allowed if self.incremental else 0), True, event
        if self.phase == "trial":
            return self.trial, True, event
        return self.allowed, False, event

    def _stand(self):
        """The knob stays at the trial step for another decision (the trial measures on)."""
        return self.trial, True, None

    def _upper(self):
        """judge="upper": the largest upper end of the trial's 95% intervals, against the reference and, stepwise, native."""
        ivs = [change_interval(self.ref, self.got)]
        if self.incremental and self.native_ref:
            ivs.append(change_interval(self.native_ref, self.got))
        ivs = [iv for iv in ivs if iv is not None]
        return max((hi for _, hi in ivs), default=math.inf)

    def _reading(self):
        """The trial's reading in the reports' words (tools/readings.py: a 95% interval wholly on one side of zero is a
        GAIN or a LOSS, across zero is EVEN), against the reference and, stepwise, against native: LOSS if any interval
        is wholly above zero, GAIN if every interval is wholly below it, else EVEN. Returns the reading, the intervals
        (for the audit), whether any interval is wider than the allowance (half-width over τ) and the largest estimate d."""
        tau = math.log(1.0 + self.tol)
        ivs = [change_interval(self.ref, self.got)]
        if self.incremental and self.native_ref:
            ivs.append(change_interval(self.native_ref, self.got))
        ivs = [iv for iv in ivs if iv is not None]
        if not ivs:
            return "EVEN", [], True, math.inf
        if any(lo > 0.0 for lo, _ in ivs):
            reading = "LOSS"
        elif all(hi < 0.0 for _, hi in ivs):
            reading = "GAIN"
        else:
            reading = "EVEN"
        wide = any((hi - lo) / 2.0 > tau for lo, hi in ivs)
        d_max = max((lo + hi) / 2.0 for lo, hi in ivs)
        return reading, [[round(lo, 5), round(hi, 5)] for lo, hi in ivs], wide, d_max
