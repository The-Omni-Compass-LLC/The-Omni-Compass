# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""OmniCompass Universal Muscle SDK.

This module does not change the six-state governor.  It standardises how a plant
surface earns authority beneath it: observe -> bound -> request -> execute ->
readback -> receipt -> restore.  Adapters may target Kubernetes, host controls,
GPU/accelerator controls, cloud/VM APIs, storage, network, runtimes, cooling or
facility power without changing the governing state law.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from time import monotonic, time
from typing import Any, Callable, Dict, Iterable, Mapping, Optional, Protocol, Tuple


class Evidence(str, Enum):
    DESIGN = "D"
    SIMULATION = "S"
    LIVE_SOFTWARE = "L"
    PHYSICAL = "P"
    COMMERCIAL = "C"


class AutomationMode(str, Enum):
    DISABLED = "disabled"
    RECOMMEND = "recommend"
    MANUAL = "manual"
    EXTERNAL_APPROVAL = "external_approval"
    AUTOMATIC = "automatic"


class MuscleStatus(str, Enum):
    AVAILABLE = "available"
    DEGRADED = "degraded"
    BLIND = "blind"
    FAILED = "failed"
    RESTORING = "restoring"


@dataclass(frozen=True)
class TimingContract:
    observation_period_s: float
    decision_period_s: float
    actuation_delay_s: float = 0.0
    minimum_hold_s: float = 0.0
    cooldown_s: float = 0.0
    timeout_s: float = 5.0
    stale_after_s: float = 30.0


@dataclass(frozen=True)
class CapabilityContract:
    minimum: float
    maximum: float
    resolution: float = 0.0
    max_step: Optional[float] = None
    max_rate_per_s: Optional[float] = None
    units: str = "unit"
    reversible: bool = True
    readback: bool = True

    def clamp(self, value: float, previous: Optional[float] = None, dt: Optional[float] = None) -> float:
        v = min(self.maximum, max(self.minimum, float(value)))
        if self.max_step is not None and previous is not None:
            v = min(previous + self.max_step, max(previous - self.max_step, v))
        if self.max_rate_per_s is not None and previous is not None and dt is not None:
            step = max(0.0, dt) * self.max_rate_per_s
            v = min(previous + step, max(previous - step, v))
        if self.resolution > 0:
            v = round(v / self.resolution) * self.resolution
            v = min(self.maximum, max(self.minimum, v))
        return v


@dataclass(frozen=True)
class SafetyContract:
    hard_min: float
    hard_max: float
    fail_closed: bool = True
    safe_default: Optional[float] = None
    forbidden: Tuple[str, ...] = ()

    def permits(self, value: float, context: Mapping[str, Any]) -> Tuple[bool, str]:
        if value < self.hard_min or value > self.hard_max:
            return False, "outside_hard_bounds"
        for key in self.forbidden:
            if bool(context.get(key, False)):
                return False, f"forbidden:{key}"
        return True, "permitted"


@dataclass(frozen=True)
class MuscleSpec:
    muscle_id: str
    plant_id: str
    resource_type: str
    adapter_version: str
    capability: CapabilityContract
    timing: TimingContract
    safety: SafetyContract
    automation: AutomationMode = AutomationMode.RECOMMEND
    evidence: Evidence = Evidence.DESIGN
    native_owner: str = "native"
    authority_priority: int = 100
    description: str = ""


@dataclass
class Observation:
    value: float
    timestamp: float = field(default_factory=time)
    quality: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def age(self, now: Optional[float] = None) -> float:
        return max(0.0, (time() if now is None else now) - self.timestamp)


@dataclass
class MuscleReceipt:
    muscle_id: str
    timestamp: float
    mode: str
    requested: Optional[float]
    bounded: Optional[float]
    realized: Optional[float]
    units: str
    permitted: bool
    reason: str
    observation_age_s: Optional[float] = None
    actuation_latency_s: Optional[float] = None
    actuator_residual: Optional[float] = None
    restored: Optional[bool] = None
    evidence: str = "D"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


class MuscleAdapter(Protocol):
    spec: MuscleSpec
    def observe(self) -> Observation: ...
    def snapshot_native(self) -> Any: ...
    def execute(self, value: float) -> None: ...
    def readback(self) -> float: ...
    def restore_native(self, snapshot: Any) -> None: ...


class FunctionalMuscle:
    """Small adapter for public APIs/commands without coupling them to the brain."""
    def __init__(self, spec: MuscleSpec, observe: Callable[[], Observation], execute: Callable[[float], None],
                 readback: Callable[[], float], snapshot: Callable[[], Any], restore: Callable[[Any], None]):
        self.spec = spec
        self._observe, self._execute, self._readback = observe, execute, readback
        self._snapshot, self._restore = snapshot, restore

    def observe(self): return self._observe()
    def execute(self, value): return self._execute(value)
    def readback(self): return float(self._readback())
    def snapshot_native(self): return self._snapshot()
    def restore_native(self, snapshot): return self._restore(snapshot)


class MuscleRuntime:
    """Uniform authority gate around one actuator.  The governor proposes; this runtime earns and verifies authority."""
    def __init__(self, adapter: MuscleAdapter, audit: Optional[Callable[[Dict[str, Any]], None]] = None):
        self.adapter = adapter
        self.spec = adapter.spec
        self.audit = audit or (lambda _: None)
        self.native_snapshot: Any = None
        self.last_realized: Optional[float] = None
        self.last_write_mono: Optional[float] = None
        self.status = MuscleStatus.AVAILABLE

    def arm(self) -> None:
        if self.native_snapshot is None:
            self.native_snapshot = self.adapter.snapshot_native()

    def command(self, requested: float, context: Optional[Mapping[str, Any]] = None,
                approved: bool = False, now: Optional[float] = None) -> MuscleReceipt:
        context = dict(context or {})
        obs = self.adapter.observe()
        wall = time() if now is None else now
        age = obs.age(wall)
        mode = self.spec.automation
        reason = ""
        permitted = True
        bounded: Optional[float] = None
        realized: Optional[float] = None
        latency: Optional[float] = None

        if age > self.spec.timing.stale_after_s or obs.quality <= 0:
            permitted, reason, self.status = False, "stale_or_invalid_observation", MuscleStatus.BLIND
        elif mode == AutomationMode.DISABLED:
            permitted, reason = False, "disabled"
        elif mode in (AutomationMode.RECOMMEND, AutomationMode.MANUAL):
            permitted, reason = False, mode.value
        elif mode == AutomationMode.EXTERNAL_APPROVAL and not approved:
            permitted, reason = False, "approval_required"

        if permitted:
            dt = None if self.last_write_mono is None else max(0.0, monotonic() - self.last_write_mono)
            bounded = self.spec.capability.clamp(requested, self.last_realized, dt)
            permitted, reason = self.spec.safety.permits(bounded, context)

        if permitted and self.last_write_mono is not None:
            elapsed = monotonic() - self.last_write_mono
            hold = max(self.spec.timing.minimum_hold_s, self.spec.timing.cooldown_s)
            if elapsed < hold:
                permitted, reason = False, "hold_or_cooldown"

        if permitted:
            self.arm()
            t0 = monotonic()
            self.adapter.execute(float(bounded))
            self.last_write_mono = monotonic()
            if self.spec.capability.readback:
                realized = self.adapter.readback()
                latency = monotonic() - t0
                self.last_realized = realized
            else:
                realized = float(bounded)
                self.last_realized = realized
            self.status = MuscleStatus.AVAILABLE
        elif reason == "":
            reason = "blocked"

        receipt = MuscleReceipt(
            muscle_id=self.spec.muscle_id, timestamp=wall, mode=mode.value,
            requested=float(requested), bounded=bounded, realized=realized,
            units=self.spec.capability.units, permitted=permitted, reason=reason,
            observation_age_s=age, actuation_latency_s=latency,
            actuator_residual=None if realized is None or bounded is None else realized - bounded,
            evidence=self.spec.evidence.value,
            metadata={"observation_quality": obs.quality, "status": self.status.value},
        )
        self.audit(receipt.as_dict())
        return receipt

    def restore(self) -> MuscleReceipt:
        self.status = MuscleStatus.RESTORING
        ok = False
        reason = "no_snapshot"
        realized = None
        if self.native_snapshot is not None:
            try:
                self.adapter.restore_native(self.native_snapshot)
                realized = self.adapter.readback() if self.spec.capability.readback else None
                ok, reason = True, "restored"
                self.status = MuscleStatus.AVAILABLE
            except Exception as exc:  # deliberately auditable fail-closed boundary
                reason = f"restore_failed:{type(exc).__name__}"
                self.status = MuscleStatus.FAILED
        receipt = MuscleReceipt(
            muscle_id=self.spec.muscle_id, timestamp=time(), mode=self.spec.automation.value,
            requested=None, bounded=None, realized=realized, units=self.spec.capability.units,
            permitted=False, reason=reason, restored=ok, evidence=self.spec.evidence.value,
            metadata={"status": self.status.value},
        )
        self.audit(receipt.as_dict())
        return receipt


class MuscleRegistry:
    """Catalog of qualified plant surfaces.  Registration expands muscles, never the six-state core."""
    def __init__(self):
        self._muscles: Dict[str, MuscleRuntime] = {}

    def register(self, runtime: MuscleRuntime) -> None:
        mid = runtime.spec.muscle_id
        if mid in self._muscles:
            raise ValueError(f"duplicate muscle_id: {mid}")
        self._muscles[mid] = runtime

    def get(self, muscle_id: str) -> MuscleRuntime:
        return self._muscles[muscle_id]

    def command(self, muscle_id: str, requested: float, **kwargs) -> MuscleReceipt:
        return self.get(muscle_id).command(requested, **kwargs)

    def restore_all(self) -> Dict[str, MuscleReceipt]:
        return {mid: m.restore() for mid, m in reversed(list(self._muscles.items()))}

    def catalog(self) -> list[Dict[str, Any]]:
        out = []
        for mid, m in sorted(self._muscles.items()):
            s = m.spec
            out.append({
                "muscle_id": mid, "plant_id": s.plant_id, "resource_type": s.resource_type,
                "mode": s.automation.value, "evidence": s.evidence.value, "units": s.capability.units,
                "min": s.capability.minimum, "max": s.capability.maximum,
                "readback": s.capability.readback, "reversible": s.capability.reversible,
                "stale_after_s": s.timing.stale_after_s, "status": m.status.value,
            })
        return out


# Standard actuator classes.  These are categories/contracts, not claims that a connector is already physically verified.
STANDARD_MUSCLE_CLASSES = (
    "kubernetes.replicas", "kubernetes.cpu_request", "kubernetes.cpu_limit", "kubernetes.memory_request",
    "kubernetes.memory_limit", "kubernetes.hpa_target", "kubernetes.pod_placement", "kubernetes.node_pool",
    "host.cpufreq", "host.cpu_quota", "host.cpuset", "host.memory", "host.io",
    "gpu.power_limit", "gpu.clock_envelope", "gpu.mig", "gpu.admission",
    "cloud.instance_count", "cloud.instance_size", "cloud.placement", "cloud.start_stop", "cloud.capacity_policy",
    "storage.volume_size", "storage.tier", "storage.iops", "storage.throughput", "storage.placement",
    "network.traffic_weight", "network.rate_limit", "network.bandwidth", "network.routing",
    "application.concurrency", "application.worker_count", "application.queue_admission", "application.jvm_heap",
    "application.thread_pool", "application.batch", "facility.cooling_setpoint", "facility.rack_power", "facility.site_power",
)
