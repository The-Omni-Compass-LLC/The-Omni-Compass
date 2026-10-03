# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Control-effort index. Experiment-defined. Sweep weights; don't trophy one set."""
from __future__ import annotations
from typing import Dict

SWEEPS = {
    "balanced": dict(replica_change=1, pod_move=1, node_provision=8, node_suspend=8, resize=2, reversal=4, power_cap_travel=1),
    "node_heavy": dict(replica_change=1, pod_move=1, node_provision=16, node_suspend=16, resize=2, reversal=4, power_cap_travel=1),
    "replica_heavy": dict(replica_change=4, pod_move=2, node_provision=8, node_suspend=8, resize=2, reversal=8, power_cap_travel=1),
    "resize_heavy": dict(replica_change=1, pod_move=1, node_provision=8, node_suspend=8, resize=8, reversal=4, power_cap_travel=1),
    "uniform": dict(replica_change=1, pod_move=1, node_provision=1, node_suspend=1, resize=1, reversal=1, power_cap_travel=1),
}


def ce(row: Dict, weights: Dict[str, float]) -> float:
    return (
        weights.get("replica_change", 0) * float(row.get("replica_change_units", 0))
        + weights.get("pod_move", 0) * float(row.get("evictions", 0))
        + weights.get("node_provision", 0) * float(row.get("node_starts", 0))
        + weights.get("node_suspend", 0) * float(row.get("node_stops", 0))
        + weights.get("resize", 0) * float(row.get("request_changes", 0))
        + weights.get("reversal", 0) * float(row.get("replica_reversals", 0))
        + weights.get("power_cap_travel", 0) * float(row.get("power_cap_travel", 0))
    )


def all_sweeps(row: Dict) -> Dict[str, float]:
    return {name: ce(row, w) for name, w in SWEEPS.items()}
