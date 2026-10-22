# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Capacity guards for shared-host Kubernetes clusters.

The kind runner is one physical host even when Kubernetes reports several nodes.
Sample the host's aggregate CPU counters and limit additional replicas to measured
headroom; an unavailable reading fails closed at the current replica count.
"""
from __future__ import annotations

import os
from pathlib import Path

KIND_SCALE_OUT_BUSY_LIMIT = 0.75


def one_host(nodes) -> bool:
    """Nodes that are containers on one machine (kind: providerID kind://...): each reports the whole host's CPU as its
    own, so the cluster's real CPU is one host's, not the sum (the replica room on kind, results/live/REPLICA_ROOM.md:
    the cap raised to 30 served no more requests and ran 78% more pods)."""
    return bool(nodes) and all(str((n.get("spec") or {}).get("providerID", "")).startswith("kind://") for n in nodes)


class HostCpuSampler:
    """Measure aggregate host CPU busy share from Linux /proc/stat.

    span: the sample intervals the share is read over (omni-v14). The governor samples once a decision; at 1 the share
    is the one since the previous decision (v13 at a decision a minute), and at a shorter period it passes the intervals
    that make the same minute (4 at 15 s), so a guard that read the host's minute still reads its minute."""

    def __init__(self, stat_path: str | os.PathLike[str] | None = None, span: int = 1):
        self.stat_path = Path(stat_path or os.environ.get("OMNI_HOST_PROC_STAT", "/proc/stat"))
        self.span = max(1, int(span))
        self._samples: list[tuple[int, int]] = []
        self.busy_share: float | None = None

    def sample(self) -> float | None:
        """Update the busy share over the last span intervals (fewer while fewer are read), or None without two valid
        samples."""
        try:
            line = next(row for row in self.stat_path.read_text().splitlines() if row.startswith("cpu "))
            fields = [int(value) for value in line.split()[1:]]
            if len(fields) < 4:
                self._samples = []
                self.busy_share = None
                return None
            total = sum(fields)
            idle = fields[3] + (fields[4] if len(fields) > 4 else 0)
            current = (total, idle)
        except (OSError, StopIteration, ValueError):
            self._samples = []
            self.busy_share = None
            return None

        self._samples = (self._samples + [current])[-(self.span + 1):]
        if len(self._samples) < 2:
            self.busy_share = None
            return None
        previous = self._samples[0]
        dt, di = current[0] - previous[0], current[1] - previous[1]
        if dt <= 0 or di < 0 or di > dt:
            self._samples = [current]
            self.busy_share = None
            return None
        self.busy_share = (dt - di) / dt
        return self.busy_share


def kind_replica_ceiling(
    allocatable_cpu_m: int,
    other_requested_cpu_m: int,
    pod_request_cpu_m: int,
    current_replicas: int,
    host_busy_share: float | None,
    reserve_share: float = 0.10,
    max_busy_share: float = KIND_SCALE_OUT_BUSY_LIMIT,
) -> int:
    """Return a total replica ceiling for kind's single shared host.

    Keep the existing Kubernetes-request ceiling as a hard upper bound. The
    host observation then limits *new* replicas to the CPU left below the
    configured reserve. If a host reading is unavailable, do not authorize
    scale-out on an unmeasured shared machine.
    """
    alloc = max(0, int(allocatable_cpu_m))
    other = max(0, int(other_requested_cpu_m))
    request = int(pod_request_cpu_m)
    current = max(0, int(current_replicas))
    if request <= 0 or alloc <= 0:
        return current

    request_ceiling = max(1, (alloc - other) // request - 1)
    request_ceiling = max(current, request_ceiling)
    if host_busy_share is None:
        return current
    if not 0.0 <= host_busy_share <= 1.0:
        return current
    # A request-based headroom calculation can still authorize more pods on a
    # host whose measured CPU is already under sustained pressure. At that
    # point, fail closed: do not expand the HPA cap until the host is below the
    # threshold. The threshold is a conservative starting guard for kind and
    # must be validated against the paired live workload before release.
    if host_busy_share >= min(1.0, max(0.0, float(max_busy_share))):
        return current

    reserve = min(0.95, max(0.0, float(reserve_share)))
    headroom_m = max(0, int(alloc * max(0.0, round(1.0 - reserve - host_busy_share, 12))))
    measured_ceiling = current + headroom_m // request
    return max(current, min(request_ceiling, measured_ceiling))


def bounded_replica_cap(
    operator_max: int,
    current_max: int,
    current_replicas: int,
    live_ceiling: int | None,
) -> int:
    """Recheck an Omni-raised HPA cap without setting it below live replicas.

    If the live ceiling cannot be read, restore the operator's original cap;
    Kubernetes must still be allowed to keep its currently running replicas.
    """
    original = max(1, int(operator_max))
    cap = max(original, int(current_max))
    running = max(0, int(current_replicas))
    measured = original if live_ceiling is None else max(0, int(live_ceiling))
    return max(original, running, min(cap, measured))
