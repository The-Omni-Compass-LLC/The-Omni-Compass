# The realms on Omni v5: 1002 muscles on modelled plants, native against the v5 law on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (modelled). Run 2026-10-11 22:47 UTC, commit `e5ce5cb2d354`, seeds 3000-3009 (10 paired seeds per muscle and per organism), catalog `realms/catalog_v5.csv`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`): the v5 compass law `realms/compass_arm_v5.py` at its default `V5CFG`, on top of each plant's own native controller. Harness `realms/`.

The v5 law carries two math-only guardrails: the **edge** (a per-knob cushion from how fast service has climbed and how far it wobbles, so nothing riding its limit falls off) and the **centre/hole** (a machine or a cooled zone is eased only while it can still climb back). Otherwise every knob is free, and a knob stays native wherever the law cannot improve it without harm. In this no-harm default the power cap, the battery shave and the generation setpoint stay native (they trade service or output for energy); they are a Max/service dial, and power is proven on the metered GPU (class P), not here.

Primary outcome: work per energy, v5 against native, with its 95% interval over seeds. Guardrails: work not lower by more than 1%, share of periods in violation not higher by more than 1 percentage point. Labels by rule. These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. What a row shows is whether the v5 law, applied to that knob, helps or hurts the model.

## The five organisms

| Organism | Muscles | Label | Work per energy | Work | Energy | Violations (pp) | Valid |
|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 481 | **SUPERIOR WITHIN GUARDRAILS** | +0.3% (+0.3 to +0.3) | +0.0% (+0.0 to +0.0) | -0.3% (-0.3 to -0.3) | -0.0 (-0.0 to -0.0) | yes |
| Physics / Robotics / Autonomous | 376 | **SUPERIOR WITHIN GUARDRAILS** | +0.1% (+0.1 to +0.1) | +0.0% (+0.0 to +0.0) | -0.1% (-0.1 to -0.1) | -0.0 (-0.0 to -0.0) | yes |
| Energy / Facility / Industrial | 470 | **SUPERIOR WITHIN GUARDRAILS** | +0.0% (+0.0 to +0.1) | +0.0% (+0.0 to +0.0) | -0.0% (-0.1 to -0.0) | -0.0 (-0.0 to -0.0) | yes |
| Distribution / Specialized | 446 | **SUPERIOR WITHIN GUARDRAILS** | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0 (-0.0 to +0.0) | yes |
| The whole tower, every muscle once | 1002 | **SUPERIOR WITHIN GUARDRAILS** | +0.0% (+0.0 to +0.1) | +0.0% (+0.0 to +0.0) | -0.0% (-0.1 to -0.0) | -0.0 (-0.0 to -0.0) | yes |

## Every muscle alone, by home realm

| Realm | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | WORSE | INVALID |
|---|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 385 | 13 | 0 | 372 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 119 | 8 | 0 | 111 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 75 | 1 | 173 | 0 | 0 | 0 |
| Distribution / Specialized | 249 | 2 | 0 | 247 | 0 | 0 | 0 |
| **All** | 1002 | **98** | **1** | **903** | **0** | **0** | **0** |

## No-harm check: muscles worse than native on any axis

- Omni acts on **161** of 1002 muscles; the rest are wired and watched but held native (no signal pushed where none helps).
- Muscles labelled **WORSE**: **0**.
- The v5 arm hands every knob back to native on the kill (the dead-man lease): 1002 of 1002 muscles, 5 of 5 organisms.

## Largest gains and largest losses (single muscles, by mean work per energy)

| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) |
|---|---|---|---|---:|---:|---:|
| zswap_pool_fraction | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.7% (+31.8 to +35.6) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| tank_level_target | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.6% (+31.6 to +35.5) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| transparent_hugepages | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.4% (+31.5 to +35.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| prefetch_aggressiveness | Content Delivery & Edge Cache | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.1% (+31.4 to +34.8) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| ttl_eviction_waste | Gut: Data-plane Intake & Waste | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.1% (+31.3 to +34.9) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| fn_timeout_budget | Serverless & Functions (FaaS) | setpoint | SUPERIOR WITHIN GUARDRAILS | +32.9% (+31.1 to +34.7) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| vm_swappiness | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +32.9% (+31.3 to +34.4) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| numa_vcpu_pinning | Virtualization & Hypervisor | setpoint | SUPERIOR WITHIN GUARDRAILS | +32.4% (+30.4 to +34.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| temperature_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +32.3% (+30.5 to +34.1) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| net_qdisc_codel_target | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +32.1% (+29.8 to +34.4) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| wind_turbine_yaw_offset | Renewable Generation & Inverter Control | capacity | NONINFERIOR / INCONCLUSIVE | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_replicas | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_route_weight | AI Inference Serving | setpoint | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_load | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_unload | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_instance_count | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| continuous_batching | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| max_batch_size | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| batch_queue_delay | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| inference_concurrency | AI Inference Serving | admission | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |

Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
