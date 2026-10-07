# The Omni-Compass register: every muscle wired, every benchmark run, every benchmark still to run

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


One list to see and show. Native is always the system running on its own: its own controller, its own autoscaler, its
own tap changer, its own servo. Omni-Compass is always on top of it, never instead of it. A row names the benchmark's
owner when the benchmark is someone else's. Every result named here is read from the file in its last column.

Status words: **done** (result in the repo), **running** (on GitHub or Azure now), **ready** (harness built, waiting
on hardware or a go), **next** (being built now), **queued** (in the order of section 4, one or two at a time).

Last updated 2026-10-07.

## 1. Every muscle wired (945 muscles, 59 families, four realms and the shared spine of 257; v1 had 656 in 46)

A muscle is one knob on one real system that Omni-Compass may move inside its cover: **capacity** (how many machines,
replicas or units), **setpoint** (a temperature, voltage, pressure or speed), **power** (a power or effort cap), or
**admission** (how much work is let in at once). Each family is modelled by a plant: the model that stands in for that
kind of system until it is measured live.


| # | Realm | Family | Muscles | Plant (model) | Knobs Omni holds |
|---:|---|---|---:|---|---|
| 1 | Compute / AI / Cloud | AI Inference Serving | 24 | compute_pool/gpu | capacity 13, admission 8, setpoint 2, power 1 |
| 2 | Compute / AI / Cloud | AI Training | 18 | compute_pool/gpu_batch | capacity 15, setpoint 1, admission 1, power 1 |
| 3 | Compute / AI / Cloud | Cloud VM & Capacity | 21 | compute_pool/node | capacity 19, setpoint 1, admission 1 |
| 4 | Compute / AI / Cloud | Container Resources | 23 | compute_pool/server | capacity 17, setpoint 3, admission 3 |
| 5 | Compute / AI / Cloud | Cross-Cluster, Multi-Region & Edge | 15 | compute_pool/node | capacity 9, admission 6 |
| 6 | Compute / AI / Cloud | DPU SmartNIC & Programmable IO | 12 | compute_pool/fabric | capacity 10, admission 2 |
| 7 | Compute / AI / Cloud | Distributed Cluster Managers | 15 | compute_pool/batch | capacity 8, admission 7 |
| 8 | Compute / AI / Cloud | GPU Fabric & RDMA | 18 | compute_pool/fabric | capacity 14, admission 4 |
| 9 | Compute / AI / Cloud | HPC & Distributed Compute | 19 | compute_pool/batch | capacity 10, admission 6, power 2, setpoint 1 |
| 10 | Compute / AI / Cloud | Host CPU & Memory | 23 | compute_pool/cpu_host | power 12, capacity 10, admission 1 |
| 11 | Compute / AI / Cloud | Kubernetes Dynamic Device Allocation | 8 | compute_pool/gpu | capacity 6, admission 1, setpoint 1 |
| 12 | Compute / AI / Cloud | Kubernetes Placement & Scheduling | 20 | compute_pool/server | capacity 13, admission 5, setpoint 2 |
| 13 | Compute / AI / Cloud | Kubernetes Workload Scaling | 31 | compute_pool/server | capacity 17, admission 8, setpoint 6 |
| 14 | Compute / AI / Cloud | NVIDIA GPU Hardware | 19 | compute_pool/gpu | capacity 10, power 6, admission 2, setpoint 1 |
| 15 | Compute / AI / Cloud | Node Fleet & Karpenter-Class Control | 24 | compute_pool/node | capacity 18, admission 5, setpoint 1 |
| 16 | Compute / AI / Cloud | OpenShift & Machine API | 9 | compute_pool/node | capacity 5, admission 4 |
| 17 | Compute / AI / Cloud | Quantum Computing Control Simulation | 16 | compute_pool/qpu | capacity 10, admission 4, setpoint 1, power 1 |
| 18 | Compute / AI / Cloud | Work Admission & Demand Shaping | 19 | compute_pool/server | admission 19 |
| 19 | Physics / Robotics / Autonomous | Automotive EV & Mobile Powertrain | 14 | motion_axis/ev_traction | power 11, admission 2, capacity 1 |
| 20 | Physics / Robotics / Autonomous | Aviation & Autonomous Flight | 20 | motion_axis/flight_axis | admission 9, capacity 7, power 4 |
| 21 | Physics / Robotics / Autonomous | Elevators & Vertical Transport (v2) | 12 | motion_axis/elevator_hoist | admission 7, capacity 3, power 2 |
| 22 | Physics / Robotics / Autonomous | Marine Propulsion & Vessel Automation (v2) | 12 | motion_axis/marine_propulsion | capacity 5, power 5, admission 2 |
| 23 | Physics / Robotics / Autonomous | Rail Traction & Train Control (v2) | 14 | motion_axis/rail_traction | power 6, capacity 4, admission 4 |
| 24 | Physics / Robotics / Autonomous | Robotics Fleet & Warehouse Automation | 15 | compute_pool/robot_fleet | capacity 12, admission 3 |
| 25 | Physics / Robotics / Autonomous | Robotics Motion Control | 18 | motion_axis/robot_joint | capacity 14, power 4 |
| 26 | Physics / Robotics / Autonomous | Spacecraft & Flight Software | 14 | motion_axis/reaction_wheel | admission 6, power 4, capacity 4 |
| 27 | Energy / Facility / Industrial | Agriculture & Irrigation (v2) | 14 | process_loop/irrigation | setpoint 10, capacity 2, power 1, admission 1 |
| 28 | Energy / Facility / Industrial | Building & Critical Environment HVAC | 15 | thermal_zone/building | capacity 6, setpoint 5, admission 3, power 1 |
| 29 | Energy / Facility / Industrial | Cooling, Chillers & Thermodynamics | 18 | thermal_zone/data_hall | capacity 8, setpoint 6, power 2, admission 2 |
| 30 | Energy / Facility / Industrial | District Heating & Cooling (v2) | 13 | process_loop/district_heat | setpoint 7, capacity 3, admission 2, power 1 |
| 31 | Energy / Facility / Industrial | Energy Storage & Microgrid | 19 | energy_storage/microgrid | power 10, capacity 4, setpoint 3, admission 2 |
| 32 | Energy / Facility / Industrial | Facility & Grid Optimization | 15 | energy_storage/facility | power 5, admission 5, capacity 4, setpoint 1 |
| 33 | Energy / Facility / Industrial | Grid Transmission & Distribution | 12 | process_loop/feeder_voltage | setpoint 4, admission 4, capacity 2, power 2 |
| 34 | Energy / Facility / Industrial | Healthcare Critical Environments (v2) | 13 | thermal_zone/hospital | setpoint 7, capacity 3, admission 2, power 1 |
| 35 | Energy / Facility / Industrial | Industrial PLC & Process Automation | 18 | process_loop/process | capacity 8, setpoint 6, admission 3, power 1 |
| 36 | Energy / Facility / Industrial | Mining & Mineral Processing (v2) | 14 | process_loop/mill | setpoint 8, power 2, capacity 2, admission 2 |
| 37 | Energy / Facility / Industrial | Oil & Gas Pipelines (v2) | 14 | process_loop/pipeline | setpoint 8, admission 3, capacity 2, power 1 |
| 38 | Energy / Facility / Industrial | PDU, UPS & Electrical Distribution | 18 | energy_storage/ups | power 8, capacity 5, admission 3, setpoint 2 |
| 39 | Energy / Facility / Industrial | Pharmaceutical & Food Manufacturing (v2) | 14 | process_loop/batch_reactor | setpoint 10, admission 4 |
| 40 | Energy / Facility / Industrial | Power Generation & Turbine Control (v2) | 14 | process_loop/turbine | setpoint 10, capacity 2, admission 2 |
| 41 | Energy / Facility / Industrial | Renewable Generation & Inverter Control (v2) | 13 | process_loop/inverter | setpoint 6, capacity 3, admission 3, power 1 |
| 42 | Energy / Facility / Industrial | Semiconductor Fab & Precision Manufacturing | 13 | process_loop/chamber | capacity 6, admission 4, setpoint 2, power 1 |
| 43 | Energy / Facility / Industrial | Water Wastewater & Pumping | 12 | process_loop/water | admission 5, setpoint 4, power 2, capacity 1 |
| 44 | Distribution / Specialized | Cache & Memory Services | 16 | compute_pool/server | capacity 11, admission 4, setpoint 1 |
| 45 | Distribution / Specialized | Commerce & Payment Systems | 15 | compute_pool/commerce | admission 8, capacity 5, setpoint 2 |
| 46 | Distribution / Specialized | Data Analytics & ETL | 15 | compute_pool/batch | capacity 9, admission 4, setpoint 2 |
| 47 | Distribution / Specialized | Database & Transactions | 19 | compute_pool/database | capacity 14, admission 5 |
| 48 | Distribution / Specialized | Medical Imaging & Clinical Systems (v2) | 12 | compute_pool/clinical | admission 9, capacity 2, setpoint 1 |
| 49 | Distribution / Specialized | Messaging & Streaming | 18 | compute_pool/server | capacity 11, admission 7 |
| 50 | Distribution / Specialized | Network Routing & Switching | 19 | compute_pool/network | capacity 9, admission 6, setpoint 3, power 1 |
| 51 | Distribution / Specialized | Observability & Telemetry | 9 | compute_pool/server | capacity 4, admission 3, setpoint 2 |
| 52 | Distribution / Specialized | Ports & Maritime Logistics (v2) | 12 | compute_pool/port | capacity 5, admission 5, power 1, setpoint 1 |
| 53 | Distribution / Specialized | Reliability, Security & Recovery | 12 | compute_pool/server | capacity 6, admission 6 |
| 54 | Distribution / Specialized | Runtime & Application | 17 | compute_pool/server | capacity 12, admission 5 |
| 55 | Distribution / Specialized | Search, Indexing & Vector DB | 16 | compute_pool/server | capacity 10, admission 6 |
| 56 | Distribution / Specialized | Service Mesh & API Reliability | 16 | compute_pool/server | admission 7, capacity 7, setpoint 2 |
| 57 | Distribution / Specialized | Storage Block/File/Object | 20 | compute_pool/storage | capacity 17, admission 2, power 1 |
| 58 | Distribution / Specialized | Telecom RAN & Edge Radio | 12 | compute_pool/ran | capacity 7, admission 3, setpoint 1, power 1 |
| 59 | Distribution / Specialized | Workflow, Logistics & Fulfillment | 15 | compute_pool/workflow | capacity 10, admission 5 |

**945 muscles in 59 families (Omni v2: the 656 of v1 byte for byte, 118 real controls the realm study had found that the tower lacked, and 171 in the thirteen families marked v2).** Every muscle by name, with its knob and what it is for: `realms/catalog.csv` and `docs/MUSCLE_CATALOG.md`; the sources of every added muscle: `docs/realm_study/TRUE_MUSCLES.csv` and `realms/wave4_families.csv`.

How they are proven so far: every muscle alone, and every organism whole, on its model (`results/realms/REALMS.md`):
**57 superior within guardrails, 9 energy improvement with a service tradeoff, 586 noninferior, 0 not established,
0 worse; all five organisms superior within guardrails.** Evidence class S: a model, not a meter. The live rows of
section 2 are where muscles meet real systems.

## 2. Every benchmark, by platform

Which engine each result ran on, and its v1 replications A, B and C: [`docs/OMNI_V1.md`](OMNI_V1.md).

### 2.1 Kubernetes on GitHub (real clusters, kind; evidence: real software, declared energy model)

| # | Benchmark | Native | Omni moves | Status | Result (Omni on top vs native) | File |
|---:|---|---|---|---|---|---|
| 1 | Steady work in steps, 10 pairs × 3 runs (v1 and v3) | Kubernetes HPA | replicas, floor, nodes | done on both engines, confirmed in 3 of 3 | v1: p95 −65% to −69%, machines −1.5% to −3.4%, standby-model energy −1.0% to −2.9%, confirmed better. **v3 (runs 37568428903, 37573736336, 37578883344): p95 −65% to −66%, p99 −68% to −72%, machines −1.5% to −2.9%, standby-model energy −1.3% to −2.1%, time over the line −97% to −99%, all confirmed better; failed requests 0 in both arms** | `results/live/V3_STEADY.md`, `results/live/V1_STEADY.md` (earlier engine: `STEADY.md`) |
| 2 | Demand that wanders, 10 pairs × 3 runs (v1 and v3) | Kubernetes HPA | replicas, floor, nodes | done on both engines, confirmed in 3 of 3 | v1: p95 −56% to −60%, failed requests −12% to −13%, confirmed better. **v3 (runs 37568434811, 37578868385, 37583079914): p95 −57% to −63%, p99 −40% to −51%, mean response −46% to −49%, time over the line −39% to −40%, failed requests −9% to −12%, all confirmed better**; machines and energy no difference beyond the noise on both engines | `results/live/V3_WANDERING.md`, `results/live/V1_WANDERING.md` (earlier engine: `WANDERING.md`) |
| 3 | All four at once (more work, faster, fewer machines, less energy), 10 pairs × 3 runs (v1 and v3) | Kubernetes HPA | replicas, floor, nodes | done on both engines, confirmed in 3 of 3 | v1: **work inside the line +42% to +48%**, p95 −57% to −63%, failed requests −12% to −13%, confirmed better. **v3 (runs 37568440904, 37578875988, 37583092384): work inside the line +35% to +49%, p95 −61% to −66%, mean response −45% to −46%, time over the line −39% to −46%, failed requests −11% to −14%, all confirmed better**; machines and energy no difference beyond the noise on both engines | `results/live/V3_ALL_FOUR.md`, `results/live/V1_ALL_FOUR.md` (earlier engine: `ALL_FOUR.md`) |
| 4 | Fairness, a noisy neighbour, 10 pairs × 3 runs (v1 and v3) | Kubernetes HPA | replicas, admission | done on both engines | v1 and **v3 (runs 37568447257, 37573744350, 37578890876)**: no difference beyond the noise on every row, the neighbour's time over its line included: Omni neither helps nor hurts | `results/live/V3_FAIRNESS.md`, `results/live/V1_FAIRNESS.md` (earlier engine: `FAIRNESS.md`) |
| 5 | Faults: machine down, spike, runaway pod, blind probe, 10 pairs × 3 runs (v1 and v3) | Kubernetes HPA | replicas, floor, nodes | done on both engines, confirmed in 3 of 3 | v1: mean response −36% to −52%, p95 −61% to −64%, confirmed better. **v3 (runs 37568453602, 37573751219, 37578899103): p95 −47% to −62%, p99 −39% to −63%, time over the line −22% to −42%, confirmed better; failed requests lower in all three, clear of the noise in 1 of 3**; machines and energy no difference beyond the noise on both engines | `results/live/V3_FAULTS.md`, `results/live/V1_FAULTS.md` (earlier engine: `FAULTS.md`) |
| 6 | A queue of batch jobs (cruise, then the emergency brake), 10 pairs × 3 runs (v1 and v3) | Kubernetes Jobs + HPA | nodes, floor | done on both engines, confirmed in 3 of 3 | v1: machines −15% to −24%, after the queue −26% to −36%, mean response −11% to −13%, confirmed better; the queue finished 0.7% to 0.9% later (clear of the noise in 2 of 3 runs). **v3 (runs 37568459663, 37573759437, 37581021752): machines −19% to −23%, after the queue −29% to −35%, standby-model energy −13% to −16%, mean response −10% to −14%, time over the line −2% to −4%, all confirmed better; the queue finished no difference beyond the noise in all three runs; failed requests 0 in both arms in run C** | `results/live/V3_BATCH.md`, `results/live/V1_BATCH.md` (earlier engine: `BATCH.md`) |
| 7 | The six organisms with the real cluster inside (Compute/AI/Cloud, Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized, the whole tower of 656, the four stacked of 1,226), 5 pairs each | HPA + the organisms' native settings | every muscle of the organism | v1 done, A on the frozen engine (run 37359815637: 98 of 100 cells; the two 1,000-copy stack cells cut off by GitHub's six-hour job limit); v3 done at 10 and 100 copies (run 37501769448, 12 cells, 5 pairs each, 62 of 62 jobs): better on 4 to 6 gauges in every cell, worse on none beyond the noise except a rounding-level work loss (6 to 11 parts in a million) in 4 of the 12 cells; the stack at 100 copies off the clock in 4 of 5 repetitions (up to 277 s past a 1,440 s window, marked); the 1,000-copy cells run on Azure (row 8) | v1: p95 and time over the line better in every cell of every organism at 1, 10, 100 and 1,000 copies; 0 gauges worse beyond the noise except a rounding-level work loss (−0.0003%) in the larger cells and HPA replicas +0.7% in one; machines 6 in both arms (no autoscaler under kind); off the clock at 1,000 copies in 2 of 3 repetitions of the Physics realm and of the tower (up to 3,820 s), marked | `results/live/V3_SIX_KUBE.md` (v3), `results/live/V1_SIX_KUBE.md` (v1), `results/live/SIX_KUBE.md` (the earlier engine) |
| 8 | The big organisms (the whole tower and the four stacked at 1,000 copies on a rented Azure machine) | as 7 | as 7 | v1 done: the tower 3 of 3 (run 37359820055; repetition 3 off the clock) and the stack 3 of 3 from the detached machine (collection run 37575930111; the compass arm off the clock in all three, up to 615 s past a 2,880 s window), one report; v3: the stack running detached with a 10,800 s window, the tower after | tower at 1,000 copies (v1): p95 −95% (4.1 s → 0.2 s), time over the line −99.7%, machines 6 in both arms, organism energy −0.2%, organism work rounding-level worse; the stack at 1,000 copies (v1): p95 −74% (274 → 70 ms), p99 −83%, machines 6 in both arms, organism energy −0.2%, organism work rounding-level worse, compass arm off the clock | workflows `big-organism`, `big-organism-detached`; `docs/OMNI_V1.md`, `docs/OMNI_V3.md` |
| 9 | Scale: KWOK simulated nodes, 50 / 500 / 1,000 | Kubernetes scheduler + HPA | replicas, nodes | running on every push; report not yet in the repo | | workflow `kwok-scale` |

### 2.2 Azure AKS (real cloud machines, Azure's own bill)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 10 | Steady load, 5 pairs (earlier engine) | AKS cluster autoscaler + HPA | replicas, floor | done | index +7.5%; response +25.4% faster; machines −0.8% | `results/live/AKS_BILL.md` |
| 11 | Steady load on Omni v1, 5 pairs | as 10 | as 10 | done (run 37385657374, commit `f162ce8`) | no difference beyond the noise on any gauge: bill −4.7% (interval −$0.028 to +$0.022), machines billed −4.7%, p95 −2.1%, failed requests −32%, all inside the noise; Omni's own CPU 0.014 cores, the declared cost | `results/live/V1_AKS_STEADY.md` |
| 12 | Burst sized to the cluster on Omni v1, 1,800 s, load 1 3 1 4 1 3 | as 10 | as 10 | done, 5 pairs (run 37534538088, `f162ce8`; repetition 4 lost its native cluster to an Azure API error in the first attempt and was run again by itself) | bill +5.0% (interval −$0.003 to +$0.013), machines +2.0%, p95 +15%, failed requests −30% (22% → 16%), all inside the noise; p99 −34% (6.0 s → 4.0 s) clear of the noise in this single run; B and C to follow | `results/live/V1_AKS_BURST.md` |
| 12b | Steady and burst on Omni v3, 4 workers | as 10 | as 10 | queued (one Azure run at a time) | | workflow `aks-metered` |
| 12c | Steady on Omni v3, a fleet of eight machine families, 39 workers (4 to 5 a family under the 10-vCPU-a-family allowance), replica ceiling 351, load `18 35 53 18 35 18`, 900 s, 5 pairs | Azure's cluster autoscaler across eight work pools + the HPA | as 10 | preregistered 2026-10-07 (replacing the one-family 11- and 15-worker plan the allowance refused); next to run | | `docs/K8S_COMPASS_PREREGISTRATION.md` (the fleet that can show one machine) |
| 12d | Burst on Omni v3, the same fleet, load `11 35 11 53 11 35`, 1,800 s, 5 pairs | as 12c | as 10 | queued after 12c | | as 12c |

### 2.3 GPU (NVIDIA cards, the card's own power meter)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 13 | One card (A10 on Lambda), 10 pairs, earlier card controller | the card's default power limit and clocks | power limit, clock ceiling | old (earlier card controller; new card runs replace it) | GPU energy −3.5% but 95th-percentile response +58.5% slower, both proven: a trade-off, not a win | `results/gpu/run-20261002T082232Z/` |
| 14 | One card on the current card controller | as 13 | as 13 | ready (founder's go on Lambda) | | `docs/GPU_RUN_GUIDE.md` |
| 15 | The card inside the six organisms | as 13 | as 13 + the organism | done once on the earlier controller; rerun ready | | `results/hil/run-20261002T082232Z/` |
| 16 | Eight cards | as 13 | as 13, per card and pooled | ready | | `scripts/gpu_8card.sh` |
| 17 | Real model serving (vLLM) on the card | vLLM as shipped | power limit, clocks, admission | ready | | `scripts/gpu_vllm.sh` |
| 18 | Two-wire card model, 10 seeds + 10 fresh seeds | the card's defaults | power limit, clocks | done (model) | work per energy +6.9% / +3.8%, p95 faster | `results/sim/gpu_two_wire/` |

### 2.4 CPU and power budgets (models calibrated on MLPerf power figures)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 19 | CPU and GPU on one conserved power budget | a fixed split | the split | done (model) | +1.4% to +5.7% work at the same cap, never over budget | `results/hardware/NODE_EXCHANGE_*.json` |
| 20 | GPU groups sharing a site budget, held out | a fixed split | the split | done (model) | 0 minutes over budget | `results/hardware/SITE_EXCHANGE_HELDOUT_*.json` |
| 21 | Fleet on PlanetLab CPU traces, held out | Kubernetes-style reference | capacity | done (model) | | `results/fleet/planetlab/` |
| 22 | The muscle studies, development and held out: cold start, containment, cooling, GPU packing, health, inference, power smoothing | each muscle's native rule | each muscle's knob | done (model) | | `results/muscles/` |
| 23 | The tower off and on, 100 scenarios | Kubernetes reference | the whole tower | done (model) | | `results/tower_off_on/` |

### 2.5 The modelled muscles (the organisms at 1 / 10 / 100 / 1,000 copies)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 24 | Every muscle alone and every organism whole | each plant's native setting | each muscle's knob | **v3 done, A/B/C (runs 37429141430, 37429151263, 37429161515), reproduced to the last digit in 3 of 3**; v2 (runs 37422832244, 37422840154, 37422847697) and v1 (656) done before it | v3, 945 muscles: 124 superior within guardrails, 807 no difference beyond the noise, 9 energy improvement with a service tradeoff (5 of them v1's: a host's minimum clock and four reaction-wheel power caps; 4 district heating setpoints), 4 service improvement with an energy tradeoff, 1 not established (hoist_speed_target (elevator_hoist, capacity)), **0 worse**; **every organism superior within guardrails** (work per energy: Compute +0.1%, Physics +0.1%, Energy +0.3%, Distribution +0.2%, the tower +0.3%; work unchanged; time over the line not above native's). v2 read Physics and the tower as a service tradeoff, carried by rail, marine and elevator speed muscles the slack gate now leaves native | `results/realms/REALMS.md` (v3), `results/realms/v2/REALMS.md` (v2), `results/realms/v1/REALMS.md` (v1), `docs/OMNI_V3.md` |
| 25 | The organisms at 1x / 10x / 100x / 1,000x copies, 1 to 1,000 runs | as 24 | as 24 | **v3: 1, 10, 100 and 1,000 copies done, 84 of 90 cells** (runs 37430723080, 37433972731, 37501765605, 37578946088; 1,000 paired runs per organism at 1, 10 and 100 copies, 10 at 1,000); v1 done except 1,000x at 100 and 1,000 runs (beyond the machines available) | v3: every organism superior within guardrails at every cell of 10 runs or more, work per energy +0.07% to +0.37%, the same figure at every size from 1 to 1,000 copies; v1: +0.08% to +0.21%, the same at every scale | `results/scale/GRID.md` (v3), `results/scale/v1/GRID.md` (v1) |

### 2.6 Energy, buildings, batteries and UPS (independent simulators)

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 26 | CityLearn, every district it ships (Intelligent Environments Lab, UT Austin): buildings, solar, batteries, EVs | CityLearn's own rule-based controller | battery and storage setpoints | done, A/B/C on v1; **v3 done, A/B/C** (runs 37568381751, 37568399439, 37568416917: 71 score-rows confirmed better, 33 confirmed worse, 1 where the runs differ, the same pattern as v1, the runner being the same bytes) | 11 battery districts: electricity bought, daily peak and daily unevenness confirmed better in all 11; carbon better in 8; the bill better in 1, worse in 7 (the 2023 districts, +0.2% to +0.35%); ramping better in 4, worse in 7 (+4.5% to +6.2%); the comfort score varies between CityLearn's own runs and is not claimed; 3 districts have no battery; 8 CityLearn cannot run | `results/live/V3_CITYLEARN.md` (v3), `results/live/V1_CITYLEARN.md` |
| 27 | UPS and battery reserve | the UPS's own reserve | none: a reserve held for an outage is never a lever (physics criterion) | done (model) | native by design | `docs/MECHANISM_OF_ACTION.md` §9.6 |
| 28 | Power grid: SimBench grids solved by pandapower (Fraunhofer IEE, Uni Kassel) | the substation tap changer at 1.00 per unit | the tap changer's setpoint (conservation voltage reduction) | done, A/B/C on v1 (runs 37377029333, 37397142210, 37412578757) **and on v3 (runs 37568375564, 37568393269, 37568411160): the same table to the digit, 67 gauge-rows better, 14 worse, 0 where the runs differ** (the runner is the same bytes); 11 untouched grids, both load models, reproduced in 3 of 3 | ZIP loads: energy drawn confirmed better in 11 of 11 (−1.3% to −1.5%), net import better in 11 of 11 (−1% to −15%), losses better in 7 and confirmed worse in 4 (rural and semi-urban grids with their own generation, +0.6% to +1.5%), tap operations fewer in 10 of 11 (−27% to −36%) and 4 → 8 a year in one rural grid (worse, the declared cost), never more often outside the band, less often in 2; constant-power loads: energy drawn the same (the load does not depend on voltage, as declared), import better in 7 and worse by 0.01% to 0.03% in 4, losses as above | `results/live/V3_PANDAPOWER.md`, `results/live/V1_PANDAPOWER.md`, `docs/PANDAPOWER_PREREGISTRATION.md`, workflow `pandapower` |

### 2.7 Robotics

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 29 | Robot arms in MuJoCo (Google DeepMind): Franka Panda (tuning), UR5e, KUKA iiwa 14, Kinova Gen3 from MuJoCo Menagerie, a pick-and-place cycle inside a takt | each robot's own shipped position servos | the speed override inside the takt; a paired physics trial leaves it native where a slower cycle is not cheaper | done, A/B/C on v1, reproduced in 3 of 3; **v3 done, A/B/C** (runs 37568387334, 37568405026, 37568422829, the three untouched robots, reproduced in 3 of 3: the same readings as v1, the runners being the same bytes) | the same job inside the same takt, hit more accurately with less force on the motors: Gen3 peak torque −29%, tracking error −21%, copper −11%, energy per takt −0.8%, all confirmed better; Panda (tuning) peak torque −10%, tracking error −21%, energy per takt −0.5% confirmed better, copper loss +14% confirmed worse; UR5e and iiwa 14: slowing would cost on their own figures, left native, nothing for Omni to move | `results/live/V3_MUJOCO.md` (v3), `results/live/V1_MUJOCO.md`, `results/live/V1_MUJOCO_PANDA.md`, `docs/ROBOTICS_PREREGISTRATION.md` |

### 2.8 Databases

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 30 | PostgreSQL 16 behind PgBouncer 1.22 (the PostgreSQL Global Development Group; the PgBouncer project), pgbench's TPC-B-like load stepping one notch at a time: `tpcb` (tuning), `select`, `simple_update`, `tpcb_hot` (untouched) | the pooler's shipped pool of 20 server connections, the DBA's one fixed setting | the pool size, through PgBouncer's own console, inside [2, 90]; handed back at the end | preregistered 2026-10-06; tuning run done (37420052827, not counted); the first untouched run (37425853293) was a loss on the read-only workload and is recorded, not counted; **amendment 1** (the reading sees the pooler's queued clients; the dwell holds only the brake) declared before the counted runs; **A/B/C on the amended rule done** (runs 37435740735, 37435751322, 37435761371): `results/live/V3_PGBENCH.md` | counted, three runs on amendment 1: server connections held open (the machines) **confirmed better** on `select` (−61% to −63%) and `tpcb_hot` (−69% to −72%), the runs disagree on `simple_update` (+12% in one run, −34% and −35% in two); host CPU-seconds **confirmed worse** on all three (+14% to +28%); work inside the line, throughput and every latency gauge no difference beyond the noise on GitHub's shared runner (native's own p95 swings a hundredfold between repetitions); 0 failed transactions in both arms; the knob handed back in every arm. The first untouched run, on the first rule, is kept in the preregistration: `select` −47% work inside the line, worse. tuning run: server connections alive 20 → 9.3 (−53%, better); work inside the 50 ms line, throughput, p50, p95 and p99 no difference beyond the noise (p95 1,361 → 433 ms with a wide interval: native's own p95 swung from 86 to 3,331 ms between repetitions); host CPU-seconds +11% **worse**; CPU per 1,000 transactions inside the line no difference; failed transactions 0 and 0; the knob handed back in every arm | `docs/POSTGRES_PREREGISTRATION.md`, workflow `pgbench`, `tools/run_pgbench.py` |

### 2.9 Outside readers

ChatGPT and Grok read the results to analyse them, never to produce them: `results/external_review/`.

## 3. What is not measured yet, said plainly

- The current card controller has not run on a real card (rows 14 to 17).
- The Kubernetes energy figure is a declared model; Azure's is its bill of machines; only the GPU rows carry a meter.
- No muscle has been measured live outside compute, the card, and the independent simulators of section 2.6.

## 4. Every open benchmark still to run, in order (one or two at a time)

Each has a recognised open benchmark with its own native controller, so Omni-Compass can sit on top of something that
is not ours.

| Order | Domain | Open benchmark (owner) | Native it runs on top of | Omni's lever | Status |
|---:|---|---|---|---|---|
| 1 | Robot arms | MuJoCo Menagerie: Panda, UR5e (Google DeepMind) | shipped position servos | motion speed, effort | next |
| 2 | Legged robots | MuJoCo Menagerie: Unitree Go2; MuJoCo Playground | shipped gait controller | gait speed, effort | queued |
| 3 | Drones | gym-pybullet-drones (University of Toronto) | its PID controller | speed, thrust margin | queued |
| 4 | Spacecraft attitude, reaction wheels | Basilisk (University of Colorado, LASP) | its attitude feedback law | wheel effort cap | queued |
| 5 | Transmission grid | Grid2Op / L2RPN (RTE France) | its do-nothing and expert baselines | redispatch, topology timing | queued |
| 6 | Distribution feeders | OpenDSS IEEE 13 / 34 / 123-bus feeders (EPRI, IEEE) | their voltage regulators and capacitors | regulator setpoints | queued |
| 7 | EV charging | ACN-Sim with ACN-Data (Caltech) | uncontrolled, earliest-deadline, least-laxity | charging rate | queued |
| 8 | Microgrids and batteries | pymgrid (Total) ; PyBaMM battery physics (Oxford, Faraday Institution) | their rule-based dispatch; CC-CV charging | dispatch, charge rate | queued |
| 9 | Building HVAC | BOPTEST (IBPSA Project 1) | each test case's own baseline controller | setpoints | queued |
| 10 | Building HVAC and data centre cooling | Sinergym on EnergyPlus (University of Granada), incl. the data-centre model | its rule-based controller | supply-air and zone setpoints | queued |
| 11 | Wind farms | FLORIS (NREL) | greedy, every turbine for itself | yaw offsets | queued |
| 12 | Water networks | WNTR / EPANET, L-Town (BattLeDIM) (US EPA, Sandia) | the network's own pump and tank rules | pump schedules | queued |
| 13 | Chemical process | Tennessee Eastman (Downs & Vogel; Ricker's decentralised control) | Ricker's controller | setpoints inside its limits | queued |
| 14 | Traffic signals | SUMO with the RESCO benchmark (DLR; UMass) | fixed-time and max-pressure | phase timing | queued |
| 15 | Driving | highway-env (Leurent) | its IDM and MOBIL drivers | speed and spacing margins | queued |
| 16 | HPC job scheduling | Batsim with the Parallel Workloads Archive (Inria; Feitelson) | EASY backfilling | node power-down, admission | queued |
| 17 | Cloud traces | Alibaba and Google cluster traces, Azure Functions trace on KWOK | Kubernetes HPA and scheduler | replicas, nodes | queued |
| 18 | CPU power | Linux cpufreq (schedutil) under SPECpower-style load on rented machines with RAPL | schedutil | frequency and power caps | queued |
| 19 | AI serving at scale | vLLM benchmark, MLPerf Inference (MLCommons) | vLLM as shipped | power, clocks, admission | ready (GPU) |
| 20 | AI training | MLPerf Training power (MLCommons) | the framework as shipped | power limit, clocks | queued (GPU) |
| 21 | Networks | ns-3 data-centre and 5G-LENA cell sleep (ns-3 consortium; CTTC) | their own congestion control and cell schedulers | pacing, cell sleep | queued |
| 22 | Supply chains | OR-Gym inventory (Hubbs et al.) | base-stock policy | order quantities | queued |
| 23 | Drone swarms, aircraft, defense | PX4 and ArduPilot multi-vehicle simulation (the shipped flight code), Crazyswarm, gym-pybullet-drones first; JSBSim for fixed-wing (NASA, AFRL); K3s edge clusters on constrained hardware | each drone's own autopilot and the fleet's own mission planner | the cruise override inside the autopilot's limits (first); drones airborne at once, climb margins, mission admission (later); collisions zero in both arms or the cell is void | **preregistered and running on v3** (`docs/SWARM_PREREGISTRATION.md`, workflow `swarm`, A/B/C dispatched 2026-10-07): gym-pybullet-drones, 20 drones in three untouched cells; the tuning swarm read energy a mission −16%, missions a charge 5.8 → 6.9, no late mission, no collision; PX4 and ArduPilot next |
| 24 | Databases and caches at large | YCSB on Cassandra, MongoDB and Redis (Yahoo; the Apache and MongoDB projects); HammerDB TPC-C on MySQL | each store's shipped settings | pools, admission, replicas | queued (added 2026-10-07) |
| 25 | Big data | Spark on TPC-DS (Apache; the TPC) | Spark's dynamic allocation as shipped | executors, admission | queued (added 2026-10-07) |
| 26 | Messaging | Kafka with the OpenMessaging benchmark (Apache; the Linux Foundation) | Kafka's shipped settings | partitions, consumer count, admission | queued (added 2026-10-07) |
| 27 | Caches | Redis with memtier (Redis Ltd) | Redis as shipped | memory ceiling, eviction, admission | queued (added 2026-10-07) |
| 28 | Search | OpenSearch with Rally (Amazon; Elastic's benchmark) | the cluster's own shard allocator | replicas, refresh interval, admission | queued (added 2026-10-07) |
| 29 | Storage | fio on block and object stores (Jens Axboe) | the store's own queue depth and cache | queue depth, admission, power | queued (added 2026-10-07) |
| 30 | Warehouse and logistics robots | Open-RMF fleet manager (Open Robotics) | its own fleet adapter and task allocator | fleet size in service, task admission | queued (added 2026-10-07) |
| 31 | Robustness, every platform | a 24-hour run; Omni killed mid-run (the dead-man lease); Omni's own CPU and memory at 1, 10, 100 and 1,000 copies | as the platform | none: the test is of Omni itself | queued (added 2026-10-07) |
| 32 | Spacecraft attitude, momentum and thrusters | Basilisk (University of Colorado, LASP) | its attitude feedback law, reaction wheels, thruster momentum dumping | wheel effort cap, dump timing, thruster duty inside limits; gauges: pointing error, wheel energy, propellant, dumps | queued (added 2026-10-07) |
| 33 | Orbit station-keeping | Orekit (CS Group); NASA GMAT | the deadband station-keeping law | deadband timing and burn sizing inside the box; gauges: propellant a year, box violations zero in both arms | queued (added 2026-10-07) |
| 34 | Satellite constellations | Basilisk multi-vehicle | each satellite's own law | fleet power and pointing admission; gauges as 32, fleet-wide | queued (added 2026-10-07) |
| 35 | Rockets | RocketPy; OpenRocket | their air-brake and recovery controllers | brake deployment inside limits; gauges: apogee error, structural loads, recovery margin | queued (added 2026-10-07) |
| 36 | Combustion and thruster chambers | Cantera | a shipped setpoint loop on mixture or temperature | setpoints inside the stable band; gauges: efficiency, temperature excursions zero, emissions | queued (added 2026-10-07) |
| 37 | Pure physics solvers: OpenFOAM, SU2, REBOUND, GADGET, MESA | none | no controller, no knob: Omni has no place on them | not a benchmark; their value here is the HPC cluster that runs them (row 16) | not benchmarked, by design |

Each row, when it runs, gets what the power grid got: a preregistration frozen on one tuning case before the untouched
cases run, a workflow on GitHub, the report with every row shown (worse included), and its line moved up into section
2.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
