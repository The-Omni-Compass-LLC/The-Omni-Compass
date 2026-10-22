#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat sweep (our own model, evidence class S; the founder's questions of 22 October: does a decision every 10
or 5 seconds do better than 15, is 20 different, and what does a faster beat cost the engine): the shipped controller of
a checkout at a decision every 5, 10, 15, 20, 30 and 60 s on one 5-second plant, against native, in two settings.

  cloud    tools/toy_gate.py's cloud toy (cloud_toy, fine): the cloud's own autoscaler makes and deletes machines in every
           arm; the governor on the machines alone (--give-back-only), as every cloud set runs it.
  onsite   pilot/selfpilot.py's plant cut into 5-second steps: native is the pod autoscaler with the cluster autoscaler;
           with Omni-Compass the governor sizes the pool itself (nodepool mode, the max), as the live page's trace 5e.

The model (the plant, the requests, the response time) is the candidate's file for every arm; the engine is imported from
the checkout under test. The governor's own cost is the process's CPU time less the native arm's on the same seed.

  python3 tools/heartbeat_sweep.py --cand CAND --base BASE --out OUT [--seeds 1-8] [--periods 5,10,15,20,30,60] [--jobs 4]
  python3 tools/heartbeat_sweep.py --one SETTING ARM SEED PERIOD DIR CAND   (one run, inside the checkout under test)

The record of 22 October is results/toy_gate/HEARTBEAT_SWEEP.md (its table, written from OUT/results.jsonl).
"""
import argparse, importlib.util, json, os, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve()


def model(cand):
    spec = importlib.util.spec_from_file_location("toy_model", Path(cand) / "tools" / "toy_gate.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def onsite_toy(seed, days, autoscaler):
    from pilot.selfpilot import SimCluster, SimKube
    from fleet.harness import hpa_step
    from fleet.sim import ALLOC, _cluster_autoscaler
    SUB = 3; STEP_S = 15.0 / SUB

    class Fine(SimCluster):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.u = 0; self.steps = self.steps * SUB; self.acc = {}; self.parked = []

        def tick(self):
            c, p = self.c, self.c.pool
            t = self.u // SUB
            sync = (self.u + 1) % SUB == 0
            if self.u % SUB == 0:
                p.booting = [b - 1 for b in p.booting]; p.nodes += sum(1 for b in p.booting if b <= 0)
                p.booting = [b for b in p.booting if b > 0]
            alloc = p.nodes * p.cores * ALLOC
            reqs = sum(w.replicas * w.request for w in c.workloads)
            frac = min(1.0, alloc / reqs) if reqs > 0 else 1.0
            used = 0.0
            for w in c.workloads:
                capw = w.replicas * w.request * frac
                srv = min(w.demand[t] / SUB + w.backlog, capw / SUB)
                w.backlog = w.demand[t] / SUB + w.backlog - srv; used += srv * SUB
                self.acc.setdefault(w.name, []).append(min(1.0, srv * SUB / max(w.replicas * w.request, 1e-9)))
            c.pending, c.reqs, c.alloc, c.used = max(0.0, reqs - alloc), reqs, alloc, used
            util = min(1.0, used / max(alloc, 1e-9))
            kw = (p.nodes * (p.idle_kw + p.dyn_kw * util) + len(p.booting) * p.idle_kw) * self.scn.pue
            pending_pods = int(sum(max(0, w.replicas - int(w.replicas * frac)) for w in c.workloads))
            cur = sum(w.replicas for w in c.workloads)
            if sync:
                for w in c.workloads:
                    got = self.acc.pop(w.name, None) or [w.metric]
                    w.metric = sum(got) / len(got)
                    before = w.replicas; hpa_step(w, w.target); w.desired = w.replicas; w.current = before
                if self.autoscaler == "ca":
                    _cluster_autoscaler(c)
            self.rows.append(["", self.u * STEP_S, p.nodes, p.nodes + len(p.booting), int(alloc / ALLOC * 1000), int(reqs * 1000),
                              int(used * 1000), pending_pods, len(c.workloads), cur, sum(w.desired for w in c.workloads), kw * 1000])
            self.u += 1
            self.t = self.u // SUB

        def billed(self):
            p = self.c.pool
            return p.nodes + len(p.booting)

    class Kube(SimKube):
        """pilot/selfpilot.py's SimKube with the fields Kubernetes shows that it leaves out: each HPA's range and target, each
        deployment, the pending pods by name (as tools/toy_gate.py's cloud toy shows them)."""
        def get(self, *args):
            import subprocess as sp
            if args[:2] == ("get", "hpa"):
                hp = super().get(*args)
                for h, w in zip(hp["items"], self.sim.c.workloads):
                    h["spec"].update({"minReplicas": int(w.min_rep), "maxReplicas": int(w.max_rep),
                                      "scaleTargetRef": {"kind": "Deployment", "name": w.name}})
                return hp
            if args[:2] == ("get", "pods") and "-o" in args and args[args.index("-o") + 1] == "name":
                c = self.sim.c
                frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
                return "\n".join(f"pod/p{i}" for i in range(sum(w.replicas - int(w.replicas * frac) for w in c.workloads)))
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
                raise sp.CalledProcessError(1, ["kubectl", *args], stderr="not in the toy cluster")

    sim = Fine(seed, days, autoscaler=autoscaler)
    return sim, Kube(sim, None), STEP_S


def one(setting, arm, seed, period, out, cand, days=1.0):
    import numpy as np
    from unittest import mock
    from pilot.score import blocks, load
    from fleet.sim import ALLOC
    M = model(cand)
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    (out / "audit.jsonl").unlink(missing_ok=True)
    rng = np.random.default_rng(seed + 7)
    if setting == "cloud":
        sim, k, STEP_S = M.cloud_toy(seed, days, fine=True)
    else:
        sim, k, STEP_S = onsite_toy(seed, days, "ca" if arm == "native" else "none")
    SUB = int(round(15.0 / STEP_S))
    billed, lat_rows, minute_ms = [], [], {}
    lat_path = out / "latency.csv"
    reads = [0]

    def time_requests():
        c = sim.c
        frac = min(1.0, c.alloc / c.reqs) if c.reqs > 0 else 1.0
        cap = sum(w.replicas * w.request * frac for w in c.workloads)
        dem = sum(w.demand[min(sim.t, len(w.demand) - 1)] for w in c.workloads)
        backlog = sum(w.backlog for w in c.workloads)
        rho = min(0.98, dem / cap) if cap > 0 else 0.98
        mean = M.SERVICE_MS / (1.0 - rho) + (1000.0 * backlog / cap if cap > 0 else 1e4)
        t0 = sim.u * STEP_S
        kk = sim.u % SUB
        n = int(round((kk + 1) * M.SAMPLES_PER_TICK / SUB)) - int(round(kk * M.SAMPLES_PER_TICK / SUB))
        for i in range(n):
            ms = float(mean * rng.lognormal(0.0, 0.25))
            lat_rows.append((t0 + i * STEP_S / n, ms))
            minute_ms.setdefault(int(t0 // 60), []).append(ms)
        del lat_rows[:-60 * M.SAMPLES_PER_TICK]
        with open(lat_path, "w") as f:
            f.write("elapsed_seconds,latency_ms,ok\n")
            f.writelines(f"{t:.2f},{ms:.3f},1\n" for t, ms in lat_rows)

    def alloc_now():
        return (sim.c.pool.nodes + len(getattr(sim, "parked", []))) * sim.c.pool.cores * ALLOC

    decisions = 0
    gov_cpu = 0.0
    if arm != "native":
        from omni_controller.controller import Controller, parser
        common = ["--interval", str(period), "--floor-interval", str(STEP_S), "--latency-file", str(lat_path),
                  "--slo-ms", str(M.SLO_MS), "--audit", str(out / "audit.jsonl"), "--kill-file", str(out / "kill"),
                  "--node-scale-cmd", "SIMSCALE {n}", "--min-nodes", str(sim.c.pool.min_nodes),
                  "--max-nodes", str(sim.c.pool.max_nodes), "--headroom", "0.5"]
        if setting == "cloud":
            argv = ["--mode", "nodepool", "--law", "compass", "--dial", "save", "--sensed", "none/none", *common,
                    "--active-nodes-only", "--max-node-step", "1", "--give-back-only"]
        else:
            argv = ["--mode", "nodepool", *common]
        ctl = Controller(parser().parse_args(argv), kube=k)
        if setting == "onsite":
            ctl.k.audit = ctl.audit
        get0 = ctl.k.get

        def counted_get(*a, **kw):
            reads[0] += 1
            return get0(*a, **kw)
        ctl.k.get = counted_get
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
                sim.tick(); sim.c.alloc = alloc_now()
                time_requests(); billed.append(sim.billed())
                c0 = time.process_time()
                if sim.u % every == 0:
                    fails = shipped.safe_step(ctl, fails) if hasattr(shipped, "safe_step") else (ctl.step() or 0)
                    decisions += 1
                else:
                    try:
                        ctl.floor_step()
                    except Exception as e:
                        ctl.audit({"error": "floor check: " + repr(e)[:500]})
                gov_cpu += time.process_time() - c0
    else:
        while sim.u < sim.steps:
            sim.tick(); time_requests(); billed.append(sim.billed())
    cap = out / "capture.csv"; sim.write_capture(cap)
    rows = load(str(cap))
    day = blocks(rows, 86400 * days + 60, None, None)[0]
    allm = sorted(ms for v in minute_ms.values() for ms in v)
    alert = sum(1 for v in minute_ms.values() if sorted(v)[int(0.95 * len(v))] > M.SLO_MS)
    res = {"machine_hours": sum(billed) * STEP_S / 3600.0, "kwh_per_core_hour": day["kwh_per_core_hour"],
           "pending_pod_minutes_per_hour": day["pending_pod_minutes_per_hour"], "p95_ms": allm[int(0.95 * len(allm))],
           "p99_ms": allm[int(0.99 * len(allm))], "alert_minutes": float(alert), "decisions": float(decisions),
           "governor_cpu_s": gov_cpu, "cluster_reads": float(reads[0]), "writes": 0.0, "machines_parked": 0.0,
           "errors": 0.0}
    if arm != "native":
        recs = [json.loads(l) for l in open(out / "audit.jsonl")]
        res["writes"] = float(sum(1 for r in recs if "write" in r and not r.get("dry_run")))
        res["machines_parked"] = float(sum(1 for r in recs if r.get("write", [None])[0] == "SIMSCALE"))
        res["errors"] = float(sum(1 for r in recs if "error" in r))
    print(json.dumps(res))


def run_one(tree, cand, setting, arm, seed, period, d):
    env = {**os.environ, "PYTHONPATH": str(tree)}
    p = subprocess.run([sys.executable, str(HERE), "--one", setting, arm, str(seed), str(period), str(d), str(cand)],
                       cwd=tree, env=env, capture_output=True, text=True, timeout=7200)
    if p.returncode != 0:
        raise RuntimeError(f"{tree} {setting} {arm} {seed} {period}: {p.stderr[-3000:]}")
    return json.loads(p.stdout.strip().splitlines()[-1])


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        setting, arm, seed, period, d, cand = sys.argv[2:8]
        return one(setting, arm, int(seed), float(period), d, cand)
    ap = argparse.ArgumentParser()
    ap.add_argument("--cand"); ap.add_argument("--base"); ap.add_argument("--out")
    ap.add_argument("--seeds", default="1-8"); ap.add_argument("--periods", default="5,10,15,20,30,60")
    ap.add_argument("--settings", default="cloud,onsite"); ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    lo, _, hi = a.seeds.partition("-"); seeds = list(range(int(lo), int(hi or lo) + 1))
    periods = [float(x) for x in a.periods.split(",")]
    cand, base, out = Path(a.cand).resolve(), Path(a.base).resolve(), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    sts = a.settings.split(",")
    jobs = [(cand, st, "native", s, 15.0) for st in sts for s in seeds]
    for tree_name, tree in (("cand", cand), ("base", base)):          # the candidate first: it is the answer
        for st in sts:
            for p in sorted(periods):
                jobs += [(tree, st, tree_name, s, p) for s in seeds]
    from concurrent.futures import ThreadPoolExecutor
    res_path = out / "results.jsonl"
    done = set()
    if res_path.exists():
        for l in res_path.read_text().splitlines():
            r = json.loads(l); done.add((r["setting"], r["arm"], r["seed"], r["period"]))
    todo = [j for j in jobs if (j[1], j[2], j[3], j[4]) not in done]
    t0 = time.time()

    def go(j):
        tree, st, arm, s, p = j
        r = run_one(tree, cand, st, "native" if arm == "native" else "omni", s, p, out / st / f"{arm}-{p:g}-{s}")
        r.update(setting=st, arm=arm, seed=s, period=p)
        with open(res_path, "a") as f:
            f.write(json.dumps(r) + "\n")
        print(f"{time.time() - t0:7.0f}s {st:6s} {arm:6s} {p:4g}s seed {s}: machines {r['machine_hours']:.2f} h, pending "
              f"{r['pending_pod_minutes_per_hour']:.3f}, p95 {r['p95_ms']:.1f} ms, decisions {r['decisions']:.0f}, "
              f"cpu {r['governor_cpu_s']:.1f} s", flush=True)
        return r
    with ThreadPoolExecutor(a.jobs) as ex:
        list(ex.map(go, todo))


if __name__ == "__main__":
    main()
