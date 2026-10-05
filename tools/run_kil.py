#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The whole stacks with the real Kubernetes cluster inside: one organism, one clock, one engine.

Started by scripts/kind_bench.sh when ORGANISM is set (kind on GitHub, or AKS on Azure). One of the six organisms of
tools/run_hil.py (the four realms, the four stacked with every duplicate kept, 1,226, and the whole tower of 656) runs
on the measured window's clock, ORGANISM_STEPS steps, and the real cluster is wired into it as one more muscle:

  efferent  the organism's own compute demand drives the cluster. Demand at step k is the organism's offered work
            over its declared mean (sum over its compute pools of lam[k] / lam0, the seeded trace, the same in both
            arms). The load generator runs 1 + round((LOAD_MAX - 1) * (demand[k] - least) / (most - least))
            replicas: the organism's quietest step is one generator, its peak is LOAD_MAX, so the cluster serves the
            organism's own swings across the whole declared range.
  afferent  the cluster's watts (capture.csv, the declared power model, the same in both arms) are heat in the
            organism's thermal zones and load on its storage sites, as the card's watts are in tools/run_hil.py.

Arms, the same organism, the same seed, the same demand:
  native  the stacks' own controllers, and Kubernetes alone underneath (Omni-Compass not started)
  omni / bowl  one engine on everything: the bowl law (omnicompass/bowl.py) on every simulated muscle
          (realms/bowl_arm.py) and the live controller on the cluster (started by kind_bench.sh). At KILL_AT of the
          window every simulated knob is handed back, and this file checks it was.

Writes organism.json (every plant's receipt, the steps, the replica trace, the cluster's watts as the organism saw
them) and appends each replica change to load_schedule.log in the format scripts/kind_bench.sh writes.

Sizes (--scale): 1, 10, 100 or 1,000 copies of the organism governed together on one clock (as tools/run_hil.py), the
one real cluster inside. A large organism is built before the window opens: this file writes organism.ready when it is
built and starts on the epoch written to the go file (--go-file), so the cluster's window and the organism's clock open
together however long the build takes.

  python3 tools/run_kil.py --organism organism_656 --arm bowl --duration 960 --out DIR [--scale 10] [--go-file F]
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import Body, KILL_AT  # noqa: E402
from realms.bowl_arm import bowl_apply  # noqa: E402
from realms.presets import ORGANISM_STEPS  # noqa: E402
from tools.run_hil import groups, NAMES, SEED0  # noqa: E402

OMNI_ARMS = ("omni", "bowl", "strict")


def demand_trace(body):
    """The organism's offered compute work over its declared mean, per step (the seeded trace: arm-independent)."""
    pools = [p for p in body.plants if hasattr(p, "lam")]
    if not pools:
        return [1.0] * ORGANISM_STEPS
    lam0 = sum(p.P["lam0"] for p in pools) or 1.0
    return [sum(p.lam[k] for p in pools) / lam0 for k in range(ORGANISM_STEPS)]


def replicas_of(trace, load_max):
    """The organism's lowest demand is one load generator, its peak is load_max, linear between: its own swings,
    across the whole range the operator declared."""
    lo, hi = min(trace), max(trace)
    if hi - lo < 1e-12:
        return [max(1, load_max // 2)] * len(trace)
    return [max(1, min(load_max, 1 + round((load_max - 1) * (d - lo) / (hi - lo)))) for d in trace]


def cluster_w(capture, fallback):
    """The cluster's latest watts from capture.csv (the declared power model, every 15 s, in every arm)."""
    try:
        rows = list(csv.DictReader(open(capture)))
        for r in reversed(rows):
            if r.get("power_w"):
                return float(r["power_w"])
    except (OSError, ValueError):
        pass
    return fallback


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--organism", required=True, choices=sorted(NAMES))
    ap.add_argument("--arm", required=True)
    ap.add_argument("--duration", type=float, required=True, help="the measured window (s); one step is duration / steps")
    ap.add_argument("--out", required=True)
    ap.add_argument("--start-at", type=float, default=0.0, help="epoch second the window opens (built before, run after)")
    ap.add_argument("--go-file", default="", help="wait for this file (the window's start epoch inside) after organism.ready")
    ap.add_argument("--scale", type=int, default=int(os.environ.get("ORGANISM_SCALE", 1)),
                    help="copies of the organism on one clock (1, 10, 100, 1000)")
    ap.add_argument("--seed", type=int, default=int(os.environ.get("ORGANISM_SEED", SEED0)))
    ap.add_argument("--load-max", type=int, default=int(os.environ.get("LOAD_MAX", 6)),
                    help="load-generator replicas at the organism's peak demand (the operator's load, declared before the run)")
    ap.add_argument("--kubectl", default=os.environ.get("KUBECTL_ADMIN", "kubectl"))
    ap.add_argument("--dry", action="store_true", help="do not call kubectl (tests)")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = groups(a.scale)[a.organism]
    body = Body(rows, a.seed)
    trace = demand_trace(body)
    reps = replicas_of(trace, a.load_max)
    omni = a.arm in OMNI_ARMS
    step_s = a.duration / ORGANISM_STEPS
    kill_at = int(KILL_AT * ORGANISM_STEPS)
    (out / "organism.ready").write_text(f"{time.time():.0f}\n")
    if a.go_file:
        while not Path(a.go_file).exists():
            time.sleep(1)
        start = float(Path(a.go_file).read_text().split()[0])
        time.sleep(max(0.0, start - time.time()))
    elif a.start_at:
        time.sleep(max(0.0, a.start_at - time.time()))
    t0 = time.time()
    nominal_cluster = None
    writes, last, set_r, seen_w = 0, {}, None, []
    log = open(out / "load_schedule.log", "a")
    for k in range(ORGANISM_STEPS):
        if reps[k] != set_r:
            log.write(f"{time.strftime('%H:%M:%S', time.gmtime())} load-generator replicas -> {reps[k]}\n"); log.flush()
            if not a.dry:
                for _ in range(6):                                   # tried again if the API server does not answer
                    try:
                        if subprocess.run([a.kubectl, "scale", "deployment/load-generator", f"--replicas={reps[k]}",
                                           "--request-timeout=20s"], capture_output=True, timeout=30).returncode == 0:
                            break
                    except subprocess.TimeoutExpired:
                        pass
                    time.sleep(5)
            set_r = reps[k]
        body.couple()
        if omni:
            for p, knob in zip(body.plants, body.knobs):
                if k >= kill_at:
                    p.override = {}
                    continue
                v = bowl_apply(p, knob)
                if v and v != last.get(id(p)):
                    writes += 1
                last[id(p)] = v
        body.step()
        w = cluster_w(out / "capture.csv", nominal_cluster or 0.0)
        if nominal_cluster is None and w:
            nominal_cluster = w
        seen_w.append(w)
        body.src_w += w; body.sz_w += w; body.all_w += w          # the cluster's watts in the organism
        wait = t0 + (k + 1) * step_s - time.time()
        if wait > 0:
            time.sleep(wait)
    restore_ok = True
    for p in body.plants:
        p.finalize()
        restore_ok = restore_ok and (not omni or p.override == {})
    rec = {"organism": a.organism, "name": NAMES[a.organism], "arm": a.arm, "omni": omni, "seed": a.seed,
           "muscles": len(rows), "scale": a.scale, "steps": ORGANISM_STEPS, "step_s": step_s, "load_max": a.load_max,
           "demand": trace, "replicas": reps, "cluster_w": seen_w, "sim_writes": writes, "sim_restore_ok": restore_ok,
           "plants": [dict(p.m) for p in body.plants], "wall_s": round(time.time() - t0, 1)}
    (out / "organism.json").write_text(json.dumps(rec) + "\n")
    behind = max(0.0, time.time() - t0 - a.duration)
    rec["behind_s"] = round(behind, 1)
    (out / "organism.json").write_text(json.dumps(rec) + "\n")
    print(f"{NAMES[a.organism]} x{a.scale}, arm {a.arm}: behind the window by {behind:.0f} s; {len(rows)} muscles, {ORGANISM_STEPS} steps of {step_s:.2f} s, "
          f"replicas {min(reps)}..{max(reps)}, simulated writes {writes}, handed back {restore_ok}")
    return 0 if restore_ok else 2


if __name__ == "__main__":
    sys.exit(main())
