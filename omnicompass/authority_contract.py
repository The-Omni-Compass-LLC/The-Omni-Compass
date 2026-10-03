# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Executable authority/evidence contracts for Omni-Compass.

This module does not claim that a plant obeyed Omni. It defines the minimum links that must
exist before software may promote a claim from COMPUTED -> REQUESTED -> ENFORCED -> ATTRIBUTED
-> BENEFICIAL -> RESTORED. Missing evidence can only lower a claim level, never raise it.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import IntEnum
from typing import Any, Iterable

class ClaimLevel(IntEnum):
    COMPUTED=0; REQUESTED=1; ENFORCED=2; ATTRIBUTED=3; BENEFICIAL=4; RESTORED=5

@dataclass(frozen=True)
class AuthorityContract:
    muscle_id: str
    resource: str
    writer: str
    command: str
    bounds: str
    readback: str
    conflict_set: tuple[str,...]
    meter: tuple[str,...]
    guardrails: tuple[str,...]
    restore: str
    evidence_class: str
    def to_dict(self):
        d=asdict(self); d['conflict_set']=list(self.conflict_set); d['meter']=list(self.meter); d['guardrails']=list(self.guardrails); return d

GPU_POWER = AuthorityContract(
    'nvidia.gpu.power_limit','GPU board power envelope','omni_controller/gpu_governor.py',
    'nvidia-smi -i <gpu> -pl <watts>','device min <= watts <= frozen start limit',
    'power.limit + enforced.power.limit',
    ('VBIOS','BMC/SMBPBI/chassis','application clocks','foreign host writer'),
    ('DCGM/NVML device joules','integrated board power','optional wall meter','RAPL package meter (separate domain)'),
    ('successful work','SLO','no thermal/HwPowerBrake confound','Watch writes == 0'),
    'restore frozen starting board-power limit and read back','physical')

RAPL_METER = AuthorityContract(
    'intel.rapl.meter','CPU package energy meter','read-only',
    'read energy_uj','read-only','start/end energy_uj + max_energy_range_uj',(),
    ('RAPL package joules','optional DRAM joules','optional psys joules'),
    ('wrap-aware delta','domain labels remain separate'), 'none (read-only)','physical-meter')

K8S_REPLICA = AuthorityContract(
    'kubernetes.replicas','workload replica allocation','Omni Kubernetes adapter/native controller',
    'scale/patch replica target','declared min/max + safety envelope','observed desired/actual replicas',
    ('HPA','operator','GitOps/deployment writer'),('work','latency','pending/backlog','optional node/wall energy'),
    ('SLO','health','backlog','unsafe == 0'),'restore/hand back original controller state','external-software')

CONTRACTS={x.muscle_id:x for x in (GPU_POWER,RAPL_METER,K8S_REPLICA)}

def catalogue(): return {k:v.to_dict() for k,v in CONTRACTS.items()}
