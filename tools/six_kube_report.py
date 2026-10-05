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

Each organism's line names what came out better and what came out worse than native, by any amount, and which of
those are inside the noise (the interval crosses zero). CPU and host load are shown, not judged. No line is drawn.

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


def scale_of(key):
    return int(key.split("@")[1]) if "@" in key else 1


def name_of(key):
    """An organism's name, with its size when it runs as more than one copy on one clock."""
    o = key.split("@")[0]
    return NAMES[o] + (f", {scale_of(key):,} copies" if scale_of(key) > 1 else "")


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
        sc = int(rec.get("scale", 1))
        runs.setdefault(rec["organism"] if sc == 1 else f"{rec['organism']}@{sc}", {}).setdefault(arm, {})[rep] = g
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
    better = (m > 0) if k in HIGHER_BETTER else (m < 0)
    if abs(m) <= 1e-9 * max(abs(nb), 1e-12):          # a change below a billionth of the value is rounding: the same
        m = 0.0
    return {"n": len(d), "native": nb, "omni": nb + m, "diff": m, "lo": m - h, "hi": m + h, "pct": pct,
            "better": bool(better), "neutral": k in NEUTRAL}


def main(root):
    root = Path(root)
    runs = collect(root)
    orgs = sorted(runs, key=lambda o: (scale_of(o), ORDER.index(o.split("@")[0])))
    keys = [k for k in CLUSTER + ORG if any(not math.isnan(g.get(k, math.nan)) for o in orgs for arms in runs[o].values()
                                             for g in arms.values())]
    out = {"organisms": {}}
    L = ["# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top", "",
         "Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its "
         "own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own "
         "controllers and Kubernetes alone. Omni: the bowl law on every simulated muscle and the live controller on the "
         "cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared "
         "power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).", "",
         "How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is "
         "better or worse. Lower is better for response times, time over the line, failed requests, pods started, "
         "replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per "
         "energy. A change whose interval crosses zero is marked inside the noise.", "",
         "## Twelve columns, mean over repetitions", ""]
    cols = []
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        cols += [(o, "native")] + ([(o, arm)] if arm else [])
    L.append("| Gauge | " + " | ".join(f"{name_of(o)}: {'native' if a == 'native' else 'omni'}" for o, a in cols) + " |")
    L.append("|---|" + "---:|" * len(cols))
    for k in keys:
        cells = []
        for o, a in cols:
            v = [g.get(k, math.nan) for g in runs[o][a].values()]
            v = [x for x in v if not math.isnan(x)]
            cells.append(f"{sum(v) / len(v):.4g}" if v else "")
        L.append(f"| {LABEL.get(k, k)} | " + " | ".join(cells) + " |")
    L += ["", "## Each organism: omni against native, paired by repetition", ""]
    for o in orgs:
        arm = next((a for a in OMNI if a in runs[o]), None)
        if not arm or "native" not in runs[o]:
            L += [f"### {name_of(o)}", "", "No paired arms.", ""]
            continue
        rows = {k: paired(runs[o], arm, k) for k in keys}
        rows = {k: v for k, v in rows.items() if v}
        n = max((v["n"] for v in rows.values()), default=0)
        restored = all(g["_restore_ok"] for g in runs[o][arm].values())
        sure = lambda v: v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
        judged = {k: v for k, v in rows.items() if not v["neutral"] and k != "host CPU busy, the real machine under kind (%)" and abs(v["diff"]) > 0.0}
        better = [LABEL.get(k, k) for k, v in judged.items() if v["better"] and sure(v)]
        worse = [LABEL.get(k, k) for k, v in judged.items() if not v["better"] and sure(v)]
        noise = [LABEL.get(k, k) for k, v in judged.items() if not sure(v)]
        verdict = (f"better on {len(better)}, worse on {len(worse)}" + (f" ({'; '.join(worse)})" if worse else "")
                   + f", inside the noise on {len(noise)}") if n >= 2 else "ONE REPETITION"
        if not restored:
            verdict += "; INVALID: a simulated knob was not handed back"
        out["organisms"][o] = {"arm": arm, "repetitions": n, "verdict": verdict, "rows": rows}
        L += [f"### {name_of(o)}: {verdict}", "", f"{n} paired repetitions.", "",
              "| Gauge | native | omni | Change | 95% interval of the difference | Reading |", "|---|---:|---:|---:|---:|---|"]
        for k, v in rows.items():
            ch = f"{v['pct']:+.1f}%" if not math.isnan(v["pct"]) else f"{v['diff']:+.3g}"
            ci = f"{v['lo']:+.4g} to {v['hi']:+.4g}" if v["n"] > 1 else ""
            if v["neutral"] or k == "host CPU busy, the real machine under kind (%)":
                rd = "shown, not judged (more or less is not better by itself)"
            elif v["diff"] == 0.0:
                rd = "same"
            else:
                sure = v["n"] > 1 and (v["lo"] > 0 or v["hi"] < 0)
                rd = ("better" if v["better"] else "WORSE") + ("" if sure else " (inside the noise)")
            L.append(f"| {LABEL.get(k, k)} | {v['native']:.4g} | {v['omni']:.4g} | {ch} | {ci} | {rd} |")
        L.append("")
    missing = [o for o in ORDER if not any(k.split("@")[0] == o for k in runs)]
    if missing:
        L += ["## Not in this run", ""] + [f"- {name_of(o)}" for o in missing] + [""]
    (root / "SIX_KUBE.md").write_text("\n".join(L) + "\n")
    (root / "SIX_KUBE.json").write_text(json.dumps(out, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
