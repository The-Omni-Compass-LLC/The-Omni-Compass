# Cisco IWO: native versus native-plus-Omni benchmark

Copyright 2026 The Omni-Compass LLC. Evaluation and Simulation use only. See LICENSE, NOTICE, DISCLOSURES.md.

STATUS: PROTOCOL ONLY. No vendor benchmark or performance win claimed.

## Source access
licensed SaaS; no source code.

## Native reference
VM/container placement and resizing. Use supported, production-recommended native settings. Freeze exact version and configuration. Do not deliberately weaken native.

## Paired arms
A: native. B: same native plus Omni supervisor, only with documented authorized levers. W: observe-only Omni (zero writes). C: standalone Omni only if an actual standalone implementation exists; report separately. Counterbalance run order and keep matched hardware, workload, and offered load.

## Measures
migration events, completed work, p95, billed compute. Also record failures, safety/SLO guardrails, native and Omni raw values, energy and cost when physically measured, actual actuator writes and read-back, rollback time, controller conflicts, and missing observations.

## Admission
Fail closed on stale/missing telemetry, unmatched workloads, unverified actuations, restoration failures, or breached preregistered SLOs. Exact equality is not a tolerance band. Report all adverse metrics and confidence intervals; do not claim a vendor comparison unless that actual product was deployed. Preserve source SHA, benchmark seed, raw traces, version pins, and run URL. No bill claim without actual rates and usage. A benchmark harness is not a performance result.

## Execution gate
Before physical runs: obtain authorized installation, verify controller API/metrics and legal use, create a read-only smoke, prove kill/restore, then freeze configuration. Paid clouds/hardware require an explicit budget. Never send write commands to unknown production systems.

Common evaluator (when request-level metrics apply): `python3 tools/paired_slo_goodput.py INPUT.json`. Run negative controls: `python3 -m unittest -v tests.test_paired_slo_goodput`. Other domain-specific data need separate adapters.
