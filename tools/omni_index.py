#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The Omni index: one number for more for the same, or the same for less (docs/K8S_COMPASS_PREREGISTRATION.md).

Every measure of every test is turned into a ratio oriented so that above 1 is better for Omni-Compass:

  work      work with Omni / work native        (capacity, or requests served)
  speed     p95 native / p95 with Omni          (a lower response time is faster)
  machines  machines native / machines with Omni (in service, or billed machine-hours)
  energy    energy native / energy with Omni    (or the bill)

A test's index is the geometric mean of its ratios, minus one, in percent. A category is the geometric mean of its
tests; the headline is the geometric mean of the real categories, each weighted the same. The modelled muscles are
shown beside the headline, never inside it. Every number is read from the test's own result file (SOURCES below names
the file, the table and the row); nothing is typed in. A test that did not take a measure leaves it out.

  python3 tools/omni_index.py  ->  results/OMNI_INDEX.md, results/OMNI_INDEX.json
"""
from __future__ import annotations

import json

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "results" / "live"

# The three-run tables (tools/confirm_abc.py, docs/OMNI_V1.md, docs/OMNI_V3.md): each test's three runs on the frozen engine, every row with
# its reading by rule. (category, test, file, {measure: row key}, work). work: "equal" (the same fixed-rate work was sent
# to both arms and none failed: ratio 1), "capacity" (the capacity row of that table), or None (not taken). A measure
# counts only as its reading allows: confirmed better or confirmed WORSE over all three runs gives the geometric mean of
# the three runs' ratios; no difference beyond the noise, same, or the runs disagree gives exactly 1 (nothing is claimed
# either way). Azure's billed runs and the six organisms join the index when their v1 tables land.
P95 = "response time (ms), 95th percentile"
MEAN = "response time (ms), mean"
NODES = "worker nodes in service, mean"
ENERGY = "energy, parked workers still on at idle power (Wh)"
STANDBY = "energy (Wh)"
CAPACITY = "work inside the response line (requests a second; the capacity test's own gauge, higher is better)"
SOURCES = [
    ("Real Kubernetes (GitHub)", "Steady same work: the load in steps at a fixed rate, ten pairs, three runs", "V1_STEADY.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, "equal"),
    ("Real Kubernetes (GitHub)", "Demand that wanders: up and down one step at a time, ten pairs, three runs", "V1_WANDERING.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "All four in one run: load up and down one step at a time, ten pairs, three runs", "V1_ALL_FOUR.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, "capacity"),
    ("Real Kubernetes (GitHub)", "Fairness: a noisy neighbour, ten pairs, three runs", "V1_FAIRNESS.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "Faults: machine down, spike, runaway pod, blind probe, ten pairs, three runs", "V1_FAULTS.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "A queue of jobs: cruise, then the emergency brake, ten pairs, three runs", "V1_BATCH.json",
     {"speed": MEAN, "machines": NODES, "energy": STANDBY}, None),
]
REAL = ("Real Kubernetes (GitHub)", "Real database (PostgreSQL behind PgBouncer, GitHub)", "Real cloud (Azure AKS, billed)",
        "Real card (NVIDIA, its own meter)")
# the database's three-run table (tools/pgbench_abc.py): per workload, work = transactions inside the line, speed = p95,
# machines = the connections held open to the database; energy = the host's CPU seconds over the run (no meter on a GitHub
# runner; the CPU the compass itself burns is the declared cost, and a confirmed loss there counts against Omni)
DB_FILE = "V3_PGBENCH.json"
DB_MEASURES = {"work": "work_inside_line_tps", "speed": "p95_ms", "machines": "servers_alive_mean", "energy": "cpu_seconds"}
LOWER_IS_BETTER = {"speed", "machines", "energy"}
PENDING = {"Real cloud (Azure AKS, billed)": "the v1 steady and burst runs on Azure (the earlier engine's +7.5% is in `docs/history/OMNI_INDEX_pre_v1.md`)",
           "Real card (NVIDIA, its own meter)": "the rerun on the current card controller (the 2026-10-02 run used the replaced one)"}


def ratio(measure, native, omni):
    if native is None or omni is None or native <= 0 or omni <= 0:
        return None
    return native / omni if measure in LOWER_IS_BETTER else omni / native


def gmean(xs):
    xs = [x for x in xs if x]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else None


def measure(row, m):
    """One measure's ratio over the three runs, as its reading allows: confirmed in all three gives the geometric mean
    of the runs' ratios (a confirmed loss counts against Omni); anything else is exactly 1, nothing claimed."""
    reading = row["reading"]
    rs = [ratio(m, r["native"], r["omni"]) for r in row["runs"]]
    g = gmean(rs) if reading.startswith("confirmed") and all(rs) else 1.0
    return {"native": row["runs"][0]["native"], "omni": row["runs"][0]["omni"], "ratio": g, "reading": reading}


def tests():
    out = []
    for cat, name, f, measures, work in SOURCES:
        path = LIVE / f
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        rows_ = data["rows"]
        r = {m: measure(rows_[key], m) for m, key in measures.items() if key in rows_}
        if work == "equal":
            r["work"] = {"native": 1.0, "omni": 1.0, "ratio": 1.0, "reading": "the same fixed-rate work sent to both arms"}
        elif work == "capacity" and CAPACITY in rows_:
            r["work"] = measure(rows_[CAPACITY], "work")
        out.append({"category": cat, "test": name, "source": f"results/live/{f}", "runs": [x["run"] for x in data["runs"]],
                    "v1": bool(data.get("v1")), "measures": r})
    db = LIVE / DB_FILE
    if db.exists():
        data = json.loads(db.read_text())
        for wl, gauges in sorted(data["workloads"].items()):
            r = {}
            for m, key in DB_MEASURES.items():
                g = gauges.get(key)
                if not g or any(x is None for x in g["runs"]):
                    continue
                reading = g["reading"]
                if reading.startswith("confirmed"):
                    ratios = [(x["omni"] / x["native"]) if m == "work" else (x["native"] / x["omni"]) for x in g["runs"] if x["native"] and x["omni"]]
                    ratio = gmean(ratios) if ratios else 1.0
                else:
                    ratio = 1.0
                r[m] = {"native": g["runs"][0]["native"], "omni": g["runs"][0]["omni"], "ratio": ratio, "reading": reading}
            out.append({"category": "Real database (PostgreSQL behind PgBouncer, GitHub)", "test": f"pgbench `{wl}`: the pooler's pool size, three paired repetitions, three runs",
                        "source": f"results/live/{DB_FILE}", "runs": [x["run"] for x in data["runs"]], "v1": False, "measures": r})
    for t in out:
        g = gmean([m["ratio"] for m in t["measures"].values()])
        t["index_pct"] = 100 * (g - 1) if g else None
    return out


def pct(x):
    return "" if x is None else f"{100 * (x - 1):+.1f}%"


def main():
    ts = tests()
    cats = {}
    for t in ts:
        cats.setdefault(t["category"], []).append(t)
    cat_g = {c: gmean([1 + t["index_pct"] / 100 for t in v if t["index_pct"] is not None]) for c, v in cats.items()}
    real = [cat_g[c] for c in REAL if c in cat_g]
    head = gmean(real)
    avg = lambda c, m: gmean([t["measures"][m]["ratio"] for t in cats[c] if m in t["measures"]])
    L = ["# The Omni index: more for the same, or the same for less", "",
         "Every measure of every test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: "
         "work (more is better), speed (a lower response time), machines (fewer), energy (less). A test's index is the "
         "geometric mean of its ratios; a category is the geometric mean of its tests; the headline is the geometric "
         "mean of the real categories, each weighted the same. Modelled muscles are shown beside it, never inside it. "
         "Every number is read from the test's own three-run table (`results/live/V1_*.json` and `results/live/V3_*.json`, made by "
         "`tools/confirm_abc.py` and `tools/pgbench_abc.py` from the three archived runs; `tools/omni_index.py`).", "",
         f"## Headline: Omni-Compass on top of native, real machines, confirmed three times: **{pct(head)}** "
         f"(more for the same, or the same for less, across work, speed, machines and energy)", "",
         "A measure enters only as its three-run reading allows (`docs/OMNI_V1.md`): confirmed better or confirmed worse in all "
         "three runs counts, as the geometric mean of the runs' ratios; no difference beyond the noise counts as exactly 1, so "
         "nothing inside the noise is claimed either way. Real Kubernetes (Omni v1) and the real database (Omni v3) are the real "
         "categories in; Azure and the card join as their three-run tables land. The law, controllers and runners are the same bytes "
         "in v1 and v3 (`docs/OMNI_V3.md`); each table names the engine it ran on.", "",
         "| Category | Index | More work by | Faster by (native p95 / omni p95) | Fewer machines by | Less energy by | Tests |", "|---|---:|---:|---:|---:|---:|---:|"]
    for c in list(REAL) + ["Modelled muscles (evidence S)"]:
        if c in cats:
            L.append(f"| {c} | **{pct(cat_g[c])}** | {pct(avg(c, 'work'))} | {pct(avg(c, 'speed'))} | {pct(avg(c, 'machines'))} | "
                     f"{pct(avg(c, 'energy'))} | {len(cats[c])} |")
        elif c in PENDING:
            L.append(f"| {c} | pending | | | | | {PENDING[c]} |")
    L += ["", "Read: every column points the same way, plus is good for Omni-Compass. \"Fewer machines by +4%\" means Omni did the "
          "same work on 4% fewer machine-hours; \"less energy by +3%\" means 3% less energy for the same work; \"faster by +95%\" means "
          "native's slowest-5% response is 1.95 times Omni's (Omni answers about twice as fast); \"more work by +45%\" means 45% more work "
          "inside the response line. The energy figure on GitHub's Kubernetes is a declared model, not a meter; the database's energy column "
          "is the host's CPU seconds (the compass's own cost, confirmed worse, counted against Omni); its machines column is the "
          "connections held open to the database; Azure's machines are its own billed count.",
          "", "## Every test", "",
          "| Category | Test | Index | More work by | Faster by | Fewer machines by | Less energy by | Source |", "|---|---|---:|---:|---:|---:|---:|---|"]
    for t in ts:
        m = t["measures"]
        def cell(k):
            if k not in m:
                return "not taken"
            rd = m[k].get("reading", "")
            if rd.startswith("confirmed"):
                return pct(m[k]["ratio"])
            return "equal" if rd.startswith("the same") else ("same" if rd == "same" else "no difference beyond the noise")
        ix = "" if t["index_pct"] is None else f"{t['index_pct']:+.1f}%"
        L.append(f"| {t['category']} | {t['test']} | **{ix}** | {cell('work')} | {cell('speed')} | {cell('machines')} | "
                 f"{cell('energy')} | `{t['source']}` |")
    (ROOT / "results" / "OMNI_INDEX.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    (ROOT / "results" / "OMNI_INDEX.json").write_text(json.dumps(
        {"headline_pct": None if head is None else 100 * (head - 1),
         "categories": {c: None if g is None else 100 * (g - 1) for c, g in cat_g.items()}, "tests": ts}, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
