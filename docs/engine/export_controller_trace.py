# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Records the shipped live controller (omni_controller/controller.py) on the toy cluster, tick by tick, for the live
engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html): the one place where the brain drives the muscles, decision by
decision (the governor's six states, the nerves and each organ's grant, the compass law on the service, the verdict's
trial, the release gate, the plug's writes).

Two settings, each as the repository already wires it, on seeds 3000, 3001 and 3002 (runs A, B and C), six hours each,
the controller deciding every 15 s, its own default (omni-v16: every clock counted in seconds; docs/OMNI_V16.md):

  selfpilot  pilot/selfpilot.py's plant: the HPA with the Cluster Autoscaler (native) against the controller in nodepool
             mode on top of the HPA, the Cluster Autoscaler off, the controller's own defaults (the max)
  cloud      tools/toy_gate.py's cloud (cloud_toy: the shipped actuator's idle machines, every pod on its machine), the
             cloud's setting: the cloud's own autoscaler makes and deletes machines in both arms; the controller (the
             compass law, the tune-down, --give-back-only) only parks a machine that exists, after its verdict's trial and
             above its warm reserve (nothing given back before the reserve's four hours are read), and wakes it on a breach

Every 15 s tick, both arms: machines in service, booting or parked, the pods the HPAs want and the pods waiting for a
place, the demand, and the response time of a queue on the running pods (the toy gate's own formula, computed the same
in both arms). Every decision of the controller: its audit records (decision, authority, compass, verdict, writes).
Readings: the paired change per tick over blocks of 40 ticks (ten minutes), Student's t, in each run; the three-run rule.
Evidence class S. Usage: python3 docs/engine/export_controller_trace.py OUT.json
"""
from __future__ import annotations

import json
import math
import statistics as st
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import numpy as np                                                       # noqa: E402
from fleet.sim import ALLOC                                              # noqa: E402
from pilot.selfpilot import SimCluster, SimKube                          # noqa: E402
from omni_controller.controller import Controller, parser               # noqa: E402
from tools.toy_gate import cloud_toy                                     # noqa: E402

SEEDS = (3000, 3001, 3002)
DAYS = 0.25
INTERVAL = 15.0                                                          # the controller's own default decision period (omni-v16)
SLO_MS, SERVICE_MS = 200.0, 20.0                                         # the toy gate's line and bare service time


def observe(sim, lat_rows, lat_path, rng):
    """One tick's record, and the toy gate's probe file (the requests of this 15 s, timed on the running pods)."""
    c, p = sim.c, sim.c.pool
    frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
    cap = sum(w.replicas * w.request * frac for w in c.workloads)
    t = min(sim.t, len(c.workloads[0].demand) - 1)
    dem = sum(w.demand[t] for w in c.workloads)
    backlog = sum(w.backlog for w in c.workloads)
    rho = min(0.98, dem / cap) if cap > 0 else 0.98
    mean = SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
    if lat_path is not None:
        t0 = sim.t * 15.0
        for i in range(20):
            lat_rows.append((t0 + i * 0.75, float(mean * rng.lognormal(0.0, 0.25))))
        del lat_rows[:-1200]
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{a:.2f},{b:.3f},1\n" for a, b in lat_rows)
    pend = int(sum(w.replicas - int(w.replicas * frac) for w in c.workloads))
    return {"nodes": p.nodes, "boot": len(p.booting), "parked": len(getattr(sim, "parked", [])),
            "pods": int(sum(w.replicas for w in c.workloads)), "pending": pend, "demand": round(dem, 3),
            "ms": round(min(mean, 5000.0), 1), "kw": round(sim.rows[-1][-1] / 1000.0, 3) if sim.rows else 0.0}


def digest(recs):
    """The decision's audit records, cut to what the page draws."""
    out = {"writes": 0}
    for r in recs:
        if "write" in r:
            out["writes"] += 1
        if "decision" in r and isinstance(r["decision"], dict):
            d = r["decision"]
            out.update(E=round(d.get("E", 0), 4), U=round(d.get("U", 0), 4), rec=d.get("nodes_recommended"), seen=d.get("nodes_observed"),
                       rho=d.get("hpa_target_recommended"), q=d.get("queue_ratio"), law=d.get("law"))
            cl = d.get("compass_law")
            if cl:
                out.update(cp=cl["position"], cv=cl["velocity"], cF=cl["force"], cc=cl["center"], cw=cl["wall"], vs=cl["verdict_state"], va=cl["machines_given_back_allowed"])
        if "authority" in r:
            a = r["authority"]
            out.update(calm=a["calm"], sc=a["scalars"], gate=a["node_gate"]["reason"], gate_ok=a["node_gate"]["ok"],
                       contract={k: v for k, v in a["contract"].items() if k in ("pods", "nodes", "cpufreq", "gpu", "power", "routing")})
        if "verdict" in r and isinstance(r["verdict"], dict):
            out["verdict"] = r["verdict"].get("verdict")
        if "idle_floor" in r:
            out["idle"] = r["idle_floor"]
        if "cruise" in r:
            out["cruise"] = r["cruise"]
    return out


def run(setting, seed, arm):
    tmp = Path(tempfile.mkdtemp())
    rng = np.random.default_rng(seed + 7)
    if setting == "cloud":
        sim, kube, _ = cloud_toy(seed, DAYS)
    else:
        sim = SimCluster(seed, DAYS, autoscaler="ca" if arm == "native" else "none")
    ticks, decisions, lat_rows = [], [], []
    lat_path = tmp / "latency.csv" if setting == "cloud" else None
    if arm == "native":
        while sim.t < sim.steps:
            sim.tick(); ticks.append(observe(sim, lat_rows, lat_path, rng))
        return ticks, decisions
    audit = tmp / "audit.jsonl"
    if setting == "cloud":
        argv = ["--mode", "nodepool", "--law", "compass", "--dial", "save", "--sensed", "none/none", "--interval", str(INTERVAL),
                "--latency-file", str(lat_path), "--slo-ms", str(SLO_MS), "--audit", str(audit), "--kill-file", str(tmp / "kill"),
                "--node-scale-cmd", "SIMSCALE {n}", "--min-nodes", str(sim.c.pool.min_nodes), "--max-nodes", str(sim.c.pool.max_nodes),
                "--headroom", "0.5", "--active-nodes-only", "--max-node-step", "1", "--floor-interval", "15", "--give-back-only"]
        ctl = Controller(parser().parse_args(argv), kube=kube)
    else:
        argv = ["--mode", "nodepool", "--interval", str(INTERVAL), "--floor-interval", "15", "--audit", str(audit), "--kill-file", str(tmp / "kill"),
                "--node-scale-cmd", "SIMSCALE {n}", "--min-nodes", str(sim.c.pool.min_nodes), "--max-nodes", str(sim.c.pool.max_nodes),
                "--headroom", "0.5"]
        ctl = Controller(parser().parse_args(argv), kube=SimKube(sim, None)); ctl.k.audit = ctl.audit   # pilot/selfpilot.py's own SimKube
    real_run = subprocess.run

    def fake_run(cmd, *k, **kw):
        if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
            sim.resize(int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
        return real_run(cmd, *k, **kw)
    seen = 0
    every = max(1, int(round(INTERVAL / 15.0)))                         # a decision every INTERVAL s on the 15 s plant
    with mock.patch("omni_controller.controller.subprocess.run", side_effect=fake_run):
        while sim.t < sim.steps:
            sim.tick()
            sim.c.alloc = (sim.c.pool.nodes + len(getattr(sim, "parked", []))) * sim.c.pool.cores * ALLOC
            ticks.append(observe(sim, lat_rows, lat_path, rng))
            if sim.t % every == 0:
                ctl.step()
                lines = audit.read_text().splitlines() if audit.exists() else []
                recs = [json.loads(x) for x in lines[seen:]]; seen = len(lines)
                decisions.append(dict(digest(recs), tick=sim.t))
            else:
                ctl.floor_step()
    return ticks, decisions


from omnicompass.student_t import t95 as _t95    # noqa: E402  (the exact two-sided 95% point of Student's t, omni-v9)
GAUGES = {"machines": ("spent", lambda t: t["nodes"] + t["boot"] + t["parked"]), "pending": ("down", lambda t: t["pending"]),
          "ms": ("down", lambda t: t["ms"]), "over": ("down", lambda t: 1.0 if t["ms"] > SLO_MS else 0.0), "kw": ("spent", lambda t: t["kw"])}


def reading(runs, aim):
    """The three-run rule as the tables read it (tools/confirm_abc.py verdict): clear runs pointing different ways disagree,
    whatever the others read; then any run whose interval holds zero makes the row EVEN; else the word by the gauge's aim."""
    if not runs:
        return "EVEN"
    clear = [r for r in runs if r["lo"] > 0 or r["hi"] < 0]
    if len({r["change"] > 0 for r in clear}) > 1:
        return "the runs disagree"
    if len(clear) < len(runs):
        return "EVEN"
    up = clear[0]["change"] > 0
    if aim == "spent":
        return "power given" if up else "GAIN"
    return "GAIN" if (up if aim == "up" else not up) else "LOSS"


def main(out):
    data = {"slo_ms": SLO_MS, "seeds": list(SEEDS), "days": DAYS, "interval_s": INTERVAL, "settings": {}}
    for setting in ("selfpilot", "cloud"):
        sec = {"runs": {}, "readings": {}}
        per = {}
        for sd in SEEDS:
            nt, _ = run(setting, sd, "native")
            ot, dec = run(setting, sd, "omni")
            sec["runs"][str(sd)] = {"native": nt, "omni": ot, "decisions": dec}
            for g, (aim, f) in GAUGES.items():
                a, b = [f(t) for t in nt], [f(t) for t in ot]
                d = [y - x for x, y in zip(a, b)]
                bl = [sum(d[i:i + 40]) / 40 for i in range(0, len(d) - 39, 40)]
                m = st.mean(bl); half = _t95(len(bl) - 1) * st.stdev(bl) / math.sqrt(len(bl))
                base = st.mean(a) or 1e-12
                per.setdefault(g, {"aim": aim, "runs": []})["runs"].append({"seed": sd, "native": st.mean(a), "omni": st.mean(b),
                                                                             "change": m / base, "lo": (m - half) / base, "hi": (m + half) / base})
        for g, v in per.items():
            v["reading"] = reading(v["runs"], v["aim"])
            print(f"{setting:9s} {g:8s} {v['reading']:18s} " + "  ".join(f"{r['change']*100:+.2f}% [{r['lo']*100:+.2f},{r['hi']*100:+.2f}]" for r in v["runs"]))
        sec["readings"] = per
        data["settings"][setting] = sec
    Path(out).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "controller_trace.json")
