# The governors and orchestrators: native under them, Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's list of 19 October, night: every governor and orchestrator he named runs with the organism native under it, then with Omni-Compass on top of it, on the engine that stands (omni-v12). The organism is a six-worker real Kubernetes cluster (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines, each arm on a fresh cluster, the two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading. Native is the governor as its project ships it; Omni-Compass sits on top with its own levers (the node pool, the service's autoscaler and processor limit, cruise and idle) and never writes the governor's objects, but where the governor owns the service's autoscaler (Crane): there its autoscaler moves reach the autoscaler through the governor's own object, by a plug, as on KEDA. Crane runs on Kubernetes 1.25.16 (its HPA is an API 1.26 removed) and Gödel on 1.24.17 (its supported range), where no pod is resized in place, so no processor limit is moved in any of their arms. Cost: $0 (GitHub's free machines). A governor's line reads only from its own three-run table; until then it says where its runs stand.

| Governor | What it governs | Register row | Where it stands | Readings (A, B and C) |
|---|---|---:|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | pod placement | 88 | as shipped: three runs in; bin-packing profile: three runs in | as shipped: 5 GAIN, 1 LOSS, 0 power given, 16 EVEN, 0 where the runs disagree ([table](V12_VANILLA.md)); bin-packing profile: 5 GAIN, 1 LOSS, 0 power given, 16 EVEN, 0 where the runs disagree ([table](V12_BINPACK.md)) |
| Kueue | batch admission (a job at a time, by queue quota) | 63 | running four ways (below) | runs not yet finished |
| Volcano | batch scheduling (queues, gangs) | 63 | running four ways (below) | runs not yet finished |
| KAI scheduler | AI workload scheduling (queues, fair share, gangs) | 91 | three runs in | 5 GAIN, 0 LOSS, 0 power given, 17 EVEN, 0 where the runs disagree ([table](V12_KAI.md)) |
| Koordinator | QoS colocation (batch work on what latency-sensitive pods leave unused) | 89 | three runs in | 3 GAIN, 0 LOSS, 0 power given, 19 EVEN, 0 where the runs disagree ([table](V12_KOORDINATOR.md)) |
| CruiseKube | rightsizing (requests and limits, in place) | 81 | built; its runs come in the campaign | not yet run |
| Crane | predictive autoscaling and resource governance | 90 | built; its runs come in the campaign | not yet run |
| KubeRay | Ray clusters (the Ray autoscaler) | 92 | built; its runs come in the campaign | not yet run |
| Gödel scheduler | unified online and offline scheduling | 93 | built; its runs come in the campaign | not yet run |
| Armada | multi-cluster batch | 94 | its rig is not yet built | not yet run |
| Karmada | multi-cluster placement | 95 | built; its runs come in the campaign | not yet run |
| Open Cluster Management | multi-cluster management | 96 | built; its runs come in the campaign | not yet run |
| KubeEdge | edge nodes | 97 | its rig is not yet built | not yet run |
| Nephio | network-function automation | 98 | its rig is not yet built | not yet run |

## The four ways (the founder's order of 20 October)

Each system runs four ways in every repetition, each way on a fresh cluster of the same configuration, back to back on one runner, the governor on its own core (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendments 5 and 6): the organism alone (the stream placed by Kubernetes' own scheduler, no orchestrator installed; for Crane, the service's HPA as Kubernetes ships it, `docs/CRANE_PREREGISTRATION.md`), the orchestrator as its project ships it, Omni-Compass on top of the organism alone, and Omni-Compass on top of the orchestrator. Each column is one comparison, the first against the second, paired within the repetition and read by the one key for the first; each cell reads only from its own three-run table. Omni-Compass never places a pod or admits a job: on the organism alone it sits on top of Kubernetes' own scheduler.

| System | Runs (A, B and C) | Omni-Compass on top of it, against it as shipped | it as shipped, against the organism alone | Omni-Compass on the organism alone, against the organism alone | Omni-Compass on the organism alone, against it as shipped | Omni-Compass on top of it, against the organism alone |
|---|---|---|---|---|---|---|
| The KAI scheduler | [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368344021) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368351097) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368358521) | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished |
| Koordinator | [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368366066) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368373713) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368380786) | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished |
| Kueue | [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368387821) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368394823) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368401852) | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished |
| Volcano | [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368409208) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368415819) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368422189) | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished |
| The scheduler's bin-packing profile | [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368428763) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368435483) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39368442002) | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished | runs not yet finished |
| KubeRay | not yet started | not yet run | not yet run | not yet run | not yet run | not yet run |
| Crane | not yet started | not yet run | not yet run | not yet run | not yet run | not yet run |
| The Gödel scheduler | not yet started | not yet run | not yet run | not yet run | not yet run | not yet run |
| Karmada | not yet started | not yet run | not yet run | not yet run | not yet run | not yet run |
| Open Cluster Management | not yet started | not yet run | not yet run | not yet run | not yet run | not yet run |

## The orchestra, the eighth organism (modelled, class S)

The founder's word of 19 October, night: the governors in a catalog group, an organism of their own. Every catalog muscle that stands for a governor's knob (below, under each governor) runs in the modelled organisms as the seven do: each governor's muscles as a body of its own, then all of them together as one body, the orchestra, native and then with Omni-Compass on top at the max, on omni-v12, seeds 3000-3009. A model, not a measurement of the governor itself; every row: [`results/orchestra/ORCHESTRA.md`](../orchestra/ORCHESTRA.md).

| Body | Muscles | Own load | The climb | Work in line |
|---|---:|---|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| Kueue | 5 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| Volcano | 5 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| KAI scheduler | 4 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| Koordinator | 4 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| CruiseKube | 4 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| Crane | 5 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| KubeRay | 3 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| Gödel scheduler | 4 | EVEN (the same as native) | EVEN (the same as native) | EVEN (the same as native) |
| Armada | 3 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Karmada | 4 | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Open Cluster Management | 3 | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) |
| KubeEdge | 4 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Nephio | 4 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| **The orchestra, every governor's muscle once** | 55 | **GAIN (more work + fewer misses)** | **GAIN (more work + fewer misses)** | **GAIN (more work + fewer misses)** |

## The Kubernetes scheduler (vanilla, and its bin-packing profile)

- **Native**: the default scheduler of Kubernetes 1.35 as shipped, which places every pod of every Kubernetes set; and the same release's scheduler with the operator's bin-packing profile (NodeResourcesFit, MostAllocated).
- **Its test on real Kubernetes (class L)**: the batch stream placed by the scheduler alone, in each setting (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 3); register row 88.
- **In the catalog (modelled, class S)**: family 4, Kubernetes Placement & Scheduling (21 muscles, in the spine and every realm): `node_selector`, `node_affinity`, `pod_anti_affinity`, `topology_spread`, `taint_toleration`, `priority_class`, `preemption_policy`, `scheduler_backoff`, `scheduler_scoring_strategy`, `scheduler_plugin_weights`, `scheduling_gates`, `deschedule`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Runs (as shipped)**: A [39356571014](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356571014) (10 pairs), B [39356586356](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356586356) (10 pairs), C [39356601235](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356601235) (10 pairs); engine omni-v12 (digest d38b58fbe28939b8, 47 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, the same |
| queue: job turnaround, submitted to done, mean (s) | LOSS in all three of our runs |
| queue: jobs unfinished at the window's end | EVEN, the same |
| batch: queue finished (s) | EVEN, no difference beyond the noise (2 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | EVEN, no difference beyond the noise (all three runs) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN in all three of our runs |
| response time (ms), 95th percentile | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed requests (%) | EVEN, the same |

Every row of the run: [`results/live/V12_VANILLA.md`](V12_VANILLA.md).

- **Runs (bin-packing profile)**: A [39356578556](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356578556) (10 pairs), B [39356594135](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356594135) (10 pairs), C [39356608147](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39356608147) (10 pairs); engine omni-v12 (digest d38b58fbe28939b8, 47 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | LOSS in all three of our runs |
| queue: jobs unfinished at the window's end | EVEN, the same |
| batch: queue finished (s) | EVEN, no difference beyond the noise (2 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | EVEN, no difference beyond the noise (all three runs) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN in all three of our runs |
| response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | EVEN, the same |

Every row of the run: [`results/live/V12_BINPACK.md`](V12_BINPACK.md).


## Kueue

- **Native**: Kueue v0.20.2 with the operator's single ClusterQueue sized to the workers.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 1, Work Admission & Demand Shaping (19 muscles, in its realm and the whole tower): `job_admission`, `batch_admission`, `queue_concurrency`, `queue_backpressure`, `tenant_admission`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Volcano

- **Native**: Volcano v1.16.0 with its default queue as shipped.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `task_priority`, `task_preemption`, `binpack_pressure`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## KAI scheduler

- **Native**: the KAI scheduler v0.18.6 with its chart's default queues.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 1; register row 91.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `cluster_quota`, `task_preemption`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Runs**: A [39350900880](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350900880) (10 pairs), B [39350907916](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350907916) (10 pairs), C [39350915166](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39350915166) (10 pairs); engine omni-v12 (digest d38b58fbe28939b8, 47 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (2 of 3 runs) |
| queue: jobs unfinished at the window's end | EVEN, the same |
| batch: queue finished (s) | EVEN, no difference beyond the noise (1 of 3 runs) |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | EVEN, no difference beyond the noise (all three runs) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN in all three of our runs |
| response time (ms), 95th percentile | EVEN, no difference beyond the noise (all three runs) |
| failed requests (%) | EVEN, the same |

Every row of the run: [`results/live/V12_KAI.md`](V12_KAI.md).


## Koordinator

- **Native**: Koordinator 1.8.0, colocation on as shipped, the operator's colocation profile.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 2; register row 89.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `oversubscription`, `resource_reclaim`, `binpack_pressure`, `spread_pressure`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Runs**: A [39359085965](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359085965) (10 pairs), B [39359094679](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359094679) (10 pairs), C [39359103518](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/39359103518) (10 pairs); engine omni-v12 (digest d38b58fbe28939b8, 47 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: job turnaround, submitted to done, mean (s) | EVEN, no difference beyond the noise (all three runs) |
| queue: jobs unfinished at the window's end | EVEN, no difference beyond the noise (all three runs) |
| batch: queue finished (s) | EVEN, no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | EVEN, no difference beyond the noise (all three runs) |
| worker nodes in service, mean | EVEN, no difference beyond the noise (all three runs) |
| node-hours | EVEN, no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh) | EVEN, no difference beyond the noise (all three runs) |
| energy (Wh) | EVEN, no difference beyond the noise (all three runs) |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN in all three of our runs |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| failed requests (%) | EVEN, the same |

Every row of the run: [`results/live/V12_KOORDINATOR.md`](V12_KOORDINATOR.md).


## CruiseKube

- **Native**: CruiseKube applying its own recommendations as shipped.
- **Its test on real Kubernetes (class L)**: `docs/CRUISEKUBE_PREREGISTRATION.md`; register row 81.
- **In the catalog (modelled, class S)**: family 3, Container Resources (25 muscles, in the spine and every realm): `cruisekube_request_rightsizing`, `in_place_resize`, `cpu_request`, `memory_request`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Crane

- **Native**: Crane 0.11.0 and the Prometheus it reads, as its installation guide installs them, the service's autoscaler handed to its Effective HPA in auto mode (its own example for this service), on Kubernetes 1.25.16 (Crane builds its HPA as autoscaling/v2beta2, which 1.26 removed).
- **Its test on real Kubernetes (class L)**: the served app under the closed load of the add-on sets, four ways (`docs/CRANE_PREREGISTRATION.md`); register row 90.
- **In the catalog (modelled, class S)**: family 2, Kubernetes Workload Scaling (32 muscles, in the spine and every realm): `hpa_cpu_target`, `hpa_custom_target`, `hpa_scaling_rate_policies`, `hpa_min_replicas`, `hpa_max_replicas`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeRay

- **Native**: KubeRay 1.7.1 and one Ray cluster (Ray 2.52.0) from KubeRay's own autoscaling sample, the Ray autoscaler as shipped.
- **Its test on real Kubernetes (class L)**: the batch stream as Ray jobs (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 7); register row 92.
- **In the catalog (modelled, class S)**: family 12, AI Training (18 muscles, in its realm and the whole tower): `training_workers`, `elastic_worker_count`, `training_gang_size`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Gödel scheduler

- **Native**: the Gödel scheduler built from its pinned source and deployed by its own manifests, its placement as shipped, on Kubernetes 1.24.17 (it supports 1.21.4 to 1.24.6).
- **Its test on real Kubernetes (class L)**: the batch stream placed by Gödel, four ways (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 8); register row 93.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `task_admission`, `binpack_pressure`, `resource_reservation`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: EVEN (the same as native); the climb: EVEN (the same as native); work in line: EVEN (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Armada

- **Native**: its queues and fair share across clusters.
- **Its test on real Kubernetes (class L)**: not yet written; register row 94.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `federation_quota`, `global_admission`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Karmada

- **Native**: Karmada v1.19.0 on a cluster of its own, two member clusters joined, its placement of the stream as shipped with the operator's one propagation policy.
- **Its test on real Kubernetes (class L)**: the batch stream sent to a group of two clusters, four ways (`docs/GROUP_PREREGISTRATION.md`); register row 95.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `region_dispatch`, `global_failover`, `cross_cluster_replication`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (more work + fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Open Cluster Management

- **Native**: OCM's hub (bundle 1.4.0, clusteradm v1.4.0) on a cluster of its own, two member clusters registered and accepted, a Placement per job with its default prioritizers and the job as a ManifestWork where it decided.
- **Its test on real Kubernetes (class L)**: the batch stream sent to a group of two clusters placed by OCM, four ways (`docs/GROUP_PREREGISTRATION.md`, amendment 1); register row 96.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `workload_migrate_region`, `federation_quota`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (more work + fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (more work + fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeEdge

- **Native**: its edge sync and offline autonomy.
- **Its test on real Kubernetes (class L)**: not yet written; register row 97.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `edge_dispatch`, `edge_offload`, `edge_sync_interval`, `edge_site_node_pool`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Nephio

- **Native**: its intent-driven deployment and scaling.
- **Its test on real Kubernetes (class L)**: not yet written (a candidate: its sandbox asks more than a free runner gives); register row 98.
- **In the catalog (modelled, class S)**: family 66, Telecom RAN & Edge Radio (12 muscles, in its realm and the whole tower): `ran_slice_resource_budget`, `ran_du_cu_placement`, `ran_cell_sleep`, `ran_carrier_enable`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
