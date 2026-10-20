# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governors and orchestrators on one page (the founder's list of 19 October, night): every one he named, what it
governs, what native is under it and what Omni-Compass does on top, where its test stands, and, once its three runs are in,
its readings by the one key, every row counted, losses included (results/live/GOVERNORS.md).

A governor's result is its three-run table on the engine that stands (tools/confirm_abc.py writes results/live/V12_<NAME>.md
and .json), one table for each setting it is read in (the Kubernetes scheduler: as shipped and with the operator's
bin-packing profile); until the table exists the page says where the runs stand, never a number. The runs started are listed
in results/live/governors_runs.json by setting, written when they are started.
Usage: python3 tools/governors_page.py [--check]"""
from __future__ import annotations

import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import receipt_key  # noqa: E402

OUT = ROOT / "results" / "live" / "GOVERNORS.md"
RUNS = ROOT / "results" / "live" / "governors_runs.json"
CATALOG_FILE = ROOT / "realms" / "catalog_v5.csv"
ENGINE = "omni-v12"
REPO_RUNS = "https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/"

# (slug, name, register row, what it governs, native under it, its test) in the founder's order of naming, the
# Kubernetes scheduler first because every other one stands on it
GOVERNORS = [
    ("scheduler", "The Kubernetes scheduler (vanilla, and its bin-packing profile)", 88, "pod placement",
     "the default scheduler of Kubernetes 1.35 as shipped, which places every pod of every Kubernetes set; and the same "
     "release's scheduler with the operator's bin-packing profile (NodeResourcesFit, MostAllocated)",
     "the batch stream placed by the scheduler alone, in each setting (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 3)"),
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

# The muscles of the catalog (realms/catalog_v5.csv) that stand for each governor's knobs in the modelled organisms (class S):
# they run in the realms, the spine and the whole tower, native and with Omni-Compass on top (results/realms_v5/REALMS_V5.md)
CATALOG = {
    "scheduler": (4, ["node_selector", "node_affinity", "pod_anti_affinity", "topology_spread", "taint_toleration",
                      "priority_class", "preemption_policy", "scheduler_backoff", "scheduler_scoring_strategy",
                      "scheduler_plugin_weights", "scheduling_gates", "deschedule"]),
    "kueue": (1, ["job_admission", "batch_admission", "queue_concurrency", "queue_backpressure", "tenant_admission"]),
    "volcano": (14, ["gang_schedule", "queue_fairness", "task_priority", "task_preemption", "binpack_pressure"]),
    "kai": (14, ["gang_schedule", "queue_fairness", "cluster_quota", "task_preemption"]),
    "koordinator": (14, ["oversubscription", "resource_reclaim", "binpack_pressure", "spread_pressure"]),
    "cruisekube": (3, ["cruisekube_request_rightsizing", "in_place_resize", "cpu_request", "memory_request"]),
    "crane": (2, ["hpa_cpu_target", "hpa_custom_target", "hpa_scaling_rate_policies", "hpa_min_replicas", "hpa_max_replicas"]),
    "kuberay": (12, ["training_workers", "elastic_worker_count", "training_gang_size"]),
    "godel": (14, ["gang_schedule", "task_admission", "binpack_pressure", "resource_reservation"]),
    "armada": (39, ["multi_cluster_dispatch", "federation_quota", "global_admission"]),
    "karmada": (39, ["multi_cluster_dispatch", "region_dispatch", "global_failover", "cross_cluster_replication"]),
    "ocm": (39, ["multi_cluster_dispatch", "workload_migrate_region", "federation_quota"]),
    "kubeedge": (39, ["edge_dispatch", "edge_offload", "edge_sync_interval", "edge_site_node_pool"]),
    "nephio": (66, ["ran_slice_resource_budget", "ran_du_cu_placement", "ran_cell_sleep", "ran_carrier_enable"]),
}

# A governor read in more than one setting: one three-run table for each (V12_<SETTING>.json), its runs listed by setting
SETTINGS = {"scheduler": (("vanilla", "as shipped"), ("binpack", "bin-packing profile"))}

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


def catalog_line(slug) -> str:
    import csv
    fid, muscles = CATALOG[slug]
    with CATALOG_FILE.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["family_id"] == str(fid)]
    fam = rows[0]["family"] if rows else f"family {fid}"
    where = "the spine and every realm" if rows and len(rows[0]["realms"].split(";")) == 4 else "its realm and the whole tower"
    return (f"- **In the catalog (modelled, class S)**: family {fid}, {fam} ({len(rows)} muscles, in {where}): "
            + ", ".join(f"`{m}`" for m in muscles) + ".")


def settings_of(slug):
    return SETTINGS.get(slug, ((slug, ""),))


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
        wheres, readings = [], []
        for key, label in settings_of(slug):
            tag = f"{label}: " if label else ""
            t, started = table_of(key), runs_of(key, runs)
            if t:
                c = counts(t)
                readings.append(f"{tag}{c['GAIN']} GAIN, {c['LOSS']} LOSS, {c['power given']} power given, {c['EVEN']} EVEN, "
                                f"{c['the runs disagree']} where the runs disagree ([table](V12_{key.upper()}.md))")
                wheres.append(f"{tag}three runs in")
            elif started:
                readings.append(f"{tag}runs not yet finished"); wheres.append(f"{tag}running: {started}")
            elif test.startswith("not yet"):
                readings.append(f"{tag}not yet run"); wheres.append(f"{tag}its rig is not yet built")
            else:
                readings.append(f"{tag}not yet run"); wheres.append(f"{tag}built; its runs come in the campaign")
        L.append(f"| {name} | {field} | {row} | {'; '.join(wheres)} | {'; '.join(readings)} |")
    L.append("")
    for slug, name, row, field, native, test in GOVERNORS:
        L += [f"## {name}", "", f"- **Native**: {native}.", f"- **Its test on real Kubernetes (class L)**: {test}; register row {row}.",
              catalog_line(slug)]
        for key, label in settings_of(slug):
            t, head = table_of(key), (f" ({label})" if label else "")
            if t:
                L.append(f"- **Runs{head}**: {', '.join(t.get('runs', []))}; engine "
                         f"{', '.join(sorted(set(t.get('engines', [])))) or ENGINE}.")
                L += ["", "| Gauge | Reading |", "|---|---|"] + [f"| {k} | {r} |" for k, r in key_rows(t)]
                L += ["", f"Every row of the run: [`results/live/V12_{key.upper()}.md`](V12_{key.upper()}.md).", ""]
            else:
                L.append(f"- **Readings{head}**: none yet; nothing is written here before its three runs are in.")
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
