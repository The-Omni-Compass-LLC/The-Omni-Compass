# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""Omni-Compass on top of a robot arm's own position servos, in MuJoCo (docs/ROBOTICS_PREREGISTRATION.md).

MuJoCo (Google DeepMind) integrates the arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the
position servos the model ships with. The task is a pick-and-place cycle between fixed joint-space waypoints scaled to
each robot's own ranges, played as a minimum-jerk trajectory with a planned duration, under a time line (the slowest
cycle the task allows). Arms:
  native  the shipped servo tracks the trajectory at its planned speed (speed override 1.0)
  omni    the same servo and trajectory, with the compass law (omnicompass/compass_law.py) on one knob, the speed override,
          read from the cycle's time margin: with slack the override eases down (gentler motion, less torque, less
          energy); as the margin shrinks it comes back up; past the wall it is full speed at once. Guards: override in
          [0.5, 1.0], at most 0.01 per control tick (100 Hz), handed back to 1.0 at the end of every cycle and read back.
Before the counted cycles, one paired trial in native mode (a cycle at override 1.0 and one at 0.8, neither counted) asks
the robot's own figures whether a slower cycle costs less energy at all, standing draw included; if it does not, the
override is left native for that robot and the result reads "nothing for Omni to move".
Energy is a declared model, the same for both arms, from MuJoCo's own joint torques and velocities: mechanical work
|torque x velocity|, copper loss torque^2 x C (C declared per robot), and a standing draw (declared per robot) drawn for
the whole takt (the time line), moving or waiting, as a robot on a line is: the unit is energy per takt. The planned speed
is set per robot, before any Omni run, as the fastest at which the robot's own servo tracks the task within 0.05 rad. Every
cycle's record is written; the report (MUJOCO.md) reads the preregistration's directions.
  python3 tools/run_mujoco.py --menagerie DIR --robots franka_emika_panda --cycles 100 --out out
  python3 tools/run_mujoco.py --report-only DIR --out DIR
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
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, clamp

CTRL_DT = 0.01            # the control tick (100 Hz)
SEG_S = 2.0               # planned seconds per trajectory segment, the starting point of each robot's feasibility calibration
SPAN = 0.25               # waypoints 25% of each joint's own range either side of home, capped at MAX_OFFSET: a brisk pick-and-place, the
MAX_OFFSET = 0.6          # same for every arm (rad; a model whose joints turn fully would otherwise be asked for 90-degree swings)
WAYPOINTS = 4             # segments per cycle (the last returns home)
LINE_FACTOR = 1.5         # the time line: the slowest cycle the task allows, as a multiple of the planned cycle
OVERRIDE_MIN, OVERRIDE_MAX, OVERRIDE_MID = 0.5, 1.0, 0.75
SLEW = 0.01               # the override moves at most this much per control tick
TRIAL_OVERRIDE = 0.8      # the paired physics trial's slower cycle
TRACK_OK = 0.05           # rad RMS: the task is feasible for the robot's own servo when native tracks within this
# the declared energy model per robot: copper coefficient C in W per (N m)^2 at the joint (R / (k_t N)^2 for a geared
# motor; 0.01 is a 1-ohm, 0.1 N m/A motor behind a 100:1 gear), and the standing draw in W, the same in both arms
MODEL = {"franka_emika_panda": {"copper_w_per_nm2": 0.01, "idle_w": 60.0, "note": "idle about 60 W per the maker's datasheet class"},
         "universal_robots_ur5e": {"copper_w_per_nm2": 0.01, "idle_w": 90.0, "note": "idle about 90 W per the maker's datasheet class"},
         "kuka_iiwa_14": {"copper_w_per_nm2": 0.01, "idle_w": 100.0, "note": "declared"},
         "kinova_gen3": {"copper_w_per_nm2": 0.01, "idle_w": 36.0, "note": "idle about 36 W per the maker's datasheet class"}}
DEFAULT_MODEL = {"copper_w_per_nm2": 0.01, "idle_w": 100.0, "note": "declared default"}
SCENES = {"franka_emika_panda": "scene.xml", "universal_robots_ur5e": "scene.xml", "kuka_iiwa_14": "scene.xml", "kinova_gen3": "scene.xml"}


def minimum_jerk(s):
    """The minimum-jerk profile from 0 to 1 over phase s in [0, 1]."""
    return 10 * s ** 3 - 15 * s ** 4 + 6 * s ** 5


class Arm:
    """A Menagerie arm with its shipped position servos: which actuators drive joints, their ranges, the home pose."""

    def __init__(self, menagerie: Path, robot: str):
        import mujoco
        self.mujoco = mujoco
        d = menagerie / robot
        xml = d / SCENES.get(robot, "scene.xml")
        if not xml.exists():
            xml = next(p for p in sorted(d.glob("*.xml")) if "mjx" not in p.name and "scene" not in p.name)
        self.model = mujoco.MjModel.from_xml_path(str(xml))
        self.data = mujoco.MjData(self.model)
        m = self.model
        self.act = [i for i in range(m.nu) if m.actuator_trntype[i] == mujoco.mjtTrn.mjTRN_JOINT]   # joint servos only
        if not self.act:
            raise RuntimeError("the model ships no joint servos (no joint-transmission actuators)")
        self.joint = [int(m.actuator_trnid[i][0]) for i in self.act]
        self.qadr = [int(m.jnt_qposadr[j]) for j in self.joint]
        self.vadr = [int(m.jnt_dofadr[j]) for j in self.joint]
        lo = [float(m.actuator_ctrlrange[i][0]) if m.actuator_ctrllimited[i] else float(m.jnt_range[j][0]) for i, j in zip(self.act, self.joint)]
        hi = [float(m.actuator_ctrlrange[i][1]) if m.actuator_ctrllimited[i] else float(m.jnt_range[j][1]) for i, j in zip(self.act, self.joint)]
        self.lo, self.hi = lo, hi
        if m.nkey > 0:
            mujoco.mj_resetDataKeyframe(m, self.data, 0)
            home = [float(self.data.qpos[a]) for a in self.qadr]
        else:
            home = [(a + b) / 2 for a, b in zip(lo, hi)]
        self.home = [clamp(h, a, b) for h, a, b in zip(home, lo, hi)]
        self.substeps = max(1, int(round(CTRL_DT / m.opt.timestep)))
        # waypoints scaled to each joint's own range: a quarter of the span either side of home, alternating per joint
        span = [(b - a) for a, b in zip(lo, hi)]
        pattern = [(1, -1, 0.5, -0.5), (-1, 1, -0.5, 0.5), (0.5, -0.5, 1, -1)]
        self.waypoints = []
        for k in range(WAYPOINTS - 1):
            w = [clamp(self.home[j] + pattern[j % 3][k] * min(SPAN * span[j], MAX_OFFSET), lo[j], hi[j]) for j in range(len(self.act))]
            self.waypoints.append(w)
        self.waypoints.append(list(self.home))         # the last segment returns home

    def target(self, phase):
        """The trajectory's joint targets at phase in [0, WAYPOINTS)."""
        k = min(int(phase), WAYPOINTS - 1); s = minimum_jerk(clamp(phase - k, 0.0, 1.0))
        a = self.waypoints[k - 1] if k > 0 else self.home; b = self.waypoints[k]
        return [x + (y - x) * s for x, y in zip(a, b)]

    def reset(self):
        self.mujoco.mj_resetData(self.model, self.data)
        if self.model.nkey > 0:
            self.mujoco.mj_resetDataKeyframe(self.model, self.data, 0)
        for i, a, h in zip(self.act, self.qadr, self.home):
            self.data.qpos[a] = h; self.data.ctrl[i] = h
        self.mujoco.mj_forward(self.model, self.data)

    def tick(self, targets):
        """One control tick: write the servo targets, step the physics, return torque and velocity per joint."""
        for i, t in zip(self.act, targets):
            self.data.ctrl[i] = t
        for _ in range(self.substeps):
            self.mujoco.mj_step(self.model, self.data)
        tau = [float(self.data.actuator_force[i]) for i in self.act]
        vel = [float(self.data.qvel[v]) for v in self.vadr]
        pos = [float(self.data.qpos[a]) for a in self.qadr]
        return tau, vel, pos


def cycle(arm: Arm, params: dict, law: CompassLaw | None, seg: float, line: float, fixed_override: float | None = None):
    """One pick-and-place cycle at seg planned seconds per segment; returns its gauges. law None: native (override
    fixed_override or 1.0). At the end the override is handed back to 1.0 and read back."""
    phase, t, override = 0.0, 0.0, (fixed_override if fixed_override is not None else 1.0)
    mech = copper = 0.0; peak = 0.0; tau_abs = 0.0; n = 0; err2 = 0.0; wp_err = []; overrides = []
    next_wp = 1
    while phase < WAYPOINTS:
        if law is not None:
            projected = t + (WAYPOINTS - phase) * seg / override
            f = law.force(projected)
            want = clamp(OVERRIDE_MID + (OVERRIDE_MAX - OVERRIDE_MID) * f, OVERRIDE_MIN, OVERRIDE_MAX)
            if projected >= line:
                want = OVERRIDE_MAX                             # a cycle that would miss its line runs full speed
            override += clamp(want - override, -SLEW, SLEW)
        phase = min(WAYPOINTS, phase + CTRL_DT * override / seg)
        targets = arm.target(phase)
        tau, vel, pos = arm.tick(targets)
        t += CTRL_DT; n += 1
        for a, v in zip(tau, vel):
            mech += abs(a * v) * CTRL_DT
            copper += a * a * params["copper_w_per_nm2"] * CTRL_DT
            peak = max(peak, abs(a)); tau_abs += abs(a)
        err2 += sum((p - q) ** 2 for p, q in zip(pos, targets)) / len(targets)
        overrides.append(override)
        if phase >= next_wp and next_wp <= WAYPOINTS:
            w = arm.waypoints[next_wp - 1]
            wp_err.append(math.sqrt(sum((p - q) ** 2 for p, q in zip(pos, w)) / len(w))); next_wp += 1
        if t > line * 3:
            break                                               # never spin forever
    standing = params["idle_w"] * line                        # drawn for the whole takt, moving or waiting, in both arms
    override_at_end = override
    override = 1.0                                             # the hand-back: the knob goes back to native's value, read back
    return {"cycle_s": t, "over_line": t > line, "override_at_end_of_motion": override_at_end, "energy_j": mech + copper + standing, "mechanical_j": mech, "copper_j": copper,
            "standing_j": standing, "peak_torque_nm": peak, "mean_abs_torque_nm": tau_abs / max(1, n * len(arm.act)),
            "tracking_rms_rad": math.sqrt(err2 / max(1, n)), "waypoint_err_rad": sum(wp_err) / max(1, len(wp_err)),
            "override_mean": sum(overrides) / max(1, len(overrides)), "override_after_handback": override}


def feasible_segment(arm: Arm, params: dict):
    """The planned seconds per segment for this robot: the fastest, in steps of 0.5 s from SEG_S, at which the robot's own
    servo tracks the task within TRACK_OK (RMS) in native mode; the task is then one the native servo can do. None when
    no speed up to 4 x SEG_S does: the robot's own servo cannot do the task, and it is listed as such."""
    g = None
    for seg in [SEG_S + 0.5 * k for k in range(int(6 * SEG_S) + 1)]:
        arm.reset(); g = cycle(arm, params, None, seg, LINE_FACTOR * WAYPOINTS * seg, 1.0)
        if g["tracking_rms_rad"] <= TRACK_OK:
            return seg, g["tracking_rms_rad"]
    return None, g["tracking_rms_rad"] if g else None


def run_robot(menagerie: Path, robot: str, cycles: int, out: Path):
    arm = Arm(menagerie, robot)
    params = MODEL.get(robot, DEFAULT_MODEL)
    seg, track0 = feasible_segment(arm, params)
    if seg is None:
        raise RuntimeError(f"the robot's own servo cannot track the task at any planned speed up to {4 * SEG_S:.0f} s per segment "
                           f"(RMS tracking {track0:.3f} rad at the slowest); the task is not feasible for it as modelled")
    planned = WAYPOINTS * seg; line = LINE_FACTOR * planned
    # the paired physics trial, in native mode, neither cycle counted: is a slower cycle cheaper at all, standing draw in?
    arm.reset(); full = cycle(arm, params, None, seg, line, 1.0)
    arm.reset(); slow = cycle(arm, params, None, seg, line, TRIAL_OVERRIDE)
    slower_is_cheaper = slow["energy_j"] < full["energy_j"]
    rec = {"robot": robot, "joints": len(arm.act), "planned_s": planned, "line_s": line, "segment_s": seg, "native_tracking_at_planned_speed": track0,
           "energy_model": params,
           "physics_trial": {"full_speed": full, f"override_{TRIAL_OVERRIDE}": slow, "slower_is_cheaper": slower_is_cheaper},
           "omni_moves": slower_is_cheaper}
    rows = []
    for name in ("native", "omni"):
        law = None
        if name == "omni" and slower_is_cheaper:
            law = CompassLaw(Band(planned, line), dt=CTRL_DT, tau=0.5, kp=1.0, smooth=0.3)
        per = []
        t0 = time.time()
        for c in range(cycles):
            arm.reset()
            if law is not None:
                law.p = None; law.v = 0.0
            g = cycle(arm, params, law, seg, line)
            g["cycle"] = c; g["arm"] = name; per.append(g); rows.append(g)
        n = len(per)
        agg = {k: sum(p[k] for p in per) / n for k in ("cycle_s", "energy_j", "mechanical_j", "copper_j", "standing_j", "peak_torque_nm",
                                                           "mean_abs_torque_nm", "tracking_rms_rad", "waypoint_err_rad", "override_mean")}
        agg["over_line_share"] = sum(1 for p in per if p["over_line"]) / n
        agg["handed_back"] = all(abs(p["override_after_handback"] - 1.0) < 1e-9 for p in per)
        agg["override_at_end_of_motion"] = sum(p["override_at_end_of_motion"] for p in per) / n
        agg["cycles"] = n; agg["seconds"] = round(time.time() - t0, 1)
        rec[name] = agg
        print(f"== {robot} {name}: {n} cycles, {agg['cycle_s']:.2f} s each, energy {agg['energy_j']:.1f} J, tracking {agg['tracking_rms_rad']:.4f} rad", flush=True)
    if not slower_is_cheaper:
        print(f"== {robot}: the paired trial says a slower cycle is not cheaper (standing draw dominates); omni leaves the override native", flush=True)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{robot}.json").write_text(json.dumps(rec, indent=1) + "\n")
    with (out / f"{robot}_cycles.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    return rec


GAUGES = [("energy_j", "energy per takt (J, declared model: motion plus the standing draw for the whole takt)", "lower"), ("copper_j", "copper loss per cycle (J, declared model)", "lower"),
          ("mechanical_j", "mechanical work per cycle (J)", "lower"), ("standing_j", "standing draw per takt (J, declared model; the same in both arms)", "lower"),
          ("peak_torque_nm", "peak joint torque (N m)", "lower"), ("mean_abs_torque_nm", "mean |torque| (N m)", "lower"),
          ("cycle_s", "cycle time (s)", "shown"), ("over_line_share", "cycles over the time line (share)", "never more"),
          ("tracking_rms_rad", "tracking error, RMS (rad)", "never more"), ("waypoint_err_rad", "end-point error at the waypoints (rad)", "never more"),
          ("override_mean", "speed override, mean", "shown")]


def report(res: dict, out: Path):
    L = ["# Omni-Compass on top of a robot arm's own servos (MuJoCo, MuJoCo Menagerie)", "",
         "MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the "
         "position servos the model ships with. Native: that servo tracks a pick-and-place cycle at its planned speed. Omni: the "
         "same servo and trajectory with the compass law on the speed override, inside the cycle's time line "
         "(`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in "
         "both arms. Evidence class: S, our model on an independent simulator. Every row is shown, losses included.", ""]
    for robot, r in sorted(res.items()):
        if "error" in r:
            L += [f"## {robot}", "", f"could not run: `{r['error']}`", ""]; continue
        n, o = r["native"], r["omni"]
        L += [f"## {robot}: {r['joints']} joints, {n['cycles']} cycles per arm, planned {r['planned_s']:.0f} s (segment {r.get('segment_s', SEG_S):.1f} s, "
              f"the fastest the robot's own servo tracks within {TRACK_OK} rad: {r.get('native_tracking_at_planned_speed', 0):.4f}), takt {r['line_s']:.0f} s", "",
              f"The task: {WAYPOINTS} segments between joint-space waypoints {int(SPAN * 100)}% of each joint's own range either side of home (at most {MAX_OFFSET} rad), "
              f"a minimum-jerk trajectory; the same for both arms.", "",
              f"Paired physics trial (native mode, not counted): a cycle at full speed cost {r['physics_trial']['full_speed']['energy_j']:.1f} J, at override "
              f"{TRIAL_OVERRIDE} {r['physics_trial'][f'override_{TRIAL_OVERRIDE}']['energy_j']:.1f} J, standing draw {r['energy_model']['idle_w']} W included: "
              + ("a slower cycle is cheaper, so omni moves the override." if r["omni_moves"] else
                 "**a slower cycle is not cheaper, so omni leaves the override native: nothing for Omni to move.**"), "",
              f"Omni handed the override back at the end of every cycle: {'yes' if o.get('handed_back') else 'NO'}.", "",
              "| Gauge | native | omni | Change | Reading |", "|---|---:|---:|---:|---|"]
        for k, name, d in GAUGES:
            a, b = n[k], o[k]
            ch = (b - a) / abs(a) if a else None
            if d == "shown":
                rd = "shown"
            elif ch is None:
                rd = "same" if b == a else ("WORSE" if b > a else "better")
            elif abs(ch) < 1e-6:
                rd = "same"
            elif d == "never more":
                rd = "WORSE: more" if ch > 0 else "better"
            else:
                rd = "WORSE" if ch > 0 else "better"
            L.append(f"| {name} | {a:.4g} | {b:.4g} | {'' if ch is None else f'{100 * ch:+.2f}%'} | {rd} |")
        L.append("")
    (out / "MUJOCO.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--menagerie", default="menagerie")
    ap.add_argument("--robots", default="")
    ap.add_argument("--cycles", type=int, default=10)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = {}
    if a.report_only:
        for f in sorted(Path(a.report_only).glob("*.json")):
            res[f.stem] = json.loads(f.read_text())
    for robot in [r for r in a.robots.split(",") if r]:
        try:
            res[robot] = run_robot(Path(a.menagerie), robot, a.cycles, out)
        except Exception as e:                                   # a robot an arm cannot run is reported, never left out
            res[robot] = {"robot": robot, "error": f"{type(e).__name__}: {e}"[:600]}
            print(f"== {robot}: ERROR {res[robot]['error']}", flush=True)
            (out / f"{robot}.json").write_text(json.dumps(res[robot], indent=1) + "\n")
    report(res, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
