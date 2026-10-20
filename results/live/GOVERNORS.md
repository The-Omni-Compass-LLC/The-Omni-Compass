# The governors and orchestrators: native under them, Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's list of 19 October, night: every governor and orchestrator he named runs with the organism native under it, then with Omni-Compass on top of it, on the engine that stands (omni-v12). The organism is a six-worker real Kubernetes cluster (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines, each arm on a fresh cluster, the two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading. Native is the governor as its project ships it; Omni-Compass sits on top with its own levers (the node pool, the service's autoscaler and processor limit, cruise and idle) and never writes the governor's objects. Cost: $0 (GitHub's free machines). A governor's line reads only from its own three-run table; until then it says where its runs stand.

| Governor | What it governs | Register row | Where it stands | Readings (A, B and C) |
|---|---|---:|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | pod placement | 88 | as shipped: running: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356571014) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356586356) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356601235); bin-packing profile: running: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356578556) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356594135) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356608147) | as shipped: runs not yet finished; bin-packing profile: runs not yet finished |
| Kueue | batch admission (a job at a time, by queue quota) | 63 | built; its runs come in the campaign | not yet run |
| Volcano | batch scheduling (queues, gangs) | 63 | built; its runs come in the campaign | not yet run |
| KAI scheduler | AI workload scheduling (queues, fair share, gangs) | 91 | running: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350900880) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350907916) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350915166) | runs not yet finished |
| Koordinator | QoS colocation (batch work on what latency-sensitive pods leave unused) | 89 | running: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359085965) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359094679) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359103518) | runs not yet finished |
| CruiseKube | rightsizing (requests and limits, in place) | 81 | built; its runs come in the campaign | not yet run |
| Crane | predictive autoscaling and resource governance | 90 | its rig is not yet built | not yet run |
| KubeRay | Ray clusters (the Ray autoscaler) | 92 | its rig is not yet built | not yet run |
| Gödel scheduler | unified online and offline scheduling | 93 | its rig is not yet built | not yet run |
| Armada | multi-cluster batch | 94 | its rig is not yet built | not yet run |
| Karmada | multi-cluster placement | 95 | its rig is not yet built | not yet run |
| Open Cluster Management | multi-cluster management | 96 | its rig is not yet built | not yet run |
| KubeEdge | edge nodes | 97 | its rig is not yet built | not yet run |
| Nephio | network-function automation | 98 | its rig is not yet built | not yet run |

## The Kubernetes scheduler (vanilla, and its bin-packing profile)

- **Native**: the default scheduler of Kubernetes 1.35 as shipped, which places every pod of every Kubernetes set; and the same release's scheduler with the operator's bin-packing profile (NodeResourcesFit, MostAllocated).
- **Its test on real Kubernetes (class L)**: the batch stream placed by the scheduler alone, in each setting (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 3); register row 88.
- **In the catalog (modelled, class S)**: family 4, Kubernetes Placement & Scheduling (21 muscles, in the spine and every realm): `node_selector`, `node_affinity`, `pod_anti_affinity`, `topology_spread`, `taint_toleration`, `priority_class`, `preemption_policy`, `scheduler_backoff`, `scheduler_scoring_strategy`, `scheduler_plugin_weights`, `scheduling_gates`, `deschedule`.
- **Readings (as shipped)**: none yet; nothing is written here before its three runs are in.
- **Readings (bin-packing profile)**: none yet; nothing is written here before its three runs are in.

## Kueue

- **Native**: Kueue v0.20.2 with the operator's single ClusterQueue sized to the workers.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 1, Work Admission & Demand Shaping (19 muscles, in its realm and the whole tower): `job_admission`, `batch_admission`, `queue_concurrency`, `queue_backpressure`, `tenant_admission`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Volcano

- **Native**: Volcano v1.16.0 with its default queue as shipped.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `task_priority`, `task_preemption`, `binpack_pressure`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## KAI scheduler

- **Native**: the KAI scheduler v0.18.6 with its chart's default queues.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 1; register row 91.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `cluster_quota`, `task_preemption`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Koordinator

- **Native**: Koordinator 1.8.0, colocation on as shipped, the operator's colocation profile.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 2; register row 89.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `oversubscription`, `resource_reclaim`, `binpack_pressure`, `spread_pressure`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## CruiseKube

- **Native**: CruiseKube applying its own recommendations as shipped.
- **Its test on real Kubernetes (class L)**: `docs/CRUISEKUBE_PREREGISTRATION.md`; register row 81.
- **In the catalog (modelled, class S)**: family 3, Container Resources (25 muscles, in the spine and every realm): `cruisekube_request_rightsizing`, `in_place_resize`, `cpu_request`, `memory_request`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Crane

- **Native**: its Effective HPA in auto mode.
- **Its test on real Kubernetes (class L)**: not yet written; register row 90.
- **In the catalog (modelled, class S)**: family 2, Kubernetes Workload Scaling (32 muscles, in the spine and every realm): `hpa_cpu_target`, `hpa_custom_target`, `hpa_scaling_rate_policies`, `hpa_min_replicas`, `hpa_max_replicas`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeRay

- **Native**: the Ray autoscaler as shipped.
- **Its test on real Kubernetes (class L)**: not yet written; register row 92.
- **In the catalog (modelled, class S)**: family 12, AI Training (18 muscles, in its realm and the whole tower): `training_workers`, `elastic_worker_count`, `training_gang_size`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Gödel scheduler

- **Native**: its placement of units and gangs as shipped.
- **Its test on real Kubernetes (class L)**: not yet written; register row 93.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `task_admission`, `binpack_pressure`, `resource_reservation`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Armada

- **Native**: its queues and fair share across clusters.
- **Its test on real Kubernetes (class L)**: not yet written; register row 94.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `federation_quota`, `global_admission`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Karmada

- **Native**: its propagation and replica division.
- **Its test on real Kubernetes (class L)**: not yet written; register row 95.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `region_dispatch`, `global_failover`, `cross_cluster_replication`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Open Cluster Management

- **Native**: its Placement and ManifestWork.
- **Its test on real Kubernetes (class L)**: not yet written; register row 96.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `workload_migrate_region`, `federation_quota`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeEdge

- **Native**: its edge sync and offline autonomy.
- **Its test on real Kubernetes (class L)**: not yet written; register row 97.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `edge_dispatch`, `edge_offload`, `edge_sync_interval`, `edge_site_node_pool`.
- **Readings**: none yet; nothing is written here before its three runs are in.

## Nephio

- **Native**: its intent-driven deployment and scaling.
- **Its test on real Kubernetes (class L)**: not yet written (a candidate: its sandbox asks more than a free runner gives); register row 98.
- **In the catalog (modelled, class S)**: family 66, Telecom RAN & Edge Radio (12 muscles, in its realm and the whole tower): `ran_slice_resource_budget`, `ran_du_cu_placement`, `ran_cell_sleep`, `ran_carrier_enable`.
- **Readings**: none yet; nothing is written here before its three runs are in.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
