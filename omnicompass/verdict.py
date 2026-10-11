# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict: Omni-Compass moves a knob only where it is sure, at one sureness for the whole engine, that the muscle is
no worse for it than the muscle's own wobble.

Omni-Compass sits on top of a muscle that already works (a card's firmware, an autoscaler, a chiller's loop). It does not
replace that muscle, and it has no reason to move the muscle's knob unless moving it costs the muscle nothing. The verdict
is how the brain finds that out, on the muscle itself, before it acts and again from time to time. There is no fixed
percentage anywhere in it (the founder's order of 10 October 2026): each machine's own wobble draws its line, and one
sureness, SURE = 99.9%, holds for the whole engine.

  steps      the knob's settings from native outward, in whole steps (step 0 is native: the muscle as it runs alone)
  cost       what each setting costs the muscle's own work, one number per piece of work (a card: the milliseconds it spends
             on one request, the wait in the queue left out, so more traffic is never mistaken for a slower card), compared
             as logarithms (a share of the cost, the same on a slow machine and a fast one), each block's 10% trimmed mean
             with Yuen's variance, so no single outlier decides
  the trial  interleaved, while the caller lets it run: a block of min_samples pieces of work at the reference (native,
             or stepwise the deepest step already allowed), then a block at the trial step, then the reference again, and
             so on: reference, trial, reference, ... Each trial block is set against the reference blocks on both sides of
             it, so a machine that drifts by itself (warming, background work, the load's own mix) cancels out instead of
             being read as the step's cost
  measured   the first trial on a machine opens with two reference blocks, the machine measured twice with nothing changed
  twice      before anything is changed, and is judged only after its second cycle. From then on every pair of windows with nothing changed between them (each
             block's two halves, and two reference blocks either side of a trial block) is the machine measured twice again;
             together they say how far the machine drifts by itself, and what the interleaving leaves of that drift is
             carried in the test's noise
  the line   how far two back-to-back reference blocks land apart by their own noise, at the engine's sureness (the normal
             quantile of the band). Neither drift nor what the engine does not yet know about the wobble ever widens the
             line: they only make a judgement more careful
  the judge  after each reference block that closes a cycle, Wellek's noninferiority test (the t statistic of the extra
             cost against the noncentral t whose noncentrality is the line in standard errors, Satterthwaite's degrees of
             freedom). Allowed when the step is inside the line at the look's sureness; refused when it is proven past the
             line; at the last of the cycles, refused unless allowed. The cycles share the 0.1% among them (Bonferroni):
             across every look, the chance of allowing a step that costs more than the line is at most 1 in 1,000. A clear
             win is taken at the first cycle, a clear loss refused at the first cycle, and only a close call takes more;
             nothing unproven is ever allowed
  gain       a step must also buy something: with gain=True the caller hands every block a second reading (lower is better:
             the watts the muscle drew), and the step is allowed only when the engine is 99.9% sure the reading fell under
             the trial step. A step that costs nothing but saves nothing has no reason to be taken ("no gain")
  stepwise   for a knob that is slow to move (a machine given back takes minutes to return), incremental=True runs the
             reference at the deepest step already allowed and adds each step's cost to the climb's cost from native: a step
             is allowed only when the whole climb is also inside native's line, so steps never add up past it
  scout      coarse to fine (docs/OMNI_V4_PLAN.md, section 4, rule 4): with bisect=True the next trial is halfway between
             the deepest step allowed and the shallowest step refused (the far end of the cover at first), so the edge of a
             hill of many steps is found in a handful of trials
  nothing    every kept step is proven again against native itself every recheck decisions (the work may have changed); a
  permanent  step that no longer proves is taken back to the deepest step still proven, and that one is proven again at the
             next probe. A refused step is not tried again until recheck decisions have passed. A trial the caller ends
             (calm False: the wall, or another trial in the same body) is abandoned and the knob goes back at once

The verdict never makes the knob more aggressive than the law: it only narrows where the law may go. Every probe and every
judgement, with its numbers, is returned to the caller for the audit. Its arithmetic (the t, normal, chi-square and
noncentral t distributions) is computed exactly here, without any library, and checked against the published tables and
by simulation in tests/test_verdict.py.
"""
from __future__ import annotations

import functools
import math

SURE = 0.999            # the one sureness of the whole engine (the founder's order, 10 October 2026); never 1
TRIM = 0.10             # the share trimmed from each end of a sample before its mean (Yuen's trimmed mean)
RESOLUTION = 1e-6       # a change under one part in a million is the arithmetic's own resolution, never a difference


def median(xs):
    s = sorted(xs)
    n = len(s)
    return None if n == 0 else (s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2]))


# ---- the distributions, exact to the arithmetic ------------------------------------------------------------------------
def z_quantile(p):
    """The standard normal's p-quantile: Acklam's approximation, then one Newton step on the exact distribution."""
    if not 0.0 < p < 1.0:
        raise ValueError("a sureness is strictly between 0 and 1")
    a = (-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02,
         -3.066479806614716e+01, 2.506628277459239e+00)
    b = (-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01,
         -1.328068155288572e+01)
    c = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00,
         4.374664141464968e+00, 2.938163982698783e+00)
    d = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00)
    lo = 0.02425
    if p < lo:
        q = math.sqrt(-2 * math.log(p))
        x = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    elif p > 1 - lo:
        q = math.sqrt(-2 * math.log(1 - p))
        x = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    else:
        q = p - 0.5
        r = q * q
        x = (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
    e = 0.5 * math.erfc(-x / math.sqrt(2.0)) - p
    return x - e * math.sqrt(2 * math.pi) * math.exp(x * x / 2.0)


def _betacf(a, b, x):
    """The continued fraction of the incomplete beta function (modified Lentz)."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 400):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        de = d * c
        h *= de
        if abs(de - 1.0) < 1e-15:
            break
    return h


def _ibeta(a, b, x):
    """The regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(ln) * _betacf(a, b, x) / a
    return 1.0 - math.exp(ln) * _betacf(b, a, 1.0 - x) / b


def t_cdf(t, df):
    """Student's t distribution function with df (any positive real) degrees of freedom."""
    if df is None or math.isinf(df):
        return 0.5 * math.erfc(-t / math.sqrt(2.0))
    tail = 0.5 * _ibeta(df / 2.0, 0.5, df / (df + t * t))
    return 1.0 - tail if t >= 0 else tail


def t_quantile(p, df):
    """Student's t p-quantile (p above one half) with df degrees of freedom, by bisection on the exact distribution."""
    if df is None or df <= 0 or math.isinf(df) or df > 1e7:
        return z_quantile(p)
    if p <= 0.5:
        return -t_quantile(1.0 - p, df) if p < 0.5 else 0.0
    return _t_quantile(p, round(df, 3))


@functools.lru_cache(maxsize=8192)
def _t_quantile(p, df):
    lo, hi = 0.0, max(1.0, z_quantile(p))
    while t_cdf(hi, df) < p:
        lo, hi = hi, 2.0 * hi
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
        if hi - lo <= 1e-12 * max(1.0, hi):
            break
    return 0.5 * (lo + hi)


def nct_cdf(t, df, delta):
    """The noncentral t distribution function: df degrees of freedom (any positive real), noncentrality delta (Lenth's
    Algorithm AS 243, Applied Statistics 38, 1989, on Guenther's twin series)."""
    if df is None or math.isinf(df):
        return 0.5 * math.erfc(-(t - delta) / math.sqrt(2.0))
    tt, dl, neg = t, delta, False
    if t < 0:
        neg, tt, dl = True, -t, -delta
    en, x, total = 1.0, tt * tt / (tt * tt + df), 0.0
    if x > 0:
        lam = dl * dl
        p = 0.5 * math.exp(-0.5 * lam)
        q = math.sqrt(2.0 / math.pi) * p * dl
        s = 0.5 - p
        a, b = 0.5, 0.5 * df
        rxb = (1.0 - x) ** b
        albeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
        xodd = _ibeta(a, b, x)
        godd = 2.0 * rxb * math.exp(a * math.log(x) - albeta)
        xeven = 1.0 - rxb
        geven = b * x * rxb
        total = p * xodd + q * xeven
        while True:
            a += 1.0
            xodd -= godd
            xeven -= geven
            godd *= x * (a + b - 1.0) / a
            geven *= x * (a + b - 0.5) / (a + 0.5)
            p *= lam / (2.0 * en)
            q *= lam / (2.0 * en + 1.0)
            s -= p
            en += 1.0
            total += p * xodd + q * xeven
            if 2.0 * s * (xodd - godd) <= 1e-14 or en > 4000:
                break
    total += 0.5 * math.erfc(dl / math.sqrt(2.0))
    return 1.0 - total if neg else total


def nct_quantile(p, df, delta):
    """The noncentral t p-quantile, by bisection on the distribution function."""
    if df is None or math.isinf(df) or df > 1e7:
        return delta + z_quantile(p)
    return _nct_quantile(p, round(df, 2), round(delta, 5))


@functools.lru_cache(maxsize=65536)
def _nct_quantile(p, df, delta):
    """Regula falsi with the Illinois step, from the normal approximation of the noncentral t (variance 1 + delta^2/2df);
    past AS 243's range (delta over 37) the approximation itself, which is then within its own resolution."""
    sd = math.sqrt(1.0 + delta * delta / (2.0 * df))
    x0 = delta + z_quantile(p) * sd
    if abs(delta) > 37.0:
        return x0
    f = lambda x: nct_cdf(x, df, delta) - p
    a, b = x0 - sd, x0 + sd
    fa, fb = f(a), f(b)
    for k in range(1, 61):
        if fa <= 0:
            break
        a -= 2.0 * k * sd
        fa = f(a)
    for k in range(1, 61):
        if fb >= 0:
            break
        b += 2.0 * k * sd
        fb = f(b)
    if fa > 0 or fb < 0:
        return x0                                   # the distribution could not be bracketed: the approximation
    c, side = x0, 0
    for _ in range(200):
        c = (a * fb - b * fa) / (fb - fa) if fb != fa else 0.5 * (a + b)
        fc = f(c)
        if abs(fc) <= 1e-14 or b - a <= 1e-11 * max(1.0, abs(c)):
            break
        if fc > 0:
            b, fb = c, fc
            if side == 1:
                fa *= 0.5
            side = 1
        else:
            a, fa = c, fc
            if side == -1:
                fb *= 0.5
            side = -1
    return c


# ---- the samples -------------------------------------------------------------------------------------------------------
def trimmed(xs, trim=TRIM):
    """(trimmed mean, variance of that mean, degrees of freedom) of a sample, Yuen's way: the mean of the middle 1 - 2*trim
    of the sorted sample and the winsorized variance scaled to it."""
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return None, None, 0
    g = int(math.floor(trim * n))
    h = n - 2 * g
    mid = s[g:n - g]
    m = sum(mid) / h
    w = [s[g]] * g + mid + [s[n - g - 1]] * g
    wm = sum(w) / n
    sw2 = sum((x - wm) ** 2 for x in w) / (n - 1) if n > 1 else 0.0
    if sw2 <= (1e-14 * max(1.0, abs(wm))) ** 2:
        sw2 = 0.0                                   # what is left of identical numbers after their rounding: no spread
    var = (n - 1) * sw2 / (h * (h - 1)) if h > 1 else 0.0
    return m, var, max(1, h - 1)


def logs(xs):
    return [math.log(max(float(x), 1e-300)) for x in xs]


def welch_df(parts):
    """Satterthwaite's degrees of freedom of a sum of variances [(variance, its degrees of freedom), ...]."""
    tot = sum(v for v, _ in parts)
    den = sum(v * v / k for v, k in parts if v > 0 and k)
    return tot * tot / den if tot > 0 and den > 0 else float("inf")


def compare(ref, got, sure=SURE, drift=(0.0, 0)):
    """The trial against the reference, as shares of the cost: (difference of the trimmed log means, its one-sided `sure`
    half-width, the variance of the reference's mean, its degrees of freedom). drift = (the variance the machine's own
    drift adds between the two windows, its degrees of freedom). Positive difference: the trial costs more."""
    mr, vr, dr = trimmed(logs(ref))
    mt, vt, dt = trimmed(logs(got))
    parts = [(vr, dr), (vt, dt), drift]
    tq = t_quantile(sure, welch_df(parts))
    return mt - mr, tq * math.sqrt(vr + vt + drift[0]), vr, dr




def stats(xs):
    """A block's (trimmed log mean, variance of that mean, degrees of freedom)."""
    return trimmed(logs(xs))


def walk_area(blocks):
    """The drift a random walk adds to a weighted sum of block means, per unit of the walk's variance per piece of work:
    the integral of the squared tail sum of the weights. blocks: [(weight of the block's mean, pieces of work in it)] in
    time order, the weights summing to zero."""
    c, area = 0.0, 0.0
    for w, n in blocks:
        c2 = c - w
        area += n * (c * c + c * c2 + c2 * c2) / 3.0
        c = c2
    return area


class Verdict:
    def __init__(self, sure=SURE, min_samples=30, probe_every=120, recheck=1800, max_steps=60, max_trial=30,
                 incremental=False, gain=False, bisect=False, cycles=4):
        if not 0.5 < sure < 1.0:
            raise ValueError("the sureness is above one half and never 1")
        self.sure = sure
        self.z_line = z_quantile(sure)        # the band two blocks of a machine fall inside by themselves, at SURE
        self.bisect = bisect
        self.gain = bool(gain)                # the step must also lower the second reading, proven at the same sureness
        self.incremental = incremental
        self.min_n = max(4, int(min_samples))  # pieces of work in one block (its halves need two each)
        self.looks = max(1, int(cycles))       # the cycles a trial may take, each one look, sharing the 0.1% among them
        self.alpha = (1.0 - sure) / self.looks
        self.probe_every = probe_every
        self.recheck = recheck
        self.max_steps = max_steps
        self.max_trial = max_trial            # decisions one block may take before the trial is abandoned (too little work)
        self.walk = []                        # nothing changed between two windows: (difference, its sampling variance,
                                              # the walk's area between them)
        self.native_block = None              # (variance of a native reference block's trimmed log mean, its df)
        self.cum = {}                         # step -> (its cost against native, variance, Satterthwaite parts)
        self.allowed = 0                      # deepest step allowed (0: native only)
        self.proven = []                      # the steps proven, shallow to deep (the knob goes back along them)
        self.kept_at = 0                      # decision at which the deepest step was last proven
        self.refused_until = {}               # step -> decision index before which it is not tried again
        self.phase = None                     # None, "ref" (a reference block) or "trial" (a trial block)
        self.trial = None
        self.reproof = False                  # the trial in flight proves a kept step again, against native
        self.blocks = []                      # the trial in flight: {"kind": "ref"/"trial", "x": costs, "b": readings}
        self.first = True                     # nothing measured on this machine yet: the first trial measures it twice first
        self.fresh = True                     # the first trial on this machine is in flight (or yet to come)
        self.block_t = 0
        self.block_no = 0                     # blocks opened so far (a caller tags its work with the block it began in)
        self.t = 0
        self.last_probe = -10 ** 9

    @property
    def state(self):
        return "left native" if self.allowed == 0 else "acting"

    def observe(self, costs, benefit=None, parts=None):
        """Costs (one per piece of work) measured since the last decision, under the step tick() last returned; where the
        verdict asks for a gain, the second readings (lower is better) taken under that step; and parts, {part: costs},
        each part of the body's own cost (one service's), for the guard that nothing anywhere is made worse."""
        if self.phase is not None and self.blocks:
            self.blocks[-1]["x"].extend(costs)
            if benefit:
                self.blocks[-1]["b"].extend(benefit)
            for name, xs in (parts or {}).items():
                self.blocks[-1]["p"].setdefault(name, []).extend(xs)

    def ready(self):
        """Whether tick(True) would open a trial now (a step to try, or a kept step due to be proven again): the body asks
        before it grants the one trial of its tick."""
        if self.phase is not None or self.t + 1 - self.last_probe < self.probe_every:
            return False
        if self.allowed > 0 and self.t + 1 - self.kept_at >= self.recheck:
            return True
        return self.allowed < self.max_steps and self.refused_until.get(self.allowed + 1, -1) <= self.t + 1

    def ref_step(self):
        """Where the knob stands in a reference block: native, or stepwise the deepest step allowed (a kept step is
        always proven again against native itself)."""
        return self.allowed if (self.incremental and not self.reproof) else 0

    # ---- the machine measured twice ------------------------------------------------------------------------------------
    def _pair(self, a, b, area):
        """Two windows with nothing changed between them: their difference, its sampling noise, the walk's area."""
        ma, va, _ = stats(a)
        mb, vb, _ = stats(b)
        self.walk.append((mb - ma, va + vb, area))

    def drift(self):
        """(the machine's walk per piece of work, its degrees of freedom): the excess of the nothing-changed differences
        over their sampling noise, per unit of the walk's area between them; never negative. Its degrees of freedom are
        what the differences can carry (each squared difference one degree, weighted by its expected size), so a walk read
        from a few windows is held as uncertain as it is. It only ever makes a judgement more careful: it is carried in
        the test's noise, never in the line."""
        if not self.walk:
            return 0.0, 0
        area = sum(a for _, _, a in self.walk)
        ex = (sum(d * d for d, _, _ in self.walk) - sum(v for _, v, _ in self.walk)) / area if area > 0 else 0.0
        if ex <= 0:
            return 0.0, 0
        df = (ex * area) ** 2 / sum((v + ex * a) ** 2 for _, v, a in self.walk)
        return ex, max(df, 1e-3)

    # ---- the judgement -------------------------------------------------------------------------------------------------
    def line(self, ref_var, ref_n=None):
        """The muscle's own wobble as a share of its cost: how far two back-to-back reference blocks (each mean's variance
        ref_var) land apart by their own noise at the engine's sureness. A machine that also wanders is judged no more
        loosely for it: its wandering is cancelled by measuring the reference on both sides of every trial block, and what
        is left of it only widens the test's noise."""
        return max(self.z_line * math.sqrt(2.0 * ref_var), RESOLUTION)

    def test(self, d, parts, area, line, design_var=None):
        """Wellek's noninferiority test of an extra cost d (shares of the cost) whose variance is the sum of parts
        [(variance, df)] plus the walk over `area`: {difference, allow_below, refuse_above, line, lambda, df}."""
        tau, k = self.drift()
        se2 = sum(v for v, _ in parts) + tau * area
        if se2 <= (RESOLUTION / 1000.0) ** 2:              # no wobble within the arithmetic's resolution: it decides
            return {"difference": d, "allow_below": line, "refuse_above": line, "line": line, "lambda": None, "df": None}
        se = math.sqrt(se2)
        lam = line / se
        if design_var is not None and design_var + tau * area > 0:
            lam = min(lam, line / math.sqrt(design_var + tau * area))
        df = welch_df(list(parts) + [(tau * area, k)])
        return {"difference": d, "allow_below": nct_quantile(self.alpha, df, lam) * se,
                "refuse_above": nct_quantile(1.0 - self.alpha, df, lam) * se, "line": line, "lambda": lam, "df": df}

    @staticmethod
    def _inside(r):
        return r["difference"] <= r["allow_below"]

    @staticmethod
    def _past(r):
        return r["difference"] > r["refuse_above"] if r["df"] is not None else r["difference"] > r["line"]

    def _judge(self, m):
        """After m cycles (reference, trial, ..., reference): None while undecided; else (allowed, event, its cost)."""
        st = [stats(b["x"]) for b in self.blocks]
        ns = [len(b["x"]) for b in self.blocks]
        w = [(1.0 / m if i % 2 else (-0.5 / m if i in (0, 2 * m) else -1.0 / m)) for i in range(2 * m + 1)]
        d = sum(wi * s[0] for wi, s in zip(w, st))
        parts = [(wi * wi * s[1], s[2]) for wi, s in zip(w, st)]
        area = walk_area(list(zip(w, ns)))
        refs = [st[i] for i in range(0, 2 * m + 1, 2)]
        ref_var = sum(s[1] for s in refs) / len(refs)
        ref_n = sum(ns[i] for i in range(0, 2 * m + 1, 2)) / len(refs)
        line = self.line(ref_var, ref_n)
        r = self.test(d, parts, area, line, design_var=ref_var * sum(wi * wi for wi in w))
        tau, _ = self.drift()
        nums = {"step": self.trial, "cycles": m, "looks": self.looks, "share_more": round(d, 6),
                "allow_below": round(r["allow_below"], 6), "refuse_above": round(r["refuse_above"], 6),
                "line": round(r["line"], 6), "sure": self.sure, "drift_per_piece": tau, "n_block": self.min_n,
                "cost_ref": median([x for b in self.blocks[0::2] for x in b["x"]]),
                "cost_step": median([x for b in self.blocks[1::2] for x in b["x"]])}
        inside, past = self._inside(r), self._past(r)
        own = (d, sum(v for v, _ in parts) + tau * area, parts + [(tau * area, len(self.walk))])
        cum = own
        if self.incremental and not self.reproof and self.ref_step() != 0 and self.native_block is not None:
            below = self.cum.get(self.ref_step())
            if below is not None:
                cum = (below[0] + d, below[1] + own[1], below[2] + own[2])
                ln = self.line(self.native_block[0], self.min_n)
                rn = self.test(cum[0], cum[2], 0.0, ln)
                nums.update({"share_more_native": round(cum[0], 6), "allow_below_native": round(rn["allow_below"], 6),
                             "line_native": round(ln, 6)})
                inside, past = inside and self._inside(rn), past or self._past(rn)
        # the guard for every part: the step must also hold every part of the body inside that part's own line, so
        # nothing anywhere is made worse to make the whole better (each part's test at the same sureness: allowed only
        # when every part is inside, refused when any part is proven past)
        hurt = []
        for name in sorted({k for b in self.blocks for k in b["p"]}):
            xs = [b["p"].get(name, []) for b in self.blocks]
            if any(len(x) < 2 for x in xs):
                inside = False                              # a part not measured in every block is not proven inside
                continue
            pst = [stats(x) for x in xs]
            pd = sum(wi * s_[0] for wi, s_ in zip(w, pst))
            pparts = [(wi * wi * s_[1], s_[2]) for wi, s_ in zip(w, pst)]
            pref = sum(pst[i][1] for i in range(0, 2 * m + 1, 2)) / (m + 1)
            pr = self.test(pd, pparts, area, self.line(pref), design_var=pref * sum(wi * wi for wi in w))
            if self._past(pr):
                hurt.append(name)
                past = True
            elif not self._inside(pr):
                inside = False
        if hurt:
            nums["parts_hurt"] = hurt
        last = m >= self.looks
        if past:
            why = "the muscle is slower there" if not hurt else "it makes a part worse (" + ", ".join(hurt) + ")"
            return False, {"verdict": "step refused: " + why, **nums}, cum
        if not inside:
            return (False, {"verdict": "step refused: never proven inside the muscle's own wobble", **nums}, cum) if last else None
        if self.gain:
            rb = [x for b in self.blocks[0::2] for x in b["b"]]
            tb = [x for b in self.blocks[1::2] for x in b["b"]]
            if len(rb) < 2 or len(tb) < 2:
                return (False, {"verdict": "step refused: no gain (no reading to show one)", **nums}, cum) if last else None
            db, hwb, _, _ = compare(rb, tb, 1.0 - self.alpha)
            nums.update({"reading_ref": median(rb), "reading_step": median(tb), "reading_share_more": round(db, 6),
                         "reading_upper": round(db + hwb, 6)})
            if db + hwb > -RESOLUTION:
                if db - hwb >= -RESOLUTION or last:
                    return False, {"verdict": "step refused: no gain (it costs nothing and saves nothing)", **nums}, cum
                return None
        return True, {"verdict": "step allowed" if not self.reproof else "step kept: proven again", **nums}, cum

    # ---- the blocks ----------------------------------------------------------------------------------------------------
    def _open(self, kind):
        self.phase, self.block_t = kind, self.t
        self.block_no += 1
        self.blocks.append({"kind": kind, "x": [], "b": [], "p": {}})

    def position(self):
        """The step the block in flight holds the knob at (None between trials): a caller hands observe() only the work
        measured with the knob actually there, never work begun under the block before."""
        if self.phase == "ref":
            return self.ref_step()
        if self.phase == "trial":
            return self.trial
        return None

    def _end(self):
        self.phase, self.trial, self.reproof, self.blocks = None, None, False, []
        self.fresh = self.first

    def _pull_back(self, step):
        """A kept step that no longer proves: back to the deepest step still proven, and that one proven again soon."""
        self.proven = [p for p in self.proven if p < step]
        for s in [s for s in self.cum if s >= step]:
            del self.cum[s]
        self.allowed = self.proven[-1] if self.proven else 0
        self.kept_at = self.t - self.recheck + self.probe_every

    def _close_block(self):
        blk = self.blocks[-1]
        x = blk["x"]
        h = len(x) // 2
        if h >= 2:
            self._pair(x[:h], x[h:2 * h], walk_area([(-1.0, h), (1.0, h)]))
        if blk["kind"] == "trial":
            self._open("ref")
            return None
        if self.first:
            # the first time on this machine: measured twice with nothing changed before anything is changed
            if len(self.blocks) == 1:
                self._open("ref")
                return None
            a = self.blocks[0]
            self._pair(a["x"], x, walk_area([(-1.0, len(a["x"])), (1.0, len(x))]))
            self.blocks = [blk]
            self.first = False
        if len(self.blocks) >= 3:
            a, b = self.blocks[-3], self.blocks[-2]
            self._pair(a["x"], x, walk_area([(-1.0, len(a["x"])), (0.0, len(b["x"])), (1.0, len(x))]))
        if len(self.blocks) == 1 and self.ref_step() == 0:
            s = stats(x)
            self.native_block = (s[1], s[2])
        m = (len(self.blocks) - 1) // 2
        if m >= (min(2, self.looks) if self.fresh else 1):     # a machine never measured before: judged after two cycles
            res = self._judge(m)
            if res is not None:
                ok, event, cum = res
                event["reproof"] = self.reproof
                step = self.trial
                if ok:
                    if not self.reproof:
                        self.allowed = step
                        self.proven = sorted(set([p for p in self.proven if p < step] + [step]))
                    self.cum[step] = cum
                    self.kept_at = self.t
                else:
                    self.refused_until[step] = self.t + self.recheck
                    if self.reproof:
                        self._pull_back(step)
                        event["back_to"] = self.allowed
                self._end()
                return event
        self._open("trial")
        return None

    def tick(self, calm):
        """One decision. calm: the caller lets a trial run (the service inside its compass, nothing waiting, no other trial
        in the body). Returns (the step the knob must stand at during a trial, or the deepest step the law may use;
        is_trial; event). The event, if any, is for the audit."""
        self.t += 1
        event = None
        if self.phase is not None:
            if not calm or self.t - self.block_t > self.max_trial:
                event = {"verdict": "trial abandoned (service not calm)" if not calm else "trial abandoned (too little work)",
                         "step": self.trial, "reproof": self.reproof}
                self._end()
            elif len(self.blocks[-1]["x"]) >= self.min_n:
                event = self._close_block()
        elif calm and self.t - self.last_probe >= self.probe_every:
            if self.allowed > 0 and self.t - self.kept_at >= self.recheck:
                # nothing permanent: the deepest kept step is proven again, against native itself
                self.trial, self.reproof = self.allowed, True
            elif self.allowed < self.max_steps and self.refused_until.get(self.allowed + 1, -1) <= self.t:
                nxt = self.allowed + 1
                if self.bisect:
                    # the shallowest step still refused bounds the search; halfway between it and the deepest allowed
                    ub = min([k for k, u in self.refused_until.items() if u > self.t and k > self.allowed] + [self.max_steps + 1]) - 1
                    nxt = self.allowed + max(1, (ub - self.allowed + 1) // 2)
                self.trial, self.reproof = nxt, False
            if self.trial is not None:
                self.last_probe = self.t
                self.blocks = []
                self._open("ref")
                event = {"verdict": "trial" if not self.reproof else "trial: a kept step proven again", "step": self.trial}
        if self.phase == "ref":
            return self.ref_step(), True, event
        if self.phase == "trial":
            return self.trial, True, event
        return self.allowed, False, event
