# The Omni-Compass register: every muscle wired, every benchmark run, every benchmark still to run

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


One list to see and show. Native is always the system running on its own: its own controller, its own autoscaler, its
own tap changer, its own servo. Omni-Compass is always on top of it, never instead of it. A row names the benchmark's
owner when the benchmark is someone else's. Every result named here is read from the file in its last column.

Status words: **done** (result in the repo), **running** (on GitHub or Azure now), **ready** (harness built, waiting
on hardware or a go), **next** (being built now), **queued** (in the order of section 4, one or two at a time).

Last updated 2026-10-05.

## 1. Every muscle wired (656 muscles, 46 families, four realms and the shared spine)

A muscle is one knob on one real system that Omni-Compass may move inside its cover: **capacity** (how many machines,
replicas or units), **setpoint** (a temperature, voltage, pressure or speed), **power** (a power or effort cap), or
**admission** (how much work is let in at once). Each family is modelled by a plant: the model that stands in for that
kind of system until it is measured live.


| # | Realm | Family | Muscles | Plant (model) | Knobs Omni holds |
|---:|---|---|---:|---|---|
| 1 | The shared spine (in all four realms) | Cloud VM & Capacity | 16 | compute_pool/node | capacity 16 |
| 2 | The shared spine (in all four realms) | Container Resources | 16 | compute_pool/server | capacity 13, setpoint 2, admission 1 |
| 3 | The shared spine (in all four realms) | Host CPU & Memory | 16 | compute_pool/cpu_host | power 8, capacity 7, admission 1 |
| 4 | The shared spine (in all four realms) | Kubernetes Placement & Scheduling | 16 | compute_pool/server | capacity 11, admission 4, setpoint 1 |
| 5 | The shared spine (in all four realms) | Kubernetes Workload Scaling | 16 | compute_pool/server | capacity 7, admission 6, setpoint 3 |
| 6 | The shared spine (in all four realms) | NVIDIA GPU Hardware | 15 | compute_pool/gpu | capacity 9, power 4, admission 2 |
| 7 | The shared spine (in all four realms) | Node Fleet & Karpenter-Class Control | 16 | compute_pool/node | capacity 12, admission 3, setpoint 1 |
| 8 | The shared spine (in all four realms) | Network Routing & Switching | 16 | compute_pool/network | capacity 7, admission 6, setpoint 3 |
| 9 | The shared spine (in all four realms) | Observability & Telemetry | 6 | compute_pool/server | admission 3, capacity 2, setpoint 1 |
| 10 | The shared spine (in all four realms) | Reliability, Security & Recovery | 12 | compute_pool/server | capacity 6, admission 6 |
| 11 | The shared spine (in all four realms) | Storage Block/File/Object | 16 | compute_pool/storage | capacity 14, admission 2 |
| 12 | The shared spine (in all four realms) | Cooling, Chillers & Thermodynamics | 15 | thermal_zone/data_hall | setpoint 6, capacity 5, power 2, admission 2 |
| 13 | The shared spine (in all four realms) | PDU, UPS & Electrical Distribution | 14 | energy_storage/ups | power 5, capacity 4, admission 3, setpoint 2 |
| 14 | Compute / AI / Cloud | AI Inference Serving | 16 | compute_pool/gpu | capacity 8, admission 6, setpoint 1, power 1 |
| 15 | Compute / AI / Cloud | AI Training | 16 | compute_pool/gpu_batch | capacity 13, setpoint 1, admission 1, power 1 |
| 16 | Compute / AI / Cloud | Cross-Cluster, Multi-Region & Edge | 15 | compute_pool/node | capacity 9, admission 6 |
| 17 | Compute / AI / Cloud | DPU SmartNIC & Programmable IO | 12 | compute_pool/fabric | capacity 10, admission 2 |
| 18 | Compute / AI / Cloud | Distributed Cluster Managers | 15 | compute_pool/batch | capacity 8, admission 7 |
| 19 | Compute / AI / Cloud | GPU Fabric & RDMA | 16 | compute_pool/fabric | capacity 12, admission 4 |
| 20 | Compute / AI / Cloud | HPC & Distributed Compute | 16 | compute_pool/batch | capacity 9, admission 6, setpoint 1 |
| 21 | Compute / AI / Cloud | Kubernetes Dynamic Device Allocation | 8 | compute_pool/gpu | capacity 6, admission 1, setpoint 1 |
| 22 | Compute / AI / Cloud | OpenShift & Machine API | 9 | compute_pool/node | capacity 5, admission 4 |
| 23 | Compute / AI / Cloud | Quantum Computing Control Simulation | 16 | compute_pool/qpu | capacity 10, admission 4, setpoint 1, power 1 |
| 24 | Compute / AI / Cloud | Work Admission & Demand Shaping | 16 | compute_pool/server | admission 16 |
| 25 | Physics / Robotics / Autonomous | Automotive EV & Mobile Powertrain | 12 | motion_axis/ev_traction | power 10, capacity 1, admission 1 |
| 26 | Physics / Robotics / Autonomous | Aviation & Autonomous Flight | 16 | motion_axis/flight_axis | admission 9, capacity 6, power 1 |
| 27 | Physics / Robotics / Autonomous | Robotics Fleet & Warehouse Automation | 15 | compute_pool/robot_fleet | capacity 12, admission 3 |
| 28 | Physics / Robotics / Autonomous | Robotics Motion Control | 15 | motion_axis/robot_joint | capacity 11, power 4 |
| 29 | Physics / Robotics / Autonomous | Spacecraft & Flight Software | 14 | motion_axis/reaction_wheel | admission 6, power 4, capacity 4 |
| 30 | Energy / Facility / Industrial | Building & Critical Environment HVAC | 12 | thermal_zone/building | capacity 5, setpoint 3, admission 3, power 1 |
| 31 | Energy / Facility / Industrial | Energy Storage & Microgrid | 16 | energy_storage/microgrid | power 9, setpoint 3, capacity 2, admission 2 |
| 32 | Energy / Facility / Industrial | Facility & Grid Optimization | 15 | energy_storage/facility | power 5, admission 5, capacity 4, setpoint 1 |
| 33 | Energy / Facility / Industrial | Grid Transmission & Distribution | 12 | process_loop/feeder_voltage | setpoint 4, admission 4, capacity 2, power 2 |
| 34 | Energy / Facility / Industrial | Industrial PLC & Process Automation | 14 | process_loop/process | setpoint 6, capacity 4, admission 3, power 1 |
| 35 | Energy / Facility / Industrial | Semiconductor Fab & Precision Manufacturing | 11 | process_loop/chamber | admission 4, capacity 4, setpoint 2, power 1 |
| 36 | Energy / Facility / Industrial | Water Wastewater & Pumping | 12 | process_loop/water | admission 5, setpoint 4, power 2, capacity 1 |
| 37 | Distribution / Specialized | Cache & Memory Services | 15 | compute_pool/server | capacity 10, admission 4, setpoint 1 |
| 38 | Distribution / Specialized | Commerce & Payment Systems | 15 | compute_pool/commerce | admission 8, capacity 5, setpoint 2 |
| 39 | Distribution / Specialized | Data Analytics & ETL | 15 | compute_pool/batch | capacity 9, admission 4, setpoint 2 |
| 40 | Distribution / Specialized | Database & Transactions | 14 | compute_pool/database | capacity 9, admission 5 |
| 41 | Distribution / Specialized | Messaging & Streaming | 16 | compute_pool/server | capacity 9, admission 7 |
| 42 | Distribution / Specialized | Runtime & Application | 15 | compute_pool/server | capacity 10, admission 5 |
| 43 | Distribution / Specialized | Search, Indexing & Vector DB | 15 | compute_pool/server | capacity 10, admission 5 |
| 44 | Distribution / Specialized | Service Mesh & API Reliability | 15 | compute_pool/server | admission 7, capacity 6, setpoint 2 |
| 45 | Distribution / Specialized | Telecom RAN & Edge Radio | 12 | compute_pool/ran | capacity 7, admission 3, setpoint 1, power 1 |
| 46 | Distribution / Specialized | Workflow, Logistics & Fulfillment | 15 | compute_pool/workflow | capacity 10, admission 5 |

**656 muscles in 46 families.** Every muscle by name, with its knob and what it is for: `realms/catalog.csv` and `docs/MUSCLE_CATALOG.md`.

How they are proven so far: every muscle alone, and every organism whole, on its model (`results/realms/REALMS.md`):
**57 superior within guardrails, 9 energy improvement with a service tradeoff, 586 noninferior, 0 not established,
0 worse; all five organisms superior within guardrails.** Evidence class S: a model, not a meter. The live rows of
section 2 are where muscles meet real systems.

## 2. Every benchmark, by platform

Which engine each result ran on, and its v1 replications A, B and C: [`docs/OMNI_V1.md`](OMNI_V1.md).

### 2.1 Kubernetes on GitHub (real clusters, kind; evidence: real software, declared energy model)

| # | Benchmark | Native | Omni moves | Status | Result (Omni on top vs native) | File |
|---:|---|---|---|---|---|---|
| 1 | Steady work in steps, 10 pairs × 3 runs (v1) | Kubernetes HPA | replicas, floor, nodes | done, confirmed in 3 of 3 | p95 −65% to −69%, machines −1.5% to −3.4%, standby-model energy −1.0% to −2.9%, confirmed better | `results/live/V1_STEADY.md` (earlier engine: `STEADY.md`) |
| 2 | Demand that wanders, 10 pairs × 3 runs (v1) | Kubernetes HPA | replicas, floor, nodes | done, confirmed in 3 of 3 | p95 −56% to −60%, failed requests −12% to −13%, confirmed better; machines no difference beyond the noise | `results/live/V1_WANDERING.md` (earlier engine: `WANDERING.md`) |
| 3 | All four at once (more work, faster, fewer machines, less energy), 10 pairs × 3 runs (v1) | Kubernetes HPA | replicas, floor, nodes | done, confirmed in 3 of 3 | **work inside the line +42% to +48%**, p95 −57% to −63%, failed requests −12% to −13%, confirmed better; machines and energy no difference beyond the noise | `results/live/V1_ALL_FOUR.md` (earlier engine: `ALL_FOUR.md`) |
| 4 | Fairness, a noisy neighbour, 10 pairs × 3 runs (v1) | Kubernetes HPA | replicas, admission | done | no difference beyond the noise on every row: Omni neither helps nor hurts | `results/live/V1_FAIRNESS.md` (earlier engine: `FAIRNESS.md`) |
| 5 | Faults: machine down, spike, runaway pod, blind probe, 10 pairs × 3 runs (v1) | Kubernetes HPA | replicas, floor, nodes | done, confirmed in 3 of 3 | mean response −36% to −52%, p95 −61% to −64%, confirmed better; machines and energy no difference beyond the noise | `results/live/V1_FAULTS.md` (earlier engine: `FAULTS.md`) |
| 6 | A queue of batch jobs (cruise, then the emergency brake), 10 pairs × 3 runs (v1) | Kubernetes Jobs + HPA | nodes, floor | done, confirmed in 3 of 3 | machines −15% to −24%, after the queue −26% to −36%, mean response −11% to −13%, confirmed better; the queue finished 0.7% to 0.9% later (clear of the noise in 2 of 3 runs) | `results/live/V1_BATCH.md` (earlier engine: `BATCH.md`) |
| 7 | The six organisms with the real cluster inside (Compute/AI/Cloud, Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized, the whole tower of 656, the four stacked of 1,226), 5 pairs each | HPA + the organisms' native settings | every muscle of the organism | done; rerun running | index +7.8% to +15.5% per organism | `results/live/SIX_KUBE.md` |
| 8 | The big organisms (the whole tower at size) | as 7 | as 7 | running | | workflow `big-organism` |
| 9 | Scale: KWOK simulated nodes, 50 / 500 / 1,000 | Kubernetes scheduler + HPA | replicas, nodes | running on every push; report not yet in the repo | | workflow `kwok-scale` |

### 2.2 Azure AKS (real cloud machines, Azure's own bill)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 10 | Steady load, 5 pairs (earlier engine) | AKS cluster autoscaler + HPA | replicas, floor | done | index +7.5%; response +25.4% faster; machines −0.8% | `results/live/AKS_BILL.md` |
| 11 | Burst sized to the cluster | as 10 | as 10 | running (one repetition to rerun) | | workflow `aks-metered` |
| 12 | Steady load on this engine, 5 pairs, 900 s | as 10 | as 10 | queued after 11 | | workflow `aks-metered` |

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

### 2.5 The 656 modelled muscles (the organisms at 1 / 10 / 100 / 1,000 copies)

| # | Benchmark | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 24 | Every muscle alone and every organism whole | each plant's native setting | each muscle's knob | done | 0 worse; all organisms superior within guardrails | `results/realms/REALMS.md` |
| 25 | The organisms at 1x / 10x / 100x / 1,000x copies, 1 to 1,000 runs | as 24 | as 24 | done except 1,000x at 100 and 1,000 runs (beyond the machines available) | work per energy +0.08% to +0.21%, the same at every scale | `results/scale/GRID.md` |

### 2.6 Energy, buildings, batteries and UPS (independent simulators)

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 26 | CityLearn, every district it ships (Intelligent Environments Lab, UT Austin): buildings, solar, batteries, EVs | CityLearn's own rule-based controller | battery and storage setpoints | done, A/B/C on v1 | 11 battery districts: electricity bought, daily peak and daily unevenness confirmed better in all 11; carbon better in 8; the bill better in 1, worse in 7 (the 2023 districts, +0.2% to +0.35%); ramping better in 4, worse in 7 (+4.5% to +6.2%); the comfort score varies between CityLearn's own runs and is not claimed; 3 districts have no battery; 8 CityLearn cannot run | `results/live/V1_CITYLEARN.md` |
| 27 | UPS and battery reserve | the UPS's own reserve | none: a reserve held for an outage is never a lever (physics criterion) | done (model) | native by design | `docs/MECHANISM_OF_ACTION.md` §9.6 |
| 28 | Power grid: SimBench grids solved by pandapower (Fraunhofer IEE, Uni Kassel) | the substation tap changer at 1.00 per unit | the tap changer's setpoint (conservation voltage reduction) | tuning grid done; 11 untouched grids running | tuning grid: load energy −1.36%, no new violations; tap operations 8 vs 4 a year (declared cost) | `docs/PANDAPOWER_PREREGISTRATION.md`, workflow `pandapower` |

### 2.7 Robotics

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 29 | Robot arms in MuJoCo (Google DeepMind): Franka Panda (tuning), UR5e, KUKA iiwa 14, Kinova Gen3 from MuJoCo Menagerie, a pick-and-place cycle inside a takt | each robot's own shipped position servos | the speed override inside the takt; a paired physics trial leaves it native where a slower cycle is not cheaper | done, A/B/C on v1, reproduced in 3 of 3 | the same job inside the same takt, hit more accurately with less force on the motors: Gen3 peak torque −29%, tracking error −21%, copper −11%, energy per takt −0.8%, all confirmed better; Panda (tuning) peak torque −10%, tracking error −21%, energy per takt −0.5% confirmed better, copper loss +14% confirmed worse; UR5e and iiwa 14: slowing would cost on their own figures, left native, nothing for Omni to move | `results/live/V1_MUJOCO.md`, `results/live/V1_MUJOCO_PANDA.md`, `docs/ROBOTICS_PREREGISTRATION.md` |

### 2.8 Databases

| # | Benchmark (owner) | Native | Omni moves | Status | Result | File |
|---:|---|---|---|---|---|---|
| 30 | PostgreSQL 16 behind PgBouncer 1.22 (the PostgreSQL Global Development Group; the PgBouncer project), pgbench's TPC-B-like load stepping one notch at a time: `tpcb` (tuning), `select`, `simple_update`, `tpcb_hot` (untouched) | the pooler's shipped pool of 20 server connections, the DBA's one fixed setting | the pool size, through PgBouncer's own console, inside [2, 90]; handed back at the end | preregistered 2026-10-06; tuning run dispatched, then the untouched workloads, A/B/C on v1 | first smoke (one repetition, not counted): more work inside the line, lower p95 over the profile, 11 server connections against 20; p95 higher at the lightest notch (inside the line), the declared cost | `docs/POSTGRES_PREREGISTRATION.md`, workflow `pgbench`, `tools/run_pgbench.py` |

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

Each row, when it runs, gets what the power grid got: a preregistration frozen on one tuning case before the untouched
cases run, a workflow on GitHub, the report with every row shown (worse included), and its line moved up into section
2.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
