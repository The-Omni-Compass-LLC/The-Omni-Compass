# Public-Policy Controller Tournament

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


Purpose: challenge Omni-Compass on one frozen plant without inventing proprietary competitor internals.

## Rules
1. Same plant, scenarios, seeds, starting state, metrics and score direction for every arm.
2. A public-policy replica may encode only documented behavior plus an explicitly labeled approximation.
3. It is never named or reported as execution of the proprietary product.
4. Adverse Omni results remain in RUNS.csv and SUMMARY.json.
5. Modeled energy is never labeled physical energy.
6. No aggregate "world best" score is emitted. Per-metric paired 95% bootstrap intervals are emitted.

## Controller provenance
- Kubernetes HPA/CA: documented-behavior model. HPA uses ratio law, tolerance and stabilization semantics.
- OpenShift autoscale replica: stack proxy using HPA+CA mechanics. It is not Red Hat code.
- Karpenter replica: repository Karpenter-lite, pending-capacity provisioning plus feasible consolidation. It is intentionally simpler than Karpenter's real empty/multi/single-node consolidation and disruption-budget machinery.
- StormForge replica: action-surface proxy using request sizing plus horizontal scaling. Proprietary ML is not reproduced.
- Turbonomic proxy: action-surface proxy only. IBM's proprietary optimizer is not reproduced.
- Omni: repository native controller.

## Interpretation
A proxy can test architectural pressure points and falsify Omni claims. It cannot establish superiority over the named commercial product. A real same-box product test is a separate evidence class.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.

Current allocator holdout result, independent validation seeds 20261229..20261258 (30 scenarios): C3 Karpenter documented-behavior replica = modeled energy 1.460808, healthy 99.3148%, balanced CE 695.23, starts/stops 19.03/23.73; C7 Omni CLAIM1 = modeled energy 1.490047, healthy 99.5694%, balanced CE 276.59, starts/stops 5.23/9.33. C7 preserves the health advantage and materially reduces motion/CE versus C3, but modeled energy is slightly worse; no energy-win or global-superiority claim is authorized.

Open external evidence remains: 500-scenario confirmation, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

