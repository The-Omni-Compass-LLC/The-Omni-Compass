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


def step_cost(plant, dw, de):
    """One decision's cost on the plant's own work, lower is better: the energy that decision drew per unit of work done
    in it (a storage site's grid draw counted from minus its connection's limit, so a decision that exports reads cheaper
    and never below zero). None when no work was done (nothing measured)."""
    if plant.template == "energy_storage":
        de = de + plant.P["p_lim_w"] * plant.P["dt"]
    if dw <= 0 or de <= 0:
        return None
    return de / dw


class Gate:
    """The muscle's body (omnicompass/body.py, Omni v4): one muscle, one step from native, "the law acts". Its trial
    interleaves native and the law's own setting block by block (omnicompass/verdict.py). Nothing anywhere is made worse to
    make one thing better: the law may act only where the plant's whole cost (its energy per unit of work times its
    service, the index's arithmetic on one plant) is proven lower at 99.9%, and neither part of it, the energy per unit of
    work nor the service, is worse beyond the plant's own wobble. It is proven again on the recheck and taken back when it
    no longer pays. A plant past its wall (or an organism at its own) ends the trial in flight and holds the muscle where
    it has proven."""

    def __init__(self, plant, block=20, recheck=120):
        self.muscle = Muscle("law", 0, 1, (0, 1), min_samples=block, probe_every=1, recheck=recheck, max_trial=4 * block,
                             incremental=False, gain=True)
        self.body = Body([self.muscle], name=getattr(plant, "template", "muscle"))
        self.prev = (plant.m["work"], plant.m["energy_j"])
        self.acting = 0

    def step(self, plant, proposal, wall=False):
        """Once a decision, before the plant steps: proposal is the override the law wants now; returns the override
        the plant gets (the law's, where the muscle may act; native otherwise)."""
        w, e = plant.m["work"], plant.m["energy_j"]
        dw, de = w - self.prev[0], e - self.prev[1]
        self.prev = (w, e)
        p = position(plant)
        c = step_cost(plant, dw, de)
        if c is not None:
            svc = 1.0 + max(0.0, p)
            whole = c * svc
            self.body.observe([whole], benefit=[whole], parts={"energy": [c], "service": [svc]}, at={"law": self.acting})
        out = self.body.tick({"law": {"force": 1.0 if proposal else 0.0, "spend_ok": bool(proposal), "wanted": 1}},
                             wall=bool(wall) or p >= LINE, calm=p < WALL)
        self.acting = out.get("law", 0)
        return dict(proposal) if (self.acting >= 1 and proposal) else {}
