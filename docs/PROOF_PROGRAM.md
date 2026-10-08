# The proof program: every benchmark at full size, every open native engine, the referee-grade package

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.

Written 2026-10-07 on the founder's order: the strongest evidence that can be built, at the largest size each platform
allows, on open native engines the industry itself runs, so that the only step left to a buyer is to run the same
harness on their own system and read the same table. This document is the program of record. Each line of it becomes a
preregistration before it runs, then a workflow, then a report with every row shown, losses included, then a line in the
register (`docs/REGISTER.md`) and a chapter in the manual (`docs/OMNI_COMPASS_MANUAL.md`).

## 1. The rules every item obeys

1. **Two arms, no third.** Native is the system on its own controller, as shipped or as its operator set it. Omni is
   Omni-Compass on top of that same controller. Omni never replaces native and is never run alone.
2. **Do no harm.** Where Omni cannot improve a knob, the knob stays native. The 2% verdict is the engine's trigger.
3. **The engine is frozen.** Omni v3 (`OMNI_V3.json`, digest `b53d05449ee04c4b`). Nothing in this program changes a
   rule, a gain, a guard, a preset or a muscle. A change would make the next version and every result would run again.
4. **Preregistered.** Rules frozen on one tuning case, written down and pushed before the untouched cases run.
5. **Three runs, three readings.** A, B and C as separate GitHub runs on the same commit. Every judged row reads
   *confirmed better*, *confirmed worse*, *no difference beyond the noise* (with the count of runs it holds in) or *the
   runs disagree*. Never "not confirmed".
6. **Every row shown.** Losses included. A benchmark may be left unpublished; it is never published with rows cut out.
7. **Evidence classes.** P (a physical meter), L (live software), S (our own models). S is never presented as proof.
8. **The clock.** An organism keeps its measured window's clock; a repetition where either arm ended more than 5% of the
   window late is marked OFF THE CLOCK and the window is lengthened for that size on that machine.
9. **Handed back.** Every knob returns to the snapshot taken at the start, checked at the end of every arm.
10. **Raw files kept.** Every artifact archived with the code under `results/live/raw/run-<id>/` with SHA-256 sums.

## 2. The sizes

| Platform | Free size (GitHub) | Paid size | How |
|---|---|---|---|
| Kubernetes, real cluster (kind) | 6 workers, 10 pairs × 3 runs; the six organisms at 1, 10 and 100 copies | the organisms at 1,000 copies on a rented machine, the window set to keep the clock | `six-kube`, `benchmark-reps`, `big-organism-detached` |
| Kubernetes, simulated nodes (KWOK) | 50, 500 and 1,000 nodes | | `kwok-scale` |
| The modelled organisms | 1, 10, 100 and 1,000 copies × 1 to 1,000 runs (the grid) | | `six` |
| Azure's managed Kubernetes | | the largest fleet the allowance gives: 15 workers today (32 cores), 96 at 200 cores once a machine family is granted; the app's ceiling 9 pods a worker | `aks-metered` (`max_workers`, `hpa_max`), `azure-quota` |
| GPU | | one card; one card inside 1,000 copies; eight cards; vLLM serving (Lambda) | `scripts/gpu_*.sh`, `tools/run_hil.py` |
| CPU power, a real meter | | one rented bare-metal machine, RAPL energy counters | to build |
| Drone swarms | 20 drones | 100 and more on a rented machine | **done, A/B/C on v3** (`results/live/V3_SWARM.md`): energy a mission −7% to −20%, missions a charge +8% to +25%, confirmed better, no collision; 100 drones on a rented machine next |
| Databases, messaging, caches, search, storage, big data | the service in a container on a 4-core runner, three untouched workloads each | | `pgbench` done; the rest to build |
| Independent simulators (grid, buildings, robots, batteries, process, water, wind, traffic) | every case the simulator ships | | `pandapower`, `citylearn`, `mujoco` done; the rest to build |

## 3. The benchmarks, in the order they run

Status words: **done** (A, B, C in the repo), **running**, **queued** (dispatched or next in line), **to build** (harness
and preregistration not yet written). Every "to build" item names the open native engine Omni will sit on top of.

### 3.1 Compute, AI and cloud

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 1 | Kubernetes, six tests (steady, wandering, all four, fairness, faults, batch) | Kubernetes HPA | replicas, floor, machines | p95, p99, work inside the line, failed requests, machines, declared energy | 10 pairs × 3 runs, free | v1 done; v3 runs A and B in progress |
| 2 | The six organisms with the real cluster inside | HPA and the organisms' native settings | every muscle | the cluster's gauges and the organism's work, energy, time over the line, behind its window | 1, 10, 100 copies free; 1,000 on Azure, about $25 | v1 done; v3 10 and 100 done, 1,000 running |
| 3 | Azure managed Kubernetes, steady and burst | Azure's cluster autoscaler and the HPA | the HPA target inside its range, the node pool | the bill (Azure's own machine count), machines, p95, failed requests | 4 workers done; 11 running; 15 and 96 when granted, about $150 | v1 done at 4; v3 at 11 running |
| 4 | Real traffic traces on Kubernetes (Alibaba cluster trace, Google cluster trace, Azure Functions trace) replayed on kind and KWOK | Kubernetes HPA and scheduler | replicas, machines | as 1 | free | to build, first |
| 5 | Kubernetes with Karpenter-class node scaling and KEDA event-driven scaling underneath | Karpenter or the Cluster Autoscaler; KEDA | the same levers, the autoscaler left in charge of machines | as 1 | free on kind where the autoscaler runs; Azure for the real one | to build |
| 6 | CPU power with a real meter | Linux cpufreq, schedutil governor | frequency ceiling and power cap inside the governor | energy from RAPL (class P), work, p95 | one rented bare-metal machine, about $10 | to build |
| 7 | GPU: one card; the card inside 1,000 copies; eight cards; vLLM serving (MLPerf-style) | the card's own power limit and clocks; vLLM as shipped | power limit, clock ceiling, admission | the card's own meter (class P), work, p95 | Lambda, about $60 | ready; founder runs |
| 8 | HPC job scheduling | Batsim with EASY backfilling on Parallel Workloads Archive logs | node power-down, admission | makespan, wait, node-hours, energy | free | queued |
| 9 | Robustness, every platform | as the platform | none: the test is of Omni itself | the governor killed mid-run and the lease (seconds to hand back, the 120 s after the kill); the long run (memory, decisions); Omni's own CPU at 1, 10, 100 and 1,000 copies | free (the 24-hour run on a rented machine about $3) | **preregistered and built** (`docs/ROBUSTNESS_PREREGISTRATION.md`); the own-cost table done from the archives (`results/live/V3_OWN_COST.md`); the kill and long scenarios run as A, B and C on v3 next |

### 3.2 Distribution and specialized

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 10 | PostgreSQL behind PgBouncer (pgbench) | the pooler's shipped pool, the DBA's fixed setting | the pool size | work inside the line, p95, connections held, host CPU | free | v3 done |
| 11 | YCSB on Cassandra, MongoDB and Redis; HammerDB TPC-C on MySQL | each store as shipped | pools, admission, replicas | throughput inside the line, p95, resources held, host CPU | free | to build |
| 12 | Apache Kafka as shipped, a producer at a stepped rate (the OpenMessaging benchmark later) | the operator's fixed consumer count | consumer count inside [1, partitions] | work inside the line, end-to-end p95, lag, consumers held, lost messages, host CPU | free | **done, A/B/C on v3** (`results/live/V3_KAFKA.md`): work inside the line +16% to +21%, p95 −99%, lag −92% to −97%, confirmed better on all three workloads; consumers held 2 → 5.8 to 7.9 confirmed worse (the cost); host CPU worse on light, inside the noise on the others; no message lost; the OpenMessaging benchmark next |
| 13 | Redis as shipped, an application in front with a declared store trip on a miss | the operator's memory ceiling and eviction rule | the memory ceiling inside [16, 512] MB | work inside the line, hit rate, p95, memory held, CPU | free | **preregistered, A/B/C running on v3** (`docs/REDIS_PREREGISTRATION.md`) |
| 14 | OpenSearch with Rally | the cluster's own shard allocator | replicas, refresh interval, admission | query p95, indexing throughput, nodes busy | free | to build |
| 15 | Storage with fio | the store's own queue depth and cache | queue depth, admission, power | IOPS, p95, power | free | to build |
| 16 | Spark on TPC-DS | Spark's dynamic allocation | executors, admission | query time, executor-hours | free | to build |
| 17 | Networks | ns-3 data-centre and 5G-LENA cell sleep | pacing, cell sleep | throughput, latency, energy | free | queued |

### 3.3 Energy, facility and industrial

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 18 | Power grid, SimBench grids in pandapower | the substation tap changer | the tap setpoint | energy drawn, losses, import, taps, buses outside the band | free | v1 done; v3 queued |
| 19 | Buildings and batteries, CityLearn | CityLearn's rule-based controller | battery setpoints | cost, peak, unevenness, carbon, comfort | free | v1 done; v3 running |
| 20 | Building HVAC and data-centre cooling | BOPTEST baselines; Sinergym on EnergyPlus | setpoints | energy, comfort, time outside the band | free | to build |
| 21 | Battery physics | PyBaMM, CC-CV charging | charge rate | energy throughput, temperature, degradation proxies | free | to build |
| 22 | Microgrids | pymgrid rule-based dispatch | dispatch | cost, unmet load, battery cycling | free | queued |
| 23 | Wind farms | FLORIS, greedy yaw | yaw offsets | farm power | free | queued |
| 24 | Water networks | WNTR/EPANET pump and tank rules | pump schedules | energy, pressure violations | free | queued |
| 25 | Chemical process | Tennessee Eastman, Ricker's controller | setpoints inside limits | cost, constraint violations | free | queued |
| 26 | Transmission and distribution feeders | Grid2Op baselines; OpenDSS regulators | redispatch timing; regulator setpoints | overloads, losses, voltage | free | queued |
| 27 | EV charging | ACN-Sim with ACN-Data | charging rate | energy delivered, peak, deadlines met | free | queued |

### 3.4 Physics, robotics and autonomous

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 28 | Robot arms, MuJoCo Menagerie | each robot's shipped position servos | the speed override inside the takt | torque, tracking error, energy per takt, cycles over the line | free | v1 and v3 done |
| 29 | Drone swarms | PX4 and ArduPilot multi-vehicle simulation (the shipped flight code); Crazyswarm; gym-pybullet-drones first | drones airborne at once, cruise and climb margins inside the autopilot's limits, battery reserve, mission admission | missions per charge, late missions, reserve breaches, near misses, energy per mission; collisions zero in both arms or the cell is void | 20 drones free; 100 on a rented machine, about $10 | **done, A/B/C on v3** (gym-pybullet-drones; PX4 and ArduPilot next) |
| 30 | Fixed-wing aircraft | JSBSim | speed and climb margins | fuel, time, envelope violations | free | to build |
| 31 | Spacecraft attitude | Basilisk | wheel effort cap | pointing error, wheel energy | free | queued |
| 32 | Legged robots | MuJoCo Playground, Unitree Go2 | gait speed, effort | energy per metre, falls | free | queued |
| 33 | Driving | highway-env, IDM and MOBIL | speed and spacing margins | travel time, energy, collisions zero | free | queued |
| 34 | Warehouse robot fleets | Open-RMF fleet manager | fleet size in service, task admission | tasks per hour, battery, idle robots | free | to build |
| 35 | Traffic signals | SUMO with RESCO | phase timing | delay, stops, emissions | free | queued |
| 36 | Supply chains | OR-Gym base-stock | order quantities | cost, stockouts | free | queued |
| 37 | Defense edge | K3s on constrained hardware with the Kubernetes six tests | HPA | as 1 | free | to build |
| 38 | Spacecraft attitude, momentum and thrusters | Basilisk: its attitude law, reaction wheels, thruster dumping | wheel effort cap, dump timing, thruster duty | pointing error, wheel energy, propellant, dumps | free | to build |
| 39 | Orbit station-keeping | Orekit, GMAT: the deadband law | deadband timing, burn sizing inside the box | propellant a year; box violations zero | free | to build |
| 40 | Satellite constellations | Basilisk multi-vehicle | fleet power and pointing admission | as 38, fleet-wide | free | to build |
| 41 | Rockets | RocketPy, OpenRocket: air-brake and recovery controllers | brake deployment inside limits | apogee error, loads, recovery margin | free | to build |
| 42 | Combustion and thruster chambers | Cantera: a shipped setpoint loop | setpoints inside the stable band | efficiency, excursions zero, emissions | free | to build |
| - | Pure physics solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) | none: no controller, no knob | | | | not a benchmark, by design; their HPC cluster is row 8 |

## 4. The defensibility package

| Item | What it is | Status |
|---|---|---|
| One-command replication kit | from any pushed commit, one command reruns any benchmark above on GitHub and prints the same table; the commit, the engine fingerprint and the raw files' sums are in the table's head | to build |
| Evidence dossier, one per benchmark | preregistration, commit, engine, run ids, raw files and sums, the table, the losses, the index line | mostly in place; to be made uniform and indexed from `docs/REGISTER.md` |
| Reviewer protocol | the written path a human auditor follows from the register to a raw file and back | to write |
| Independent readers | ChatGPT and Grok read results; they never produce them (`results/external_review/`) | in place |
| Security review of the controllers | what Omni can touch, what it provably cannot, the kill switch, the dead-man lease, the permissions it holds | to write |
| The manual | every chapter above, the wiring stack by stack, the readings, the results, the file map | to rewrite (`docs/OMNI_COMPASS_MANUAL.md`, PDF rebuilt) |

## 5. Schedule and budget

| Weeks | Work | Compute cost |
|---|---|---|
| 1 | finish the running work; Azure at the largest fleet granted; the manual rewrite; traces (4); robustness (9) | about $200 |
| 2 | swarms (29), Kafka (12), YCSB (11), the real meter (6) | about $20 |
| 3 | Redis, OpenSearch, Spark, fio, Karpenter and KEDA (5), BOPTEST (20), PyBaMM (21) | about $20 |
| 4 | the rest of the queue, the replication kit, the reviewer protocol, the security review; the GPU runs on Lambda when the founder gives the go | about $60 |

Build time is the binding cost: two to three days per new benchmark, several in parallel on GitHub. Every result is
pushed as it lands, wins and losses alike, and reported to the founder in plain tables.

## 6. Disclosures

- Omni-Compass is a supervisory governor evaluated on top of native controllers. Nothing here is a production
  deployment, a product warranty, or advice to operate any system.
- Results of class S are models. They are labelled as such everywhere they appear and are never presented as proof.
- Results of class L and P are measured on the named open systems at the named sizes and commits. They do not by
  themselves establish the same effect on any other system; the replication kit exists so that a buyer can establish it
  on theirs.
- Negative and null results are published with the same prominence as positive ones. A benchmark may be withheld by the
  founder; it is never published with rows removed.
- The engine's version fingerprints are bookkeeping. The engine that stands when the founder declares it final is
  published as Omni-Compass 1.0; earlier fingerprints go to `docs/history`.
- Patent applications, copyright registrations and trademark applications have been filed in the United States by The
  Omni-Compass LLC. Numbers are not given here.
-

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
