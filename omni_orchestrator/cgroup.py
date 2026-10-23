# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A machine's and a unit's walls: the kernel's own control groups, version 2 (the unified hierarchy) or version 1.

A group is omni/<machine> for a machine and omni/<machine>/<unit> for a unit. A machine's CPU quota caps everything in
it; a unit's quota caps the unit; the kernel's own counter gives the processor time each one used. Version 2 (cgroup.controllers
at the root, the default on modern kernels and on GitHub's runners): cpu.max, memory.max, cpu.stat, and the cpu and memory
controllers handed down to each level through cgroup.subtree_control; processes live only in the leaves (the units). Version 1
(the cpu, cpuacct and memory hierarchies mounted apart): cpu.cfs_quota_us, memory.limit_in_bytes, cpuacct.usage. Where the
groups cannot be written, nothing is walled and `Walls.make` says so (the caller records it)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(os.environ.get("OMNI_CGROUP_ROOT", "/sys/fs/cgroup"))
HIER = ("cpu", "cpuacct", "memory")
PERIOD_US = 100_000


def v2() -> bool:
    return (ROOT / "cgroup.controllers").exists()


def _write(p: Path, text: str) -> bool:
    try:
        p.write_text(text)
        return True
    except OSError:
        return False


class Walls:
    def __init__(self, *parts: str):
        self.parts = ("omni", *parts)

    def _dir(self, h: str = "") -> Path:
        return ROOT.joinpath(h, *self.parts) if h else ROOT.joinpath(*self.parts)

    # ---- make ----------------------------------------------------------------------------------------------------
    def make(self, cpu_m: float | None = None, mem_mb: float | None = None) -> bool:
        """Create the group; set its CPU quota (millicores) and memory limit. True when the CPU wall is in place."""
        return self._make_v2(cpu_m, mem_mb) if v2() else self._make_v1(cpu_m, mem_mb)

    def _make_v2(self, cpu_m, mem_mb) -> bool:
        try:
            d = ROOT
            for part in self.parts:                      # every level above the leaf hands the controllers down
                d = d / part
                d.mkdir(exist_ok=True)
                _write(d.parent / "cgroup.subtree_control", "+cpu +memory")
            if cpu_m:
                ok = _write(d / "cpu.max", f"{int(cpu_m * PERIOD_US / 1000)} {PERIOD_US}")
                if not ok:
                    return False
            if mem_mb:
                _write(d / "memory.max", str(int(mem_mb) * 1024 * 1024))     # a limit the kernel refuses: the CPU wall stands
            return True
        except OSError:
            return False

    def _make_v1(self, cpu_m, mem_mb) -> bool:
        try:
            for h in HIER:
                if (ROOT / h).is_dir():
                    self._dir(h).mkdir(parents=True, exist_ok=True)
            if cpu_m:
                (self._dir("cpu") / "cpu.cfs_period_us").write_text(str(PERIOD_US))
                (self._dir("cpu") / "cpu.cfs_quota_us").write_text(str(int(cpu_m * PERIOD_US / 1000)))
            if mem_mb and (ROOT / "memory").is_dir():
                _write(self._dir("memory") / "memory.limit_in_bytes", str(int(mem_mb) * 1024 * 1024))
            return True
        except OSError:
            return False

    def set_cpu(self, cpu_m: float) -> bool:
        """Move the group's CPU wall to cpu_m millicores (the quota the kernel enforces); True when the kernel took it."""
        q = str(int(cpu_m * PERIOD_US / 1000))
        if v2():
            return _write(self._dir() / "cpu.max", f"{q} {PERIOD_US}")
        return _write(self._dir("cpu") / "cpu.cfs_quota_us", q)

    def cpu_limit_m(self) -> float | None:
        """The group's CPU wall as it stands, in millicores (None: no wall, or none readable)."""
        try:
            if v2():
                q, p = (self._dir() / "cpu.max").read_text().split()
                return None if q == "max" else int(q) * 1000.0 / int(p)
            q = int((self._dir("cpu") / "cpu.cfs_quota_us").read_text())
            p = int((self._dir("cpu") / "cpu.cfs_period_us").read_text())
            return None if q < 0 else q * 1000.0 / p
        except (OSError, ValueError):
            return None

    # ---- join, read, list, remove --------------------------------------------------------------------------------
    def join(self, pid: int) -> None:
        if v2():
            _write(self._dir() / "cgroup.procs", str(pid))
            return
        for h in HIER:
            f = self._dir(h) / "cgroup.procs"
            if f.exists():
                _write(f, str(pid))

    def cpu_s(self) -> float:
        """The processor time used by everything in the group so far, in seconds."""
        try:
            if v2():
                for line in (self._dir() / "cpu.stat").read_text().splitlines():
                    if line.startswith("usage_usec"):
                        return int(line.split()[1]) / 1e6
                return 0.0
            return int((self._dir("cpuacct") / "cpuacct.usage").read_text()) / 1e9
        except (OSError, ValueError):
            return 0.0

    def pids(self) -> set[int]:
        """Every process in the group and the groups under it."""
        out: set[int] = set()
        base = self._dir() if v2() else self._dir("cpu")
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
        for base in ([self._dir()] if v2() else [self._dir(h) for h in HIER]):
            if not base.is_dir():
                continue
            for d, _, _ in sorted(os.walk(base), key=lambda w: -len(w[0])):
                try:
                    os.rmdir(d)
                except OSError:
                    pass

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
