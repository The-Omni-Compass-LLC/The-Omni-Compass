# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governors and orchestrators on one page (the founder's list of 19 October, night): every one he named, what it
governs, what native is under it and what Omni-Compass does on top, where its test stands, and, once its three runs are in,
its readings by the one key, every row counted, losses included (results/live/GOVERNORS.md).

A governor's result is its three-run table on the engine that stands (tools/confirm_abc.py writes results/live/V12_<NAME>.md
and .json); until the table exists the page says where the runs stand, never a number. The runs started are listed in
results/live/governors_runs.json, written when they are started.
Usage: python3 tools/governors_page.py [--check]"""
from __future__ import annotations

import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import receipt_key  # noqa: E402

OUT = ROOT / "results" / "live" / "GOVERNORS.md"
RUNS = ROOT / "results" / "live" / "governors_runs.json"
ENGINE = "omni-v12"
REPO_RUNS = "https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/"

# (slug, name, register row, what it governs, native under it, its test) in the founder's order of naming, the
# Kubernetes scheduler first because every other one stands on it
GOVERNORS = [
    ("scheduler", "The Kubernetes scheduler as shipped (vanilla)", 88, "pod placement",
     "the default scheduler of Kubernetes 1.35, as shipped: it places every pod of every Kubernetes set",
     "under every Kubernetes set of the campaign (its own bin-packing set queued)"),
    ("kueue", "Kueue", 63, "batch admission (a job at a time, by queue quota)",
     "Kueue v0.20.2 with the operator's single ClusterQueue sized to the workers",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`"),
    ("volcano", "Volcano", 63, "batch scheduling (queues, gangs)", "Volcano v1.16.0 with its default queue as shipped",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`"),
    ("kai", "KAI scheduler", 91, "AI workload scheduling (queues, fair share, gangs)",
     "the KAI scheduler v0.18.6 with its chart's default queues", "`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 1"),
    ("koordinator", "Koordinator", 89, "QoS colocation (batch work on what latency-sensitive pods leave unused)",
     "Koordinator 1.8.0, colocation on as shipped, the operator's colocation profile",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 2"),
    ("cruisekube", "CruiseKube", 81, "rightsizing (requests and limits, in place)",
     "CruiseKube applying its own recommendations as shipped", "`docs/CRUISEKUBE_PREREGISTRATION.md`"),
    ("crane", "Crane", 90, "predictive autoscaling and resource governance", "its Effective HPA in auto mode", "not yet written"),
    ("kuberay", "KubeRay", 92, "Ray clusters (the Ray autoscaler)", "the Ray autoscaler as shipped", "not yet written"),
    ("godel", "Gödel scheduler", 93, "unified online and offline scheduling", "its placement of units and gangs as shipped",
     "not yet written"),
    ("armada", "Armada", 94, "multi-cluster batch", "its queues and fair share across clusters", "not yet written"),
    ("karmada", "Karmada", 95, "multi-cluster placement", "its propagation and replica division", "not yet written"),
    ("ocm", "Open Cluster Management", 96, "multi-cluster management", "its Placement and ManifestWork", "not yet written"),
    ("kubeedge", "KubeEdge", 97, "edge nodes", "its edge sync and offline autonomy", "not yet written"),
    ("nephio", "Nephio", 98, "network-function automation", "its intent-driven deployment and scaling",
     "not yet written (a candidate: its sandbox asks more than a free runner gives)"),
]

WORDS = ("GAIN", "LOSS", "power given", "EVEN", "the runs disagree", "shown, not judged")


def word_of(reading: str) -> str:
    r = reading.strip()
    if r.startswith("GAIN"):
        return "GAIN"
    if r.startswith("LOSS"):
        return "LOSS"
    if r.startswith("power given"):
        return "power given"
    if r.startswith("EVEN"):
        return "EVEN"
    if "disagree" in r:
        return "the runs disagree"
    return "shown, not judged"


def table_of(slug: str):
    """The governor's three-run table on the engine that stands, as tools/confirm_abc.py wrote it, or None."""
    p = ROOT / "results" / "live" / f"V12_{slug.upper()}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def counts(table) -> dict:
    out = {w: 0 for w in WORDS}
    for row in (table.get("rows") or {}).values():
        out[word_of(row.get("reading", ""))] += 1
    return out


def key_rows(table, limit=8):
    """The rows a reader looks at first: the queue's own gauges, then machines and energy; each with its reading."""
    rows = table.get("rows") or {}
    first = [k for k in rows if k.startswith("queue:")] + [k for k in rows if k.startswith("batch:")]
    rest = [k for k in rows if ("machines" in k or "energy" in k) and k not in first]
    return [(k, rows[k].get("reading", "")) for k in (first + rest)[:limit]]


def runs_of(slug, runs):
    r = runs.get(slug) or {}
    return " ".join(f"[{letter}]({REPO_RUNS}{rid})" for letter, rid in sorted(r.items()) if rid)


def render(runs=None) -> str:
    runs = json.loads(RUNS.read_text()) if runs is None and RUNS.exists() else (runs or {})
    L = ["# The governors and orchestrators: native under them, Omni-Compass on top", ""]
    L += receipt_key() + [""]
    L += [f"The founder's list of 19 October, night: every governor and orchestrator he named runs with the organism native "
          f"under it, then with Omni-Compass on top of it, on the engine that stands ({ENGINE}). The organism is a six-worker "
          f"real Kubernetes cluster (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines, each arm on a fresh cluster, the "
          f"two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading. Native is "
          f"the governor as its project ships it; Omni-Compass sits on top with its own levers (the node pool, the service's "
          f"autoscaler and processor limit, cruise and idle) and never writes the governor's objects. Cost: $0 (GitHub's free "
          f"machines). A governor's line reads only from its own three-run table; until then it says where its runs stand.", ""]
    L += ["| Governor | What it governs | Register row | Where it stands | Readings (A, B and C) |", "|---|---|---:|---|---|"]
    for slug, name, row, field, native, test in GOVERNORS:
        t = table_of(slug)
        started = runs_of(slug, runs)
        if t:
            c = counts(t)
            reading = (f"{c['GAIN']} GAIN, {c['LOSS']} LOSS, {c['power given']} power given, {c['EVEN']} EVEN, "
                       f"{c['the runs disagree']} where the runs disagree ([table](V12_{slug.upper()}.md))")
            where = "three runs in"
        elif started:
            reading, where = "runs not yet finished", f"running: {started}"
        elif test.startswith("not yet"):
            reading, where = "not yet run", "its rig is not yet built"
        else:
            reading, where = "not yet run", "built; its runs come in the campaign"
        L.append(f"| {name} | {field} | {row} | {where} | {reading} |")
    L.append("")
    for slug, name, row, field, native, test in GOVERNORS:
        t = table_of(slug)
        L += [f"## {name}", "", f"- **Native**: {native}.", f"- **Its test**: {test}; register row {row}."]
        if t:
            L.append(f"- **Runs**: {', '.join(t.get('runs', []))}; engine {', '.join(sorted(set(t.get('engines', [])))) or ENGINE}.")
            L += ["", "| Gauge | Reading |", "|---|---|"] + [f"| {k} | {r} |" for k, r in key_rows(t)]
            L += ["", f"Every row of the run: [`results/live/V12_{slug.upper()}.md`](V12_{slug.upper()}.md)."]
        else:
            L.append("- **Readings**: none yet; nothing is written here before its three runs are in.")
        L.append("")
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if the page is not what the tables and runs give")
    a = ap.parse_args(argv)
    text = render()
    if a.check:
        if not OUT.exists() or OUT.read_text() != text:
            print("governors page: out of date (python3 tools/governors_page.py)")
            return 1
        print("governors page: current")
        return 0
    OUT.write_text(text)
    print(f"governors page -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
