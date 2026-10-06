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
    """(override key, native value, low, high, sign): sign +1 when a higher value is more capacity."""
    P, t = plant.P, plant.template
    if knob == "admission":
        return None
    if t == "compute_pool":
        if knob == "power":
            return ("power", 1.0, 0.4, 1.0, 1) if capping_saves(plant) else None
        if P.get("ca"):
            return ("release", None, 0, 0, 0)
        return None                                            # the HPA target is held at the operator's own
    if t == "thermal_zone":
        if knob == "setpoint":
            return ("setpoint", P["t_set"], min(P["stress"], P["calm"]), max(P["stress"], P["calm"]), -1)
        if knob == "capacity":
            return ("release", None, 0, 0, 0)
        # the cooling power cap gives nothing back: the heat the zone makes must leave it either way, so a lower cap only
        # lets the temperature drift up while the PI command grows and stages more units (and their fans). Native
        # (MECHANISM_OF_ACTION 9.6)
        return None
    if t == "energy_storage":
        if knob == "setpoint" and P.get("backup"):
            return None                                        # a backup reserve (a UPS) is kept for an outage: native
        if knob == "setpoint":
            # the reserve may go down to the stress end (the battery given to the site under strain), never above the
            # operator's own: a kWh held back in a calm battery is a kWh bought from the grid (MECHANISM_OF_ACTION 9.6)
            return ("setpoint", P["reserve"], min(P["stress"], P["reserve"]), P["reserve"], -1)
        return None                                            # a battery's power limit gives nothing back: native
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
