# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The compass law on every realm muscle (omnicompass/compass_law.py): each plant's knob held by its own compass.

Each plant's service is read as one position in its compass (0 calm, 1 the line): the worst of its queue or lateness, its
load above half, and, for a storage site, its draw on the grid connection above half. The last period in violation
reads as past the wall (fail up). The compass's force moves the knob: a positive force adds capacity, power, cooling or
protection, a negative force gives it back, each knob inside its own cover. At the kill every knob returns to native.

Knob by plant (the override key the plant already obeys, its native value, its cover, and which way is "more"):
  compute_pool   power: limit share 0.4-1; replicas-type: the HPA target held at native (loosening it past the
                 operator's own costs the service time, the same rule as the card's speed floor); machine pools: one
                 machine released while the force is clearly down and the machines left cover the recent peak with
                 margin (RELEASE_MARGIN); admission: native
  thermal_zone   setpoint between the band's stress (colder, more cooling) and calm ends; units: one released while the
                 force is clearly down; power: native (a cooling cap moves heat later, never away)
  energy_storage reserve between the band's ends (a lower reserve gives the battery to the site); power: native
  motion_axis    speed and effort: 0.4-1
  process_loop   setpoint from native toward the band's calm end; actuator range 0.3-1; power 0.4-1
"""
from __future__ import annotations

from omnicompass.body import Body, Muscle
from omnicompass.compass_law import Band, CompassLaw, clamp

UP, DOWN, RELEASE = 0.10, 0.02, -0.2
RELEASE_MARGIN = 0.3     # a machine goes back only when the rest covers the recent peak at 0.3 of the plant's own release level
# 0.3: the largest margin at which no node pool is later than native (results/realms/RELEASE_MARGIN_SWEEP.md, the
# per-muscle sweep of 2026-10-05: 0.6 saved 2.0% energy with 32 of 42 pools later, 0.4 left 4 later, 0.3 none). A machine
# boots in minutes and a burst that comes in the meantime is served late, so speed first holds the machines (the same
# rule as the verdict on real Kubernetes: a machine goes back only where it costs no speed)


def position(plant) -> float:
    if plant.vhist and plant.vhist[-1]:
        return 1.0
    if plant.template == "thermal_zone":                       # a zone's service is its temperature against its limit
        P = plant.P
        return (plant.T - min(P["stress"], P["calm"])) / (P["t_limit"] - min(P["stress"], P["calm"]))
    o = plant.observe()
    p = max(o["queue_ratio"], (o["load_ratio"] - 0.5) / 0.5)
    if plant.template == "energy_storage":
        p = max(p, (o["power_stress"] - 0.5) / 0.5)
    return p


def release_safe(plant) -> bool:
    """A discrete unit goes back only when what is left covers the recent peak (the plant's own release window), with
    RELEASE_MARGIN of headroom on a machine pool: a machine boots in minutes, so a burst that arrives after a release
    is served late until it is back."""
    P = plant.P
    if plant.template == "compute_pool":
        from .plants import RELEASE_WINDOW, RELEASE_FRAC
        n = plant.n
        return (n > P["n_min"] and not plant.pending and plant.Q <= 0.0
                and len(plant.ahist) == RELEASE_WINDOW * P["startup_steps"]
                and max(plant.ahist) / ((n - 1) * plant.mu(plant.cap)) <= RELEASE_FRAC * 0.95 * RELEASE_MARGIN)
    u = plant.units_on
    return u > 1 and plant.T <= plant.setpoint() and plant.qc_cmd_avg / ((u - 1) * P["q_unit_w"]) <= 0.8


def capping_saves(plant) -> bool:
    """Whether a lower power cap saves energy on this pool at all (race to idle, MECHANISM_OF_ACTION 9.6).

    With throughput mu(c) ~ c^eps at power cap c and the autoscaler holding utilisation near its target u*, the energy
    per unit of work is (p_idle / u* + p_dyn c) / mu(c). Its slope at c = 1 is positive (a lower cap saves) only if
    eps < p_dyn / (p_idle / u* + p_dyn). Where idle power dominates (a quantum computer's cryostat, a network switch),
    running slower keeps the machines on longer and costs more than it saves: the cap is left native."""
    import math
    P = plant.P
    eps = math.log(plant.mu(1.0) / plant.mu(0.99)) / math.log(1.0 / 0.99)   # the machine's own speed curve at full power
    u = P.get("target", 0.7)
    return eps < P["p_dyn"] / (P["p_idle"] / u + P["p_dyn"])


def effort_cap_saves(plant) -> bool:
    """Whether a lower effort cap saves energy on this axis at all (MECHANISM_OF_ACTION 9.6).

    A cap on effort lowers the copper loss of a full-acceleration move, (J a_max / kt)^2 R, and stretches the move, during
    which the axis keeps drawing its idle power and turning against viscous friction, p_idle + b v_max^2. It pays only
    where the first exceeds the second (a reaction wheel); elsewhere (traction, a flight axis, a robot joint) a slower
    move costs more than the current it saves, and the cap is left native."""
    P = plant.P
    copper = (P["J"] * P["a_max"] / P["kt"]) ** 2 * P["R"]
    standing = P["p_idle"] + P["b"] * P["v_max"] ** 2
    return copper > standing


SLACK = 0.5              # a speed knob is offered only where the axis at full speed is busy at most half the time (Omni v3)


def speed_slack(plant) -> bool:
    """Whether the axis has slack to spend on a slower, gentler move at all (Omni v3, docs/REALMS_PREREGISTRATION.md).

    The compass may ease a motion axis down to 0.4 of its speed, which stretches every move by up to 2.5 times. An axis
    whose duty at full speed, task rate x (move time + dwell), is already above one half has no room for that: tasks
    arrive in bunches, and a stretched move pushes the next ones past their deadline (a train on its timetable, a lift at
    rush hour). There the speed knob is left native, as the robot benchmark's paired trial leaves it
    (docs/ROBOTICS_PREREGISTRATION.md). Computed from the plant's own figures before any decision."""
    import math
    P = plant.P
    v, a, D = P["v_max"], P["a_max"], P["D"]
    move = 2.0 * math.sqrt(D / a) if D < v * v / a else D / v + v / a
    return P["task_rate"] * (move + P["dwell"]) <= SLACK


def lever(plant, knob):
    """(override key, native value, low, high, sign): sign +1 when a higher value is more capacity.

    Omni v4: every knob is wired (docs/OMNI_V4_PLAN.md, section 1, rule 8). The v3 rules that held a knob native by the
    plant's physics (capping_saves, effort_cap_saves, speed_slack, the cooling and battery power caps) no longer decide:
    the muscle's own verdict does, live, on the plant (Gate below), and refuses the step where the physics says it cannot
    pay. Only two stay out: a backup reserve (a UPS kept for an outage: a safety lock, never a trial), and admission,
    which is the organism's power-budget muscle (the pace rule), not a muscle with a service of its own to steer."""
    P, t = plant.P, plant.template
    if knob == "admission":
        return None
    if t == "compute_pool":
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1)
        if P.get("ca"):
            return ("release", None, 0, 0, 0)
        # the HPA target: a lower target is more pods (more capacity), never above the operator's own
        return ("target", P["target"], 0.6 * P["target"], P["target"], -1)
    if t == "thermal_zone":
        if knob == "setpoint":
            return ("setpoint", P["t_set"], min(P["stress"], P["calm"]), max(P["stress"], P["calm"]), -1)
        if knob == "capacity":
            return ("release", None, 0, 0, 0)
        return ("power", 1.0, 0.4, 1.0, 1)
    if t == "energy_storage":
        if knob == "setpoint" and P.get("backup"):
            return None                                        # a backup reserve (a UPS) is kept for an outage: locked
        if knob == "setpoint":
            # the reserve may go down to the stress end (the battery given to the site under strain), never above the
            # operator's own: a kWh held back in a calm battery is a kWh bought from the grid (MECHANISM_OF_ACTION 9.6)
            return ("setpoint", P["reserve"], min(P["stress"], P["reserve"]), P["reserve"], -1)
        return ("power", 1.0, 0.4, 1.0, 1)
    if t == "motion_axis":
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1)
        return ("capacity", 1.0, 0.4, 1.0, 1)
    if t == "process_loop":
        if knob == "setpoint":
            lo, hi = min(P["sp"], P["calm"]), max(P["sp"], P["calm"])
            return ("setpoint", P["sp"], lo, hi, 1 if P["sp"] > P["calm"] else -1)
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1)
        return ("capacity", 1.0, 0.3, 1.0, 1)
    return None


def compass_apply(plant, knob, dt=1.0, tau=3.0):
    """One decision: the plant's compass reads its position and moves its knob. Returns the override written."""
    lv = lever(plant, knob)
    if lv is None:
        plant.override = {}
        return {}
    if not hasattr(plant, "_compass_law"):
        plant._compass_law = CompassLaw(Band(0.0, 1.0), dt=dt, tau=tau, kp=1.0, smooth=0.3)
        plant._compass_law.kd *= 3.0
        plant._compass_law_x = lv[1]
    b = plant._compass_law
    F = b.force(position(plant))
    key, native, lo, hi, sign = lv
    if key == "release":
        ok = F < RELEASE and b.p < b.band.center and release_safe(plant)
        plant.override = {"release": 1.0} if ok else {}
        return plant.override
    span = hi - lo
    if key == "setpoint" and plant.template == "energy_storage":
        # a battery's reserve is spent only where it buys service: at the connection's wall the reserve drops to the
        # stress end at once; anywhere else the operator's own reserve, so no round trip is paid for nothing (9.6)
        P = plant.P
        excess = plant.imp - P["p_lim_w"]                       # what the connection is over its limit by, now
        coverable = 0.0 < excess <= P["p_batt_w"] * plant.override.get("power", 1.0)
        x = lo if (b.p >= b.band.wall_high and (coverable or plant.imp >= 0.95 * P["p_lim_w"] and excess <= 0.0)) else native
        plant._compass_law_x = x
        plant.override = {} if abs(x - native) < 1e-9 else {key: x}
        return plant.override
    if b.p >= b.band.wall_high:
        x = hi if sign > 0 else lo                                 # fail up: full capacity at once
    else:
        g = UP if F > 0 else DOWN
        x = clamp(plant._compass_law_x + sign * g * F * span, lo, hi)
    plant._compass_law_x = x
    plant.override = {} if abs(x - native) < 1e-9 else {key: x}
    return plant.override


# ---- Omni v4: every muscle through its body ---------------------------------------------------------------------
WALL = 0.95                # the compass's high wall (omnicompass/compass_law.py): past it the service is out of its calm
LINE = 1.0                 # the service line itself: a service that hits it ends the trial in flight (the founder's rule 7)


def settle_steps(plant) -> int:
    """Decisions a muscle takes to settle after its knob moves, from the plant's own physics (docs/OMNI_V4_PLAN.md, section
    4, rule 1: samples count only once the muscle is settled): a compute pool's machine start; a process loop's three time
    constants and its dead time; a thermal zone's three time constants (its heat capacity over its loss to outside); a
    storage site or a motion axis answers within its own decision."""
    import math
    P, t = plant.P, plant.template
    dt = float(P.get("dt", 15.0))
    if t == "compute_pool":
        return max(1, int(P.get("startup_steps", 1)))
    if t == "process_loop":
        return max(1, math.ceil((3.0 * P.get("tau", dt) + P.get("theta", 0.0)) / dt))
    if t == "thermal_zone":
        return max(1, math.ceil(3.0 * P["c_j_k"] / P["ua"] / dt))
    return 1


def step_cost(plant, dw, de):
    """One decision's cost on the plant's own work, lower is better: the energy that decision drew per unit of work done
    in it (a storage site's grid draw counted from minus its connection's limit, so a decision that exports reads cheaper
    and never below zero). None when no work was done (nothing measured)."""
    if plant.template == "energy_storage":
        de = de + plant.P["p_lim_w"] * plant.P["dt"]
    if dw <= 0 or de <= 0:
        return None
    return de / dw


def saves(plant, key) -> bool:
    """Whether giving this knob back can lower the plant's energy per unit of work at all, by the plant's own figures
    (MECHANISM_OF_ACTION 9.6), read at every decision: a power cap only where the machine is not racing to idle
    (capping_saves), an effort cap only where the copper it saves outweighs the longer move (effort_cap_saves), a speed
    knob only where the axis has room to stretch its moves (speed_slack); a cooling cap moves heat later, never away, and a
    battery's power cap defers its draw, never saves it, and a process loop draws what its demand needs, so a cap on its
    actuator or power saves only where it binds, that is, only by not delivering. Everything else given back (a machine or
    a unit handed back, a setpoint toward its calm end) draws less. This is the brain's own reading of what the plant
    shows, never a hold: where the figures say a step cannot save, there is nothing to try."""
    t = plant.template
    if t == "process_loop" and key in ("power", "capacity"):
        return False                       # a loop draws what its demand needs: a cap that binds saves only by not delivering
    if key == "power":
        if t == "compute_pool":
            return capping_saves(plant)
        if t == "motion_axis":
            return effort_cap_saves(plant)
        return False
    if key == "capacity" and t == "motion_axis":
        return speed_slack(plant)
    return True


def give_back(plant, knob, proposal):
    """The part of the law's proposal on one copy that gives back (less capacity, power or cooling than native, where the
    plant's own figures say it saves); {} otherwise. Omni v4 never buys service with energy: where the law would spend
    beyond native, the copy stays at native, which is always free, and its own controller answers the stress."""
    if not proposal:
        return {}
    lv = lever(plant, knob)
    if lv is None:
        return {}
    key, native, lo, hi, sign = lv
    if key == "release":
        return dict(proposal)
    x = proposal.get(key)
    if x is None or sign * (x - native) >= 0.0:
        return {}
    return dict(proposal) if saves(plant, key) else {}


class Gate:
    """The muscle's body (omnicompass/body.py, Omni v4): one muscle, one step from native, "the law gives back", for every
    copy of that muscle at once (a muscle in a ten-copy organism is the same muscle ten times: it is proven on all ten, so
    the proof sharpens with the size of the fleet, as a fleet's operator would prove it).

      what is tried   only what the law gives back where the plant's own figures say it saves (give_back); never a spend
                      beyond native: native is always free, and nothing is made worse to make one thing better
      the trial       interleaves native and the law's give-back block by block (omnicompass/verdict.py), every copy in
                      the same block; each block's first decisions are left out while the muscle settles (settle_steps).
                      Every copy's work counts in every block, a copy the law held at native for its own safety included,
                      so whatever the trial does to any copy is in its measurement
      the judgement   the law may give back only where the muscle's whole cost (its energy per unit of work times its
                      service, the index's arithmetic on one plant) is proven lower at 99.9%, and neither part of it is
                      worse beyond the muscle's own wobble; proven again on the recheck and taken back when it no longer
                      pays
      calm            a give-back is asked for, and its trial runs, only while the muscle is calm (its copies on average
                      inside their compass); a copy outside its own calm is held at native that moment
      the wall        an organism at its own line ends the trial in flight"""

    def __init__(self, plants, knob, block=20, recheck=120):
        plants = list(plants) if isinstance(plants, (list, tuple)) else [plants]
        n = max(1, len(plants))
        self.knob = knob
        self.settle = settle_steps(plants[0])
        # native stands at 1 and the law's give-back at 0: one step down from native, so the body's give-back rules hold
        self.muscle = Muscle("law", 1, 1, (0, 1), min_samples=block * n, probe_every=1, recheck=recheck,
                             max_trial=4 * block + self.settle, incremental=False, gain=True)
        self.body = Body([self.muscle], name=getattr(plants[0], "template", "muscle"))
        self.prev = [(p.m["work"], p.m["energy_j"]) for p in plants]
        self.acc = [(0.0, 0.0)] * n                       # work and energy since the copy's last finished piece of work
        self.at = 1                                       # where the muscle stood for the decision just measured
        self.block_seen, self.settling = None, 0

    def step(self, plants, proposals, wall=False):
        """Once a decision, before the plants step: proposals are the overrides the law wants now, one per copy; returns
        the override each copy gets (the law's give-back where the muscle may give back and the copy is calm; native
        otherwise)."""
        single = not isinstance(plants, (list, tuple))
        if single:
            plants, proposals = [plants], [proposals]
        v = self.muscle.verdicts["give back"]
        if v.block_no != self.block_seen:                 # the knob moved to a new block: let the muscle settle
            self.block_seen, self.settling = v.block_no, self.settle
            self.acc = [(0.0, 0.0)] * len(plants)
        whole, energy, service, pos = [], [], [], []
        for i, plant in enumerate(plants):
            w, e = plant.m["work"], plant.m["energy_j"]
            if w < self.prev[i][0]:                      # the meters started again (the end of the learning period)
                self.prev[i] = (0.0, 0.0)
            dw, de = w - self.prev[i][0], e - self.prev[i][1]
            self.prev[i] = (w, e)
            p = position(plant)
            pos.append(p)
            aw, ae = self.acc[i]
            aw, ae = aw + dw, ae + de
            c = step_cost(plant, aw, ae)
            if c is None:
                self.acc[i] = (aw, ae) if aw <= 0 else (0.0, 0.0)
                continue
            self.acc[i] = (0.0, 0.0)
            svc = 1.0 + max(0.0, p)
            whole.append(c * svc)
            energy.append(c)
            service.append(svc)
        if self.settling > 0:
            self.settling -= 1
        elif whole:
            self.body.observe(whole, benefit=whole, parts={"energy": energy, "service": service}, at={"law": self.at})
        offers = [give_back(pl, self.knob, pr) if p < WALL else {} for pl, pr, p in zip(plants, proposals, pos)]
        asking = sum(1 for o in offers if o) / len(offers)
        calm = sum(pos) / len(pos) < WALL
        out = self.body.tick({"law": {"force": -asking, "give_ok": asking > 0, "wanted": 0}}, wall=bool(wall), calm=calm)
        self.at = out.get("law", 1)
        res = [o if self.at <= 0 else {} for o in offers]
        return res[0] if single else res
