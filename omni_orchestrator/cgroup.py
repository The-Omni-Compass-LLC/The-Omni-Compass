# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A machine's and a unit's walls: the kernel's own control groups (version 1 hierarchies cpu, cpuacct, memory).

A group is omni/<machine> for a machine and omni/<machine>/<unit> for a unit. A machine's CPU quota caps everything in
it; a unit's quota caps the unit; cpuacct counts the processor time each one used. Where the hierarchies cannot be
written, nothing is walled and `Walls.make` says so (the caller records it)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(os.environ.get("OMNI_CGROUP_ROOT", "/sys/fs/cgroup"))
HIER = ("cpu", "cpuacct", "memory")
PERIOD_US = 100_000


class Walls:
    def __init__(self, *parts: str):
        self.parts = ("omni", *parts)

    def _dir(self, h: str) -> Path:
        return ROOT.joinpath(h, *self.parts)

    def make(self, cpu_m: float | None = None, mem_mb: float | None = None) -> bool:
        """Create the group in every hierarchy there is; set its CPU quota (millicores) and memory limit."""
        try:
            for h in HIER:
                if (ROOT / h).is_dir():
                    self._dir(h).mkdir(parents=True, exist_ok=True)
            if cpu_m:
                (self._dir("cpu") / "cpu.cfs_period_us").write_text(str(PERIOD_US))
                (self._dir("cpu") / "cpu.cfs_quota_us").write_text(str(int(cpu_m * PERIOD_US / 1000)))
            if mem_mb and (ROOT / "memory").is_dir():
                try:
                    (self._dir("memory") / "memory.limit_in_bytes").write_text(str(int(mem_mb) * 1024 * 1024))
                except OSError:
                    pass                                     # a memory limit the kernel refuses: the CPU walls stand
            return True
        except OSError:
            return False

    def join(self, pid: int) -> None:
        for h in HIER:
            f = self._dir(h) / "cgroup.procs"
            if f.exists():
                try:
                    f.write_text(str(pid))
                except OSError:
                    pass

    def cpu_s(self) -> float:
        """The processor time used by everything in the group so far, in seconds."""
        try:
            return int((self._dir("cpuacct") / "cpuacct.usage").read_text()) / 1e9
        except (OSError, ValueError):
            return 0.0

    def pids(self) -> set[int]:
        """Every process in the group and the groups under it."""
        out: set[int] = set()
        base = self._dir("cpu")
        if not base.is_dir():
            return out
        for d, _, _ in os.walk(base):
            try:
                out |= {int(x) for x in (Path(d) / "cgroup.procs").read_text().split()}
            except (OSError, ValueError):
                pass
        return out

    def remove(self) -> None:
        """Remove the group and the groups under it, deepest first (a group with a process left in it stays)."""
        for h in HIER:
            base = self._dir(h)
            if not base.is_dir():
                continue
            for d, _, _ in sorted(os.walk(base), key=lambda w: -len(w[0])):
                try:
                    os.rmdir(d)
                except OSError:
                    pass

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
