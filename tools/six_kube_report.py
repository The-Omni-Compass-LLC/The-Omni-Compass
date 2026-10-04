#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The six organisms with the real cluster inside: twelve columns, one report.

Reads every bench-<arm>-<rep>/ under DIR that carries organism.json (tools/run_kil.py, started by scripts/kind_bench.sh
with ORGANISM set), groups the runs by organism, and pairs each Omni arm with native by repetition. Each organism gives
two columns, native and native with Omni-Compass on top: six organisms, twelve columns.

Two kinds of rows, kept apart:
  the cluster  real Kubernetes, measured (response times from the probe, pods, replicas and CPU from the API server;
               energy from the declared power model; on AKS the bill from Azure's own count of machines)
  the organism the simulated stacks around it (evidence S, models): work, energy, time over the line

The one rule labels each organism: no measure more than 2% worse than native (a measure that is more or less by
itself, CPU and host load, is shown and not judged), and a gain counts only where energy or the bill is lower.

  python3 tools/six_kube_report.py DIR   ->  DIR/SIX_KUBE.md, DIR/SIX_KUBE.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.live_reps import arm_gauges, T95, LABEL, NEUTRAL  # noqa: E402
from tools.run_hil import NAMES, REALMS  # noqa: E402
from pilot.bench_report import LOWER_BETTER  # noqa: E402

ORDER = list(REALMS) + ["organism_656", "stack_1226"]
OMNI = ("bowl", "omni")
CLUSTER = ["response time (ms), 95th percentile", "response time (ms), 99th percentile",
           "time over the response line (% of samples)", "failed requests (%)", "HPA replicas, mean", "pods started",
           "worker nodes in service, mean", "energy, parked workers still on at idle power (Wh)", "energy (Wh)",
           "CPU used with Omni's own (cores), mean", "host CPU busy, the real machine under kind (%)",
           "machines billed, machine-hours", "compute bill at list price ($)"]
ORG = ["organism work", "organism energy (J)", "organism time over the line (% of steps)", "organism work per energy"]
SAVING = {"energy, parked workers still on at idle power (Wh)", "energy (Wh)", "organism energy (J)",
          "machines billed, machine-hours", "compute bill at list price ($)"}
HIGHER_BETTER = {"organism work", "organism work per energy"}
LOWER = set(LOWER_BETTER) | {"organism energy (J)", "organism time over the line (% of steps)",
                             "machines billed, machine-hours", "compute bill at list price ($)"}


def organism_gauges(rec):
    pl = rec["plants"]
    work = sum(p["work"] for p in pl)
    energy = sum(p["energy_j"] for p in pl)
    steps = sum(p["steps"] for p in pl) or 1
    return {"organism work": work, "organism energy (J)": energy,
            "organism time over the line (% of steps)": 100.0 * sum(p["viol"] for p in pl) / steps,
            "organism work per energy": work / energy if energy else float("nan")}


def collect(root):
    runs = {}
    for d in sorted(root.rglob("bench-*-*")):
        if not d.is_dir() or not (d / "organism.json").exists() or (d / "INVALID").exists() or not (d / "capture.csv").exists():
            continue
        rec = json.loads((d / "organism.json").read_text())
        _, arm, rep = d.name.split("-", 2)
        g = arm_gauges(d)
        g.update(organism_gauges(rec))
        g["_restore_ok"] = rec.get("sim_restore_ok", True)
        runs.setdefault(rec["organism"], {}).setdefault(arm, {})[rep] = g
    return runs


def paired(runs_o, a, k):
    reps = sorted(set(runs_o.get(a, {})) & set(runs_o.get("native", {})))
    xs = [(runs_o["native"][r].get(k, math.nan), runs_o[a][r].get(k, math.nan)) for r in reps]
    xs = [(n, o) for n, o in xs if not (math.isnan(n) or math.isnan(o))]
    if not xs:
        return None
    d = [o - n for n, o in xs]
    nb = sum(n for n, _ in xs) / len(xs); m = sum(d) / len(d)
    if len(d) > 1:
        sd = math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1)); h = T95.get(len(d) - 1, 1.96) * sd / math.sqrt(len(d))
    else:
        h = math.nan
    pct = 100.0 * m / abs(nb) if abs(nb) > 1e-12 else math.nan
    if k in NEUTRAL or k == "host CPU busy, the real machine under kind (%)":
        worse = False
    elif k in HIGHER_BETTER:
        worse = pct < -2.0
    else:
        worse = pct > 2.0
    better = (m > 0) if k in HIGHER_BETTER else (m < 0)
    return {"n": len(d), "native": nb, "omni": nb + m, "diff": m, "lo": m - h, "hi": m + h, "pct": pct,
            "worse_2pct": bool(worse and k not in NEUTRAL), "better": bool(better), "neutral": k in NEUTRAL}


def main(root):
    root = Path(root)
    runs = collect(root)
    orgs = [o for o in ORDER if o in runs]
    keys = [k for k in CLUSTER + ORG if any(not math.isnan(g.get(k, math.nan)) for o in orgs for arms in runs[o].values()
                                             for g in arms.values())]
    out = {"organisms": {}}
    L = ["# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top", "",
         "Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its "
         "own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own "
         "controllers and Kubernetes alone. Omni: the bowl law on every simulated muscle and the live controller on the "
         "cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared "
         "power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).", "",
         "## Twelve columns, mean over repetitions", ""]
    cols = []
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        cols += [(o, "native")] + ([(o, arm)] if arm else [])
    L.append("| Gauge | " + " | ".join(f"{NAMES[o]}: {'native' if a == 'native' else 'native + Omni'}" for o, a in cols) + " |")
    L.append("|---|" + "---:|" * len(cols))
    for k in keys:
        cells = []
        for o, a in cols:
            v = [g.get(k, math.nan) for g in runs[o][a].values()]
            v = [x for x in v if not math.isnan(x)]
            cells.append(f"{sum(v) / len(v):.4g}" if v else "")
        L.append(f"| {LABEL.get(k, k)} | " + " | ".join(cells) + " |")
    L += ["", "## Each organism: native + Omni against native, paired by repetition", ""]
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        if not arm or "native" not in runs[o]:
            L += [f"### {NAMES[o]}", "", "No paired arms.", ""]
            continue
        rows = {k: paired(runs[o], arm, k) for k in keys}
        rows = {k: v for k, v in rows.items() if v}
        n = max((v["n"] for v in rows.values()), default=0)
        worse = [k for k, v in rows.items() if v["worse_2pct"]]
        saved = [k for k, v in rows.items() if k in SAVING and v["better"] and v["n"] > 1 and v["hi"] < 0]
        restored = all(g["_restore_ok"] for g in runs[o][arm].values())
        if n < 2:
            verdict = "ONE REPETITION (no label)"
        elif worse:
            verdict = "NOT LABELLED: " + "; ".join(f"{LABEL.get(k, k)} {rows[k]['pct']:+.1f}%" for k in worse)
        elif saved:
            verdict = "BETTER BY THE ONE RULE: nothing more than 2% worse; saved " + ", ".join(LABEL.get(k, k) for k in saved)
        else:
            verdict = "NO WORSE (nothing more than 2% worse; no saving shown)"
        if not restored:
            verdict += "; INVALID: a simulated knob was not handed back"
        out["organisms"][o] = {"arm": arm, "repetitions": n, "verdict": verdict, "rows": rows}
        L += [f"### {NAMES[o]}: {verdict}", "", f"{n} paired repetitions.", "",
              "| Gauge | Native | Native + Omni | Change | 95% interval of the difference |", "|---|---:|---:|---:|---:|"]
        for k, v in rows.items():
            ch = f"{v['pct']:+.1f}%" if not math.isnan(v["pct"]) else f"{v['diff']:+.3g}"
            ci = f"{v['lo']:+.4g} to {v['hi']:+.4g}" if v["n"] > 1 else ""
            L.append(f"| {LABEL.get(k, k)} | {v['native']:.4g} | {v['omni']:.4g} | {ch} | {ci} |")
        L.append("")
    missing = [o for o in ORDER if o not in runs]
    if missing:
        L += ["## Not in this run", ""] + [f"- {NAMES[o]}" for o in missing] + [""]
    (root / "SIX_KUBE.md").write_text("\n".join(L) + "\n")
    (root / "SIX_KUBE.json").write_text(json.dumps(out, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
