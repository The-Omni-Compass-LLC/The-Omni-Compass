#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The toy gate: every change to the engine or a live controller runs here first, in our own models (evidence class S),
against the engine that stands, on the same seeds, before any real run is started (the founder's order of 15 October,
night). A change goes on to real runs only where it reads no LOSS here and shows promise; a LOSS here is root-caused and
fixed in the model, never carried into a real run. A reading here is a model's, never a benchmark's result.

  python3 tools/toy_gate.py --base <checkout> --cand <checkout> [--seeds 1-8] [--days 1] [--toys cluster,cluster15,cluster_blink,verdict]

Each checkout is a working tree: one on the engine that stands, one on the candidate. Each runs in its own process with
its own code, so the two never share a module.

  cluster    the shipped Kubernetes controller in the cloud's setting (node-pool mode, the compass law, the tune-down,
             nothing sensed but the machines; --give-back-only where the checkout has it) on the toy cluster of
             pilot/selfpilot.py: the fleet harness's web workload, the HPA at its target, a node's boot delay, power;
             a decision every 60 s and the fast check every 15 s. Response times come from a queue on the running pods
             (an M/M/1 delay on each pod's share, log-normal spread, the backlog's wait added). Native is the HPA with
             the Cluster Autoscaler on the same demand.
  cluster15  the same with a decision every 15 s: each rule's time at a shorter period.
  cluster_blink  the cluster toy with every machine out of service in the governor's reading for two minutes every six
             hours while the cluster serves on (the kind cluster of the CruiseKube test, 18 October): a decision or a
             check that fails is recorded and skipped, as the shipped loop does.
  verdict   the do-no-harm trigger (omnicompass/verdict.py) on noisy work: how often a give-back step that truly costs
             0 to 5% more is allowed against a 2% allowance, the candidate's verdict against the standing one, at 20 and at
             200 pieces of work a decision (slow work, and work fast enough to read a 2% step in a trial's time).
  card, card_floor  the checkout's own GPU governor (omni_controller/gpu_governor.py, cap mode, its defaults) on the
             modelled card of tools/gpu_physics_sim.py, written into this file so both engines meet one model: the card
             whose voltage falls with its clock (gamma 3) and the card near its voltage floor (gamma 1.5), under Poisson
             work at 30 to 80% of capacity for 600 s; native is the card's own firmware at its start limit (omni-v15).

Gauges per seed (a day each): machine-hours, energy per used core-hour, pending-pod minutes an hour, HPA shortfall
minutes an hour, the 95th-percentile response time, alert minutes (minutes whose 95th percentile is over the line), and
the brain's request for the power cap: its moves, its reversals and its travel over the day (omni-v15; never written in
the cloud setting). The card toys read the requests served and not served, the 95th and 99th percentiles, the card's
energy and peak temperature, and the power limit's writes, moves, reversals and travel in watts.
The candidate is read against the standing engine paired by seed: the mean change, its 95% interval over the seeds
(Student's t), and the word by the gauge's aim (tools/readings.py): a fall in time waited, missed or over the line is a
GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given; an interval across zero is EVEN.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLO_MS = 200.0                       # the toy service's line
SERVICE_MS = 20.0                    # the bare service time of one request
SAMPLES_PER_TICK = 20                # requests timed every 15 s
BLINK_EVERY, BLINK = 1440, (700, 708)  # the blink toy: two minutes (8 ticks of 15 s) out of service every six hours
# after the checkout under test (a worker's PYTHONPATH), never before it: placed first, the gate's own tree shadowed the
# checkout and both arms ran the gate tree's engine (18 October; from omni-v9's gate of 17 October on). Every worker now
# names the tree its engine was imported from, and run() refuses a reading taken on the wrong one
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
try:   # the readings' table, keyed by degrees of freedom (the table it replaced was keyed by seeds and read one row early);
    from omnicompass.student_t import T95  # noqa: E402
except ImportError:   # a worker on a checkout from before omni-v9 has none, and needs none: only the parent reads
    T95 = None
# gauge -> (aim, a resource spent?)
GAUGES = {"machine_hours": ("lower", True), "kwh_per_core_hour": ("lower", True),
          "pending_pod_minutes_per_hour": ("lower", False), "hpa_shortfall_minutes_per_hour": ("lower", False),
          "p95_ms": ("lower", False), "alert_minutes": ("lower", False),
          # the brain's request for the power cap over the day (omni-v15): how often it moved, how often it turned back the
          # other way, and how far it travelled in all; wear on the part that would obey it, a resource held (a fall is a
          # cut, a rise is power given). In the cloud setting the request is never written; native asks for none
          "power_cap_moves": ("lower", True), "power_cap_reversals": ("lower", True), "power_cap_travel": ("lower", True)}


def cap_wear(caps):
    """A request's wear over a run: moves (a change from one decision to the next), reversals (a move the other way from
    the move before it) and travel (the sizes of the moves, summed)."""
    moves = [b - a for a, b in zip(caps, caps[1:]) if b != a]
    return {"power_cap_moves": float(len(moves)), "power_cap_travel": float(sum(abs(m) for m in moves)),
            "power_cap_reversals": float(sum(1 for a, b in zip(moves, moves[1:]) if (a > 0) != (b > 0)))}


# the cluster toys: (the standing engine's decision period, the candidate's, the 5-second plant, the blink). The first three
# run both engines at one period; the x60 toys run the candidate at its own default against the standing engine at its own
# (omni-v14: 15 s against 60 s, and 10 s against 60 s on the 5-second plant, where a decision every 10 s falls on a step)
CLUSTER_TOYS = {"cluster": (60.0, 60.0, False, False), "cluster15": (15.0, 15.0, False, False),
                "cluster_blink": (60.0, 60.0, False, True), "cluster15x60": (60.0, 15.0, False, False),
                "cluster_blink15x60": (60.0, 15.0, False, True), "fine60": (60.0, 60.0, True, False),
                "fine15x60": (60.0, 15.0, True, False), "fine10x60": (60.0, 10.0, True, False),
                "fine15": (15.0, 15.0, True, False), "fine10": (10.0, 10.0, True, False)}


# ---- the worker: one arm, one seed, run inside one checkout --------------------------------------------------------
def cloud_toy(seed, days, fine=False, blink=False):
    """The cloud toy's plant and the cluster as its API shows it, for the worker and for the live engine's controller trace
    (docs/engine/export_controller_trace.py): (sim, kube, STEP_S). The actuator is the shipped one (CloudSim below)."""
    from pilot.selfpilot import SimCluster, SimKube
    from fleet.harness import hpa_step
    from fleet.sim import ALLOC, _cluster_autoscaler
    IDLE = "omnicompass.io/idle"
    # the plant's step: the harness's 15 s, or 5 s in the fine plant (omni-v16's gate: a decision every 10 s, and every
    # period that divides the minute, falls on a step; the autoscaler and the cloud's autoscaler still sync every 15 s)
    SUB = 3 if fine else 1
    STEP_S = 15.0 / SUB

    class CloudSim(SimCluster):
        """The cloud as the governor meets it (scripts/kind_bench.sh, the cloud setting): the cloud's own autoscaler
        makes machines and deletes an unneeded one, in every arm; the governor only marks a machine that exists idle
        and wakes it, and never adds one. An idle machine is the shipped actuator's (scripts/kind_nodepool.sh, omni-v14's
        gate): marked PreferNoSchedule, Ready, powered and billed; no pod is moved off it; a pod that finds the open
        machines full lands on it at once; once it carries no work it stands empty for the cloud's scale-down time and
        is deleted. (Until omni-v14 the toy took an idle machine's room away at once, as if drained, which the actuator
        never does: pods waited there that wait nowhere on a real cluster.)"""
        PARK_TICKS = 40 * SUB                                  # ten minutes: the autoscaler's scale-down-unneeded time

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.c.pool.power_off = True                       # a machine the cloud scales down is deleted, not kept
            self.parked = []                                   # idle machines, carrying ones first: steps left once empty
            self.u = 0                                         # plant steps taken
            self.steps = self.steps * SUB
            self.acc = {}                                      # each workload's busy share over the autoscaler's 15 s

        def tick(self):
            c, p = self.c, self.c.pool
            t = self.u // SUB                                  # the harness's 15 s demand sample
            sync = (self.u + 1) % SUB == 0                     # this step closes a 15 s window: the autoscalers' sync
            if self.u % SUB == 0:                              # boots count in the harness's 15 s steps (BOOT_TICKS)
                p.booting = [b - 1 for b in p.booting]; p.nodes += sum(1 for b in p.booting if b <= 0)
                p.booting = [b for b in p.booting if b > 0]
            cap = p.cores * ALLOC
            alloc = (p.nodes + len(self.parked)) * cap         # every Ready machine: the idle ones take pods once the open are full
            reqs = sum(w.replicas * w.request for w in c.workloads)
            frac = min(1.0, alloc / reqs) if reqs > 0 else 1.0
            used = 0.0
            for w in c.workloads:
                capw = w.replicas * w.request * frac
                srv = min(w.demand[t] / SUB + w.backlog, capw / SUB)   # a step carries 1/SUB of the 15 s work
                w.backlog = w.demand[t] / SUB + w.backlog - srv; used += srv * SUB
                self.acc.setdefault(w.name, []).append(min(1.0, srv * SUB / max(w.replicas * w.request, 1e-9)))
            c.pending, c.reqs, c.alloc, c.used = max(0.0, reqs - alloc), reqs, alloc, used
            # the idle machines carrying pods (the requests past the open machines' room) stay in service, their clock
            # reset; the empty ones count down to the cloud's own scale-down
            carrying = min(len(self.parked), int(math.ceil(max(0.0, reqs - p.nodes * cap) / cap - 1e-9)))
            self.parked = [self.PARK_TICKS] * carrying + [x - 1 for x in self.parked[carrying:] if x > 1]
            util = min(1.0, used / max(alloc, 1e-9))
            kw = ((p.nodes + len(self.parked)) * (p.idle_kw + p.dyn_kw * util) + len(p.booting) * p.idle_kw) * self.scn.pue
            pending_pods = int(sum(max(0, w.replicas - int(w.replicas * frac)) for w in c.workloads))
            cur = sum(w.replicas for w in c.workloads)
            if sync:
                for w in c.workloads:
                    got = self.acc.pop(w.name, None) or [w.metric]
                    w.metric = sum(got) / len(got)             # the window the autoscaler reads
                    before = w.replicas; hpa_step(w, w.target); w.desired = w.replicas; w.current = before
                if self.autoscaler == "ca":
                    # the cloud's autoscaler: a pod that finds no room even on the idle machines starts one; an unneeded
                    # open machine leaves after its ten minutes (an idle one leaves by its own clock above)
                    c.alloc = p.nodes * cap
                    _cluster_autoscaler(c)
                    c.alloc = alloc
            self.rows.append(["", self.u * STEP_S, p.nodes + len(self.parked), p.nodes + len(self.parked) + len(p.booting),
                              int(alloc / ALLOC * 1000), int(reqs * 1000), int(used * 1000), pending_pods, len(c.workloads),
                              cur, sum(w.desired for w in c.workloads), kw * 1000])
            self.u += 1
            self.t = self.u // SUB

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting) + len(self.parked)

        def resize(self, n):
            p = self.c.pool; n = max(p.min_nodes, int(n))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [self.PARK_TICKS] * k
            elif n > p.nodes:
                # those still carrying work first: they are warm (scripts/kind_nodepool.sh)
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

    sim = CloudSim(seed, days, autoscaler="ca")

    def placed():
        """Every running pod on its machine, as the API shows it: the open machines filled first, then the idle ones (a
        pod lands on an idle machine only when the open ones are full); the rest wait, with no machine."""
        c, p = sim.c, sim.c.pool
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = p.cores * ALLOC
        names = [f"n{i}" for i in range(p.nodes)] + [f"n{p.nodes + j}" for j in range(len(sim.parked))]
        room = [cap] * len(names); out_ = []; i = 0
        for w in c.workloads:
            run = int(w.replicas * frac)
            for _ in range(run):
                while i < len(names) - 1 and room[i] < w.request - 1e-9:
                    i += 1
                if names:
                    room[i] -= w.request
                out_.append((w, names[i] if names else None))
            out_ += [(w, None)] * (w.replicas - run)
        return out_, names, room

    class Kube(SimKube):
        def get(self, *args):
            if args[:2] == ("get", "nodes"):                    # in service, then idle-marked until the cloud deletes them
                p = self.sim.c.pool
                node = lambda i, taints: {"metadata": {"name": f"n{i}", "labels": {}},
                                          "spec": {"taints": taints}, "status": {"allocatable": {"cpu": str(p.cores)},
                                          "conditions": [{"type": "Ready", "status": "True"}]}}
                # the blink (omni-v11): four times a day every machine in service leaves service for two minutes in the
                # governor's reading, while the toy cluster serves on, as the kind cluster of the CruiseKube test did on 18
                # October (run 39120444653, repetition 8)
                out_now = blink and BLINK[0] <= self.sim.t % BLINK_EVERY < BLINK[1]
                gone = [{"key": "node.kubernetes.io/unreachable", "effect": "NoSchedule"}] if out_now else []
                return {"items": [node(i, list(gone)) for i in range(p.nodes)]
                        + [node(p.nodes + j, [{"key": IDLE, "effect": "PreferNoSchedule"}]) for j in range(len(self.sim.parked))]}
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                pend = sum(w.replicas - int(w.replicas * frac) for w in c.workloads)
                return "\n".join(f"pod/p{i}" for i in range(pend))
            if args[:2] == ("get", "pods"):                     # every pod with its machine, as the API shows it
                cpu = lambda w: f"{int(w.request * 1000)}m"
                return {"items": [{"metadata": {"name": f"p{k}", "namespace": "default", "ownerReferences": [{"kind": "ReplicaSet"}]},
                                   "spec": {"nodeName": nm, "containers": [{"resources": {"requests": {"cpu": cpu(w)}}}]} if nm else
                                           {"containers": [{"resources": {"requests": {"cpu": cpu(w)}}}]},
                                   "status": {"phase": "Running" if nm else "Pending"}} for k, (w, nm) in enumerate(placed()[0])]}
            if args[:2] == ("top", "nodes"):                    # each machine's use, by the requests placed on it
                c, p = self.sim.c, self.sim.c.pool
                pods, names, room = placed()
                cap = p.cores * ALLOC
                load_ = {nm: cap - r for nm, r in zip(names, room)}
                tot = sum(load_.values()) or 1.0
                return "\n".join(f"{nm} {int(c.used * load_[nm] / tot * 1000)}m 1% 1Gi 1%" for nm in names if load_[nm] > 1e-9)
            if args[:2] == ("get", "hpa"):                      # the HPA as Kubernetes shows it: its range and target
                hp = super().get(*args)
                for h, w in zip(hp["items"], self.sim.c.workloads):
                    h["spec"].update({"minReplicas": int(w.min_rep), "maxReplicas": int(w.max_rep),
                                      "scaleTargetRef": {"kind": "Deployment", "name": w.name}})
                return hp
            if args[:2] == ("get", "deployment"):
                w = next(x for x in self.sim.c.workloads if x.name == args[2])
                cpu = f"{int(w.request * 1000)}m"
                return {"metadata": {"name": w.name, "namespace": "default", "annotations": {}},
                        "spec": {"replicas": int(w.replicas), "selector": {"matchLabels": {"app": w.name}},
                                 "template": {"metadata": {"labels": {"app": w.name}}, "spec": {"containers": [
                                     {"name": "app", "resources": {"requests": {"cpu": cpu}, "limits": {"cpu": cpu}}}]}}},
                        "status": {"replicas": int(w.replicas), "readyReplicas": int(w.replicas)}}
            try:
                return super().get(*args)
            except ValueError:
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not in the toy cluster")

    return sim, Kube(sim, None), STEP_S


def worker(arm, seed, days, period, out, blink=False, fine=False):
    import csv
    from unittest import mock
    import numpy as np
    from pilot.score import blocks, load
    from fleet.sim import ALLOC
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    # a fresh audit every run: the governor appends to its audit, so a folder left by an earlier, interrupted gate would
    # carry that run's records into this one's counts (21 October: a container restart left half-written audits, and the
    # next gate appended to them)
    (out / "audit.jsonl").unlink(missing_ok=True)
    rng = np.random.default_rng(seed + 7)
    sim, k, STEP_S = cloud_toy(seed, days, fine, blink)
    SUB = int(round(15.0 / STEP_S))
    billed = []
    lat_path = out / "latency.csv"
    lat_rows, minute_ms, p95s = [], {}, []

    def time_requests():
        """The requests of this step, timed on the pods running now (the same queue in every arm): SAMPLES_PER_TICK
        every 15 s, spread over the step's own seconds."""
        c = sim.c
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = sum(w.replicas * w.request * frac for w in c.workloads)
        dem = sum(w.demand[min(sim.t, len(w.demand) - 1)] for w in c.workloads)
        backlog = sum(w.backlog for w in c.workloads)
        rho = min(0.98, dem / cap) if cap > 0 else 0.98
        mean = SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
        t0 = sim.u * STEP_S
        k = sim.u % SUB
        n = int(round((k + 1) * SAMPLES_PER_TICK / SUB)) - int(round(k * SAMPLES_PER_TICK / SUB))
        for i in range(n):
            ms = float(mean * rng.lognormal(0.0, 0.25))
            lat_rows.append((t0 + i * STEP_S / n, ms))
            minute_ms.setdefault(int(t0 // 60), []).append(ms)
        del lat_rows[:-60 * SAMPLES_PER_TICK]                  # the probe file keeps the last 15 minutes
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{t:.2f},{ms:.3f},1\n" for t, ms in lat_rows)

    if arm != "native":
        from omni_controller.controller import Controller, parser
        argv = ["--mode", "nodepool", "--law", "compass", "--dial", "save", "--sensed", "none/none",
                "--interval", str(period), "--latency-file", str(lat_path), "--slo-ms", str(SLO_MS),
                "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"), "--node-scale-cmd", "SIMSCALE {n}",
                "--min-nodes", str(sim.c.pool.min_nodes), "--max-nodes", str(sim.c.pool.max_nodes), "--headroom", "0.5",
                "--active-nodes-only", "--max-node-step", "1", "--floor-interval", str(STEP_S)]
        p = parser()
        if any("--give-back-only" in getattr(x, "option_strings", []) for x in p._actions):
            argv.append("--give-back-only")
        a = p.parse_args(argv)
        ctl = Controller(a, kube=k)
        real_run = subprocess.run

        def fake_run(cmd, *kw_a, **kw):
            if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
                sim.resize(int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, *kw_a, **kw)
        every = max(1, int(round(period / STEP_S)))
        from omni_controller import controller as shipped
        fails = 0
        with mock.patch("omni_controller.controller.subprocess.run", side_effect=fake_run):
            while sim.u < sim.steps:
                sim.tick(); sim.c.alloc = (sim.c.pool.nodes + len(sim.parked)) * sim.c.pool.cores * ALLOC
                time_requests(); billed.append(sim.billed())
                # the shipped loop's own handling (omni_controller.controller.main): a failed decision is recorded and
                # skipped, a failed floor check recorded, and the next one comes on time
                if sim.u % every == 0:
                    fails = shipped.safe_step(ctl, fails)
                else:
                    try:
                        ctl.floor_step()
                    except Exception as e:
                        ctl.audit({"error": "floor check: " + repr(e)[:500], "stderr": ""})
    else:
        while sim.u < sim.steps:
            sim.tick(); time_requests(); billed.append(sim.billed())
    cap = out / "capture.csv"; sim.write_capture(cap)
    rows = load(str(cap))
    day = blocks(rows, 86400 * days + 60, None, None)[0]                # one block: the whole run
    hours = sum(billed) * STEP_S / 3600.0                               # the bill: every machine that exists
    allm = sorted(ms for v in minute_ms.values() for ms in v)
    alert = sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > SLO_MS)
    res = {"machine_hours": hours, "kwh_per_core_hour": day["kwh_per_core_hour"],
           "pending_pod_minutes_per_hour": day["pending_pod_minutes_per_hour"],
           "hpa_shortfall_minutes_per_hour": day["hpa_shortfall_minutes_per_hour"],
           "p95_ms": allm[int(0.95 * len(allm))], "alert_minutes": alert,
           "power_cap_moves": 0.0, "power_cap_reversals": 0.0, "power_cap_travel": 0.0}
    if arm != "native":
        recs = [json.loads(l) for l in open(out / "audit.jsonl")]
        res.update(cap_wear([float(r["decision"]["power_cap"]) for r in recs
                             if isinstance(r.get("decision"), dict) and "power_cap" in r["decision"]]))
        ev = [r["verdict"].get("verdict", "") for r in recs if isinstance(r.get("verdict"), dict)]
        res["steps_allowed"] = sum(1 for v in ev if v == "step allowed")
        res["steps_refused"] = sum(1 for v in ev if v.startswith("step refused"))
        res["trials_abandoned"] = sum(1 for v in ev if v.startswith("trial abandoned"))
        res["machines_parked"] = sum(1 for r in recs if r.get("write", [None])[0] == "SIMSCALE")
        res["errors"] = sum(1 for r in recs if "error" in r)
        res["readings_held"] = sum(1 for r in recs if str(r.get("decision", "")).startswith("held"))
        res["engine_tree"] = engine_tree("omni_controller.controller")
    print(json.dumps(res))


# ---- the conveyance toy: one kind host, the checkout's own conveyance code ------------------------------------------
# the toy host's calibration, set so the native arm sits where the v6 KEDA run's native arm did (results/live/raw/addons-run-
# 38725705826: host busy mean 0.27 and p95 0.42, response p50 91 ms and p95 248 ms, the HPA's replicas), see docs/OMNI_V7.md
CAL = {"cost_s": 0.06, "clients": 1.0, "think_s": 0.05, "other_cores": 0.55, "loadgen_s": 0.004}
CAL.update(json.loads(os.environ.get("TOY_CAL", "{}")))        # a heavier or lighter load for one run, without a code change
CONVEY_GAUGES = {"requests_served": ("higher", False), "start_wait_s": ("lower", False), "start_wait_p95_s": ("lower", False), "p95_ms": ("lower", False),
                 "alert_minutes": ("lower", False), "host_busy": ("lower", True), "limit_given_m": ("lower", True),
                 "pod_seconds": ("lower", True), "writes": ("lower", True)}
# the batch muscle beside the serving one (omni-v13's gate, 20 October): the stream of KubeRay's rig with the organism
# alone (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 7): 24 jobs, one every 30 s, each ten pods run five at a time,
# every pod requesting 500m with a 1-core limit and hashing a fixed amount of work. BATCH_POD_CORE_S is set so the native
# arm's queue finishes where the saturated runners' did (the 16 KubeRay repetitions whose native queue ran past 760 s:
# mean 834 s, the host at its top through the stream). BATCH_INTERFERENCE is the batch pods' loss of work per processor
# second while a serving pod's quota is lifted above its operator's on a host at its top, read from those repetitions'
# own pods (hashing time 59.2 s native, 63.1 s with the quota lifted: +7.64%, so 1 - 1/1.0764 = 0.071); with the host
# not at its top the same pods read +0.30%, and the toy takes none
BATCH = {"jobs": 24, "every_s": 30, "completions": 10, "parallel": 5, "req_m": 500, "lim_m": 1000, "pod_core_s": 8.1,
         "interference": 0.071, "start_lag_s": 3, "kind_cores": 3.0, "gov_cores": 0.017}
# the batch rig's host as it ran (amendment 5): the kind nodes on 3 of its 4 cores, the governor alone on the fourth (its
# own processor 0.017 cores, the table's "Omni's own CPU"); a batch pod running 2.66 s after it was made (the saturated
# repetitions' mean, rounded up to whole seconds); and the governor's reading as its sampler takes it (capacity.py): the
# host's busy share over the whole time since its previous reading, none at the first
BATCH.update(json.loads(os.environ.get("TOY_BATCH", "{}")))
CONVEY_BATCH_GAUGES = {**CONVEY_GAUGES, "batch_queue_s": ("lower", False), "batch_turnaround_s": ("lower", False),
                       "batch_work_core_s": ("higher", False)}


def water_fill(avail, wants, weights):
    """The kernel's fair share between cgroups under contention: each gets min(its want, weight x level), the level set
    so the shares sum to what is available; with room for every want, each gets its want."""
    if sum(wants) <= avail:
        return list(wants)
    lo, hi = 0.0, max((w / max(g, 1e-9) for w, g in zip(wants, weights)), default=0.0)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if sum(min(w, g * mid) for w, g in zip(wants, weights)) > avail:
            hi = mid
        else:
            lo = mid
    return [min(w, g * lo) for w, g in zip(wants, weights)]


def start_time(busy):
    """Seconds a pod takes to start on the host at this busy share, fitted to the v6 KEDA table's own 151 pod starts
    (results/live/V6_KEDA_REQUESTS.md): about 8 s to half busy, 9.5 s at three quarters, 12.4 s near the top."""
    if busy <= 0.5:
        return 8.0
    if busy <= 0.75:
        return 8.0 + 6.0 * (busy - 0.5)
    return 9.5 + 11.6 * (min(busy, 1.0) - 0.75)


def worker_convey(arm, seed, out, quota="none", batch=False):
    """A 4-core host carrying three kind nodes (each reports the host's 4 cores as its own); php-apache (200m request,
    500m limit) under an HPA at 50%, minimum 1, maximum 10, five minutes' scale-down window; load generators stepping
    1 2 3 1 2 1 every 150 s, each two closed-loop clients (a client sends its next request when the last one is answered,
    after half a second), 30 ms of CPU a request, so faster answers bring more requests, as on kind, and the HPA sits at
    one to three pods as the v6 KEDA run did (three serving pods at its peak); a starting pod uses 300m and starts at the
    pace the host's busy share allows. Native keeps the operator's limit; the omni arms call the checkout's own
    Muscles.convey every 15 s, as the governor's fast check does.

    With batch, the batch muscle of KubeRay's rig runs beside it (BATCH above): its pods are placed where the nodes'
    requests leave room, and the host's processor is shared as the kernel shares it between cgroups, each pod its want
    up to its own limit, by the weight of its request, when the wants exceed the host (water_fill); a serving pod's
    limit lifted above its operator's on a host at its top costs the batch pods BATCH_INTERFERENCE of their work."""
    import random
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed * 101 + 3)
    HOST, REQ_M, LIM_M, COST = 4.0, 200, 500, CAL["cost_s"]
    nodes = ["w0", "w1", "w2"]
    pods, ann, nid, busy = [], {}, [0], 0.3
    bpods, jobs, bid, win = [], [], [0], []                            # the batch muscle and the busy since the last reading (batch only)
    writes = [0]                                                       # every settings command the governor sent, refused ones included

    def new_pod():
        counts = {n: sum(1 for p in pods if p["node"] == n) for n in nodes}
        nid[0] += 1
        pods.append({"name": f"php-{nid[0]}", "node": min(nodes, key=lambda n: counts[n]), "limit": LIM_M,
                     "progress": 0.0, "ready": False, "born": t})

    class Kube:
        audit = None

        def get(self, *args):
            if args[:2] == ("get", "nodes"):
                return {"items": [{"metadata": {"name": n, "labels": {}}, "spec": {"providerID": f"kind://docker/kind/{n}"},
                                   "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}
                                  for n in nodes]}
            if args[:2] == ("get", "pods"):
                items = [{"metadata": {"name": p["name"], "namespace": "default", "labels": {"run": "php-apache"}},
                          "spec": {"nodeName": p["node"], "containers": [{"name": "php", "resources": {
                              "requests": {"cpu": f"{REQ_M}m"}, "limits": {"cpu": f"{p['limit']}m"}}}]},
                          "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True" if p["ready"] else "False"}]}}
                         for p in pods]
                items += [{"metadata": {"name": f"sys-{n}", "namespace": "kube-system", "labels": {}},
                           "spec": {"nodeName": n, "containers": [{"name": "s", "resources": {"requests": {"cpu": "100m"}}}]},
                           "status": {"phase": "Running", "conditions": [{"type": "Ready", "status": "True"}]}} for n in nodes]
                # a batch pod is Pending, not ready, until its container runs (start_lag_s, the rig's own pod start), as the
                # cluster lists it; the toy listed it Running from its creation until 21 October
                items += [{"metadata": {"name": b["name"], "namespace": "default", "labels": {"app": "omni-batch-stream"}},
                           "spec": {"nodeName": b["node"], "containers": [{"name": "work", "resources": {
                               "requests": {"cpu": f"{BATCH['req_m']}m"}, "limits": {"cpu": f"{BATCH['lim_m']}m"}}}]},
                           "status": {"phase": "Running" if b["runs"] <= t else "Pending", "conditions": [
                               {"type": "Ready", "status": "True" if b["runs"] <= t else "False"}]}} for b in bpods]
                return {"items": items}
            if args[:2] == ("get", "deployment"):
                return {"metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(ann)},
                        "spec": {"replicas": len(pods), "selector": {"matchLabels": {"run": "php-apache"}},
                                 "template": {"spec": {"containers": [{"name": "php", "resources": {
                                     "requests": {"cpu": f"{REQ_M}m"}, "limits": {"cpu": f"{LIM_M}m"}}}]}}}}
            if args[:2] == ("get", "resourcequota"):
                if quota in ("unreadable", "refused"):               # the governor's role cannot list quotas (every kind test)
                    raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="resourcequotas is forbidden")
                return {"items": []}
            raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not in the toy host")

        def write(self, args, why):
            writes[0] += 1
            if quota == "refused" and args[0] == "patch" and "resize" in args \
                    and int(str(json.loads(args[args.index("-p") + 1])[0]["value"]).rstrip("m")) > LIM_M:
                # the capacity test's namespace: a quota at the operator's limits, which the governor cannot read; admission
                # refuses every raise above it (exceeded quota: omni-cap), as on the omni-v11 capacity runs
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="pods is forbidden: exceeded quota: omni-cap")
            if args[0] == "annotate":
                k, _, v = args[-1].partition("="); ann[k] = v
            elif args[0] == "patch" and "resize" in args:
                val = json.loads(args[args.index("-p") + 1])[0]["value"]
                for p in pods:
                    if p["name"] == args[2]:
                        p["limit"] = int(str(val).rstrip("m"))

    m = None
    if arm != "native":
        from omni_controller.controller import parser
        from omni_controller.muscles import Muscles
        a = parser().parse_args(["--cap-deployments", "default/php-apache", "--audit", "", "--mode", "nodepool"])
        held = []
        m = Muscles(Kube(), a, lambda r: held.append(r) or r)

        class Sampler:
            def sample(self):
                if not batch:
                    return busy
                if not hasattr(self, "seen"):           # the governor's sampler: two readings make one share
                    self.seen = True; win.clear(); return None
                share = sum(win) / len(win) if win else None
                win.clear()
                return share
        m.host_cpu = Sampler()
    t = 0
    new_pod(); pods[0]["ready"] = True; pods[0]["progress"] = 1.0
    desired_hist, starts, lat, minute_ms, backlog = [], [], [], {}, 0.0
    busy_sum, limit_sum, pod_s, served, r_prev, busy_hist = 0.0, 0.0, 0.0, 0.0, 0.15, []
    steps = [1, 2, 3, 1, 2, 1] * 4
    for t in range(len(steps) * 150):
        # each load generator: 20 requests in a row, then 0 to 2 s of sleep (deploy/kind/loadgen.yaml), one request at a time
        lam = steps[t // 150] * CAL["clients"] / (min(r_prev, 5.0) + CAL["think_s"]) * (1.0 + 0.03 * rng.gauss(0, 1))
        demand = lam * COST                                            # cores the requests ask for
        ready = [p for p in pods if p["ready"]]; boot = [p for p in pods if not p["ready"]]
        other = CAL["other_cores"] + lam * CAL["loadgen_s"]            # control plane, KEDA, system pods, governor; the load generators
        start_use = 0.3 * len(boot)
        if batch:
            # the stream: a job every 30 s; its pods placed on the node whose requests leave the most room, five at a time
            if t % BATCH["every_s"] == 0 and len(jobs) < BATCH["jobs"]:
                jobs.append({"arrive": t, "made": 0, "done": 0, "end": None})
            req_on = {n: 100 + REQ_M * sum(1 for p in pods if p["node"] == n)
                      + BATCH["req_m"] * sum(1 for b in bpods if b["node"] == n) for n in nodes}
            for j in jobs:
                while j["end"] is None and j["made"] < BATCH["completions"] \
                        and sum(1 for b in bpods if b["job"] is j) < BATCH["parallel"]:
                    n = min(nodes, key=lambda x: req_on[x])
                    if 4000 - req_on[n] < BATCH["req_m"]:
                        break
                    bid[0] += 1; j["made"] += 1; req_on[n] += BATCH["req_m"]
                    bpods.append({"name": f"batch-{bid[0]}", "node": n, "left": BATCH["pod_core_s"], "job": j,
                                  "runs": t + BATCH["start_lag_s"]})
            run_b = [b for b in bpods if b["runs"] <= t]
            avail = max(0.05, BATCH["kind_cores"] - other - start_use)
            weights = [REQ_M / 1000.0] * len(ready) + [BATCH["req_m"] / 1000.0] * len(run_b)
            blim = [BATCH["lim_m"] / 1000.0] * len(run_b)
            # what each serving pod could have at this level (its whole limit wanted), and what it takes of its demand
            caps = water_fill(avail, [p["limit"] / 1000.0 for p in ready] + blim, weights)[:len(ready)]
            give = water_fill(avail, [min(c, demand / max(1, len(ready))) for c in caps] + blim, weights)
            used = sum(give[:len(ready)])
            busy = min(1.0, (other + start_use + used + sum(give[len(ready):]) + (BATCH["gov_cores"] if m else 0.0)) / HOST)
            win.append(busy)
            eff = 1.0 - (BATCH["interference"] if busy >= 0.75 and any(p["limit"] > LIM_M for p in ready) else 0.0)
            for b, g in zip(run_b, give[len(ready):]):
                b["left"] -= g * eff
                if b["left"] <= 0:
                    bpods.remove(b); b["job"]["done"] += 1
                    if b["job"]["done"] >= BATCH["completions"]:
                        b["job"]["end"] = t + 1
            cap_total = max(1e-6, sum(caps))
        else:
            want = [min(p["limit"] / 1000.0, demand / max(1, len(ready))) for p in ready]
            avail = max(0.05, HOST - other - start_use)
            scale = min(1.0, avail / sum(want)) if want and sum(want) > 0 else 1.0
            caps = [min(p["limit"] / 1000.0, avail / max(1, len(ready))) if scale < 1.0 else p["limit"] / 1000.0 for p in ready]
            used = sum(w * scale for w in want)
            busy = min(1.0, (other + start_use + used) / HOST)
            cap_total = max(1e-6, sum(min(c, avail) for c in caps))
        rho = demand / cap_total
        backlog = max(0.0, backlog + (demand - cap_total))
        svc = COST / max(1e-6, min(1.0, cap_total / max(1, len(ready))))
        mean_ms = 1000.0 * (svc / (1.0 - min(0.98, rho)) + backlog / cap_total)
        r_prev = mean_ms / 1000.0; served += lam
        for _ in range(5):
            ms = mean_ms * rng.lognormvariate(0.0, 0.3)
            lat.append(ms); minute_ms.setdefault(t // 60, []).append(ms)
        for p in boot:                                                  # starts advance at the host's pace
            p["progress"] += 8.0 / start_time(busy) / 8.0
            if p["progress"] >= 1.0:
                p["ready"] = True; starts.append(t - p["born"] + 1)
        if t % 15 == 0:                                                 # the HPA, every 15 s, on the ready pods' CPU
            util = (used / max(1, len(ready))) / (REQ_M / 1000.0) if ready else 0.0
            d = max(1, min(10, math.ceil(len(ready) * util / 0.5))) if ready else len(pods)
            desired_hist = [x for x in desired_hist if x[0] > t - 300] + [(t, d)]
            target = max(x[1] for x in desired_hist) if d < len(pods) else d
            while len(pods) < target:
                new_pod()
            while len(pods) > target and len(pods) > 1:
                pods.remove(max(pods, key=lambda p: p["born"]))
            if m is not None:
                m.convey()
        busy_sum += busy; limit_sum += sum(p["limit"] for p in pods); pod_s += len(pods); busy_hist.append(busy)
    lat.sort(); st = sorted(starts)
    res = {"start_wait_s": sum(st) / len(st) if st else 0.0, "start_wait_p95_s": st[int(0.95 * len(st))] if st else 0.0,
           "p95_ms": lat[int(0.95 * len(lat))], "alert_minutes": sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > 500.0),
           "host_busy": busy_sum / (t + 1), "limit_given_m": limit_sum / (t + 1), "pod_seconds": pod_s,
           "requests_served": served, "starts": len(st), "busy_p95": sorted(busy_hist)[int(0.95 * len(busy_hist))],
           "pods_mean": pod_s / (t + 1), "writes": writes[0],
           "starts_past_75": sum(1 for b in busy_hist if b >= 0.75)}
    if batch:
        ends = [j["end"] if j["end"] is not None else t + 1 for j in jobs]
        res["batch_queue_s"] = float(max(ends)) if ends else 0.0
        res["batch_turnaround_s"] = sum(e - j["arrive"] for j, e in zip(jobs, ends)) / len(jobs) if jobs else 0.0
        res["batch_work_core_s"] = BATCH["pod_core_s"] * sum(j["done"] for j in jobs)
    if arm != "native":
        res["engine_tree"] = engine_tree("omni_controller.muscles")
    print(json.dumps(res))


# ---- the verdict toy: the trigger alone on noisy work, in one checkout ---------------------------------------------
# ---- the card toy: the checkout's own GPU governor on a modelled card -----------------------------------------------
# the card of tools/gpu_physics_sim.py, written here so both engines meet one model: idle draw 40 W; busy draw
# 80 + 220 s^gamma W at speed s (1 = full clock, 300 W, the start limit); a power limit under 300 W slows the card to the
# speed whose draw is the limit, as real cards do by lowering their clocks; heat first order toward 30 C + 0.12 C/W x draw
# with a 20 s time constant. gamma 3: voltage falls with the clock (capping cheap in speed); gamma 1.5: the card near its
# voltage floor (capping dear). The work: Poisson arrivals at 30, 60, 80, 30, 60, 30% of full-speed capacity, 100 s each,
# one server first come first served, 50 ms a request at full speed, 600 s and a 30 s drain, the response line ten service
# times (500 ms). The governor is omni_controller/gpu_governor.py at its command-line defaults (cap mode, a decision every
# 2 s), reading the modelled card as it reads nvidia-smi and the response-time file as on hardware; native is the card's own
# firmware at the start limit. A reading here is a model's (class S): the hardware answer is scripts/gpu_paired.sh
CARD = {"start_w": 300.0, "min_w": 100.0, "idle_w": 40.0, "static_w": 80.0, "demand_w": 300.0, "service_ms": 50.0, "slo_ms": 500.0,
        "phases": (0.3, 0.6, 0.8, 0.3, 0.6, 0.3), "duration_s": 600, "drain_s": 30}
CARD_GAUGES = {"requests_served": ("higher", False), "requests_not_served": ("lower", False), "p95_ms": ("lower", False),
               "p99_ms": ("lower", False), "gpu_energy_j": ("lower", True), "peak_temp_c": ("lower", True),
               "limit_writes": ("lower", True), "limit_moves": ("lower", True), "limit_reversals": ("lower", True),
               "limit_travel_w": ("lower", True)}
CARD_SMI = '''#!/usr/bin/env python3
import json, os, sys
p = os.environ["PHYS_STATE"]; st = json.load(open(p)); a = sys.argv[1:]
if "-pl" in a:
    st["limit"] = float(a[a.index("-pl") + 1]); json.dump(st, open(p, "w")); print("ok"); sys.exit(0)
f = [x for x in a if x.startswith("--query-gpu=")][0].split("=", 1)[1].split(",")
if any("reasons" in x for x in f): sys.exit(2)
v = {"index": 0, "power.draw": st["draw"], "temperature.gpu": st["temp"], "utilization.gpu": round(100 * st["util"]),
     "power.limit": st["limit"], "power.min_limit": %s, "clocks.sm": round(1800 * st["speed"]),
     "enforced.power.limit": st["limit"], "power.management": "Enabled", "persistence_mode": "Enabled",
     "power.default_limit": 300, "power.max_limit": 300}
print(", ".join(str(v[x]) for x in f))
''' % CARD["min_w"]


def worker_card(arm, seed, gamma, out):
    """One arm of the card toy on one seed: native (the start limit throughout) or the checkout's governor in cap mode."""
    import random
    import statistics
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    C = CARD
    speed_at = lambda limit: 1.0 if limit >= C["demand_w"] else max(0.05, (limit - C["static_w"]) / (C["demand_w"] - C["static_w"])) ** (1.0 / gamma)
    busy_power = lambda s: C["static_w"] + (C["demand_w"] - C["static_w"]) * s ** gamma
    rng = random.Random(seed); arr = []; per = C["duration_s"] / len(C["phases"])
    for i, share in enumerate(C["phases"]):
        rate = share / (C["service_ms"] / 1000.0); t = i * per
        while True:
            t += rng.expovariate(rate)
            if t >= (i + 1) * per:
                break
            arr.append(t)
    smi, state, lat = out / "smi.py", out / "state.json", out / "latency.csv"
    smi.write_text(CARD_SMI); smi.chmod(0o755)
    state.write_text(json.dumps({"limit": C["start_w"], "draw": C["idle_w"], "temp": 35.0, "util": 0.0, "speed": 1.0}))
    lat.write_text("elapsed_seconds,latency_ms,ok\n")
    os.environ["PHYS_STATE"] = str(state)
    gov = None
    if arm != "native":
        from omni_controller.gpu_governor import GpuGovernor, parser as gov_parser
        a = gov_parser().parse_args(["--mode", "cap", "--smi", str(smi), "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "no-kill"),
                                     "--latency-file", str(lat), "--slo-ms", str(C["slo_ms"])])
        gov = GpuGovernor(a); every = max(1, int(round(a.interval)))
    ai = 0; queue = []; energy = 0.0; temp = 35.0; lats = []; limits = []; peak = 0.0
    for sec in range(C["duration_s"] + C["drain_s"]):
        st = json.loads(state.read_text()); limit = st["limit"]; limits.append(limit)
        s = speed_at(limit); pb = busy_power(s)
        t, end, busy, rows = float(sec), sec + 1.0, 0.0, []
        while t < end:
            while ai < len(arr) and arr[ai] <= t:
                queue.append([arr[ai], C["service_ms"] / 1000.0]); ai += 1
            nxt = arr[ai] if ai < len(arr) else math.inf
            if not queue:
                t = min(end, nxt); continue
            job = queue[0]
            step = min(job[1] / s, end - t, nxt - t)
            job[1] -= step * s; busy += step; t += step
            if job[1] <= 1e-12:
                queue.pop(0); ms = (t - job[0]) * 1000.0; lats.append(ms); rows.append(f"{t:.3f},{ms:.2f},1\n")
        draw = busy * pb + (1 - busy) * C["idle_w"]
        energy += draw; temp += (30 + 0.12 * draw - temp) / 20.0; peak = max(peak, temp)
        with open(lat, "a") as f:
            f.writelines(rows)
        st.update(draw=round(draw, 2), temp=round(temp, 1), util=busy, speed=s); state.write_text(json.dumps(st))
        if gov and sec < C["duration_s"] and sec % every == every - 1:
            gov.step()
    if gov:
        gov.restore()
    lats.sort()
    held = limits[:C["duration_s"]]
    wear = cap_wear(held)
    res = {"requests_served": float(len(lats)), "requests_not_served": float(len(arr) - len(lats)),
           "p95_ms": lats[int(0.95 * len(lats))], "p99_ms": lats[int(0.99 * len(lats))], "gpu_energy_j": energy, "peak_temp_c": peak,
           "limit_writes": float(gov.writes if gov else 0), "limit_moves": wear["power_cap_moves"],
           "limit_reversals": wear["power_cap_reversals"], "limit_travel_w": wear["power_cap_travel"]}
    if gov:
        res["engine_tree"] = engine_tree("omni_controller.gpu_governor")
        if engine_tree("omnicompass.adapter") != res["engine_tree"]:
            raise RuntimeError("the card governor and the brain were imported from two trees")
    print(json.dumps(res))


VERDICT_RATES = (20, 200)


def worker_verdict(seeds):
    import random
    from omnicompass.verdict import Verdict
    out = {}
    for rate in VERDICT_RATES:                     # pieces of work a decision: slow work, and work fast enough to read a 2% step
        out[str(rate)] = {}
        for rise in (0.0, 0.01, 0.02, 0.03, 0.05):
            allowed = 0
            for s in range(seeds):
                rng = random.Random(s)
                v = Verdict(tolerance=0.02, min_samples=60, probe_every=1, recheck=10 ** 6, max_trial=40)
                step = 0
                for _ in range(120):
                    base = 10.0 * (1.0 + rise * step)
                    v.observe([base * rng.lognormvariate(0.0, 0.25) for _ in range(rate)])
                    step, _, ev = v.tick(True)
                    if ev and str(ev.get("verdict", "")).startswith(("step", "trial not started")):
                        allowed += ev["verdict"] == "step allowed"
                        break
            out[str(rate)][f"{rise:.2f}"] = allowed / seeds
    out["engine_tree"] = engine_tree("omnicompass.verdict")
    print(json.dumps(out))


def verdict_rates(r):
    """The verdict toy's readings by pieces of work a decision; a checkout whose toy ran one rate (20) is read as that rate."""
    return r if all(isinstance(v, dict) for v in r.values()) else {"20": r}


# ---- the parent: both checkouts, every seed, the readings -----------------------------------------------------------
def engine_tree(module):
    """The checkout a worker's engine module was imported from (the root above its package)."""
    return str(Path(sys.modules[module].__file__).resolve().parents[1])


def run(tree, args):
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(Path(__file__).resolve()), *args], cwd=tree, env=env, capture_output=True,
                       text=True, timeout=7200)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {args}: {p.stderr[-2000:]}")
    r = json.loads(p.stdout.strip().splitlines()[-1])
    got = r.pop("engine_tree", None) if isinstance(r, dict) else None
    if got is not None and Path(got).resolve() != Path(tree).resolve():
        raise RuntimeError(f"{args[:2]}: the engine was imported from {got}, not from the checkout under test {tree}")
    return r


def reading(gauge, diffs, base_vals, gauges=None):
    aim, spent = (gauges or GAUGES)[gauge]
    n = len(diffs); m = sum(diffs) / n
    sd = math.sqrt(sum((d - m) ** 2 for d in diffs) / (n - 1)) if n > 1 else float("inf")
    t = T95.get(n - 1, 2.0); lo, hi = m - t * sd / math.sqrt(n), m + t * sd / math.sqrt(n)
    if sd == 0.0:
        lo = hi = m
    if lo <= 0.0 <= hi and not (lo == hi == 0.0):
        word = "EVEN"
    elif lo == hi == 0.0:
        word = "EVEN (identical)"
    elif (hi < 0) == (aim == "lower"):
        word = "GAIN"
    else:
        word = "power given" if spent else "LOSS"
    b = sum(base_vals) / n
    return {"mean_change": m, "ci95": [lo, hi], "relative": m / b if b else float("nan"), "word": word}


def toy_period(t):
    """A cluster toy's heading: the decision periods of the two engines, and the plant's step where it is not 15 s."""
    if "period_s" not in t:
        return ""
    bp, cp = t.get("base_period_s", t["period_s"]), t.get("cand_period_s", t["period_s"])
    plant = f"; the plant in {t['plant_s']:.0f}-second steps" if t.get("plant_s", 15.0) != 15.0 else ""
    if bp == cp:
        return f" (a decision every {cp:g} s{plant})"
    return f" (the standing engine every {bp:g} s, the candidate every {cp:g} s{plant})"


def render(report_path, out_md):
    """TOY_GATE.json -> a page with the notice: the toys, their gauges, the readings, the counts (class S, never a benchmark)."""
    from tools.legal import stamp
    r = json.loads(Path(report_path).read_text())

    def engine(tree):
        """The engine a tree declares (tools/omni_version.py), or the tree's name where it cannot be read."""
        try:
            out = subprocess.run([sys.executable, "tools/omni_version.py"], cwd=tree, env={**os.environ, "PYTHONPATH": tree},
                                 capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
            differs = [ln.split(": ", 1)[1] for ln in out if ln.startswith("differs from ")]
            if differs:                    # every engine file the tree changes, not only the last one printed
                return f"{out[0].split(': ', 1)[0]}: {', '.join(differs)}"
            return out[-1].split(" (")[0] if out else Path(tree).name
        except (OSError, subprocess.SubprocessError):
            return Path(tree).name
    base_e = engine(r["base"]) if Path(r["base"]).exists() else r["base"]
    cand_e = engine(r["cand"]) if Path(r["cand"]).exists() else r["cand"]
    lines = ["# The toy gate: the candidate against the engine that stands, in our own models", "",
             f"Seeds {r['seeds'][0]} to {r['seeds'][-1]}, {r['days']} day each where a day is run; the standing engine "
             f"{base_e}, the candidate {cand_e}. Evidence class S, our own models: a reading here says "
             "whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed "
             "with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: "
             "tools/readings.py).", ""]
    if r.get("note"):
        lines += [r["note"], ""]
    for toy, t in r["toys"].items():
        lines += [f"## {toy}{toy_period(t)}", ""]
        if toy == "verdict":
            for rate, b in verdict_rates(t["base"]).items():
                c = verdict_rates(t["cand"]).get(rate, {})
                lines += [f"{rate} pieces of work a decision, their log spread 0.25:", "",
                          "| True extra cost of a give-back step | Allowed, standing | Allowed, candidate |", "|---|---|---|"]
                lines += [f"| +{100 * float(k):.0f}% | {100 * b[k]:.0f}% | "
                          f"{(f'{100 * c[k]:.0f}%') if k in c else 'not run'} |" for k in b]
                lines.append("")
            continue
        lines += ["| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |",
                  "|---|---:|---:|---:|---|---|---|"]
        cell = lambda d: f"{100 * d['relative']:+.2f}% {d['word']}" if d["relative"] == d["relative"] else d["word"]
        for g, x in t["gauges"].items():
            lines.append(f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | {cell(x['cand_vs_base'])} | "
                         f"{cell(x['base_vs_native'])} | {cell(x['cand_vs_native'])} |")
        lines += ["", "Counts over all seeds: " + ", ".join(f"{k} {v}" for k, v in t["counts"].items()), ""]
        first = t.get("candidate_as_first_pushed")
        if first:                                   # the reading that caught a fault, kept beside the corrected candidate's
            lines += [f"The candidate as first pushed (digest {first['digest']}), the reading that caught the fault:", "",
                      "| Gauge | Native | Standing | Candidate as first pushed | Against standing | Against native |", "|---|---:|---:|---:|---|---|"]
            for g, x in first["gauges"].items():
                lines.append(f"| {g} | {x['native']:.3f} | {x['base']:.3f} | {x['cand']:.3f} | {cell(x['cand_vs_base'])} | {cell(x['cand_vs_native'])} |")
            lines.append("")
    lines += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    Path(out_md).write_text("\n".join(stamp(lines)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--render", nargs=2, metavar=("TOY_GATE.json", "TOY_GATE.md"), help="write the page from a report")
    ap.add_argument("--base", help="checkout of the engine that stands")
    ap.add_argument("--cand", help="checkout of the candidate")
    ap.add_argument("--seeds", default="1-8")
    ap.add_argument("--days", type=float, default=1.0)
    ap.add_argument("--toys", default=",".join(list(CLUSTER_TOYS) + ["convey", "convey_unreadable_quota", "convey_refused",
                                                                   "convey_batch", "card", "card_floor", "verdict"]))
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--out", default="")
    ap.add_argument("--worker", help=argparse.SUPPRESS)
    ap.add_argument("--seed", type=int, help=argparse.SUPPRESS)
    ap.add_argument("--period", type=float, default=60.0, help=argparse.SUPPRESS)
    ap.add_argument("--dir", help=argparse.SUPPRESS)
    ap.add_argument("--blink", action="store_true", help=argparse.SUPPRESS)  # the cluster toy with its machines out of service a while
    ap.add_argument("--fine", action="store_true", help=argparse.SUPPRESS)   # the cluster toy on the 5-second plant
    ap.add_argument("--quota", default="none", help=argparse.SUPPRESS)      # the convey toy's quota: none (readable, empty), unreadable, or refused (unreadable, every raise refused)
    ap.add_argument("--batch", action="store_true", help=argparse.SUPPRESS)  # the convey toy with the batch muscle beside the serving one
    ap.add_argument("--gamma", type=float, default=3.0, help=argparse.SUPPRESS)  # the card toy's clock-cost exponent
    a = ap.parse_args(argv)
    if a.render:
        return render(*a.render)
    if a.worker == "verdict":
        return worker_verdict(a.seed)
    if a.worker in ("convey-native", "convey-omni"):
        return worker_convey(a.worker.split("-")[1], a.seed, a.dir, a.quota, a.batch)
    if a.worker in ("card-native", "card-omni"):
        return worker_card(a.worker.split("-")[1], a.seed, a.gamma, a.dir)
    if a.worker:
        return worker(a.worker, a.seed, a.days, a.period, a.dir, a.blink, a.fine)
    lo_s, _, hi_s = a.seeds.partition("-")
    seeds = list(range(int(lo_s), int(hi_s or lo_s) + 1))
    base, cand = Path(a.base).resolve(), Path(a.cand).resolve()
    work = Path(a.out or tempfile.mkdtemp(prefix="toy_gate_"))
    from concurrent.futures import ThreadPoolExecutor
    report = {"seeds": seeds, "days": a.days, "base": str(base), "cand": str(cand), "toys": {}}
    toys = a.toys.split(",")
    memo = {}                                       # a run's reading by what decides it: the same run is never run twice

    def cluster_run(j):
        arm, tree, sd, period, blink, fine, d = j
        key = ("native", sd, fine) if arm == "native" else (str(tree), sd, period, blink, fine)
        if key not in memo:
            memo[key] = run(tree, ["--worker", "native" if arm == "native" else "omni", "--seed", str(sd), "--days", str(a.days),
                                   "--period", str(period), *(["--blink"] if blink else []), *(["--fine"] if fine else []),
                                   "--dir", str(d)])
        return memo[key]
    for toy, (bp, cp, fine, blink) in CLUSTER_TOYS.items():
        if toy not in toys:
            continue
        jobs = [(arm, tree, sd, cp if arm == "cand" else bp, blink, fine, work / toy / f"{arm}-{sd}")
                for sd in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(cluster_run, jobs))
        res = {}
        for (arm, _, s, *_), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in GAUGES:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv)}
        extra = {k: {arm: sum(res[arm][s].get(k, 0) for s in seeds) for arm in ("base", "cand")}
                 for k in ("steps_allowed", "steps_refused", "trials_abandoned", "machines_parked", "errors", "readings_held")}
        report["toys"][toy] = {"period_s": cp, "base_period_s": bp, "cand_period_s": cp, "plant_s": 5.0 if fine else 15.0,
                               "gauges": rows, "counts": extra, "per_seed": res}
    # the convey toy twice: the namespace's quota readable and empty, and unreadable (the governor's role cannot list
    # quotas on every kind test, and on any stack whose role withholds it; the first v7 trial read that as a zero budget)
    # and a third time with every raise refused by a quota the governor cannot read (the capacity test, v12); and a
    # fourth with the batch muscle of KubeRay's rig beside the serving one (omni-v13)
    for toy, quota, bat in (("convey", "none", False), ("convey_unreadable_quota", "unreadable", False),
                            ("convey_refused", "refused", False), ("convey_batch", "none", True)):
        if toy not in toys:
            continue
        gauges = CONVEY_BATCH_GAUGES if bat else CONVEY_GAUGES
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "convey-native" if j[0] == "native" else "convey-omni",
                                                    "--seed", str(j[2]), "--quota", quota, *(["--batch"] if bat else []),
                                                    "--dir", str(work / toy / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in gauges:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv, gauges),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv, gauges),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv, gauges)}
        report["toys"][toy] = {"gauges": rows, "counts": {k: {arm: sum(res[arm][s][k] for s in seeds) for arm in ("native", "base", "cand")}
                                                          for k in ("starts", "starts_past_75")}, "per_seed": res}
    # the card toys (omni-v15): the GPU governor of each checkout on the modelled card, native the card's own firmware at its
    # start limit; the card whose voltage falls with its clock (gamma 3) and the card near its voltage floor (gamma 1.5)
    for toy, gamma in (("card", 3.0), ("card_floor", 1.5)):
        if toy not in toys:
            continue
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "card-native" if j[0] == "native" else "card-omni",
                                                    "--seed", str(j[2]), "--gamma", str(gamma),
                                                    "--dir", str(work / toy / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in CARD_GAUGES:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv, CARD_GAUGES),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv, CARD_GAUGES),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv, CARD_GAUGES)}
        report["toys"][toy] = {"gauges": rows, "counts": {k: {arm: sum(res[arm][s][k] for s in seeds) for arm in ("native", "base", "cand")}
                                                          for k in ("limit_writes", "limit_moves", "limit_reversals")}, "per_seed": res}
    if "verdict" in toys:
        report["toys"]["verdict"] = {"base": run(base, ["--worker", "verdict", "--seed", "300"]),
                                     "cand": run(cand, ["--worker", "verdict", "--seed", "300"])}
    (work / "TOY_GATE.json").write_text(json.dumps(report, indent=1))
    for toy, r in report["toys"].items():
        print(f"\n== {toy}{toy_period(r)}")
        if toy == "verdict":
            print("share of give-back steps allowed, by the step's true extra cost (2% allowance, noisy work):")
            for rate, b in verdict_rates(r["base"]).items():
                c = verdict_rates(r["cand"]).get(rate, {})
                print(f" {rate} pieces of work a decision:")
                for k in b:
                    print(f"  +{100 * float(k):.0f}%: standing {100 * b[k]:.0f}%  candidate "
                          f"{(f'{100 * c[k]:.0f}%') if k in c else 'not run'}")
            continue
        print(f"{'gauge':32s} {'native':>10s} {'standing':>10s} {'candidate':>10s}  candidate vs standing         standing vs native   candidate vs native")
        for g, x in r["gauges"].items():
            cb, bn, cn = x["cand_vs_base"], x["base_vs_native"], x["cand_vs_native"]
            print(f"{g:32s} {x['native']:10.3f} {x['base']:10.3f} {x['cand']:10.3f}  {100 * cb['relative']:+7.2f}% {cb['word']:18s}"
                  f"  {100 * bn['relative']:+7.2f}% {bn['word']:10s}  {100 * cn['relative']:+7.2f}% {cn['word']}")
        print("counts over all seeds:", json.dumps(r["counts"]))
    print(f"\n(our own models, evidence class S; {work / 'TOY_GATE.json'})")
    return report


if __name__ == "__main__":
    main()
