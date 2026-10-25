# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Python's 500 scenarios a seed (the held-out seeds), for the live benchmark engine's replay monitor.

benchmarks/stack_benchmark.py runs 500 scenarios of 72 steps from one seed base (each scenario's own stream drawn from it,
omnicompass/stack_sim.py), every scenario through every arm, and writes one row a scenario and arm with the run's trace hash
(the SHA-256 of its whole trace, first 16 hex digits): results/heldout_seed_<seed>/RUNS.csv and SUMMARY.json. verify.py
replays scenarios of both seeds on every push and compares every trace hash (python3 verify.py --full-replay regenerates the
whole file byte for byte). The monitor replays the record scenario by scenario, native beside each Omni-Compass arm, with the
file's own SHA-256 and every scenario's trace hash; nothing in it is recomputed by the page (the engine's own runs, recomputed
by the page, are tools/engine_runs.py's).

  python3 docs/engine/export_heldout.py OUT.json
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
# Omni-Compass always on top of native (the founder's order of 25 October: never by itself): the record's own arm that runs
# Omni-Compass alone, omni_direct, stays in its file and is not drawn
ARMS = ["native", "omni_k8s_protect", "omni_k8s_throughput", "k8s_ref_70", "omni_k8s_observe"]
GAUGES = [("time_healthy", "time healthy (share of the 72 steps)", "higher"), ("sla_violation_physical", "service-level violations, physical (share of steps)", "lower"),
          ("recovery_minutes", "recovery after the event (minutes)", "lower"), ("energy_kwh", "energy (kWh)", "spent"), ("node_hours", "machine-hours", "spent")]


def sig(v: float) -> float:
    return float(f"{v:.6g}")


def one(seed_dir: Path) -> dict:
    runs = seed_dir / "RUNS.csv"
    summ = json.loads((seed_dir / "SUMMARY.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader(runs.open(encoding="utf-8")))
    by = {}
    fam = {}
    for r in rows:
        sid = int(r["scenario_id"])
        fam[sid] = r["family"]
        by.setdefault(r["arm"], {})[sid] = r
    ids = sorted(fam)
    data = {"seed": summ.get("seed_base"), "scenarios": summ.get("scenarios"), "steps": summ.get("steps"), "file": str(runs.relative_to(ROOT)),
            "sha256": hashlib.sha256(runs.read_bytes()).hexdigest(), "arms_all": summ.get("arms"), "arms": [a for a in ARMS if a in by],
            "family": [fam[i] for i in ids], "gauges": [{"key": k, "name": n, "aim": a} for k, n, a in GAUGES], "values": {}, "hash": {}, "paired": {}}
    for arm in data["arms"]:
        data["values"][arm] = {k: [sig(float(by[arm][i][k])) for i in ids] for k, _, _ in GAUGES}
        data["hash"][arm] = [by[arm][i]["trace_hash"] for i in ids]
        pk = f"{arm}_vs_native"
        if pk in (summ.get("paired") or {}):
            data["paired"][arm] = {p["metric"]: {k: p.get(k) for k in ("base_mean", "cand_mean", "mean_delta", "ci95", "better", "worse", "tied", "n")}
                                   for p in summ["paired"][pk] if p["metric"] in {k for k, _, _ in GAUGES}}
    data["observe_identical"] = summ.get("observe_mode_identical_to_native")
    return data


def main(out: str) -> None:
    seeds = sorted(ROOT.glob("results/heldout_seed_*/RUNS.csv"))
    data = {"tool": "benchmarks/stack_benchmark.py", "check": "verify.py (every push: scenarios of both seeds replayed, every trace hash compared; --full-replay: every scenario, byte for byte)",
            "rerun": "python3 -c \"from benchmarks.stack_benchmark import run; from omnicompass.adapter import AllocationLaw; from pathlib import Path; run(500, SEED, Path('out'), AllocationLaw())\"",
            "seeds": [one(p.parent) for p in seeds]}
    Path(out).write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "heldout.json")
