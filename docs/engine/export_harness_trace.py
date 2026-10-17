# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Records the realms harness, decision by decision, for the live engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html).

The sixty muscles the page draws (twelve from the spine, twelve from each realm, named in MUSCLES below) are put in one
organism of the realms harness (realms/harness.py Body: the plants of realms/plants.py, coupled through their heat and
their power) under the climb, on seeds 3000, 3001 and 3002 (runs A, B and C). Two arms on each seed, the same demand:

  native  the plants and their native controllers alone
  omni    Omni-Compass on top: the max (realms/compass_arm_v5.py max_body_step with the body's Bone, its twins and the
          muscles' cards), exactly as run_bodies runs the arm v5; at 80% of the run the brain goes silent and the lease
          walks every setting back to native over 24 decisions (KILL_AT, WALK)

Every decision it records, for each plant: the service position the law reads (v5_position: 1 or more is past the
line), whether the decision was over the line, whether Omni-Compass held a setting away from native and whether it
wrote one; for the body: its electrical power and the harness's aggregate observation (what a governor would read).
The work each plant did is recorded per decision so the page can show work against native's.

The three-run readings: for each gauge, the paired change per decision, averaged over blocks of ten decisions, with its
95% interval (Student's t over the blocks), in each run; GAIN or LOSS when all three runs point the same way with every
interval clear of zero (the word by the gauge's aim), EVEN when an interval includes zero, "the runs disagree" when clear
runs point different ways (tools/readings.py). Evidence class S. Usage: python3 docs/engine/export_harness_trace.py OUT.json
"""
from __future__ import annotations

import json
import math
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from realms.harness import (Body, KILL_AT, WALK, aggregate, catalog, scale_load, walk_back)   # noqa: E402
from realms.compass_arm_v5 import Bone, V5CFG, max_body_step, v5_position                    # noqa: E402
from realms.presets import ORGANISM_STEPS                                                     # noqa: E402

SEEDS = (3000, 3001, 3002)
MUSCLES = {
    "spine": ["pump_speed", "pdb_policy", "unhealthy_pod_eviction_policy", "memory_high", "cpu_idle_policy", "node_selector",
              "generator_dispatch", "cpu_quota", "ear_cpu_frequency_policy", "expire_after", "memory_limit", "transparent_hugepages"],
    "compute": ["model_replicas", "tls_session_cache", "edge_dispatch", "qubit_mapping", "global_admission", "retry_budget_window",
                "training_precision", "task_preemption", "machine_remediation", "compute_comm_overlap", "memory_ballooning", "checkpoint_trigger"],
    "physics": ["altitude_target", "velocity_target", "force_limit", "px4_mpc_xy_vel_max", "amr_fleet_active_robots", "regen_drive_mode",
                "smart_charging_schedule", "ros2_executor_threads", "motor_thermal_derate", "timetable_recovery_margin", "horizontal_speed_limit", "space_power_budget"],
    "energy": ["chromatography_flow_setpoint", "boiler_steam_pressure_setpoint", "inverter_real_power", "storage_dispatch", "flotation_aeration_rate",
               "mill_speed_target", "heat_pump_staging", "feeder_voltage_target", "controller_mode", "energy_load_shed",
               "heater_outlet_temperature_setpoint", "reserve_dispatch_priority"],
    "distribution": ["lock_timeout", "cache_compression", "dispatch_priority", "shuffle_bandwidth", "broker_failover", "service_timeout",
                     "stage_parallelism", "inventory_allocation", "executor_size", "compensation_action", "gc_budget", "shipment_batch"],
}
T95 = {k: v for k, v in zip(range(1, 31), [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179,
                                          2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064,
                                          2.060, 2.056, 2.052, 2.048, 2.045, 2.042])}


def rows():
    by = {r["muscle"]: r for r in catalog(ROOT / "realms" / "catalog_v5.csv")}
    out = []
    for part, names in MUSCLES.items():
        for n in names:
            r = dict(by[n]); r["part"] = part; out.append(r)
    return out


def run(rs, seed, arm):
    b = Body(rs, seed)
    scale_load(b, "climb")
    n, kill_at = len(b.plants), int(KILL_AT * ORGANISM_STEPS)
    bone = Bone(b, V5CFG) if arm == "omni" else None
    last = [None] * n
    rec = {"p": [], "over": [], "held": [], "wrote": [], "work": [], "power_kw": [], "obs": []}
    prev_viol, prev_work = [0] * n, [0.0] * n
    for k in range(ORGANISM_STEPS):
        b.couple()
        wrote = [0] * n
        if arm == "omni":
            if k >= kill_at:
                for p in b.plants:
                    walk_back(p, kill_at + WALK - k)
            else:
                bone.advance_twin()
                max_body_step(b, V5CFG, bone)
                for i, p in enumerate(b.plants):
                    v = p.override
                    if v and v != last[i]:
                        wrote[i] = 1
                    last[i] = dict(v)
        b.step()
        ps, ov, wk = [], [], []
        for i, p in enumerate(b.plants):
            ps.append(round(min(2.0, max(-0.5, v5_position(p))), 3))
            ov.append(p.m["viol"] - prev_viol[i]); prev_viol[i] = p.m["viol"]
            wk.append(p.m["work"] - prev_work[i]); prev_work[i] = p.m["work"]
        o = aggregate([b])
        rec["p"].append(ps); rec["over"].append(ov); rec["wrote"].append(wrote)
        rec["held"].append([1 if p.override else 0 for p in b.plants]); rec["work"].append(wk)
        rec["power_kw"].append(round(b.all_w / 1000.0, 3))
        rec["obs"].append({k2: round(o[k2], 4) for k2 in ("queue_ratio", "load_ratio", "power_stress", "thermal",
                                                         "network_stress", "drift_ratio")})
    return rec


def blocks(xs, size=10):
    return [sum(xs[i:i + size]) / size for i in range(0, len(xs) - size + 1, size)]


def interval(d):
    b = blocks(d)
    m = st.mean(b)
    half = T95[len(b) - 1] * st.stdev(b) / math.sqrt(len(b))
    return m, m - half, m + half


def gauges(nat, omn):
    """The per-decision gauges, native and omni, for one seed."""
    steps, n = len(nat["p"]), len(nat["p"][0])
    tot_nat = [max(sum(nat["work"][k][i] for k in range(steps)), 1e-12) for i in range(n)]
    def work(rec):
        return [sum(rec["work"][k][i] / (tot_nat[i] / steps) for i in range(n)) / n for k in range(steps)]
    return {
        "work": (work(nat), work(omn), "up"),
        "over": ([sum(x) for x in nat["over"]], [sum(x) for x in omn["over"]], "down"),
        "spread": ([st.pstdev([min(p, 1.5) for p in x]) for x in nat["p"]], [st.pstdev([min(p, 1.5) for p in x]) for x in omn["p"]], "shown"),
        "power": (nat["power_kw"], omn["power_kw"], "spent"),
    }


def reading(per_run, aim):
    """The three-run rule on the per-run intervals [(mean, lo, hi)]."""
    if aim == "shown":
        return "shown"          # a gauge no rule of the engine aims at: its change is shown, never judged
    clear = [(lo > 0) or (hi < 0) for _, lo, hi in per_run]
    if not all(clear):
        return "EVEN"
    signs = {m > 0 for m, _, _ in per_run}
    if len(signs) > 1:
        return "the runs disagree"
    rose = signs.pop()
    if aim == "shown":
        return "shown"
    if aim == "spent":
        return "power given" if rose else "GAIN"
    return "GAIN" if (rose if aim == "up" else not rose) else "LOSS"


def pack(rec, n):
    """The page's compact form: positions as int16 thousandths and three flags a byte (1 over the line, 2 a setting held
    away from native, 4 a write), each base64; the body's power, the aggregate observation, and the work index."""
    import base64, array
    pos = array.array("h", [int(round(max(-0.5, min(2.0, x)) * 1000)) for row in rec["p"] for x in row])
    fl = bytes((1 if o else 0) | (2 if h else 0) | (4 if w else 0)
               for ro, rh, rw in zip(rec["over"], rec["held"], rec["wrote"]) for o, h, w in zip(ro, rh, rw))
    return {"p": base64.b64encode(pos.tobytes()).decode(), "f": base64.b64encode(fl).decode(), "kw": rec["power_kw"],
            "obs": [[o["queue_ratio"], o["load_ratio"], o["power_stress"], o["thermal"], o["network_stress"], o["drift_ratio"]]
                    for o in rec["obs"]]}


def main(out):
    rs = rows()
    data = {"muscles": [{"name": r["muscle"], "family": r["family"], "part": r["part"], "template": r["template"],
                         "knob": r["knob"], "id": r["muscle_id"]} for r in rs],
            "steps": ORGANISM_STEPS, "kill_at": int(KILL_AT * ORGANISM_STEPS), "walk": WALK, "seeds": list(SEEDS),
            "runs": {}, "readings": {}}
    per = {}
    for s in SEEDS:
        nat, omn = run(rs, s, "native"), run(rs, s, "omni")
        g = gauges(nat, omn)
        pn, po = pack(nat, len(rs)), pack(omn, len(rs))
        pn["wk"], po["wk"] = [round(x, 6) for x in g["work"][0]], [round(x, 6) for x in g["work"][1]]
        data["runs"][str(s)] = {"native": pn, "omni": po}
        for key, (a, b, aim) in g.items():
            d = [y - x for x, y in zip(a, b)]
            m, lo, hi = interval(d)
            base = st.mean(a) or 1e-12
            per.setdefault(key, {"aim": aim, "runs": []})["runs"].append(
                {"seed": s, "native": st.mean(a), "omni": st.mean(b), "change": m / base, "lo": lo / base, "hi": hi / base})
    for key, v in per.items():
        v["reading"] = reading([(r["change"], r["lo"], r["hi"]) for r in v["runs"]], v["aim"])
    data["readings"] = per
    Path(out).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    for key, v in per.items():
        print(f"{key:7s} {v['reading']:18s} " + "  ".join(f"{r['change']*100:+.4f}% [{r['lo']*100:+.4f}, {r['hi']*100:+.4f}]" for r in v["runs"]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "harness_trace.json")
