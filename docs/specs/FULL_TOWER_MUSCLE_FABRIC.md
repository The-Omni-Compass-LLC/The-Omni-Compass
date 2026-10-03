# Omni-Compass Full-Tower Muscle Fabric — Pass 2

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any other use requires a signed, paid
> Omni-Compass Enterprise License. See [`LICENSE`](../../LICENSE).

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: the manual, section 15 (`docs/OMNI_COMPASS_MANUAL.md`).

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


This pass extends the Universal Muscle SDK into a C++ qualification harness with **128 normalized actuator capabilities across 16 families**. The six-state governing engine is not modified.

## Evidence boundary

The 128 catalog entries are normalized actuator **contracts**. They are not claims that 128 production integrations have been physically executed. The C++ harness exercises the common observation/bound/execute/readback/restore path using simulated adapters. Concrete Kubernetes/Linux/NVIDIA/cloud/storage/database/network adapters must independently earn L/P/C evidence.

## Design rule

Any accessible actuator may become an Omni muscle if it supplies observation, bounds, timing, execution, readback, shielding, restoration and receipts. New muscles expand the authority surface; they do not create a new governing brain.

## Harness

`oc_full_tower` instantiates all 128 contracts, routes authority from the existing nervous-system gate, performs an actuation/readback/restore transaction for every muscle, then asserts fail-closed behavior under a global security hold.

The machine-readable catalogs are `muscles/FULL_TOWER_128.csv` and `.json`.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario confirmation, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*Evaluation and simulation use only. Commercial use, commercialization or monetization requires a signed, paid
Omni-Compass Enterprise License from The Omni-Compass LLC. See [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE).*
