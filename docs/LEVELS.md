# Every level: Omni-Compass on top of the muscle, the organism, the cluster, the service, the plant, the cloud

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's order of 17 October: Omni-Compass is shown on top at every level, on every gauge, and every level's gauges should go the same way; where one does not, it is named here and taken to the founder. Each row is built from its result files by `tools/levels.py`; nothing is typed in. A count is of judged gauges (a table's rows that read a word), each under its own table's rule (the three runs, or the realms result's ten seeds); **power given** is a resource put in, shown and never called a loss. Every row names the engine its tables ran on, and no reading is carried from one engine to another.

| Level | Engine | Evidence | GAIN | EVEN | power given | LOSS | runs disagree | Goes the other way? |
|---|---|---|---:|---:|---:|---:|---:|---|
| The muscle, alone (1,107 muscles, each on its own native controller, under its own load) | omni-v8 | S (our model) | 527 | 580 | 0 | 0 | 0 | no: every judged gauge GAIN or EVEN |
| The organism, the stack: the seven organisms under three loads (own load, the climb, work waiting in line) | omni-v8 | S (our model) | 21 | 0 | 0 | 0 | 0 | no: every judged gauge GAIN or EVEN |
| The cluster: real Kubernetes, native its own HPA and scheduler | omni-v10, omni-v11 | L | 32 | 93 | 4 | 0 | 0 | no LOSS; resources put in shown as power given |
| The cluster with its add-ons native: KEDA, Goldilocks, CruiseKube | omni-v10, omni-v11 | L | 17 | 40 | 7 | 0 | 0 | no LOSS; resources put in shown as power given |
| A muscle inside a running service: database, broker, cache | omni-v11, omni-v12 | L | 18 | 334 | 5 | 0 | 2 | **yes: 2, listed below** |
| A physical plant in an independent simulator: buildings, power grids, robot arms, drone swarms | omni-v11 | independent simulator | 113 | 132 | 15 | 0 | 0 | no LOSS; resources put in shown as power given |
| The organism with the real cluster inside (the grid, at 1, 10, 100 and on GitHub's machines 1,000 copies) | older engines' tables; the grid runs again on the engine that stands | L, the cluster; S, the organism | – | – | – | – | – | no table on the engine that stands yet; the grid's runs (results/grid_v8/) are going |
| The cluster in a cloud: Azure Kubernetes Service, the bill | single runs, omni-v5 to omni-v7 | L, the bill metered | – | – | – | – | – | no three-run table yet: eight single runs at the tune-down, machines billed −6.5% to +7.6%, every one EVEN; the fleet (about 1.9 of 4 machines busy) leaves no whole machine to give back |
| A group of clusters | not run | none yet | – | – | – | – | – | no run at this level yet, real or modelled, on the engine that stands (`k8s_fleet/` holds a model of an earlier engine) |

## Each level

### The muscle, alone (1,107 muscles, each on its own native controller, under its own load)

Native at this level: each muscle's native controller. Engine: omni-v8. Evidence: S (our model).
421 of the EVEN are at their limit on native (nothing to push).
Tables: `results/realms_v5/MUSCLES_V5.csv`.

### The organism, the stack: the seven organisms under three loads (own load, the climb, work waiting in line)

Native at this level: every muscle on its native controller, coupled in one body. Engine: omni-v8. Evidence: S (our model).
The organism's own reading; inside them no plant did less work or missed its line more often than native, under any load (the realms result's stricter look, plant by plant).
Tables: `results/realms_v5/REALMS_V5.md`.

### The cluster: real Kubernetes, native its own HPA and scheduler

Native at this level: Kubernetes as shipped with the operator's HPA target. Engine: omni-v10, omni-v11. Evidence: L.
Tables: `results/live/V10_ALL_FOUR.md`, `results/live/V10_BATCH.md`, `results/live/V11_CAPACITY.md`, `results/live/V10_FAIRNESS.md`, `results/live/V10_FAULTS.md`, `results/live/V10_TRACE_GOOGLE2011.md`, `results/live/V11_ROBUST_KILL.md`, `results/live/V11_ROBUST_LONG.md`.

### The cluster with its add-ons native: KEDA, Goldilocks, CruiseKube

Native at this level: Kubernetes with the add-on as shipped and as used, its own recommendations applied. Engine: omni-v10, omni-v11. Evidence: L.
Tables: `results/live/V11_KEDA_REQUESTS.md`, `results/live/V11_KEDA_CPU_REQUESTS.md`, `results/live/V11_GOLDILOCKS.md`, `results/live/V10_CRUISEKUBE.md`.

### A muscle inside a running service: database, broker, cache

Native at this level: the server as shipped but for the one setting an operator sets (each table names it). Engine: omni-v11, omni-v12. Evidence: L.
Tables: `results/live/V12_REDIS.md`, `results/live/V12_REDIS_SERVICE.md`, `results/live/V12_KAFKA.md`, `results/live/V12_KAFKA_SERVICE.md`, `results/live/V12_PGBENCH.md`, `results/live/V12_SYSBENCH.md`, `results/live/V11_YCSB.md`.

Goes the other way:

- V12_KAFKA_SERVICE.md: light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run: consumers running, mean (the resources held) (the runs disagree)
- V12_SYSBENCH.md: read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run: buffer pool held, mean (MB; the knob, the resource) (the runs disagree)

### A physical plant in an independent simulator: buildings, power grids, robot arms, drone swarms

Native at this level: the simulator's own controller, unchanged. Engine: omni-v11. Evidence: independent simulator.
Tables: `results/live/V11_CITYLEARN.md`, `results/live/V11_PANDAPOWER.md`, `results/live/V11_MUJOCO.md`, `results/live/V11_SWARM.md`.

### The organism with the real cluster inside (the grid, at 1, 10, 100 and on GitHub's machines 1,000 copies)

Native at this level: the organism's native controllers around Kubernetes with its HPA. Engine: older engines' tables; the grid runs again on the engine that stands. Evidence: L, the cluster; S, the organism.
No table on the engine that stands yet; the grid's runs (results/grid_v8/) are going.
Tables: `results/live/SIX_KUBE.md`, `results/live/V3_SIX_KUBE.md`, `results/live/V3_BIG_ORGANISM.md`.

### The cluster in a cloud: Azure Kubernetes Service, the bill

Native at this level: Azure's own cluster autoscaler and the HPA. Engine: single runs, omni-v5 to omni-v7. Evidence: L, the bill metered.
No three-run table yet: eight single runs at the tune-down, machines billed −6.5% to +7.6%, every one EVEN; the fleet (about 1.9 of 4 machines busy) leaves no whole machine to give back.
Tables: `results/live/AKS_BILL.md`, `results/live/raw/run-38981149348/`.

### A group of clusters

Native at this level: each cluster's own autoscaler. Engine: not run. Evidence: none yet.
No run at this level yet, real or modelled, on the engine that stands (`k8s_fleet/` holds a model of an earlier engine).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
