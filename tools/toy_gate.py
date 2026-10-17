#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The toy gate: every change to the engine or a live controller runs here first, in our own models (evidence class S),
against the engine that stands, on the same seeds, before any real run is started (the founder's order of 15 October,
night). A change goes on to real runs only where it reads no LOSS here and shows promise; a LOSS here is root-caused and
fixed in the model, never carried into a real run. A reading here is a model's, never a benchmark's result.

  python3 tools/toy_gate.py --base <checkout> --cand <checkout> [--seeds 1-8] [--days 1] [--toys cluster,cluster15,verdict]

Each checkout is a working tree: one on the engine that stands, one on the candidate. Each runs in its own process with
its own code, so the two never share a module.

  cluster    the shipped Kubernetes controller in the cloud's setting (node-pool mode, the compass law, the tune-down,
             nothing sensed but the machines; --give-back-only where the checkout has it) on the toy cluster of
             pilot/selfpilot.py: the fleet harness's web workload, the HPA at its target, a node's boot delay, power;
             a decision every 60 s and the fast check every 15 s. Response times come from a queue on the running pods
             (an M/M/1 delay on each pod's share, log-normal spread, the backlog's wait added). Native is the HPA with
             the Cluster Autoscaler on the same demand.
  cluster15  the same with a decision every 15 s: each rule's time at a shorter period.
  verdict    the do-no-harm trigger (omnicompass/verdict.py) on noisy work: how often a give-back step that truly costs
             0 to 5% more is allowed against a 2% allowance, the candidate's verdict against the standing one.

Gauges per seed (a day each): machine-hours, energy per used core-hour, pending-pod minutes an hour, HPA shortfall
minutes an hour, the 95th-percentile response time, and alert minutes (minutes whose 95th percentile is over the line).
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
sys.path.insert(0, str(ROOT))
from omnicompass.student_t import T95  # noqa: E402  (keyed by degrees of freedom; the table it replaces was keyed by seeds
#                                                        and read one row early)
# gauge -> (aim, a resource spent?)
GAUGES = {"machine_hours": ("lower", True), "kwh_per_core_hour": ("lower", True),
          "pending_pod_minutes_per_hour": ("lower", False), "hpa_shortfall_minutes_per_hour": ("lower", False),
          "p95_ms": ("lower", False), "alert_minutes": ("lower", False)}


# ---- the worker: one arm, one seed, run inside one checkout --------------------------------------------------------
def worker(arm, seed, days, period, out):
    import csv
    from unittest import mock
    import numpy as np
    from pilot.selfpilot import SimCluster, SimKube
    from pilot.score import blocks, load
    from fleet.sim import ALLOC
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed + 7)
    IDLE = "omnicompass.io/idle"

    class CloudSim(SimCluster):
        """The cloud as the governor meets it (scripts/kind_bench.sh, the cloud setting): the cloud's own autoscaler
        makes machines and deletes an unneeded one, in every arm; the governor only parks a machine that exists (marked
        idle and drained), which the cloud deletes once it has stood empty for its scale-down time, and wakes a parked
        machine at once while it still exists. It never adds one."""
        PARK_TICKS = 40                                        # ten minutes: the autoscaler's scale-down-unneeded time

        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.c.pool.power_off = True                       # a machine the cloud scales down is deleted, not kept
            self.parked = []

        def tick(self):
            self.parked = [x - 1 for x in self.parked if x > 1]
            super().tick()

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting) + len(self.parked)

        def resize(self, n):
            p = self.c.pool; n = max(p.min_nodes, int(n))
            if n < p.nodes:
                k = p.nodes - n; p.nodes -= k; self.parked += [self.PARK_TICKS] * k
            elif n > p.nodes:
                k = min(n - p.nodes, len(self.parked)); p.nodes += k; self.parked = self.parked[k:]

    sim = CloudSim(seed, days, autoscaler="ca")
    billed = []
    lat_path = out / "latency.csv"
    lat_rows, minute_ms, p95s = [], {}, []

    def time_requests():
        """The requests of this 15 s, timed on the pods running now (the same queue in every arm)."""
        c = sim.c
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = sum(w.replicas * w.request * frac for w in c.workloads)
        dem = sum(w.demand[min(sim.t, len(w.demand) - 1)] for w in c.workloads)
        backlog = sum(w.backlog for w in c.workloads)
        rho = min(0.98, dem / cap) if cap > 0 else 0.98
        mean = SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
        t0 = sim.t * 15.0
        for i in range(SAMPLES_PER_TICK):
            ms = float(mean * rng.lognormal(0.0, 0.25))
            lat_rows.append((t0 + i * 15.0 / SAMPLES_PER_TICK, ms))
            minute_ms.setdefault(int(t0 // 60), []).append(ms)
        del lat_rows[:-60 * SAMPLES_PER_TICK]                  # the probe file keeps the last 15 minutes
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{t:.2f},{ms:.3f},1\n" for t, ms in lat_rows)

    class Kube(SimKube):
        def get(self, *args):
            if args[:2] == ("get", "nodes"):                    # in service, then parked (marked idle) until deleted
                p = self.sim.c.pool
                node = lambda i, taints: {"metadata": {"name": f"n{i}", "labels": {}},
                                          "spec": {"taints": taints}, "status": {"allocatable": {"cpu": str(p.cores)},
                                          "conditions": [{"type": "Ready", "status": "True"}]}}
                return {"items": [node(i, []) for i in range(p.nodes)]
                        + [node(p.nodes + j, [{"key": IDLE, "effect": "PreferNoSchedule"}]) for j in range(len(self.sim.parked))]}
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                pend = sum(w.replicas - int(w.replicas * frac) for w in c.workloads)
                return "\n".join(f"pod/p{i}" for i in range(pend))
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

    if arm != "native":
        from omni_controller.controller import Controller, parser
        argv = ["--mode", "nodepool", "--law", "compass", "--dial", "save", "--sensed", "none/none",
                "--interval", str(period), "--latency-file", str(lat_path), "--slo-ms", str(SLO_MS),
                "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"), "--node-scale-cmd", "SIMSCALE {n}",
                "--min-nodes", str(sim.c.pool.min_nodes), "--max-nodes", str(sim.c.pool.max_nodes), "--headroom", "0.5",
                "--active-nodes-only", "--max-node-step", "1"]
        p = parser()
        if any("--give-back-only" in getattr(x, "option_strings", []) for x in p._actions):
            argv.append("--give-back-only")
        a = p.parse_args(argv)
        k = Kube(sim, None)
        ctl = Controller(a, kube=k)
        real_run = subprocess.run

        def fake_run(cmd, *kw_a, **kw):
            if isinstance(cmd, list) and cmd and cmd[0] == "SIMSCALE":
                sim.resize(int(cmd[1])); return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, *kw_a, **kw)
        every = max(1, int(round(period / 15.0)))
        with mock.patch("omni_controller.controller.subprocess.run", side_effect=fake_run):
            while sim.t < sim.steps:
                sim.tick(); sim.c.alloc = sim.c.pool.nodes * sim.c.pool.cores * ALLOC
                time_requests(); billed.append(sim.billed())
                if sim.t % every == 0:
                    ctl.step()
                else:
                    ctl.floor_step()
    else:
        while sim.t < sim.steps:
            sim.tick(); time_requests(); billed.append(sim.billed())
    cap = out / "capture.csv"; sim.write_capture(cap)
    rows = load(str(cap))
    day = blocks(rows, 86400 * days + 60, None, None)[0]                # one block: the whole run
    hours = sum(billed) * 15.0 / 3600.0                                 # the bill: every machine that exists
    allm = sorted(ms for v in minute_ms.values() for ms in v)
    alert = sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > SLO_MS)
    res = {"machine_hours": hours, "kwh_per_core_hour": day["kwh_per_core_hour"],
           "pending_pod_minutes_per_hour": day["pending_pod_minutes_per_hour"],
           "hpa_shortfall_minutes_per_hour": day["hpa_shortfall_minutes_per_hour"],
           "p95_ms": allm[int(0.95 * len(allm))], "alert_minutes": alert}
    if arm != "native":
        recs = [json.loads(l) for l in open(out / "audit.jsonl")]
        ev = [r["verdict"].get("verdict", "") for r in recs if isinstance(r.get("verdict"), dict)]
        res["steps_allowed"] = sum(1 for v in ev if v == "step allowed")
        res["steps_refused"] = sum(1 for v in ev if v.startswith("step refused"))
        res["trials_abandoned"] = sum(1 for v in ev if v.startswith("trial abandoned"))
        res["machines_parked"] = sum(1 for r in recs if r.get("write", [None])[0] == "SIMSCALE")
        res["errors"] = sum(1 for r in recs if "error" in r)
    print(json.dumps(res))


# ---- the conveyance toy: one kind host, the checkout's own conveyance code ------------------------------------------
# the toy host's calibration, set so the native arm sits where the v6 KEDA run's native arm did (results/live/raw/addons-run-
# 38725705826: host busy mean 0.27 and p95 0.42, response p50 91 ms and p95 248 ms, the HPA's replicas), see docs/OMNI_V7.md
CAL = {"cost_s": 0.06, "clients": 1.0, "think_s": 0.05, "other_cores": 0.55, "loadgen_s": 0.004}
CAL.update(json.loads(os.environ.get("TOY_CAL", "{}")))        # a heavier or lighter load for one run, without a code change
CONVEY_GAUGES = {"requests_served": ("higher", False), "start_wait_s": ("lower", False), "start_wait_p95_s": ("lower", False), "p95_ms": ("lower", False),
                 "alert_minutes": ("lower", False), "host_busy": ("lower", True), "limit_given_m": ("lower", True),
                 "pod_seconds": ("lower", True)}


def start_time(busy):
    """Seconds a pod takes to start on the host at this busy share, fitted to the v6 KEDA table's own 151 pod starts
    (results/live/V6_KEDA_REQUESTS.md): about 8 s to half busy, 9.5 s at three quarters, 12.4 s near the top."""
    if busy <= 0.5:
        return 8.0
    if busy <= 0.75:
        return 8.0 + 6.0 * (busy - 0.5)
    return 9.5 + 11.6 * (min(busy, 1.0) - 0.75)


def worker_convey(arm, seed, out, quota="none"):
    """A 4-core host carrying three kind nodes (each reports the host's 4 cores as its own); php-apache (200m request,
    500m limit) under an HPA at 50%, minimum 1, maximum 10, five minutes' scale-down window; load generators stepping
    1 2 3 1 2 1 every 150 s, each two closed-loop clients (a client sends its next request when the last one is answered,
    after half a second), 30 ms of CPU a request, so faster answers bring more requests, as on kind, and the HPA sits at
    one to three pods as the v6 KEDA run did (three serving pods at its peak); a starting pod uses 300m and starts at the
    pace the host's busy share allows. Native keeps the operator's limit; the omni arms call the checkout's own
    Muscles.convey every 15 s, as the governor's fast check does."""
    import random
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed * 101 + 3)
    HOST, REQ_M, LIM_M, COST = 4.0, 200, 500, CAL["cost_s"]
    nodes = ["w0", "w1", "w2"]
    pods, ann, nid, busy = [], {}, [0], 0.3

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
                return {"items": items}
            if args[:2] == ("get", "deployment"):
                return {"metadata": {"name": "php-apache", "namespace": "default", "annotations": dict(ann)},
                        "spec": {"replicas": len(pods), "selector": {"matchLabels": {"run": "php-apache"}},
                                 "template": {"spec": {"containers": [{"name": "php", "resources": {
                                     "requests": {"cpu": f"{REQ_M}m"}, "limits": {"cpu": f"{LIM_M}m"}}}]}}}}
            if args[:2] == ("get", "resourcequota"):
                if quota == "unreadable":                            # the governor's role cannot list quotas (every kind test)
                    raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="resourcequotas is forbidden")
                return {"items": []}
            raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="not in the toy host")

        def write(self, args, why):
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
                return busy
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
           "pods_mean": pod_s / (t + 1),
           "starts_past_75": sum(1 for b in busy_hist if b >= 0.75)}
    print(json.dumps(res))


# ---- the verdict toy: the trigger alone on noisy work, in one checkout ---------------------------------------------
def worker_verdict(seeds):
    import random
    from omnicompass.verdict import Verdict
    out = {}
    for rise in (0.0, 0.01, 0.02, 0.03, 0.05):
        allowed = 0
        for s in range(seeds):
            rng = random.Random(s)
            v = Verdict(tolerance=0.02, min_samples=60, probe_every=1, recheck=10 ** 6, max_trial=40)
            step = 0
            for _ in range(60):
                base = 10.0 * (1.0 + rise * step)
                v.observe([base * rng.lognormvariate(0.0, 0.25) for _ in range(20)])
                step, _, ev = v.tick(True)
                if ev and str(ev.get("verdict", "")).startswith("step"):
                    allowed += ev["verdict"] == "step allowed"
                    break
        out[f"{rise:.2f}"] = allowed / seeds
    print(json.dumps(out))


# ---- the parent: both checkouts, every seed, the readings -----------------------------------------------------------
def run(tree, args):
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(Path(__file__).resolve()), *args], cwd=tree, env=env, capture_output=True,
                       text=True, timeout=7200)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {args}: {p.stderr[-2000:]}")
    return json.loads(p.stdout.strip().splitlines()[-1])


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
        period = f" (a decision every {t['period_s']:.0f} s)" if "period_s" in t else ""
        lines += [f"## {toy}{period}", ""]
        if toy == "verdict":
            lines += ["| True extra cost of a give-back step | Allowed, standing | Allowed, candidate |", "|---|---|---|"]
            lines += [f"| +{100 * float(k):.0f}% | {100 * t['base'][k]:.0f}% | {100 * t['cand'][k]:.0f}% |" for k in t["base"]]
            lines.append(""); continue
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
    ap.add_argument("--toys", default="cluster,cluster15,convey,convey_unreadable_quota,verdict")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--out", default="")
    ap.add_argument("--worker", help=argparse.SUPPRESS)
    ap.add_argument("--seed", type=int, help=argparse.SUPPRESS)
    ap.add_argument("--period", type=float, default=60.0, help=argparse.SUPPRESS)
    ap.add_argument("--dir", help=argparse.SUPPRESS)
    ap.add_argument("--quota", default="none", help=argparse.SUPPRESS)      # the convey toy's quota read: none (readable, empty) or unreadable
    a = ap.parse_args(argv)
    if a.render:
        return render(*a.render)
    if a.worker == "verdict":
        return worker_verdict(a.seed)
    if a.worker in ("convey-native", "convey-omni"):
        return worker_convey(a.worker.split("-")[1], a.seed, a.dir, a.quota)
    if a.worker:
        return worker(a.worker, a.seed, a.days, a.period, a.dir)
    lo_s, _, hi_s = a.seeds.partition("-")
    seeds = list(range(int(lo_s), int(hi_s or lo_s) + 1))
    base, cand = Path(a.base).resolve(), Path(a.cand).resolve()
    work = Path(a.out or tempfile.mkdtemp(prefix="toy_gate_"))
    from concurrent.futures import ThreadPoolExecutor
    report = {"seeds": seeds, "days": a.days, "base": str(base), "cand": str(cand), "toys": {}}
    toys = a.toys.split(",")
    for toy, period in (("cluster", 60.0), ("cluster15", 15.0)):
        if toy not in toys:
            continue
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "native" if j[0] == "native" else "omni", "--seed", str(j[2]),
                                                    "--days", str(a.days), "--period", str(period),
                                                    "--dir", str(work / toy / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
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
                 for k in ("steps_allowed", "steps_refused", "trials_abandoned", "machines_parked", "errors")}
        report["toys"][toy] = {"period_s": period, "gauges": rows, "counts": extra, "per_seed": res}
    # the convey toy twice: the namespace's quota readable and empty, and unreadable (the governor's role cannot list
    # quotas on every kind test, and on any stack whose role withholds it; the first v7 trial read that as a zero budget)
    for toy, quota in (("convey", "none"), ("convey_unreadable_quota", "unreadable")):
        if toy not in toys:
            continue
        jobs = [(arm, tree, s) for s in seeds for arm, tree in (("native", cand), ("base", base), ("cand", cand))]
        with ThreadPoolExecutor(a.jobs) as ex:
            got = list(ex.map(lambda j: run(j[1], ["--worker", "convey-native" if j[0] == "native" else "convey-omni",
                                                    "--seed", str(j[2]), "--quota", quota,
                                                    "--dir", str(work / toy / f"{j[0]}-{j[2]}")]), jobs))
        res = {}
        for (arm, _, s), r in zip(jobs, got):
            res.setdefault(arm, {})[s] = r
        rows = {}
        for g in CONVEY_GAUGES:
            bv = [res["base"][s][g] for s in seeds]; cv = [res["cand"][s][g] for s in seeds]
            nv = [res["native"][s][g] for s in seeds]
            rows[g] = {"native": sum(nv) / len(nv), "base": sum(bv) / len(bv), "cand": sum(cv) / len(cv),
                       "cand_vs_base": reading(g, [c - b for c, b in zip(cv, bv)], bv, CONVEY_GAUGES),
                       "base_vs_native": reading(g, [b - n for b, n in zip(bv, nv)], nv, CONVEY_GAUGES),
                       "cand_vs_native": reading(g, [c - n for c, n in zip(cv, nv)], nv, CONVEY_GAUGES)}
        report["toys"][toy] = {"gauges": rows, "counts": {k: {arm: sum(res[arm][s][k] for s in seeds) for arm in ("native", "base", "cand")}
                                                          for k in ("starts", "starts_past_75")}, "per_seed": res}
    if "verdict" in toys:
        report["toys"]["verdict"] = {"base": run(base, ["--worker", "verdict", "--seed", "300"]),
                                     "cand": run(cand, ["--worker", "verdict", "--seed", "300"])}
    (work / "TOY_GATE.json").write_text(json.dumps(report, indent=1))
    for toy, r in report["toys"].items():
        print(f"\n== {toy}" + (f" (a decision every {r['period_s']:.0f} s)" if "period_s" in r else ""))
        if toy == "verdict":
            print("share of give-back steps allowed, by the step's true extra cost (2% allowance, noisy work):")
            for k in r["base"]:
                print(f"  +{100 * float(k):.0f}%: standing {100 * r['base'][k]:.0f}%  candidate {100 * r['cand'][k]:.0f}%")
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
