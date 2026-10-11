# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A10 card of the paid run, modelled (evidence class S), with the same brain the real card runs.

Every constant below was fitted to the paid run of 2 October 2026 (results/gpu/run-20261002T082232Z: one NVIDIA A10,
150 W, ten repetitions of native, Omni watching and the earlier governor, 200 ms meter samples and every request's
times; the fit is in docs/GPU_PREREGISTRATION.md, amendment 13). On that run's own arrival times the model reproduces
the card's energy within 0.1% for native and for the earlier governor, the earlier governor's slowdown (modelled +72%
on the slowest responses, measured +57%) and its energy change (-3.0%, measured -3.0%); it reads the slowest responses
about 15% short of the meter in absolute terms, so it is used for differences between arms on the same arrivals.

The card
  work      one request is 62,475 MHz*ms of clock (service follows 1/clock: 85 ms at the 735 MHz the 150 W limit
            holds under sustained work, 170 ms at the 367 MHz a 105 W limit holds), times a per-request spread
            (lognormal, 6.5%, the run's own spread at a fixed temperature). memb is the share of a request's time at
            the top clock spent waiting on memory, which does not follow the clock (0 for the paid run's matrix
            products; AI token generation is memory-bound, modelled, never measured on this card)
  busy      61.8 + 0.1108 f + 0.615 (T - 60) watts at clock f MHz (regressed on settled requests under every limit the
            earlier governor set, all within 2 W); memory-bound work lights fewer cores: the clock term times (1 - 0.78 memb),
            so AI token generation (memb 0.85) draws about 125 W at the top clock (assumed; the probe measures it)
  idle      by clock, from the run's pure-idle stretches: 1695 MHz 66.2 W, 1500 57.1, 1300 50.0, 700 45.7 (210 MHz
            41 W extrapolated), the same leakage term; and 30 W after each request, fading over 40 ms
  heat      T' = (33 + 0.26 P + T2 - T) / 35 s, T2' = (0.04 P - T2) / 150 s (1.3 C rms on every arm of the run)
  firmware  a power limiter: the power filtered over 20 ms; over the limit the clock drops 1.2 MHz per watt over per
            millisecond, under it climbs 6 MHz per ms while busy and 40 while idle, never above the ceiling. Fitted to
            the run's first request after a rest (62 ms), the second (86 ms), sustained (81 ms) and the recovery after
            gaps of 3 to 120 ms. A raised ceiling is answered at `ramp` MHz per ms (unknown on the real chip until the
            probe measures it: tools/gpu_probe.py); a write lands `delay_ms` after it is decided
  work in   the bench's own schedule (tools/gpu_workload.py): Poisson arrivals, the rate stepping through the phases
            0.3, 0.6, 0.8, 0.3, 0.6, 0.3 of the card's sustained capacity, from the seed

The arms: each base alone, and the same base with Omni-Compass on top (Omni never runs the card itself)
  native    the card as shipped: power limit 150 W, clock ceiling at the top, firmware alone
  omni      native + the card's brain (omni_controller/gpu_brain.py) on its two wires, with the arrival signal: park
            the clock when the work stops, race back the moment it arrives, the verdict deciding how deep (handback=True
            hands both wires back at 90% of the run, for the restore check)
  cap       an operator's fixed power cap (105 W, 70%), firmware alone under it
  cap_omni  the cap + the brain on top, the lid never above the cap
"""
from __future__ import annotations

import bisect
import math
import random
from typing import Dict

from omni_controller.gpu_brain import CardBrain

TOP, FLOOR = 1695.0, 210.0
WORK = 62475.0
PA, PB, PK = 61.8, 0.1108, 0.615
IDLE_PTS = ((210.0, 41.0), (700.0, 45.7), (1300.0, 50.0), (1500.0, 57.1), (1695.0, 66.2))
TAIL_W, TAIL_TAU = 30.0, 40.0
TAMB, RTH, TAU_T, RTH2, TAU_T2 = 33.0, 0.26, 35000.0, 0.04, 150000.0
TAU, KD, KU, KU_IDLE = 20.0, 1.2, 6.0, 40.0
SPREAD = 0.065
PHASES = (0.3, 0.6, 0.8, 0.3, 0.6, 0.3)
SERVICE_MS = 81.6                     # the run's calibrated service time (sustained, at the 150 W limit)
SLO_MS = 10.0 * SERVICE_MS            # the service line: ten service times, as the bench sets it
LIMIT_DEFAULT, LIMIT_CAP = 150.0, 105.0
DECIDE_S = 0.25
OMNI = ("omni", "cap_omni")
_IX = [p[0] for p in IDLE_PTS]; _IY = [p[1] for p in IDLE_PTS]


def p_idle(f):
    if f <= _IX[0]:
        return _IY[0]
    i = min(len(_IX) - 1, bisect.bisect_left(_IX, f))
    x0, y0 = _IX[i - 1], _IY[i - 1]
    return y0 + (_IY[i] - y0) * (f - x0) / (_IX[i] - x0)


def arrivals(seed, duration, service_ms=SERVICE_MS, phases=PHASES):
    """The bench's schedule (tools/gpu_workload.py arrivals), in milliseconds."""
    rng = random.Random(seed)
    per = duration / len(phases)
    out, t = [], 0.0
    for i, f in enumerate(phases):
        rate = f / (service_ms / 1000.0)
        t = max(t, i * per)
        while True:
            t += rng.expovariate(rate)
            if t >= (i + 1) * per:
                t = (i + 1) * per
                break
            out.append(t * 1000.0)
    return out


def run(seed: int, arm: str, duration: float = 600.0, memb: float = 0.0, ramp: float = 40.0, delay_ms: float = 2.0,
        arrivals_ms=None, spread=None, T0: float = 50.0, brain_kw=None, log=None, handback: bool = False) -> Dict:
    """One arm on one seed. arrivals_ms replaces the bench's schedule (for replaying a run's own arrival times)."""
    arr = sorted(arrivals_ms) if arrivals_ms is not None else arrivals(seed, duration)
    rng = random.Random(seed * 7 + 1)
    sp = SPREAD if spread is None else spread
    need = [WORK * math.exp(rng.gauss(0.0, sp)) for _ in arr]
    horizon = int(duration * 1000.0) + 30000                  # the bench's 30 s drain
    start_w = LIMIT_CAP if arm in ("cap", "cap_omni") else LIMIT_DEFAULT
    brain = None
    if arm in OMNI:
        kw = dict(samples=30, decision_s=DECIDE_S, signal=True)
        kw.update(brain_kw or {})
        brain = CardBrain(TOP, FLOOR, start_w, **kw)
    kill_ms = int(0.9 * duration * 1000.0)
    b_eff = PB * (1.0 - 0.78 * memb)
    f, T, T2, pf, tail = TOP, T0, 0.0, 66.0, 0.0
    ceiling, lid = TOP, start_w
    pending = []                                               # (t_ms the write lands, ceiling)
    racing, prev_c = False, TOP
    q = []; qi = 0; head = 0; cur = None; work = 0.0; done_n = 0
    resp, svc_l, first_l = [], [], []
    e = 0.0; t_sum = 0.0; t_peak = 0.0; f_sum = 0.0; f_sq = 0.0
    writes = 0; restored = True; handed_back = False
    last_done = -1e9
    win = []                                                   # (done ms, response ms) for the position
    events = {"trials": 0, "allowed": 0, "refused": 0}
    next_decide = int(DECIDE_S * 1000)
    idle_check = None

    def apply(w, now):
        nonlocal writes
        if w is not None:
            pending.append((now + delay_ms, w[0])); writes += 1

    for t in range(horizon):
        # the brain: hand back at 90% of the run
        if handback and brain is not None and not handed_back and t >= kill_ms:
            handed_back = True
            pending.append((t + delay_ms, TOP)); lid = start_w
            brain = None
        while qi < len(arr) and arr[qi] <= t:
            q.append(qi); qi += 1
            if brain is not None:
                apply(brain.arrival(t / 1000.0, q[-1]), t)
        if cur is None and head < len(q):
            cur = q[head]; head += 1; work = 0.0
            cur_start = t
        busy = cur is not None
        if brain is not None:
            nxt = brain.next_idle_check()
            if nxt is not None and t / 1000.0 >= nxt:
                apply(brain.idle_due(t / 1000.0), t)
            if t >= next_decide:
                next_decide += int(DECIDE_S * 1000)
                w5 = [r for (d, r) in win if d >= t - 5000]
                if w5:
                    mean = sum(w5) / len(w5); p95 = sorted(w5)[min(len(w5) - 1, int(0.95 * len(w5)))]
                    pos = (mean - SLO_MS / 10.0) / (SLO_MS - SLO_MS / 10.0)
                    if p95 >= SLO_MS:
                        pos = max(pos, 1.0)
                else:
                    pos = 0.0
                tele = {"util": 1.0 if busy else 0.0, "draw_w": pf, "clock_mhz": f, "limit_w": lid}
                c, lid, why = brain.decide(t / 1000.0, tele, pos, False)
                if abs(c - ceiling) >= 0.5 and not any(abs(c - x[1]) < 0.5 for x in pending):
                    apply((c, why), t)
                for ev in brain.take_events():
                    if log is not None:
                        log.append((t / 1000.0, ev))
                    v = ev.get("verdict", {}).get("verdict", "") if isinstance(ev.get("verdict"), dict) else ""
                    if v == "trial":
                        events["trials"] += 1
                    elif v == "step allowed":
                        events["allowed"] += 1
                    elif "refused" in v:
                        events["refused"] += 1
        while pending and pending[0][0] <= t:
            ceiling = pending.pop(0)[1]
        if ceiling > prev_c + 1.0:
            racing = True
        prev_c = ceiling
        # the card
        if busy:
            p = PA + b_eff * f + PK * (T - 60.0)
        else:
            p = p_idle(f) + PK * (T - 58.0) + tail
            tail -= tail / TAIL_TAU
        pf += (p - pf) / TAU
        if pf > lid:
            f -= KD * (pf - lid); racing = False
        else:
            f += ramp if racing else (KU if busy else KU_IDLE)
        if racing and f >= ceiling - 1.0:
            racing = False
        f = min(f, ceiling, TOP); f = max(f, FLOOR)
        T += (TAMB + RTH * p + T2 - T) / TAU_T
        T2 += (RTH2 * p - T2) / TAU_T2
        e += p / 1000.0
        t_sum += T; t_peak = max(t_peak, T); f_sum += f; f_sq += f * f
        if busy:
            # memory-bound share: that part of the request does not follow the clock
            rate = f if memb <= 0 else 1.0 / ((1.0 - memb) / f + memb / TOP)
            work += rate
            if work >= need[cur]:
                d = t + 1 - (work - need[cur]) / rate          # the finish inside this millisecond, not its end
                r_ms = d - arr[cur]; s_ms = d - cur_start
                resp.append(r_ms); svc_l.append(s_ms); win.append((d, r_ms))
                if cur_start - last_done >= 80:
                    first_l.append(s_ms)
                last_done = d; done_n += 1
                if brain is not None:
                    apply(brain.done(d / 1000.0, cur, s_ms), t)
                cur = None; tail = TAIL_W
                if len(win) > 4000:
                    win = win[-2000:]
    n = len(resp)
    served = sum(1 for x in resp if x <= (duration * 1000.0 + 30000))

    def pct(xs, q):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))] if xs else float("nan")
    steps = horizon
    mean_f = f_sum / steps
    return {"energy_j": e, "served": float(served), "work_per_kj": served / (e / 1000.0),
            "p50_ms": pct(resp, 0.5), "p95_ms": pct(resp, 0.95), "p99_ms": pct(resp, 0.99),
            "svc_p50_ms": pct(svc_l, 0.5), "svc_p95_ms": pct(svc_l, 0.95), "first_p50_ms": pct(first_l, 0.5),
            "viol_share": sum(1 for x in resp if x > SLO_MS) / max(1, n), "hammer_per_s": 0.0, "reversals_per_s": 0.0,
            "clock_mean": mean_f / TOP, "clock_jitter": math.sqrt(max(0.0, f_sq / steps - mean_f ** 2)) / TOP,
            "t_peak": t_peak, "t_mean": t_sum / steps, "backlog_end": float(len(q) - head), "restored": restored,
            "writes": writes, "verdict_steps_allowed": events["allowed"], "verdict_events": events,
            "svc": svc_l, "resp": resp}
