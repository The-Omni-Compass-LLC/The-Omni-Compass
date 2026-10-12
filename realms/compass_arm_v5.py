# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The Omni v5 compass law, in the engine (additive beside the frozen v3 law in realms/compass_arm.py). It is the engine
# change that makes this tree omni-v5: two math-only guardrails (the edge, so nothing riding its limit falls off; the
# centre/hole, so nothing drops into a pit it cannot climb out of), free arms otherwise, every move proven no worse than
# native on the modelled organism. Run by the v5 arm in realms/harness.py and tools/run_realms_v5.py. Evidence class S.
#
#   free arms     every knob may move both ways inside its physical cover; the only exclusions are knobs whose own
#                 physics says moving them cannot lower energy (a cooling cap, a battery's power cap, a backup reserve,
#                 admission, a power cap on a machine racing to idle): the brain's knowledge, not a guardrail
#   the edge      the compass's balance point is not a fixed middle: it is 1 - cushion, where
#                   cushion = climb (how fast the service has climbed lately, per decision) x reaction (decisions the knob
#                             takes to act) + z x wobble (the service's own spread lately)
#                 widened at once when the need rises, narrowed slowly when it falls; past 1 - climb x reaction the
#                 law fails up at once (the wall moves with the cushion too)
#   the hole      nothing is eased into a pit it cannot climb out of: a cooled zone never warmer than its cooling can
#                 recover (the Lindley reach), a process loop's setpoint never closer to its band's edge than the loop's
#                 own largest swing toward that edge (the loop reach), a serving pool never capped below the largest jump
#                 in demand it has shown; and nothing permanent: a machine handed back to a cloud is the cluster
#                 autoscaler's own decision (it shrinks from wherever it is left, so an early hand-back would leave the
#                 pool a machine short of native for good)
from __future__ import annotations

import math

from omnicompass.compass_law import Band, CompassLaw
from omnicompass.edge import Edge as _CoreEdge, physics_memory
from .compass_arm import (UP, DOWN, RELEASE, clamp, position, release_safe, capping_saves, effort_cap_saves,
                         speed_slack)


class Cfg:
    def __init__(self, z=3.09, window=20, react_mult=1.0, narrow=0.05, start=0.5, target_hi=0.95, spend_beyond=False,
                 memory=0.0, target_free=True, est=1, snap=True, learn_fall=0.0, fall_decay=0.9995, hybrid=False,
                 base_center=0.5, base_wall=0.95, headroom=False, physics_memory=False, motion_safe=False,
                 motion_q=0.999, burst_window=20, hole_guard=False, drop_guard=False, jump0=1.0, band=False,
                 hole_floor=True, precool=False, storage_shave=False, power_cap=False, loop_reach=False,
                 ca_release=False, dial="save", edge_util=0.95, line_z=3.09):
        self.dial = dial                      # "max" (the default brain: every muscle pushed to its own limit for the most
                                              # work, the energy that takes shown as power given) or "save" (the tune-down:
                                              # the least energy for native's work)
        self.edge_util = edge_util            # max: how full a machine pool runs on the forecast before it calls for more
        self.line_z = line_z                  # max: the wobbles of margin a battery keeps its site's draw under its line
        self.loop_reach = loop_reach          # a process loop's setpoint never closer to its band's calm-side edge than the
                                              # loop's own largest swing toward that edge leaves room for (loop_clamp)
        self.ca_release = ca_release          # a machine pool under a cluster autoscaler: Omni may hand a machine back
                                              # (off in the default: the autoscaler shrinks from wherever it is left, so an
                                              # early hand-back is permanent; the reflex rule: nothing permanent)
        self.storage_shave = storage_shave    # battery peak-shaving (discharge to hold an import limit) costs round-trip
                                              # energy, so it is a service<->energy tradeoff, off in the no-harm default;
                                              # a service/Max dial turns it on. Off: the storage setpoint stays native.
        self.power_cap = power_cap            # a power cap on a serving pool whose response line is longer than one decision
                                              # (lever_v5); an interactive pool's cap stays native either way
        self.hole_floor = hole_floor          # the hole guard never below the earlier law's balance point (hybrid)
        self.precool = precool                # a cooled zone may also sit warm while its headroom can pull it back in time
        self.band = band                      # a process loop's margin read against its band's edge, not its setpoint
        self.jump0 = jump0                    # the jump in demand the brain assumes a pool can make in one decision until it
                                              # has seen a larger one (1.0: demand can double)
        self.drop_guard = drop_guard          # a pool that can turn requests away is never capped below the largest jump
                                              # in demand it has seen (a request turned away is work lost for good)
        self.hole_guard = hole_guard          # a cooled zone is never warmer than it can be pulled back from before its
                                              # cooling could run out (the hole a saturated cooling plant cannot climb out of)
        self.motion_safe = motion_safe        # a motion axis's speed and effort never below what its own physics needs
        self.motion_q = motion_q              # the share of next-decision arrival counts the speed must cover (z = 3.09)
        self.burst_window = burst_window      # decisions of arrival history the rate estimate keeps its peak over
        self.z, self.window, self.react_mult, self.narrow, self.start = z, window, react_mult, narrow, start
        self.memory = memory                  # 0: only the recent window; near 1: the worst climb ever seen, forgotten slowly
        self.target_free = target_free        # the autoscaler's target free both ways (False: held at the operator's, as v3)
        self.est = est                        # 1: level spread and the steepest one-step climb x reaction; 2: the step-to-step
                                              # wobble and the largest rise seen within one reaction time
        self.snap = snap                      # at the wall: snap back to native (True) or climb back at the law's full force
        self.learn_fall = learn_fall          # > 0: a miss while Omni had given something back raises that plant's cushion floor
        self.fall_decay = fall_decay          # how slowly that floor is forgotten, per decision
        self.hybrid = hybrid                  # True: everything the earlier law did stays (its balance point, its wall, its
                                              # fail-up), and the edge only ever adds: the balance point is the higher of the
                                              # earlier one and the edge, the wall the higher of the earlier one and the edge's
        self.base_center, self.base_wall = base_center, base_wall
        self.headroom = headroom              # a cooling zone's headroom as a second gauge
        self.physics_memory = physics_memory  # each plant remembers its risks for as long as its own physics carries them
        self.target_hi = target_hi            # a compute pool's utilization may never be set past this (a queue at 1 explodes)
        self.spend_beyond = spend_beyond      # spend beyond native away from the wall (the speed edge); False: the energy edge


def reaction_steps(plant, key=None) -> float:
    """Decisions the knob takes to act: the knob's own, not the plant's (a power cap answers in one decision; a machine
    pool answers only once its machines have started)."""
    P, t = plant.P, plant.template
    dt = float(P.get("dt", P.get("dt_dec", 15.0)))
    if t == "compute_pool":
        if key == "power":
            return 1.0
        return max(1.0, float(P.get("startup_steps", 1)))
    if t == "process_loop":
        return max(1.0, (3.0 * P.get("tau", dt) + P.get("theta", 0.0)) / dt)
    if t == "thermal_zone":
        # the cooling's own reaction: how long the spare cooling takes to pull the zone back across its band (the
        # passive time constant, hours, is how slowly it drifts without cooling, not how fast the loop answers)
        spare = max(P["units"] * P["q_unit_w"] - P["q_it_w"], 0.1 * P["q_it_w"])
        return max(1.0, P["c_j_k"] * (P["t_limit"] - P["t_set"]) / spare / dt)
    return 1.0


def lever_v5(plant, knob, cfg):
    """(override key, native, low, high, sign): sign +1 when a higher value is more capacity."""
    P, t = plant.P, plant.template
    if knob == "admission":
        return None
    if t == "compute_pool":
        if knob == "power":
            # a pool whose response line is shorter than one decision (an interactive GPU or CPU, a radio, a switch) cannot
            # have a cap's one decision of slower service seen and undone inside its line, so its cap stays native (the
            # metered GPU, class P, is where an interactive cap is proven); a pool whose line is longer than a decision
            # (a batch queue, a training job, a terminal's moves) absorbs it, held by the drop and latency floors
            ok = cfg.power_cap and capping_saves(plant) and P["slo_s"] >= P["dt"]
            return ("power", 1.0, 0.4, 1.0, 1) if ok else None
        if P.get("ca"):
            return ("release", None, 0, 0, 0) if cfg.ca_release else None
        # the autoscaler's target, free both ways: lower is more machines, higher is fewer, never past target_hi
        if not cfg.target_free:
            return None
        return ("target", P["target"], 0.6 * P["target"], max(P["target"], cfg.target_hi), -1)
    if t == "thermal_zone":
        if knob == "setpoint":
            return ("setpoint", P["t_set"], min(P["stress"], P["calm"]), max(P["stress"], P["calm"]), -1)
        if knob == "capacity":
            return ("release", None, 0, 0, 0)
        return None
    if t == "energy_storage":
        if knob == "setpoint" and not P.get("backup") and cfg.storage_shave:
            return ("setpoint", P["reserve"], min(P["stress"], P["reserve"]), P["reserve"], -1)
        return None
    if t == "motion_axis":
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1) if effort_cap_saves(plant) else None
        return ("capacity", 1.0, 0.4, 1.0, 1) if speed_slack(plant) else None
    if t == "process_loop":
        if knob == "setpoint":
            lo, hi = min(P["sp"], P["calm"]), max(P["sp"], P["calm"])
            return ("setpoint", P["sp"], lo, hi, 1 if P["sp"] > P["calm"] else -1)
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1)
        return ("capacity", 1.0, 0.3, 1.0, 1)
    return None


def memory_horizon(plant) -> float:
    """Decisions a plant carries a risk: its own slowest physics (a room's heat capacity over its loss to outside, a
    process loop's three time constants, a machine pool's start)."""
    P, t = plant.P, plant.template
    dt = float(P.get("dt", P.get("dt_dec", 15.0)))
    if t == "thermal_zone":
        return 3.0 * P["c_j_k"] / P["ua"] / dt
    if t == "process_loop":
        return (3.0 * P.get("tau", dt) + P.get("theta", 0.0)) / dt
    if t == "compute_pool":
        return float(P.get("startup_steps", 1))
    return 1.0


class Edge(_CoreEdge):
    """The v5 edge (omnicompass/edge.py) for one plant's knob: the knob's own reaction, and, with physics memory, its
    risks kept as long as the plant's own slowest physics carries them."""

    def __init__(self, plant, cfg, key=None):
        mem = cfg.memory
        if cfg.physics_memory:
            mem = physics_memory(memory_horizon(plant), cfg.window)
        super().__init__(reaction_steps(plant, key) * cfg.react_mult, z=cfg.z, window=cfg.window, narrow=cfg.narrow,
                         start=cfg.start, memory=mem, fall_decay=cfg.fall_decay, est=cfg.est)
        self.cfg = cfg


def deadline_share(plant) -> float:
    """A motion axis's lateness ahead: the oldest waiting task's wait plus the time to clear the whole backlog at the
    axis's present speed, as a share of the deadline (0 when nothing waits). It reads a late task before it is late."""
    w = getattr(plant, "waits", None)
    if not w:
        return 0.0
    P = plant.P
    clear = len(w) * (plant.move_time(plant.s) + P["dwell"])
    return (w[0] + clear) / P["deadline_s"]


def poisson_hi(mean: float, q: float) -> int:
    """The smallest count n with P(N <= n) >= q for a Poisson count of this mean."""
    if mean <= 0.0:
        return 0
    p = math.exp(-mean)
    c, n = p, 0
    while c < q and n < 100000:
        n += 1
        p *= mean / n
        c += p
    return n


def serve_time(plant, n: int, s: float) -> float:
    """Seconds to finish n tasks when the moves started within the next decision run at speed s and every later one at
    full speed (the brain's next decision can restore the speed only for moves not yet started)."""
    if n <= 0:
        return 0.0
    P = plant.P
    cs = plant.move_time(s) + P["dwell"]
    c1 = plant.move_time(1.0) + P["dwell"]
    m = min(n, max(1, math.ceil(P["dt_dec"] / cs)))
    return m * cs + (n - m) * c1


def safe_speed(plant, cfg, lo: float) -> float:
    """The slowest speed a motion axis may be given at this decision, from its own physics:
      a move that would outlast one decision is never slowed (once started its speed cannot be taken back, so the knob's
        reaction time is the whole move, and every task arriving meanwhile would wait behind it);
      a queue is never slowed (every task behind the move would finish later);
      the tasks waiting now and the most that can arrive in the next decision (the motion_q share of a Poisson count at the
        recent peak rate) are all finished inside the deadline even if the whole burst arrives at once;
      and the wake forecast over a whole deadline (the most that can arrive in one deadline at the recent peak rate) is
        finished inside that deadline at the slowed speed, so the axis always goes idle again and a delay is recovered
        before a later rush could make it permanent (an axis one task behind native in a rush stays behind it).
    1.0 is native (full speed): when work comes, the axis wakes straight to it."""
    P = plant.P
    dt = P["dt_dec"]
    hist = getattr(plant, "_v5_arr", None)
    if hist is None:
        hist = plant._v5_arr = []
    k = plant.k
    if k > 0:
        hist.append(plant.arrivals[k - 1])        # what the brain counted arriving in the last decision
        if len(hist) > cfg.burst_window:
            hist.pop(0)
    if plant.backlog > 1 or plant.move_time(1.0) + P["dwell"] > dt:
        return 1.0
    lam = max(plant.demand_rate, (max(hist) / dt) if hist else 0.0)
    burst = plant.backlog + poisson_hi(lam * dt, cfg.motion_q)
    w0 = plant.waits[0] if plant.waits else 0.0
    room = P["deadline_s"] - w0
    # the wake forecast over a whole deadline: the motion_q share of the tasks that can arrive in one deadline at the recent
    # peak rate. A slowed axis must still finish all of them inside that deadline, so it always goes idle again and any
    # delay is recovered before a later rush could make it permanent (a task one behind native in a rush stays behind)
    H = P["deadline_s"]
    n_h = poisson_hi(lam * H, cfg.motion_q)
    s = lo
    while s < 1.0:
        cycle = plant.move_time(s) + P["dwell"]
        if cycle <= dt and serve_time(plant, burst, s) <= room and n_h * cycle <= H:
            return s
        s = min(1.0, s + 0.02)
    return 1.0


def effort_floor(plant) -> float:
    """The least effort a motion axis may be capped to: the torque its next full-speed move needs (inertia times the
    acceleration, the viscous drag at top speed, the standing load and the largest disturbance), as a share of its limit.
    Below it the axis cannot follow its own trajectory and falls behind it."""
    P = plant.P
    need = P["J"] * P["a_max"] + P["b"] * P["v_max"] + abs(P["load_bias"]) + P["dist"]
    return min(1.0, need / P["tau_max"])


class PoolTwin:
    """What the operator's own autoscaler would have had with no cap: the same arrivals the brain counts, the same rules
    (the HPA's tolerance, its scale-down window, the machines' start time). The brain knows the controller it sits on."""

    def __init__(self, P):
        self.n = int(P["n0"])
        self.pending = []
        self.Q = 0.0
        self.hist = []

    def step(self, P, k, lam):
        self.n += sum(1 for s in self.pending if s <= k)
        self.pending = [s for s in self.pending if s > k]
        dt, mu = P["dt"], P["mu"]
        A = lam * dt
        C = self.n * mu * dt
        adm = min(A, max(0.0, C + P["queue_limit_s"] * self.n * mu - self.Q))
        served = min(self.Q + adm, C)
        self.Q += adm - served
        util = served / C if C > 0 else 1.0
        cur = self.n + len(self.pending)
        ratio = util / P["target"]
        rec = cur if abs(ratio - 1.0) <= 0.1 else math.ceil(self.n * ratio)
        self.hist = (self.hist + [rec])[-P["stab_steps"]:]
        want = rec if rec >= cur else min(cur, max(self.hist))
        want = int(clamp(want, P["n_min"], P["n_max"]))
        if want > cur:
            self.pending += [k + P["startup_steps"]] * min(want - cur, max(4, cur))
        elif want < cur:
            cut = cur - want
            while cut and self.pending:
                self.pending.pop()
                cut -= 1
            self.n = max(P["n_min"], self.n - cut)

    def machines_at(self, k):
        return self.n + sum(1 for s in self.pending if s <= k)


def drop_floor(plant, cfg) -> float:
    """The lowest power cap a request-serving pool may be given now. A pool with a bounded queue turns requests away once
    the queue is full, and a request turned away is work lost for good; a burst that starts while the pool is capped finds
    less room than native would have had. So the capped pool must still serve, at once, what is queued plus the arrivals
    after the largest jump in demand this pool has shown (never less than jump0, nor than the jump its operator's own target
    leaves room for, 1/target - 1), and nothing is capped while requests are queued or were turned away."""
    P = plant.P
    hist = getattr(plant, "_v5_lam", None)
    if hist is None:
        hist = plant._v5_lam = []
        plant._v5_jump = max(cfg.jump0, 1.0 / P["target"] - 1.0)
        plant._v5_twin = PoolTwin(P) if not P.get("ca") else None
    k = plant.k
    twin = plant._v5_twin
    if k > 0:
        a = plant.lam[k - 1]
        if hist and hist[-1] > 0:
            plant._v5_jump = max(plant._v5_jump, a / hist[-1] - 1.0)
        hist.append(a)
        if len(hist) > cfg.window:
            hist.pop(0)
        if twin is not None:
            twin.step(P, k - 1, a)
    if plant.drop_share > 0.0 or not hist or plant.Q > (twin.Q if twin is not None else 0.0):
        return 1.0                                                   # turning requests away, or behind native: no cap
    # (1) no less serving capacity than native would have now: the cap spends only machines the autoscaler has added
    # beyond native's (it adds them because the cap raises the utilisation it sees)
    surplus = 1.0
    if twin is not None:
        n_arm = plant.n + sum(1 for s in plant.pending if s <= k)
        n_nat = twin.machines_at(k)
        surplus = (n_nat / n_arm) ** 2.5 if n_arm >= n_nat else 1.0
    # a cap acts until the next decision, so a burst that starts now meets one decision of capped service: the queue it
    # leaves behind is at most the capacity the cap took away. It turns requests away only if, on top of what native's
    # own queue would reach before the autoscaler's new machines start (startup_steps), it overfills the queue's bound
    dt, n, S = P["dt"], plant.n, P["startup_steps"]
    C1 = n * P["mu"] * dt
    B1 = P["queue_limit_s"] * n * P["mu"]
    X1 = max(0.0, hist[-1] * (1.0 + plant._v5_jump) * dt - C1)
    room = B1 - plant.Q - S * X1                                     # what native's queue would leave free in the burst
    # (2) or a shortfall a burst cannot turn into requests turned away; either one alone keeps the work
    if room <= 0.0:
        burst = 1.0
    elif room >= C1:
        burst = 0.0
    else:
        burst = (1.0 - room / C1) ** 2.5                             # mu(cap) = mu cap^0.4: C(cap) >= C1 - room
    return min(surplus, burst)


def latency_floor(plant, cfg) -> float:
    """The lowest power cap that keeps a serving pool's response time inside its line through a burst whenever native's
    would stay inside it (read after drop_floor, which keeps the pool's arrival history and its largest jump). A cap acts
    until the next decision: if the burst (the latest arrivals after the largest jump this pool has shown) outruns the
    capped capacity, the work the cap held back waits behind everything native itself would queue until its new machines
    start (startup_steps), and every request is served a little slower. At most, one capped decision leaves behind all the
    capacity it took away, whatever the burst. The cap is allowed only while that extra wait fits in the room native's own
    worst response time in the burst leaves under the line; where native itself would be late, nothing is capped."""
    P = plant.P
    hist = getattr(plant, "_v5_lam", None)
    if not hist or plant.drop_share > 0.0:
        return 1.0
    dt, n, S, slo = P["dt"], max(plant.n, 1), max(1, int(P["startup_steps"])), P["slo_s"]
    mu1 = plant.mu(1.0)
    lam_b = hist[-1] * (1.0 + plant._v5_jump)
    grow = max(0.0, lam_b * dt - n * mu1 * dt)                       # native's own queue growth per decision in the burst
    room = slo - ((plant.Q + plant.H + grow * S) / (n * mu1) + 1.0 / mu1)
    if room <= 0.0:
        return 1.0
    c = 0.4
    while c < 1.0:
        mu_c = plant.mu(c)
        held = n * (mu1 - mu_c) * dt                                  # the most one capped decision can leave behind:
                                                                       # all the capacity it took away (any burst)
        if held / (n * mu1) + (1.0 / mu_c - 1.0 / mu1) <= room:
            return c
        c = min(1.0, c + 0.02)
    return 1.0


# How far a wandering load runs over its line: the 99.9% quantile, over one hour of decisions, of the deepest excursion
# R = max(0, R - (k + x)) of a load whose spare capacity wanders as a standardized AR(phi) process x with mean k spreads
# (Lindley's recursion: the spare capacity pulls the excursion back, its shortfall pushes it on). In spreads x decisions.
# Rows phi = 0.8, 0.9, 0.95, 0.98; columns k = 0, 0.25, ..., 6. (Monte Carlo, 20,000 hours each: scratchpad/lindley_mc.py)
LINDLEY_PHI = (0.8, 0.9, 0.95, 0.98)
LINDLEY = (
    (152.708, 104.52, 70.88, 48.499, 34.735, 26.563, 20.498, 15.714, 11.983, 9.01, 6.777, 4.898, 3.411, 2.233, 1.426,
     0.814, 0.432, 0.152, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    (213.775, 159.008, 116.768, 83.079, 60.201, 46.878, 37.396, 29.04, 22.051, 16.486, 12.974, 9.636, 6.317, 4.438,
     2.726, 1.381, 0.499, 0.157, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    (289.729, 238.03, 190.297, 148.51, 112.981, 84.525, 66.894, 48.288, 36.794, 26.801, 17.795, 11.811, 7.975, 4.807,
     2.508, 1.017, 0.251, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    (424.6, 365.52, 307.666, 254.623, 207.105, 162.118, 126.978, 97.331, 69.401, 51.264, 38.243, 24.412, 16.657, 9.051,
     3.737, 1.082, 0.082, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
)


def lindley_reach(phi: float, k: float) -> float:
    """The table read between its rows and columns (beyond its edges: the nearest row, and nothing past k = 6)."""
    k = max(0.0, k)
    if k >= 6.0:
        return 0.0
    j = int(k / 0.25)
    fk = k / 0.25 - j

    def row(r):
        return r[j] + (r[j + 1] - r[j]) * fk

    phi = clamp(phi, LINDLEY_PHI[0], LINDLEY_PHI[-1])
    for i in range(len(LINDLEY_PHI) - 1):
        if phi <= LINDLEY_PHI[i + 1]:
            f = (phi - LINDLEY_PHI[i]) / (LINDLEY_PHI[i + 1] - LINDLEY_PHI[i])
            return row(LINDLEY[i]) + (row(LINDLEY[i + 1]) - row(LINDLEY[i])) * f
    return row(LINDLEY[-1])


def cooling_hole_ceiling(plant, cfg, native: float) -> float:
    """The warmest setpoint a cooled zone may be given now, from its own physics: the hole is a cooling plant that runs
    out (the heat in exceeds everything its units can remove); then no setpoint can pull the zone down, and only the
    degrees the zone has in hand below its limit carry it through. So the zone may be held warmer than the operator's
    setpoint only by the degrees its worst plausible saturation would not need.

    The brain reads the heat the zone sheds each decision from its own energy balance (the cooling delivered plus what
    the room's mass stored) as the cooling's headroom h, the share of its installed capacity left, and keeps h's mean,
    spread and memory (lag-one correlation) over everything it has seen; the spread is never taken below what the
    step-to-step swing implies over the wander's correlation time. How far such a wander runs the room over its setpoint
    in an hour at 99.9% is the Lindley reach, in spreads x decisions; times the spread, Q / C and the decision gives the
    degrees. The ceiling leaves those degrees, plus the loop's own tracking overshoot seen so far, below the limit.
    Nothing is raised until the brain has a window of readings."""
    P = plant.P
    Q = P["units"] * P["q_unit_w"] * plant.override.get("power", 1.0)
    t_prev = getattr(plant, "_v5_Tprev", plant.T)
    plant._v5_Tprev = plant.T
    q_heat = plant.qc_avg + P["c_j_k"] * (plant.T - t_prev) / P["dt"]
    h = 1.0 - q_heat / max(Q, 1e-9)
    st = getattr(plant, "_v5_hs", None)
    if st is None:
        st = plant._v5_hs = {"n": 0, "m": h, "v": 0.0, "dv": 0.0, "last": h, "c": 0.0, "track": 0.1}
    st["n"] += 1
    n = st["n"]
    a = 1.0 / n                                                     # every reading kept: the whole memory
    d = h - st["last"]
    dm = h - st["m"]
    st["m"] += a * dm
    st["v"] = (1.0 - a) * (st["v"] + a * dm * dm)
    st["c"] = (1.0 - a) * st["c"] + a * (h - st["m"]) * (st["last"] - st["m"])     # lag-one covariance
    st["dv"] = (1.0 - a) * st["dv"] + a * d * d
    st["last"] = h
    hh = st.setdefault("hh", [])                                    # the headroom's recent readings, for its trend
    hh.append(h)
    if len(hh) > cfg.window:
        hh.pop(0)
    if h > 0.0:
        st["track"] = max(st["track"], plant.T - plant.setpoint())  # the loop's own overshoot while it had headroom
    if len(hh) > 1:
        # the headroom read ahead: falling at its present rate (the steeper of the fall over the window and over the
        # cooling's own answer time), would it run out before the cooling could pull the zone back? Then the zone goes
        # into that hole at the operator's own temperature, never warmer: the setpoint is native until the fall stops
        react = reaction_steps(plant)
        r = max(1, min(len(hh) - 1, int(math.ceil(react))))
        fall = max(0.0, (hh[0] - hh[-1]) / (len(hh) - 1), (hh[-1 - r] - hh[-1]) / r)
        if h - fall * react <= 0.0:
            return native
    hi = max(P["stress"], P["calm"])
    # never behind what came before: the earlier law's own balance point (the zone held at the middle of its band) stays
    # allowed from the first decision; only the degrees beyond it must be proven by the reach
    lo = min(P["stress"], P["calm"])
    floor = lo + cfg.base_center * (P["t_limit"] - lo) if (cfg.hybrid and cfg.hole_floor) else native
    if n < cfg.window:
        return clamp(floor, native, hi)
    phi = clamp(st["c"] / st["v"], 0.0, 0.999) if st["v"] > 1e-12 else 0.0
    tc = max(float(cfg.window), 1.0 / (1.0 - phi))                   # the wander's correlation time, in decisions
    sd = max(math.sqrt(st["v"]), math.sqrt(st["dv"]) * math.sqrt(tc / 2.0), 1e-6)
    reach = lindley_reach(1.0 - 1.0 / tc, st["m"] / sd)              # spreads x decisions
    rise = sd * Q / P["c_j_k"] * P["dt"] * reach                     # degrees the worst hour's saturation adds
    ceiling = max(P["t_limit"] - rise - st["track"], floor)
    if cfg.precool and h > 0.0:
        # or, while the cooling has headroom now: the degrees it can pull back before that headroom could run out (it
        # falls by at most z step-to-step swings times the square root of the steps the pull-back takes), held only as
        # long as each decision proves it again; the zone is cooled ahead of a surge instead of held back all hour
        fall = cfg.z * max(math.sqrt(st["dv"]), 1e-6)
        room = (h / fall) ** 2 - 1.0
        if room > 0.0:
            ceiling = max(ceiling, native + room * P["dt"] * h * Q / P["c_j_k"] - st["track"])
    return clamp(ceiling, native, hi)


def cooling_headroom_position(plant) -> float:
    """A cooling zone's second gauge: how close its cooling is to running flat out ((load ratio - 0.5) / 0.5). A room whose
    cooling has no spare capacity cannot be pulled back by any setpoint, so its margin must already be there."""
    o = plant.observe()
    return (o["load_ratio"] - 0.5) / 0.5


def v5_position(plant) -> float:
    """The service position the v5 law reads: the plant's own, and for a motion axis the deadline margin too, and for a
    cooling zone the cooling's own headroom too (every gauge the plant offers, the worst one decides)."""
    p = position(plant)
    if plant.template == "motion_axis":
        p = max(p, deadline_share(plant))
    elif plant.template == "thermal_zone" and getattr(plant, "_v5_headroom", False):
        p = max(p, cooling_headroom_position(plant))
    return p


def band_position(plant) -> float:
    """A process loop's place in its own band: how far it strayed from its setpoint in the last decision plus how far
    that setpoint sits from the band's middle, in half-bands (1 is the band's edge). The plant's deviation reading is
    taken from wherever the setpoint is, so a setpoint eased toward the band's calm end reads as calm while the margin
    to the edge shrinks; this is the margin itself."""
    P = plant.P
    return plant.dev + abs(plant.setpoint() - P["mid"]) / P["half"]


def loop_reach(plant, cfg, calm_low: bool):
    """How far this loop's disturbance pushes it off its setpoint toward the band's calm-side edge, in half-bands, from
    everything the brain has seen (the historian's low, or high, over each decision: a swing toward the band's middle
    cannot take the loop out, so it is not counted). The larger of the deepest such swing seen and its mean plus z
    spreads, the spread never below what the step-to-step swing implies over the swing's own correlation time (the reading
    the cooling hole guard uses). A loop slower than one decision is also read ahead: its swing now, carried on at its
    present climb (the steeper of the climb over the window and over the loop's own answer time) for as long as the loop
    takes to answer once its setpoint goes back. None until the brain has a window of readings."""
    d = plant.dev_dn if calm_low else plant.dev_up
    st = getattr(plant, "_v5_ls", None)
    if st is None:
        st = plant._v5_ls = {"n": 0, "m": d, "v": 0.0, "dv": 0.0, "last": d, "c": 0.0, "peak": 0.0, "h": []}
    st["n"] += 1
    n = st["n"]
    a = 1.0 / n                                                     # every reading kept: the whole memory
    dd = d - st["last"]
    dm = d - st["m"]
    st["m"] += a * dm
    st["v"] = (1.0 - a) * (st["v"] + a * dm * dm)
    st["c"] = (1.0 - a) * st["c"] + a * (d - st["m"]) * (st["last"] - st["m"])     # lag-one covariance
    st["dv"] = (1.0 - a) * st["dv"] + a * dd * dd
    st["last"] = d
    st["peak"] = max(st["peak"], d)
    h = st["h"]
    h.append(d)
    if len(h) > cfg.window:
        h.pop(0)
    if n < cfg.window:
        return None
    phi = clamp(st["c"] / st["v"], 0.0, 0.999) if st["v"] > 1e-12 else 0.0
    tc = max(float(cfg.window), 1.0 / (1.0 - phi))                   # the swing's correlation time, in decisions
    sd = max(math.sqrt(st["v"]), math.sqrt(st["dv"]) * math.sqrt(tc / 2.0), 1e-9)
    reach = max(st["peak"], st["m"] + cfg.z * sd)
    P = plant.P
    answer = (P.get("tau", 0.0) + P.get("theta", 0.0)) / P["dt"]       # decisions the loop takes to answer its setpoint
    if answer > 1.0:
        r = max(1, min(len(h) - 1, int(math.ceil(answer))))
        climb = max(0.0, (h[-1] - h[0]) / (len(h) - 1), (h[-1] - h[-1 - r]) / r)
        reach = max(reach, d + climb * answer)
    return reach


def loop_clamp(plant, cfg, x: float, native: float) -> float:
    """The setpoint never sits closer to its band's calm-side edge than the loop's own reach leaves room for: at most
    (1 - reach) half-bands from the band's middle, and native once that room is gone. Before the brain has a window of
    readings the band reading alone holds the loop (the earlier law's own behaviour, as the hole guard allows)."""
    P = plant.P
    reach = loop_reach(plant, cfg, P["calm"] < P["mid"])
    if reach is None:
        return x
    room = (1.0 - reach) * P["half"]
    if room <= abs(native - P["mid"]):
        return native
    return clamp(x, P["mid"] - room, P["mid"] + room)


def raw_position(plant) -> float:
    """The service position without the last decision's violation flag (for the climb and wobble statistics)."""
    if plant.template == "motion_axis":
        o = plant.observe()
        return max(o["queue_ratio"], (o["load_ratio"] - 0.5) / 0.5, deadline_share(plant))
    if plant.template == "thermal_zone":
        P = plant.P
        t = (plant.T - min(P["stress"], P["calm"])) / (P["t_limit"] - min(P["stress"], P["calm"]))
        return max(t, cooling_headroom_position(plant)) if getattr(plant, "_v5_headroom", False) else t
    o = plant.observe()
    p = max(o["queue_ratio"], (o["load_ratio"] - 0.5) / 0.5)
    if plant.template == "energy_storage":
        p = max(p, (o["power_stress"] - 0.5) / 0.5)
    # (a process loop's statistics stay on its deviation from its own setpoint: the cushion is for what the disturbance
    # does, while the setpoint's own offset toward the band's edge is the brain's known choice, read by the law itself)
    return p


# ---------------------------------------------------------------------------------------------------------------------
# MAX, the work edge: the default brain (the founder's orders of 11 and 12 October). Every muscle is pushed toward its
# own limit to do the most work, faster; never past its limit and never below native (native's own setting is always one
# of the brain's choices, so a muscle native already runs flat out stays native, wired and watched). The energy that
# takes is reported as power given, beside the work and the speed it bought. One pedal: push for more, lift off for
# less, and lifting hands the setting back toward native.
#
#   compute pool   the machines the forecast needs are started before the rush lands: the recent peak arrivals widened
#                  by the largest rise this pool has shown within one machine start, plus the standing queue, at the edge
#                  utilisation. The HPA target is lowered just enough that the operator's own autoscaler starts them (a
#                  machine pool: a floor under its cluster autoscaler). Never fewer machines than native would keep; the
#                  power cap and admission stay native (full clock, every request admitted)
#   cooled zone    cooled ahead of the heat: the setpoint goes from the operator's toward the band's cold end as the
#                  room nears its limit or its cooling nears flat out, both read ahead by the cooling's own answer time;
#                  never warmer than native
#   battery site   the charge is held for the line instead of spent on the first minutes of load, and only the draw
#                  that would cross the site's line (the forecast draw plus line_z of its step-to-step wobbles) is taken
#                  from it; a UPS lends only the charge above its outage floor (its band's stress end), never below it
#   motion axis    native: full speed and effort, native already runs it flat out
#   process loop   native: the full actuator, native already runs it flat out
def max_pool_want(plant, cfg) -> int:
    """The machines a pool needs when a machine started now is ready: the recent peak arrivals (what the brain counted,
    never the decision still to come) widened by the largest rise this pool has shown within one machine start (at
    first, the room its operator's own target leaves: 1/target - 1), plus the standing queue, at the edge utilisation."""
    P = plant.P
    k = plant.k
    S = max(1, int(P["startup_steps"]))
    st = getattr(plant, "_mx", None)
    if st is None:
        st = plant._mx = {"lam": [], "rise": max(0.0, 1.0 / P["target"] - 1.0)}
    h = st["lam"]
    if k > 0:
        a = plant.lam[k - 1]
        if len(h) > 0:
            lo = min(h[-S:])
            if lo > 0.0:
                st["rise"] = max(st["rise"], a / lo - 1.0)
        h.append(a)
        if len(h) > max(cfg.window, S + 1):
            h.pop(0)
    if not h:
        return int(P["n_min"])
    fore = max(h) * (1.0 + st["rise"])
    need = (fore + plant.Q / P["dt"]) / (plant.mu(1.0) * cfg.edge_util)
    return int(clamp(math.ceil(need - 1e-9), P["n_min"], P["n_max"]))


def max_cool(plant, cfg) -> float:
    """A cooled zone's setpoint for the most work: the operator's, moved toward the band's cold end as the room nears its
    limit or its cooling nears flat out. The cooling's load is read from the room's own energy balance (the cooling
    delivered plus what the room's mass stored) against its installed capacity, carried ahead at its present climb for the
    cooling's own answer time; heat that outruns the cooling is carried by the degrees the room already has in hand."""
    P = plant.P
    native = P["t_set"]
    cold = min(P["stress"], P["calm"])
    Q = P["units"] * P["q_unit_w"]
    t_prev = getattr(plant, "_mx_T", plant.T)
    plant._mx_T = plant.T
    load = (plant.qc_avg + P["c_j_k"] * (plant.T - t_prev) / P["dt"]) / max(Q, 1e-9)
    hist = getattr(plant, "_mx_q", None)
    if hist is None:
        hist = plant._mx_q = []
    hist.append(load)
    if len(hist) > cfg.window:
        hist.pop(0)
    react = reaction_steps(plant)
    climb = 0.0
    if len(hist) > 1:
        r = max(1, min(len(hist) - 1, int(math.ceil(react))))
        climb = max(0.0, (hist[-1] - hist[0]) / (len(hist) - 1), (hist[-1] - hist[-1 - r]) / r)
    ahead = load + climb * react
    room = (plant.T - cold) / max(P["t_limit"] - cold, 1e-9)
    risk = max(clamp((ahead - 0.8) / 0.2, 0.0, 1.0), clamp((room - 0.6) / 0.3, 0.0, 1.0))
    return min(native, native - (native - cold) * risk)


def max_hold(plant, cfg, key):
    """A battery site's knob for the most work held inside its line: the charge kept for the line, and only the draw
    that would cross the line taken from it. The draw is forecast from the brain's own readings: the last decision's net
    draw, plus its latest rise, plus line_z of its step-to-step wobbles. A UPS lends only the charge above its outage
    floor (its band's stress end); any other site, down to its band's stress end."""
    P = plant.P
    st = getattr(plant, "_mx_s", None)
    if st is None:
        st = plant._mx_s = {"last": plant.net, "n": 0, "dv": 0.0}
    d = plant.net - st["last"]
    st["last"] = plant.net
    if plant.k > 0:
        st["n"] += 1
        a = 1.0 / st["n"]
        st["dv"] = (1.0 - a) * st["dv"] + a * d * d
    fore = plant.net + max(0.0, d) + cfg.line_z * math.sqrt(st["dv"])
    over = max(0.0, fore - P["p_lim_w"])                         # the draw that would cross the line this decision
    floor = P["stress"]
    if key == "setpoint":
        E, sq = P["e_wh"] * 3600.0, math.sqrt(P["eta_rt"])
        dt = P["dt"]
        # native plus: the operator's own reserve while nothing would cross the line (the site's own use of its
        # battery is native's), and below it, down to the floor, exactly the draw that would cross
        r = clamp(plant.soc - over * dt / (E * sq), floor, P["reserve"])
        return {} if abs(r - P["reserve"]) < 1e-12 else {"setpoint": r}
    # the ceiling the battery defends (the capacity knob): the line less the forecast's own margin
    cap = clamp(1.0 - (fore - plant.net) / P["p_lim_w"], 0.5, 1.0)
    return {"capacity": cap}


def machines(pool) -> int:
    """A pool's machines in service and starting."""
    return pool.n + len(pool.pending)


def max_ask(plant, knob, cfg, twin=None):
    """What a muscle asks for the most work this decision. A pool: the machines its forecast needs, never fewer than its
    twin (the brain's model of native: the same plant under its own autoscaler alone, on the same arrivals) runs now. A
    cooled zone at risk: a colder setpoint and the most its pull-down can add. None: the muscle asks nothing (it holds
    native, a donor's spare or a battery's own line)."""
    P, t = plant.P, plant.template
    if t == "compute_pool" and knob not in ("power", "admission"):
        base = machines(twin) if twin is not None else int(P["n_min"])
        want = max(max_pool_want(plant, cfg), base)
        return {"want": want, "base": base, "cur": machines(plant), "held": int(plant.override.get("floor", 0)),
                "unit_w": P["p_idle"], "line": "src"}
    if t == "thermal_zone" and knob == "setpoint":
        x = max_cool(plant, cfg)
        if x >= P["t_set"] - 1e-9:
            return None
        cop = plant.cop(x, plant.tout[min(plant.k, plant.steps - 1)])
        cost = max(0.0, P["units"] * P["q_unit_w"] - plant.qc_avg) / cop   # the most the pull-down can add
        return {"x": x, "cost": cost, "line": "zone"}
    return None


def max_apply(plant, knob, cfg, twin=None):
    """The max for a muscle alone (no body around it to share with): a pool's machines started before the rush and
    never fewer than its twin runs, a room cooled ahead of the heat, a battery's line clipped from its charge; every
    other knob native."""
    P, t = plant.P, plant.template
    ov = {}
    a = max_ask(plant, knob, cfg, twin)
    if a is not None and t == "compute_pool":
        ov = {"floor": float(a["want"])} if a["want"] > P["n_min"] else {}
    elif a is not None and t == "thermal_zone":
        ov = {"setpoint": a["x"]}
    elif t == "energy_storage" and knob in ("setpoint", "capacity"):
        ov = max_hold(plant, cfg, knob)
    plant.override = ov
    return ov


class Bone:
    """The body's skeleton for the max: the lines every muscle stands on. A battery site's grid line and a room's
    cooling are loaded by the whole body (the body's power swing is load on every site, the machines' power is heat in
    every room), so no muscle may take power the bone cannot carry: what the max adds is granted only out of the room the
    most loaded line has left, read one decision ahead (the line's latest reading plus line_z of its own step-to-step
    wobbles; a battery that clips its own line counts the power it can still clip). With no room, the machines this
    brain added go back at once, never below what the pool's twin runs (the brain's model of native: the same pool under
    its own autoscaler alone, on the same arrivals), so a pool never has fewer machines than native and the lines never
    carry more of this brain's power than they have room for. Nothing is taken from one muscle to give to another: the
    max never shaves (the tune-down does that, on the dial)."""

    def __init__(self, body, cfg):
        self.body, self.cfg = body, cfg
        self.st = {}
        self.twins = {}
        for i, (p, r) in enumerate(zip(body.plants, body.rows)):
            if p.template == "compute_pool" and r["knob"] not in ("power", "admission"):
                from .harness import make_plant
                from .plants import pack
                self.twins[i] = pack(make_plant(r, body.seed, organism=True))
                if getattr(body, "load", None) is not None:
                    from .harness import scale_load_plant
                    scale_load_plant(self.twins[i], body.load)

    def advance_twin(self):
        """Step every twin one decision (each decides on the same arrivals native sees)."""
        for tw in self.twins.values():
            tw.step()

    def _ahead(self, key, x, prior):
        """How far a line's reading can climb in one decision, from everything the brain has seen of it: the larger of
        line_z of its step-to-step wobbles and the largest single climb it has shown (never forgotten: a line that once
        jumped can jump again), and never less than the prior (a twentieth of the line) until it has shown more."""
        st = self.st.get(key)
        if st is None:
            st = self.st[key] = {"last": x, "n": 0, "dv": 0.0, "rise": 0.0}
            return prior
        d = x - st["last"]
        st["last"] = x
        st["n"] += 1
        a = 1.0 / st["n"]
        st["dv"] = (1.0 - a) * st["dv"] + a * d * d
        st["rise"] = max(st["rise"], d)
        return max(self.cfg.line_z * math.sqrt(st["dv"]), st["rise"], prior)

    def room(self):
        """(room for machines, room for cooling): the W the body may still add, one decision ahead."""
        b = self.body
        r_src = r_all = math.inf
        n_st = max(1, len(b.stores))
        for s, kl in zip(b.stores, b.k_load):
            P = s.P
            g = kl / n_st                                            # site draw per W of the body's power
            clip = 0.0
            if getattr(s, "override_kind", None) == "clip":
                E, sq = P["e_wh"] * 3600.0, math.sqrt(P["eta_rt"])
                clip = min(P["p_batt_w"], max(0.0, s.soc - P["stress"]) * E * sq / P["dt"])
            margin = P["p_lim_w"] + clip - (s.imp + self._ahead(id(s), s.imp, 0.05 * P["p_lim_w"]))
            r_all = min(r_all, margin / g if g > 0 else math.inf)
        n_z = max(1, len(b.zones))
        for zn, kh in zip(b.zones, b.k_heat):
            P = zn.P
            h = kh / n_z                                             # room heat per W of the body's machine power
            Q = P["units"] * P["q_unit_w"]
            margin = Q - (zn.qc_cmd_avg + self._ahead(id(zn), zn.qc_cmd_avg, 0.05 * Q))
            r_src = min(r_src, margin / h if h > 0 else math.inf)
        return min(r_src, r_all), r_all


def _units(room: float, unit: float, cap: int) -> int:
    """How many units of unit W fit in room W (cap when the room is unbounded)."""
    if not math.isfinite(room):
        return cap
    return max(0, min(cap, int(room // unit)))


def max_body_step(body, cfg, bone):
    """One decision of the max over one body: every battery that can clips its own line, and the machines and cooling
    the muscles ask for are granted out of the room the bone has left; with no room, what this brain added goes back at
    once, never below what the twin runs. Every other muscle is wired, watched and native."""
    asks = []
    for i, (p, knob) in enumerate(zip(body.plants, body.knobs)):
        t = p.template
        p.override_kind = None
        if t == "energy_storage" and knob in ("setpoint", "capacity"):
            p.override = max_hold(p, cfg, knob)
            p.override_kind = "clip"
            continue
        a = max_ask(p, knob, cfg, bone.twins.get(i))
        if a is None:
            p.override = {}
            continue
        asks.append((p, a))
    r_src, r_all = bone.room()
    if r_src < 0.0 or r_all < 0.0:
        # no room on a line: every pool goes to exactly its twin's machines at once (floor and ceiling both at native's
        # count: what this brain added is handed back, nothing native has is taken), and no room is cooled below the
        # operator's setpoint, until the bone has room again
        for p, a in asks:
            if a["line"] == "src":
                base = float(max(a["base"], p.P["n_min"]))
                extra = a["cur"] > a["base"]
                p.override = ({"floor": base, "cap": base} if extra else
                              ({"floor": base} if base > p.P["n_min"] else {}))
            else:
                p.override = {}
        return
    for p, a in sorted(asks, key=lambda pa: -(pa[1].get("want", 0) - max(pa[1].get("cur", 0), pa[1].get("base", 0)))):
        if a["line"] == "src":
            now = max(a["cur"], a["base"])
            add = max(0, a["want"] - now)
            can = min(_units(r_src, a["unit_w"], add), _units(r_all, a["unit_w"], add)) if add else 0
            floor = max(now + can if add else a["want"], a["base"])
            r_src -= can * a["unit_w"]
            r_all -= can * a["unit_w"]
            p.override = {"floor": float(floor)} if floor > p.P["n_min"] else {}
        elif a["cost"] <= r_all:
            p.override = {"setpoint": a["x"]}
            r_all -= a["cost"]
        else:
            p.override = {}                                          # the pull-down waits for room


def compass_apply_v5(plant, knob, cfg, dt=1.0, tau=3.0):
    if cfg.dial == "max":
        return max_apply(plant, knob, cfg)
    lv = lever_v5(plant, knob, cfg)
    if lv is None:
        plant.override = {}
        return {}
    if not hasattr(plant, "_v5"):
        plant._v5_headroom = cfg.headroom
        plant._v5_band = cfg.band
        law = CompassLaw(Band(0.0, 1.0), dt=dt, tau=tau, kp=1.0, smooth=0.3)
        law.kd *= 3.0
        plant._v5 = (law, Edge(plant, cfg, lv[0]))
        plant._v5_x = lv[1]
    law, edge = plant._v5
    p = v5_position(plant)
    edge.since = 0 if plant.override else getattr(edge, "since", 10 ** 9) + 1
    if plant.template == "motion_axis":
        blame = max(3.0, plant.P["deadline_s"] / plant.P["dt_dec"])     # a late task was decided a deadline ago
    else:
        # a fall within the knob's own reaction/settling time of Omni holding back is Omni's doing: a power cap on a
        # serving pool shows up as latency a few decisions later (its startup lag), a process loop's overshoot within its
        # three time constants. So the cap teaches that plant's cushion floor even when the fall is not the same decision.
        blame = memory_horizon(plant)
    if cfg.learn_fall > 0 and plant.vhist and plant.vhist[-1] and edge.since <= blame:
        # a fall while, or soon after, Omni held something back: this plant needs more room than its statistics said
        edge.floor = min(1.0, max(edge.floor, edge.cushion) + cfg.learn_fall)
    center = edge.update(raw_position(plant))
    if cfg.hybrid:
        # never behind what came before: the edge only moves the balance point and the wall further out; but a plant
        # that has fallen while Omni held something back has taught the brain otherwise, and its own lesson decides
        base = cfg.base_center if edge.floor <= 0.0 else 0.0
        law.band.center = clamp(max(base, center), 0.0, 0.995)
        law.band.cushion = min(1.0 - cfg.base_wall, max(0.005, edge.react_part))
    else:
        law.band.center = clamp(center, 0.0, 0.995)
        law.band.cushion = min(0.5, max(0.005, edge.react_part))      # the wall moves with the reaction part
    if cfg.band and plant.template == "process_loop":
        # the band's own edge (1 is the edge). A loop faster than one decision is pushed about within the decision by its
        # disturbance alone, so it is read ahead: the setpoint's offset from the band's middle plus the most the
        # disturbance has pushed it off its setpoint (mean plus z times the spread over the window). A slower loop's
        # deviation from a moving setpoint is mostly its own lag, so it is read as it stands (offset plus deviation) and
        # acts only at the wall. Either way, once the reading reaches the wall the law fails up; away from the edge the
        # law reads the plant as before.
        P = plant.P
        off = abs(plant.setpoint() - P["mid"]) / P["half"]
        if (3.0 * P.get("tau", 0.0) + P.get("theta", 0.0)) / P["dt"] <= 1.0:
            hist = getattr(plant, "_v5_band_h", None)
            if hist is None:
                hist = plant._v5_band_h = []
            hist.append(plant.dev)
            if len(hist) > cfg.window:
                hist.pop(0)
            md = sum(hist) / len(hist)
            sd = math.sqrt(sum((x - md) ** 2 for x in hist) / max(1, len(hist) - 1)) if len(hist) > 1 else md
            p = max(p, off + md + cfg.z * sd)
        elif off + plant.dev >= law.band.wall_high:
            p = max(p, off + plant.dev)
    F = law.force(p)
    key, native, lo, hi, sign = lv
    if key == "release":
        ok = F < RELEASE and law.p < law.band.center and release_safe(plant)
        plant.override = {"release": 1.0} if ok else {}
        return plant.override
    span = hi - lo
    if key == "setpoint" and plant.template == "energy_storage":
        P = plant.P
        excess = plant.imp - P["p_lim_w"]
        coverable = 0.0 < excess <= P["p_batt_w"] * plant.override.get("power", 1.0)
        x = lo if (law.p >= law.band.wall_high and (coverable or plant.imp >= 0.95 * P["p_lim_w"] and excess <= 0.0)) else native
        plant._v5_x = x
        plant.override = {} if abs(x - native) < 1e-9 else {key: x}
        return plant.override
    if law.p >= law.band.wall_high:
        # at the wall: the energy edge snaps straight back to native (always free, never beyond it); the speed edge
        # and the hybrid fail up to full capacity at once, as the earlier law did
        if cfg.spend_beyond or cfg.hybrid:
            x = hi if sign > 0 else lo
        elif cfg.snap:
            x = native
        else:
            x = clamp(plant._v5_x + sign * UP * span, lo, hi)          # the law's full force up, smooth, never a snap
            x = min(x, native) if sign > 0 else max(x, native)
    else:
        g = UP if F > 0 else DOWN
        x = clamp(plant._v5_x + sign * g * F * span, lo, hi)
        if not (cfg.spend_beyond or cfg.hybrid):
            # the energy edge: away from the wall nothing is spent beyond native (native is always free)
            x = min(x, native) if sign > 0 else max(x, native)
    if cfg.drop_guard and plant.template == "compute_pool" and key == "power":
        x = max(x, drop_floor(plant, cfg))                             # no request turned away (keeps the history)
        x = max(x, latency_floor(plant, cfg))                          # no response pushed over the line
    if cfg.hole_guard and plant.template == "thermal_zone" and key == "setpoint":
        x = min(x, cooling_hole_ceiling(plant, cfg, native))
    if cfg.motion_safe and plant.template == "motion_axis":
        # the edge read from the axis's own physics, at once: never slower than its queue and the next decision's burst
        # allow, never weaker than its next move needs
        x = max(x, safe_speed(plant, cfg, lo) if key == "capacity" else effort_floor(plant))
    if cfg.loop_reach and plant.template == "process_loop" and key == "setpoint":
        x = loop_clamp(plant, cfg, x, native)
    plant._v5_x = x
    plant.override = {} if abs(x - native) < 1e-9 else {key: x}
    return plant.override


# The tune-down setting (the dial turned from the max down to save): native's work on the least energy, every muscle equal
# or better than native on the modelled plants. The autoscaler's target held at the operator's; the step-to-step
# estimator; a fall while Omni held back raises that plant's cushion floor; the hybrid never behind the earlier law; each
# plant remembers its own physics; motion speed and effort never below what the axis needs; a process loop read against
# its band's edge, its setpoint never closer to that edge than its own largest swing (generators included); a request pool
# never capped below the largest demand jump; a cooled zone never warmer than its cooling can recover; a power cap only on
# a pool whose response line outlasts a decision, never below the largest demand jump or past the line; the battery shave
# and a cloud machine pool's hand-back held native.
V5SAVE = Cfg(dial="save", target_free=False, est=2, learn_fall=0.1, hybrid=True, physics_memory=True, motion_safe=True,
             band=True, drop_guard=True, hole_guard=True, loop_reach=True, power_cap=True)

# The engine's default: the max (the founder's order of 12 October: "We're going to show a benchmark that shows it to the
# max. And we're going to show one native... anybody can tune it from the max down"). Every muscle pushed to its own limit
# for the most work, faster; the energy that takes is power given.
V5CFG = Cfg(dial="max", window=20, edge_util=0.95, line_z=3.09)


def apply_v5(plant, knob):
    """compass_apply_v5 with the engine's default v5 configuration (V5CFG, the max)."""
    return compass_apply_v5(plant, knob, V5CFG)


def apply_v5_save(plant, knob):
    """compass_apply_v5 turned down to save (V5SAVE)."""
    return compass_apply_v5(plant, knob, V5SAVE)
