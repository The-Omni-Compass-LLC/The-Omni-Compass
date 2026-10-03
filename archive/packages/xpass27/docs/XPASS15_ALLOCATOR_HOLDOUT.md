# XPASS15 Allocator Holdout

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


## Frozen core
XPASS15 does not change the canonical six-state/eight-line engine, CLAIM1 held-u law, causal authority contract, C++ core, GPU writer, watchdog, or physical evidence gates.

## Finding
The XPASS14 C7 tournament path coupled the Omni HPA target to a coordinated request sizer. Ablation on development seeds 20261029..20261036 isolated that request-sizing path as the dominant churn amplifier. With the request sizer disabled, C7 starts/stops and CE collapsed while modeled health remained high. This is an allocation-policy finding, not a new physics claim.

## Frozen XPASS15 C7 allocation policy
- request sizer: disabled in C7 tournament arm
- node power cap floor: 0.45
- cap margin: 0.02
- canonical CLAIM1 dynamics: unchanged
- common plant/comparator arms: unchanged

The cap settings were selected on development seeds only. A separate 30-scenario validation population begins at seed 20261229.

## Validation interpretation
On validation seeds 20261229..20261258, C7 used materially less control effort, fewer starts/stops, fewer evictions, fewer replica-change units and fewer reversals than C3, while healthy-time was higher. C7 modeled energy was slightly higher than C3 and its paired CI was adverse, so XPASS15 does not claim an energy win over C3.

This is a better governor tradeoff than XPASS14's C7 allocation path because it removes the dominant motion defect without modifying the governing equations. It does not establish superiority over the Karpenter product or any proprietary product.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.

Current allocator holdout result, independent validation seeds 20261229..20261258 (30 scenarios): C3 Karpenter documented-behavior replica = modeled energy 1.460808, healthy 99.3148%, balanced CE 695.23, starts/stops 19.03/23.73; C7 Omni CLAIM1 = modeled energy 1.490047, healthy 99.5694%, balanced CE 276.59, starts/stops 5.23/9.33. C7 preserves the health advantage and materially reduces motion/CE versus C3, but modeled energy is slightly worse; no energy-win or global-superiority claim is authorized.

Open external evidence remains: 500-scenario confirmation, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

