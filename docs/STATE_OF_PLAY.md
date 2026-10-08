# Omni-Compass: state of play (read this first)

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Protected by copyright, patents and trademarks: Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.


## In one paragraph (2026-10-07, Omni v3)

**The engine is Omni v3, frozen and fingerprinted** (`OMNI_V3.json`, `docs/OMNI_V3.md`: v1's law and controllers byte
for byte, 945 muscles in 59 families, a do-no-harm gate on speed knobs). Every benchmark runs three times as separate
GitHub runs on it (A the result, B and C the replications) and every judged row reads confirmed better, confirmed worse,
no difference beyond the noise, or the runs disagree (`docs/OMNI_V1.md`, the rule). **Real Kubernetes, six tests, ten
pairs each, all six confirmed on v3** (`results/live/V3_*.md`): work inside the response line **+35% to +49%** in all
three runs of the all-four test (21.0 → 31.2 requests a second in run A); the 95th percentile **−47% to −66%** in every
run of the steady, wandering, all-four and fault tests; failed requests −9% to −14% where load swings; machines −1.5% to
−2.9% at steady load and −19% to −23% on the batch queue, with the standby-model energy −13% to −16% there; beside a
noisy neighbour no difference beyond the noise on every row. **A real database** (PostgreSQL behind PgBouncer,
`results/live/V3_PGBENCH.md`): 61% to 72% fewer connections held open for the same work and latency on two of three
workloads, at a confirmed cost in the host's CPU seconds (+14% to +28%), counted against Omni. **Real messaging** (Apache
Kafka as shipped, `results/live/V3_KAFKA.md`): on all three untouched workloads work inside the 500 ms line **+16% to
+21%**, the 95th percentile 1.6 s → 9 to 14 ms and messages waiting −92% to −97%, confirmed better, no message lost;
consumers held 2 → 6 to 8, **confirmed worse**, the resource the gain costs; host CPU worse on one workload, inside the
noise on two. **A real cache** (Redis as shipped, `results/live/V3_REDIS.md`): on all three untouched workloads work inside
the 2 ms line **+14% to +27%**, the hit rate +14% to +27% and the mean latency −30% to −61%, confirmed better; the memory
ceiling held 64 → 200 to 270 MB, **confirmed worse**, the resource the gain costs; host CPU inside the noise. **A real
database's storage-engine cache** (MongoDB as its publisher ships it under YCSB, `results/live/V3_YCSB.md`): on four
untouched workloads the cache size held fell about half on c and burst and 13% to 37% on f, **confirmed better** (b inside
the noise in one run); work inside the 1 ms line, p95 and host CPU inside the noise on all four; no failed operation; the
burst mean latency **+2% to +4%, confirmed worse**, the one loss. **The Omni index, real machines only, confirmed three
times: +25.9%** (`results/OMNI_INDEX.md`; Kubernetes +25.5%, the database +14.2%, Kafka +166.9%, Redis −24.9%, the
database's cache +10.2%, each category weighed the same; a row inside the noise counts as exactly 1; Kafka's speed ratio
is large because native's queue grew at nine tenths of its capacity and Omni's did not; Redis's category is negative
because the memory it holds for a wide working set is the resource it trades and reads worse by rule; MongoDB's is
positive because there the governor gave memory back). The v1 tables read the same and stay as the first engine's record.

**What is shown and what is not.** Shown: more work inside the response line on the same machines and a faster tail,
on real Kubernetes, three times on a frozen engine; a real database holding fewer connections for the same service; a
real message queue kept short at the cost of more consumers running.
Not yet shown: an energy or cloud-bill saving on real machines. Energy on kind is a declared model (the machines are
containers on one runner); Azure's bill on a 4-worker fleet read no difference beyond the noise on every gauge
(`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`), which is a fleet too small to show one machine; the fleet of 40
workers in nine machine families that can show one is preregistered and dispatched (`docs/K8S_COMPASS_PREREGISTRATION.md`,
the fleet that can show one machine, amendments 1 to 3), waiting on Azure's own capacity in eastus. The real card has
not run on the current governor; every earlier card result is obsolete and is run again by the founder on rented cards.

## Measured on real systems (evidence class L), Omni v3

| Test, ten pairs × three runs | Work | Speed (p95) | Machines | Energy (declared model) | Source |
|---|---|---|---|---|---|
| All four in one run | **+35% to +49%** | −61% to −66% | inside the noise | inside the noise | `results/live/V3_ALL_FOUR.md` |
| Steady work in steps | equal by design | −65% to −66% | **−1.5% to −2.9%** | −1.3% to −2.1% | `results/live/V3_STEADY.md` |
| Demand that wanders | failed requests −9% to −12% | −57% to −63% | inside the noise | inside the noise | `results/live/V3_WANDERING.md` |
| Faults: machine down, spike, runaway pod, blind probe | failed requests lower in all three, clear of the noise in one | −47% to −62% | inside the noise | inside the noise | `results/live/V3_FAULTS.md` |
| A queue of batch jobs | queue finished no difference beyond the noise | mean response −10% to −14% | **−19% to −23%** (−29% to −35% after the queue) | **−13% to −16%** | `results/live/V3_BATCH.md` |
| Fairness, a noisy neighbour | inside the noise on every row | inside the noise | inside the noise | inside the noise | `results/live/V3_FAIRNESS.md` |
| PostgreSQL behind PgBouncer, three workloads | inside the noise | inside the noise | connections held open **−61% to −72%** on two workloads; the runs disagree on the third | host CPU-seconds **+14% to +28%, confirmed worse** | `results/live/V3_PGBENCH.md` |
| Apache Kafka, a consumer group's size, three workloads | work inside the line **+16% to +21%**; no message lost | p95 **1.6 s → 9 to 14 ms**, lag −92% to −97% | consumers held **2 → 5.8 to 7.9, confirmed worse** | host CPU-seconds +10% to +20% confirmed worse on light, inside the noise on heavy and burst; CPU per message inside the line −10% to −12% on burst | `results/live/V3_KAFKA.md` |
| Redis, a cache's memory ceiling, three workloads | work inside the line **+14% to +27%**, hit rate +14% to +27%; no failed request | mean latency −30% to −61%; p95 within a hair of native's (a miss is a miss in both arms) | memory ceiling held **64 → 200 to 270 MB, confirmed worse** | host CPU-seconds inside the noise on all three | `results/live/V3_REDIS.md` |
| MongoDB under YCSB, a database's storage-engine cache size, four workloads | inside the noise on all four; no failed operation | p95 and p99 inside the noise; mean latency on burst **+2% to +4%, confirmed worse** | cache size held **−49% on c, −41% to −49% on burst, −13% to −37% on f, confirmed better**; b inside the noise in one run | host CPU-seconds inside the noise on all four | `results/live/V3_YCSB.md` |
| Robustness: the governor killed outright at 40% of the window, 10 pairs × 3 runs | **every setting back at the operator's 7 to 11 s after the kill, 30 of 30**; a second governor to the end; failed requests over the window −9% to −15% | the 120 s after the kill inside the noise against native; the whole window p95 −42% to −45% | inside the noise | inside the noise | `results/live/V3_ROBUST_KILL.md` |
| Robustness: the long run, 7,200 s an arm, 3 pairs × 3 runs | decisions 97.5% or more of expected (valid); failed requests inside the noise | service confirmed better in A, inside the noise in B and C (no difference beyond the noise in 2 of 3) | inside the noise; **memory at most 1.07 of its first ten minutes (no leak)**; decision time at most 1.20 (no slowing); every setting handed back at the end | inside the noise | `results/live/V3_ROBUST_LONG.md` |
| The six organisms with the real cluster inside, 10 and 100 copies, 5 pairs a cell | the organisms' work unchanged | p95 better in every cell | 6 in both arms (no autoscaler under kind) | the organisms' energy lower in every cell | `results/live/V3_SIX_KUBE.md` (v1 at 1 to 1,000 copies: `V1_SIX_KUBE.md`, `V1_BIG_ORGANISM.md`) |

## Measured on a real cloud (Azure, its own bill), Omni v1

| Test | Reading | Source |
|---|---|---|
| Steady load, 4 workers, 5 pairs | no difference beyond the noise on any gauge; the bill −4.7% with its interval across zero | `results/live/V1_AKS_STEADY.md` |
| A burst sized to the cluster, 4 workers, 5 pairs | the bill +5.0% with its interval across zero; p99 −34% clear of the noise in this one run; the rest inside the noise | `results/live/V1_AKS_BURST.md` |
| The fleet that can show one machine (40 workers, nine families) on v3 | dispatched; two earlier dispatches refused by the subscription's family allowances before any arm ran, the third by Azure's own cluster capacity in eastus; every refusal cost cents and is recorded | `docs/K8S_COMPASS_PREREGISTRATION.md` |

## Simulated (evidence class S: models, never counted in the headline), Omni v3

| What | Reading | Source |
|---|---|---|
| The 945 muscles and six organisms, A/B/C | reproduced to the digit in 3 of 3; 0 muscles worse; every organism superior within guardrails (work per energy +0.1% to +0.3%) | `results/realms/REALMS.md` |
| The four stacked at 1,000 copies with the real cluster inside, on a rented machine, 3 pairs (v3) | the organism's work unchanged (rounding-level) | the cluster's p95 **2.9 s → 150 ms**, p99 −97%, time over the line **51% → 0**, failed requests **0.14% → 0** | 6 machines in both arms | inside the noise (standby model); the organism's energy −0.4% (model) | `results/live/V3_BIG_ORGANISM.md` |
| The organisms at 1, 10, 100 and 1,000 copies × 1 to 1,000 runs, 84 of 90 cells | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left are beyond the machines available | `results/scale/GRID.md` |
| Power grid, 11 SimBench grids in pandapower, A/B/C (v1 and v3 identical) | with ZIP loads energy drawn and net import better in all 11; losses better in 7, worse in 4; tap operations fewer in 10, 4 → 8 a year in one (worse, the declared cost) | `results/live/V3_PANDAPOWER.md` |
| Robot arms, MuJoCo Menagerie, A/B/C | Gen3 and Panda: peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%; the Panda's copper +14% worse; UR5e and iiwa left native | `results/live/V3_MUJOCO.md`, `V1_MUJOCO_PANDA.md` |
| CityLearn, every district, A/B/C | electricity bought, peak and unevenness better in all 11 battery districts, carbon in 8; the bill worse in 7, ramping worse in 7 | `results/live/V3_CITYLEARN.md` |
| Drone swarms, gym-pybullet-drones, 20 drones in three cells, A/B/C | energy a mission −7% to −20% and missions a charge +8% to +25%, confirmed better; no late mission, reserve breach, near miss or collision in any arm | `results/live/V3_SWARM.md` |

## The card (evidence class P)

Every earlier card result ran on a controller since replaced and is obsolete. The one-card, card-inside-the-organisms
and eight-card runs are the founder's, on rented cards, after the CPU and cloud work, at one named commit
(`docs/GPU_RUN_GUIDE.md`, `docs/GPU_PREREGISTRATION.md`).

## Verified in code

| Property | Where |
|---|---|
| The canonical engine is `symmetric_verified`; the printed chart is a named variant, not benchmarked | `docs/CANONICAL_ENGINE.md` |
| Nine laws twinned in C++20 and proven equal to the Python; sealed by fingerprint | `results/SEAL.json`, `tools/seal.py` |
| The conveyance law conserves its budget and converges (proof and 20,000 random systems) | `docs/CONVEYANCE_LAW.md`, `tests/test_conveyance.py` |
| Safety shield: 2,000,000 adversarial cases, 0 violations; C++ engine: 100,000,000 decisions, no failures | `tests/test_shield_properties.py`, `results/SOAK.json` |


## Open

1. **Azure, the fleet that can show one machine**: steady and burst on 40 workers, v3; waiting on Azure's cluster
   capacity in eastus (the only region where this subscription has more than 10 cores). Then B and C.
2. **The four stacked and the tower at 1,000 copies with the real cluster inside, on v3**: the stack is done, 3 of 3 on
   the clock (`results/live/V3_BIG_ORGANISM.md`: the cluster's p95 2.9 s → 150 ms, time over the line 51% → 0, failed
   requests 0.14% → 0, machines and energy unchanged, 22 s behind a 10,800 s window); the tower runs now on a second rented
   machine the same way (about $10, about a day).
3. **The real card**: the founder's runs on Lambda, one exact commit.
4. **Robustness** (`docs/ROBUSTNESS_PREREGISTRATION.md`, no engine file changes): the kill scenario is done
   (`results/live/V3_ROBUST_KILL.md`: every setting back 7 to 11 s after the kill in 30 of 30 repetitions) and the
   governor's own CPU is tabulated (`results/live/V3_OWN_COST.md`); the long run is done (`results/live/V3_ROBUST_LONG.md`, 3 pairs × 3 runs, 7,200 s an arm: no leak, the decisions valid, no slowing, every setting handed back at the end; service inside the noise in two of three runs);
   the 24-hour run on a rented machine follows.
5. **YCSB on MongoDB, done** (`docs/YCSB_PREREGISTRATION.md`, `results/live/V3_YCSB.md`): the operator's WiredTiger cache
   as native, Omni on the cache size through the server's own console; four smoke runs recorded, then A, B and C on v3; the
   cache held given back by about half on two untouched workloads at no measurable cost in work, p95 or CPU, one confirmed
   loss (the burst mean latency, +2% to +4%); the index now spans five real categories at +25.9%. Cassandra and Redis under
   YCSB and HammerDB are next in row 24.
6. **The queue** (`docs/REGISTER.md` section 4, `docs/PROOF_PROGRAM.md`): drone swarms on PX4 and ArduPilot (gym-pybullet-drones done), YCSB on
   Cassandra and Redis and HammerDB, Spark, OpenSearch, fio, Open-RMF, the 24-hour robustness run, Basilisk, Orekit and GMAT,
   RocketPy, Cantera (Kafka and Redis done); one or two at a time, each preregistered.
7. **Omni-Compass 1.0**: when the founder declares the engine final, v3 as it stands is published as 1.0 and the older
   fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the manual: the governor, its mechanism, the wiring stack by stack, the frozen engines, the three-run rule, every result |
| `docs/OMNI_V3.md`, `docs/OMNI_V1.md` | what each engine is and every result read on it |
| `docs/REGISTER.md`, `docs/PROOF_PROGRAM.md` | every muscle, every benchmark run and still to run; the program to full size |
| `results/live/V3_*.md`, `V1_*.md`, `results/live/raw/` | the three-run tables and every archived run's files |
| `results/OMNI_INDEX.md` | the one combined number |
| `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md` | wiring it in yourself |
| `docs/METRICS_CATALOG.md` | every gauge, and whether it is measured or modelled |
| `omnicompass/`, `omni_controller/`, `realms/`, `cpp/` | the engine, the controllers, the muscles, the C++20 twins |
| `docs/HISTORY.md` | earlier states of play, kept whole |

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
