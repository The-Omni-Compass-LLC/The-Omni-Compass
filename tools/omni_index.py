#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The Omni index: one number for more for the same, or the same for less (docs/K8S_BOWL_PREREGISTRATION.md).

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
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "results" / "live"

P95 = r"response time.*95th percentile"
NODES = r"worker nodes in service"
ENERGY = r"energy, parked workers still on at idle power"
BILLED = r"machines billed, machine-hours"

# (category, test, file, section heading regex or None, {measure: row regex}, work)
# work: "equal" (the same fixed-rate work was sent to both arms and none failed: ratio 1), "capacity" (read from the
# capacity table of that file), or None (not taken)
SOURCES = [
    *[("Real Kubernetes (GitHub)", f"Set {n}: same work, ten pairs", f"LIVE_REPS_{n}.md", None,
       {"speed": P95, "machines": NODES, "energy": ENERGY}, "equal") for n in (22, 23, 24, 25, 26, 27)],
    ("Real Kubernetes (GitHub)", "Capacity: load rising, ten pairs", "AMENDMENT_3_RUNS.md", r"### Capacity, B with the bowl law",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, "capacity"),
    ("Real Kubernetes (GitHub)", "Fairness: a noisy neighbour, ten pairs", "AMENDMENT_3_RUNS.md", r"## Fairness, B with the bowl law",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "Faults: machine down, spike, runaway pod, blind probe, ten pairs", "AMENDMENT_3_RUNS.md",
     r"### Faults, B with the bowl law", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "All four in one run: load up and down one step at a time, ten pairs", "ALL_FOUR.md",
     r"^## B with the bowl law", {"speed": P95, "machines": NODES, "energy": ENERGY}, "capacity"),
    ("Real cloud (Azure AKS, billed)", "Steady load, Azure's autoscaler underneath, five pairs", "AKS_BILL.md",
     r"## B with the bowl law", {"speed": P95, "machines": BILLED}, "equal"),
]
ORGANISMS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized",
             "organism_656", "stack_1226"]
NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         "organism_656": "the whole tower (656)", "stack_1226": "the four stacked (1,226)"}
REAL = ("Real Kubernetes (GitHub)", "Real cloud (Azure AKS, billed)", "Real card (NVIDIA, its own meter)")
LOWER_IS_BETTER = {"speed", "machines", "energy"}


def num(cell):
    c = cell.replace("**", "").replace("−", "-").replace(",", "").strip()
    m = re.match(r"^[-+]?\d+(\.\d+)?(e[-+]?\d+)?", c)
    return float(m.group(0)) if m else None


def rows(path, section):
    """Table rows (label, cells) of a result file, from the first line matching section (the whole file if None)."""
    lines = path.read_text().splitlines()
    if section:
        start = next((i for i, l in enumerate(lines) if re.search(section, l)), None)
        if start is None:
            raise KeyError(f"{path.name}: no section {section!r}")
        lines = lines[start + 1:]
        end = next((i for i, l in enumerate(lines) if l.startswith("#")), len(lines))
        lines = lines[:end]
    out = []
    for l in lines:
        if l.startswith("|") and not l.startswith("|---"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            out.append((cells[0].replace("**", ""), cells[1:]))
    return out


def pick(table, rx):
    for label, cells in table:
        if re.search(rx, label, re.I) and len(cells) >= 2 and num(cells[0]) is not None and num(cells[1]) is not None:
            return num(cells[0]), num(cells[1])
    return None


def capacity(path):
    for label, cells in rows(path, r"^## (Capacity|The capacity test)"):
        if label == "native":
            n = num(cells[0])
        if label == "bowl":
            return n, num(cells[0])
    return None


def ratio(measure, native, omni):
    if native is None or omni is None or native <= 0 or omni <= 0:
        return None
    return native / omni if measure in LOWER_IS_BETTER else omni / native


def gmean(xs):
    xs = [x for x in xs if x]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else None


def tests():
    out = []
    for cat, name, f, sec, measures, work in SOURCES:
        path = LIVE / f
        if not path.exists():
            continue
        table = rows(path, sec)
        r = {}
        for m, rx in measures.items():
            v = pick(table, rx)
            if v:
                r[m] = {"native": v[0], "omni": v[1], "ratio": ratio(m, *v)}
        if work == "equal":
            r["work"] = {"native": 1.0, "omni": 1.0, "ratio": 1.0, "note": "the same fixed-rate work sent to both arms"}
        elif work == "capacity":
            v = capacity(path)
            if v:
                r["work"] = {"native": v[0], "omni": v[1], "ratio": ratio("work", *v)}
        out.append({"category": cat, "test": name, "source": f"results/live/{f}", "measures": r})
    six = LIVE / "SIX_KUBE.json"
    if six.exists():
        data = json.loads(six.read_text())["organisms"]
        for o in ORGANISMS:
            if o not in data:
                continue
            g = data[o]["rows"]
            get = lambda k: (g[k]["native"], g[k]["omni"]) if k in g else None
            r = {}
            for m, k in (("speed", "response time (ms), 95th percentile"), ("machines", "worker nodes in service, mean"),
                         ("energy", "energy, parked workers still on at idle power (Wh)")):
                v = get(k)
                if v:
                    r[m] = {"native": v[0], "omni": v[1], "ratio": ratio(m, *v)}
            f = get("failed requests (%)")
            if f:
                r["work"] = {"native": 100 - f[0], "omni": 100 - f[1], "ratio": ratio("work", 100 - f[0], 100 - f[1]),
                             "note": "requests served (100 - failed %)"}
            out.append({"category": "Real Kubernetes (GitHub)", "test": f"Six organisms: {NAMES[o]}, the cluster inside, five pairs",
                        "source": "results/live/SIX_KUBE.json", "measures": r})
            mw, me = get("organism work"), get("organism energy (J)")
            rm = {}
            if mw:
                rm["work"] = {"native": mw[0], "omni": mw[1], "ratio": ratio("work", *mw)}
            if me:
                rm["energy"] = {"native": me[0], "omni": me[1], "ratio": ratio("energy", *me)}
            out.append({"category": "Modelled muscles (evidence S)", "test": f"{NAMES[o]}: the modelled stacks around the real cluster",
                        "source": "results/live/SIX_KUBE.json", "measures": rm})
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
         "Every number is read from the test's own result file (`tools/omni_index.py`).", "",
         f"## Headline: Omni-Compass on top of native, real machines: **{pct(head)}** "
         f"(more for the same, or the same for less, across work, speed, machines and energy)", "",
         "| Category | Index | Work | Speed | Machines | Energy | Tests |", "|---|---:|---:|---:|---:|---:|---:|"]
    for c in list(REAL) + ["Modelled muscles (evidence S)"]:
        if c in cats:
            L.append(f"| {c} | **{pct(cat_g[c])}** | {pct(avg(c, 'work'))} | {pct(avg(c, 'speed'))} | {pct(avg(c, 'machines'))} | "
                     f"{pct(avg(c, 'energy'))} | {len(cats[c])} |")
        elif c == "Real card (NVIDIA, its own meter)":
            L.append(f"| {c} | pending | | | | | the rerun on the current card controller (the 2026-10-02 run used the replaced one) |")
    L += ["", "Read: +10% in a column means 10% better for Omni-Compass in that measure (more work, a faster answer, "
          "fewer machines, less energy). The energy figure on GitHub's Kubernetes is a declared model, not a meter; "
          "Azure's machines are its own billed count.", "", "## Every test", "",
          "| Category | Test | Index | Work | Speed | Machines | Energy | Source |", "|---|---|---:|---:|---:|---:|---:|---|"]
    for t in ts:
        m = t["measures"]
        cell = lambda k: pct(m[k]["ratio"]) if k in m else "not taken"
        ix = "" if t["index_pct"] is None else f"{t['index_pct']:+.1f}%"
        L.append(f"| {t['category']} | {t['test']} | **{ix}** | {cell('work')} | {cell('speed')} | {cell('machines')} | "
                 f"{cell('energy')} | `{t['source']}` |")
    (ROOT / "results" / "OMNI_INDEX.md").write_text("\n".join(L) + "\n")
    (ROOT / "results" / "OMNI_INDEX.json").write_text(json.dumps(
        {"headline_pct": None if head is None else 100 * (head - 1),
         "categories": {c: None if g is None else 100 * (g - 1) for c, g in cat_g.items()}, "tests": ts}, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
