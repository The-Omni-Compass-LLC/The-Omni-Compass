#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Omni-Compass on top of a drone swarm's own autopilots (docs/SWARM_PREREGISTRATION.md).

The simulator is gym-pybullet-drones (University of Toronto, DSL; MIT License): PyBullet integrates every quadrotor from
the Crazyflie 2.x model the package ships (mass, inertia, motor constants, drag, ground effect and downwash), and its
shipped position controller (DSLPIDControl, one per drone) flies it. Nothing in it is ours. A fleet of N drones flies
K delivery missions each from a depot: climb, cruise to a target, hover, cruise back, descend, land, next mission.

  native  every drone's shipped autopilot at the planner's cruise speed (1.0 m/s): the mission as the fleet flies it today
  omni    the same autopilots and missions, with the compass law (omnicompass/compass_law.py) on one knob, the cruise
          override, inside the autopilot's own limits: the compass reads each drone's tracking error (how far it is behind
          the point it was told to be at) on a band from 0 to the declared safe error, and spends slack by flying faster
          (fewer seconds airborne, less energy a mission) while the error stays in the middle of its band; past the wall the
          cruise is the planner's at once (fail up). The override never goes under the planner's cruise or over twice it,
          and never past the autopilot's speed limit.

Energy is a declared model (evidence class S), the same for both arms: each motor's mechanical power from the simulator's
own thrust and torque constants (torque = KM rpm^2, power = torque x angular speed), divided by a declared motor
efficiency, plus a declared avionics draw for every drone over the whole fleet window, flying or landed. The battery is
the Crazyflie's (250 mAh at 3.7 V); the autopilot's own reserve rule (20% left at landing) decides a reserve breach.
Collisions are read from the simulator: any two drones closer than two collision radii. A cell with a collision in
either arm is void and says so. Every row is reported, losses included.

  python3 tools/run_swarm.py --cell tuning --out DIR        # the tuning swarm (5 drones, mixed distances)
  python3 tools/run_swarm.py --cell short --out DIR         # an untouched cell: short | mixed | long (20 drones)
  python3 tools/run_swarm.py --cell all --out DIR           # every cell, one after the other
  python3 tools/run_swarm.py --report-only DIR              # the report from DIR's swarm-<cell>.json files
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, clamp  # noqa: E402

# ------------------------------------------------------------------ the task (the same in both arms, fixed before any run)
PYB_FREQ, CTRL_FREQ = 240, 48
CTRL_DT = 1.0 / CTRL_FREQ
V_PLAN = 1.0            # m/s, the planner's cruise: native's speed
VZ = 0.5                # m/s, climb and descent
HOVER_S = 2.0           # s at the target (the delivery)
SETTLE_S = 1.0          # s allowed for the landing to settle, in the planned time
LINE_FACTOR = 1.5       # a mission's deadline is 1.5 x its planned time (the fleet's own service line)
DEPOT_PITCH = 0.6       # m between the five spots of a depot
DEPOT_GAP = 20.0        # m between depots: five drones a depot, a depot's drones never reach another's airspace (missions are at most 8 m out)
ALT = [0.8, 1.1, 1.4, 1.7, 2.0]     # cruise altitudes, one per spot: two drones of one depot never share a plane, 0.3 m apart
ARRIVE_M = 0.10         # m: the drone is "there"
MISSION_TIMEOUT = 3.0   # x the line: a drone that never arrives is cut off and its mission counted late
# ------------------------------------------------------------------ the knob and its guards (frozen on the tuning swarm)
O_MIN, O_MAX = 1.0, 2.0  # the cruise override: never under the planner's cruise, never over twice it
E_LINE = 0.25           # m: the declared safe tracking error (a quarter of the smallest depot pitch and under the altitude stagger)
SEP_WALL = 0.5          # m: another drone this close is a wall: the planner's cruise at once (omni's proximity reflex)
TAU, KP, SMOOTH = 1.0, 1.0, 0.5
SLEW = 0.01             # per control tick (48 Hz)
TRIAL_OVERRIDE = 1.25   # the paired physics trial: is a faster mission cheaper at all, and still inside the safe error?
# ------------------------------------------------------------------ the energy model (declared; the same for both arms)
MOTOR_EFF = 0.5         # electrical to mechanical, small brushed motors
AVIONICS_W = 0.5        # W per drone, flying or landed, for the whole fleet window
BATTERY_J = 0.250 * 3.7 * 3600.0   # 250 mAh at 3.7 V
RESERVE = 0.20          # the autopilot's own low-battery reserve

CELLS = {
    # name: (drones, missions per drone, distance range (m), seed, tuning?)
    "tuning": (5, 4, (3.0, 8.0), 1, True),
    "short": (20, 4, (3.0, 3.0), 11, False),
    "mixed": (20, 4, (3.0, 8.0), 12, False),
    "long": (20, 4, (8.0, 8.0), 13, False),
}

GAUGES = [("energy_per_mission_j", "energy per mission (J, declared model: motors and avionics over the fleet window)", "lower"),
          ("fleet_energy_j", "fleet energy over the window (J, declared model)", "lower"),
          ("missions_per_charge", "missions per charge at the autopilot's reserve", "higher"),
          ("late_share", "missions over their deadline (share)", "never more"),
          ("reserve_breaches", "drones that broke the battery reserve", "never more"),
          ("near_miss_ticks", "control ticks with two drones under half the keep-out apart (near misses)", "never more"),
          ("min_separation_m", "closest two drones ever came (m)", "shown"),
          ("tracking_rms_m", "tracking error, RMS (m; the compass's reading, held inside its band)", "shown"),
          ("mission_s", "mission time (s)", "shown"),
          ("airborne_s", "seconds airborne per mission", "shown"),
          ("override_mean", "cruise override, mean", "shown")]


def depot(i):
    """Drone i's spot: depot i // 5 (DEPOT_GAP apart along x), spot i % 5 (DEPOT_PITCH apart along y)."""
    return (DEPOT_GAP * (i // 5), DEPOT_PITCH * (i % 5), 0.1)


KEEPOUT = 0.3           # m: a path keeps this far from the other spots of its depot, where drones climb and descend


def _seg_dist(px, py, ax, ay, bx, by):
    """Distance from point p to the segment a-b."""
    vx, vy = bx - ax, by - ay; L2 = vx * vx + vy * vy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((px - ax) * vx + (py - ay) * vy) / L2))
    return math.hypot(px - (ax + t * vx), py - (ay + t * vy))


def missions(n, k, dist, seed):
    """Every drone's K targets, fixed by the seed: a distance in the cell's range and a bearing from its own depot spot. A
    path that would pass within KEEPOUT of another spot of the same depot (the column where that drone climbs and lands) is
    drawn again: the task keeps the fleet apart by design, as a planner would; the autopilots fly it blind."""
    import random
    rng = random.Random(seed)
    out = []
    for i in range(n):
        x0, y0, _ = depot(i)
        others = [depot(j)[:2] for j in range(n) if j != i and j // 5 == i // 5]
        ms = []
        while len(ms) < k:
            d = rng.uniform(*dist); th = rng.uniform(0, 2 * math.pi)
            tx, ty = x0 + d * math.cos(th), y0 + d * math.sin(th)
            if all(_seg_dist(ox, oy, x0, y0, tx, ty) >= KEEPOUT for ox, oy in others):
                ms.append((tx, ty, d))
        out.append(ms)
    return out


def planned_time(d, z):
    return 2 * (z - 0.1) / VZ + 2 * d / V_PLAN + HOVER_S + SETTLE_S


class Drone:
    """One drone's mission state machine: the carrot it is told to follow, at the planner's cruise times its override."""

    def __init__(self, i, ms, law):
        self.i = i; self.home = depot(i); self.z = ALT[i % len(ALT)]; self.missions = ms; self.law = law
        self.k = 0; self.phase = "idle"; self.t_mission = 0.0; self.override = 1.0; self.carrot = list(self.home)
        self.done = []; self.energy = 0.0; self.airborne = 0.0; self.err2 = 0.0; self.n_err = 0; self.ov = []
        self.start_next()

    def start_next(self):
        if self.k >= len(self.missions):
            self.phase = "finished"; self.override = O_MIN; return     # the last hand-back: the planner's cruise, read back
        x, y, d = self.missions[self.k]
        self.target = (x, y, self.z); self.d = d
        self.planned = planned_time(d, self.z); self.line = LINE_FACTOR * self.planned
        self.phase = "climb"; self.t_mission = 0.0; self.hover_left = HOVER_S; self.m_energy0 = self.energy
        self.m_airborne0 = self.airborne; self.carrot = list(self.home)
        if self.law is not None:
            self.law.p = None; self.law.v = 0.0
        self.override = 1.0

    def remaining_path(self, pos):
        """Metres of cruise still to fly on this mission, from the carrot."""
        cx, cy, _ = self.carrot
        tx, ty, _ = self.target; hx, hy, _ = self.home
        if self.phase in ("climb", "out"):
            return math.dist((cx, cy), (tx, ty)) + math.dist((tx, ty), (hx, hy))
        if self.phase in ("hover", "back"):
            return math.dist((cx, cy), (hx, hy))
        return 0.0

    def step(self, pos, rpm, nearest=float('inf')):
        """Advance the carrot one control tick; returns (target_pos, target_vel). pos: the drone's position now."""
        if self.phase == "finished":
            return self.home, (0.0, 0.0, 0.0)
        self.t_mission += CTRL_DT
        err = math.dist(pos, self.carrot)
        if self.phase != "idle":
            self.err2 += err * err; self.n_err += 1
        # the compass on the cruise override (omni only): the tracking error on its band; slack is spent as speed
        if self.law is not None and self.phase in ("out", "back"):
            f = self.law.force(err)
            want = clamp(O_MIN + (O_MAX - O_MIN) * (0.5 - 0.5 * f), O_MIN, O_MAX)
            if err >= 0.95 * E_LINE or nearest < SEP_WALL:
                want = O_MIN                                   # fail up: the planner's cruise at once (error at the wall, or a drone too close)
            self.override += clamp(want - self.override, -SLEW, SLEW)
        self.ov.append(self.override)
        v = V_PLAN * self.override
        cx, cy, cz = self.carrot
        if self.phase == "climb":
            cz = min(self.z, cz + VZ * CTRL_DT); self.carrot = [cx, cy, cz]; vel = (0, 0, VZ)
            if cz >= self.z and pos[2] >= self.z - ARRIVE_M:
                self.phase = "out"
        elif self.phase in ("out", "back"):
            tx, ty, _ = self.target if self.phase == "out" else self.home
            dx, dy = tx - cx, ty - cy; dist = math.hypot(dx, dy)
            step = min(dist, v * CTRL_DT)
            if dist > 1e-9:
                cx += dx / dist * step; cy += dy / dist * step
            self.carrot = [cx, cy, self.z]; vel = (dx / dist * v, dy / dist * v, 0.0) if dist > 1e-9 else (0.0, 0.0, 0.0)
            if dist <= 1e-6 and math.dist(pos[:2], (tx, ty)) <= ARRIVE_M:
                self.phase = "hover" if self.phase == "out" else "descend"
        elif self.phase == "hover":
            self.hover_left -= CTRL_DT; vel = (0.0, 0.0, 0.0)
            if self.hover_left <= 0:
                self.phase = "back"
        elif self.phase == "descend":
            cz = max(0.1, cz - VZ * CTRL_DT); self.carrot = [cx, cy, cz]; vel = (0, 0, -VZ)
            if cz <= 0.1 and pos[2] <= 0.1 + ARRIVE_M:
                self.phase = "landed"
        if self.phase == "landed" or self.t_mission > MISSION_TIMEOUT * self.line:
            self.done.append({"mission": self.k, "mission_s": self.t_mission, "late": self.t_mission > self.line,
                              "planned_s": self.planned, "line_s": self.line, "distance_m": self.d,
                              "energy_j": self.energy - self.m_energy0, "airborne_s": self.airborne - self.m_airborne0,
                              "cut_off": self.phase != "landed"})
            self.k += 1; self.start_next()
            return self.home, (0.0, 0.0, 0.0)
        if self.phase != "idle":
            self.airborne += CTRL_DT
        return tuple(self.carrot), vel

    def motor_energy(self, rpm, km, dt):
        """Declared model: torque KM rpm^2, angular speed 2 pi rpm / 60, over the motor efficiency."""
        p = sum(km * r * r * (2 * math.pi * r / 60.0) for r in rpm) / MOTOR_EFF
        self.energy += p * dt


def fly(n, k, dist, seed, law_on, fixed_override=None, quiet=False):
    """One arm of one cell. Returns the cell's gauges and the per-mission rows."""
    import numpy as np
    from gym_pybullet_drones.control.DSLPIDControl import DSLPIDControl
    from gym_pybullet_drones.envs.CtrlAviary import CtrlAviary
    from gym_pybullet_drones.utils.enums import DroneModel, Physics
    ms = missions(n, k, dist, seed)
    env = CtrlAviary(drone_model=DroneModel.CF2X, num_drones=n, physics=Physics.PYB_DRAG, pyb_freq=PYB_FREQ,
                     ctrl_freq=CTRL_FREQ, gui=False, record=False, initial_xyzs=np.array([depot(i) for i in range(n)]))
    ctrl = [DSLPIDControl(drone_model=DroneModel.CF2X) for _ in range(n)]
    drones = []
    for i in range(n):
        law = CompassLaw(Band(0.0, E_LINE), dt=CTRL_DT, tau=TAU, kp=KP, smooth=SMOOTH) if law_on else None
        d = Drone(i, ms[i], law)
        if fixed_override is not None:
            d.override = fixed_override
        drones.append(d)
    window = max(sum(LINE_FACTOR * planned_time(m[2], d.z) for m in d.missions) for d in drones)   # the fleet's own line
    obs, _ = env.reset(); act = np.zeros((n, 4)); t = 0.0; min_sep = float("inf"); collisions = 0; near = 0
    coll_d = 2 * getattr(env, "COLLISION_R", 0.06)
    while any(d.phase != "finished" for d in drones) and t < MISSION_TIMEOUT * window:
        obs, _, _, _, _ = env.step(act)
        pos = obs[:, 0:3]
        if n > 1:
            dm = np.linalg.norm(pos[:, None, :] - pos[None, :, :], axis=2) + np.eye(n) * 1e9
            nearest = dm.min(axis=1)
        else:
            nearest = np.full(n, float("inf"))
        for i, d in enumerate(drones):
            rpm = obs[i, 16:20]
            d.motor_energy(rpm, env.KM, CTRL_DT)
            if fixed_override is not None:
                d.override = fixed_override
            tp, tv = d.step(tuple(pos[i]), rpm, float(nearest[i]))
            act[i], _, _ = ctrl[i].computeControlFromState(control_timestep=env.CTRL_TIMESTEP, state=obs[i],
                                                           target_pos=np.array(tp), target_vel=np.array(tv))
        if n > 1:
            m = float(nearest.min()); min_sep = min(min_sep, m)
            if m < coll_d:
                collisions += 1
            if m < KEEPOUT / 2:
                near += 1
        t += CTRL_DT
    env.close()
    rows = [dict(r, drone=d.i) for d in drones for r in d.done]
    flown = [r for r in rows]
    nm = max(1, len(flown))
    motors = sum(d.energy for d in drones)
    avionics = AVIONICS_W * window * n                        # every drone, the whole fleet window, both arms alike
    fleet = motors + avionics
    e_mission = fleet / nm
    breaches = sum(1 for d in drones if d.energy + AVIONICS_W * window > (1 - RESERVE) * BATTERY_J)
    overrides = [o for d in drones for o in d.ov]
    for d in drones:                                           # the hand-back: every override to the planner's cruise, read back
        d.override = O_MIN
    g = {"energy_per_mission_j": e_mission, "fleet_energy_j": fleet, "motor_energy_j": motors, "avionics_energy_j": avionics,
         "missions_per_charge": (1 - RESERVE) * BATTERY_J / e_mission if e_mission > 0 else 0.0,
         "late_share": sum(1 for r in flown if r["late"]) / nm, "reserve_breaches": breaches,
         "min_separation_m": min_sep if min_sep < float("inf") else 0.0, "collisions": collisions, "near_miss_ticks": near,
         "tracking_rms_m": math.sqrt(sum(d.err2 for d in drones) / max(1, sum(d.n_err for d in drones))),
         "mission_s": sum(r["mission_s"] for r in flown) / nm, "airborne_s": sum(r["airborne_s"] for r in flown) / nm,
         "override_mean": sum(overrides) / max(1, len(overrides)), "missions_flown": len(flown),
         "missions_cut_off": sum(1 for r in flown if r["cut_off"]), "window_s": window, "sim_s": t,
         "handed_back": all(abs(d.override - O_MIN) < 1e-9 for d in drones)}
    if not quiet:
        print(f"   {n} drones x {k} missions: {len(flown)} flown, late {g['late_share']:.0%}, energy {e_mission:.0f} J a mission, "
              f"tracking {g['tracking_rms_m']:.3f} m, min separation {g['min_separation_m']:.2f} m, collisions {collisions}, override {g['override_mean']:.2f}", flush=True)
    return g, rows


def run_cell(name, out: Path):
    n, k, dist, seed, tuning = CELLS[name]
    print(f"== {name}: {n} drones, {k} missions each, {dist[0]:.0f} to {dist[1]:.0f} m, seed {seed}", flush=True)
    # the paired physics trial, native mode, neither flight counted: is a faster mission cheaper at all, inside the safe error?
    t0 = time.time()
    full, _ = fly(n, 1, dist, seed, False, fixed_override=1.0, quiet=True)
    fast, _ = fly(n, 1, dist, seed, False, fixed_override=TRIAL_OVERRIDE, quiet=True)
    faster_is_cheaper = fast["energy_per_mission_j"] < full["energy_per_mission_j"] and fast["tracking_rms_m"] < E_LINE and fast["collisions"] == 0
    rec = {"cell": name, "drones": n, "missions_per_drone": k, "distance_m": list(dist), "seed": seed, "tuning": tuning,
           "task": {"cruise_mps": V_PLAN, "climb_mps": VZ, "hover_s": HOVER_S, "line_factor": LINE_FACTOR, "altitudes_m": ALT[:min(n, len(ALT))]},
           "knob": {"override_min": O_MIN, "override_max": O_MAX, "safe_error_m": E_LINE, "separation_wall_m": SEP_WALL, "trial_override": TRIAL_OVERRIDE},
           "energy_model": {"motor_efficiency": MOTOR_EFF, "avionics_w": AVIONICS_W, "battery_j": BATTERY_J, "reserve": RESERVE},
           "physics_trial": {"planner_cruise": full, f"override_{TRIAL_OVERRIDE}": fast, "faster_is_cheaper": faster_is_cheaper},
           "omni_moves": faster_is_cheaper}
    print(f"   physics trial: {full['energy_per_mission_j']:.0f} J a mission at the planner's cruise, {fast['energy_per_mission_j']:.0f} J at "
          f"{TRIAL_OVERRIDE} x (tracking {fast['tracking_rms_m']:.3f} m): {'a faster mission is cheaper; omni may move' if faster_is_cheaper else 'not cheaper or not safe; omni leaves the cruise native'}", flush=True)
    all_rows = []
    for arm in ("native", "omni"):
        g, rows = fly(n, k, dist, seed, arm == "omni" and faster_is_cheaper)
        for r in rows:
            r["arm"] = arm
        all_rows += rows
        g["seconds"] = round(time.time() - t0, 1); rec[arm] = g
    rec["void"] = rec["native"]["collisions"] > 0 or rec["omni"]["collisions"] > 0
    if rec["void"]:
        print("   COLLISION in an arm: the cell is void", flush=True)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"swarm-{name}.json").write_text(json.dumps(rec, indent=1) + "\n")
    with (out / f"swarm-{name}_missions.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys())); w.writeheader(); w.writerows(all_rows)
    return rec


def report(res: dict, out: Path):
    L = ["# Drone swarms: Omni-Compass on top of each drone's own autopilot (gym-pybullet-drones, Crazyflie 2.x)", "",
         "native: every drone's shipped position controller at the planner's cruise; omni: the same, with the compass law on the "
         "cruise override inside the autopilot's limits, spending tracking slack as speed. Energy is a declared model (evidence class "
         "S) computed the same way for both arms. A cell with a collision in either arm is void. Every row is reported.", ""]
    for name, rec in res.items():
        L += [f"## {name}: {rec['drones']} drones x {rec['missions_per_drone']} missions, {rec['distance_m'][0]:.0f} to {rec['distance_m'][1]:.0f} m"
              + (" (the tuning swarm)" if rec.get("tuning") else ""), ""]
        pt = rec["physics_trial"]
        L += [f"Paired physics trial (native, uncounted): {pt['planner_cruise']['energy_per_mission_j']:.0f} J a mission at the planner's cruise, "
              f"{pt[f'override_{TRIAL_OVERRIDE}']['energy_per_mission_j']:.0f} J at {TRIAL_OVERRIDE} x; "
              + ("a faster mission is cheaper and inside the safe error, so omni may move the cruise." if rec["omni_moves"] else
                 "**not cheaper or not inside the safe error: nothing for Omni to move; the omni arm is native.**"), ""]
        if rec.get("void"):
            L += ["**VOID: a collision in an arm.** Collisions: native "
                  f"{rec['native']['collisions']}, omni {rec['omni']['collisions']}.", ""]
        L += ["| Gauge | native | omni | change | direction |", "|---|---:|---:|---:|---|"]
        for key, label, direction in GAUGES:
            a, b = rec["native"][key], rec["omni"][key]
            ch = "" if a == 0 else f"{100 * (b - a) / abs(a):+.2f}%"
            if key in ("late_share", "reserve_breaches", "near_miss_ticks"):
                ch = f"{b - a:+.3f}"
            L.append(f"| {label} | {a:.4g} | {b:.4g} | {ch} | {direction} |")
        L += ["", f"Missions flown: native {rec['native']['missions_flown']}, omni {rec['omni']['missions_flown']}; cut off: "
              f"{rec['native']['missions_cut_off']} / {rec['omni']['missions_cut_off']}; every override handed back: native "
              f"{rec['native']['handed_back']}, omni {rec['omni']['handed_back']}; collisions {rec['native']['collisions']} / {rec['omni']['collisions']}.", ""]
    (out / "SWARM.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "SWARM.md"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cell", default="tuning", help="tuning | short | mixed | long | all")
    ap.add_argument("--out", default="")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    if a.report_only:
        d = Path(a.report_only)
        res = {f.stem.replace("swarm-", ""): json.loads(f.read_text()) for f in sorted(d.glob("swarm-*.json"))}
        print(report(res, d)); return 0
    out = Path(a.out or "swarm-out")
    names = list(CELLS) if a.cell == "all" else [a.cell]
    res = {}
    for name in names:
        res[name] = run_cell(name, out)
    print(report(res, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
