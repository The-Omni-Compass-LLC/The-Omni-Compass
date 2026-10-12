# The receipts, in their totality: what every result shows, and what it does not

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

A **receipt** here is a result file in this repository made by a paired run: the system as it runs on its own
(native) and the same system with Omni-Compass on top, the same work in both arms, the rules written down before the
counted runs, the engine identified by its fingerprint (`tools/omni_version.py --commit`), every row reported, losses
included. A receipt is read in the class of evidence it is: **P** a physical meter, **L** real software (a real
Kubernetes cluster, a real database), **S** our own models, **V** a property of the code. S is never presented as
proof of a physical saving. A result belongs to the engine it ran on (v1, v3, v5) and is never read across engines.
How to read a single table: `docs/HOW_TO_READ_THE_RESULTS.md`. The wording of every three-run row: `tools/readings.py`.

## 1. What the receipts say, read together

1. **More work in time, and a faster tail, on the same machines (L, v3).** On a real Kubernetes cluster, Omni-Compass
   on top of the pod autoscaler cut the 95th-percentile response by 57% to 67% in the steady, wandering, all-four,
   fault and public-trace tests, in all three runs each; where demand outran what native served in time, the work done
   inside the response line rose 54% to 68% (the all-four test); failed requests fell 11% to 18% where demand swung or
   machines failed. On top of KEDA the 95th percentile fell 51% to 53%, and on top of KEDA's HTTP add-on 73% to 76%.
   Read together: the governor turns capacity the native controller leaves unused into service, on the same machines.
2. **The same service on less, where less is enough (L, v3).** PostgreSQL held 6% to 11% fewer connections open on
   `select`, MySQL's buffer pool 10% to 20% less on `read_write`, MongoDB's cache 3% to 13% less on `f`, each at the same
   service, each better in all three runs, every other workload inside the noise; machines 1.7% to 2.0% fewer at steady
   load, 16% to 20% fewer on a batch queue (26% to 33% after it), 7% to 9% fewer under the Google trace of 2011, 5.9% to
   7.8% fewer on top of KEDA's HTTP add-on.
3. **What it cost, shown beside it.** On top of KEDA, the energy of workers left on at idle power (a declared model)
   rose 1.0% to 2.6%, worse in all three runs, in both setups: power given for the faster service. Kafka and Redis read
   nothing at all in their sets of 10 October, because the rule of that day ended every spend trial before it could be
   judged; that was our wiring, amended the same day (amendment 3), and the sets on it are the result of record when
   they land.
4. **Everything handed back (L, v3).** The governor killed outright at 40% of the window: every setting back with the
   operator's within 11 seconds (9 on average), in 30 of 30 repetitions; the long run (two hours an arm): no leak, every decision
   valid, no slowing.
5. **On our own models, nothing worse, alone or inside a body (S, v5).** Of the 1,107 muscles of the catalog (the
   founder's nine open-source pieces among them), each alone on the preregistered seeds under its own load and under work
   waiting in line: 517 better, 421 at their limit on native (the max writes nothing to them), 169 no difference beyond the
   noise, none worse and none mixed. Inside the six organisms every organism is better as a whole under all three loads,
   and not one plant is worse than native in any organism under any load (the engine before left 3 of 1,868 under the
   climb; the living body that cures them is `docs/FORMAL_V5.md`, section 4).
6. **What is not yet shown.** No energy saving on a real chip: the physical receipt (P), the GPU's own meter on the
   current governor, on the same clock as the Kubernetes runs, is the decisive one still to be produced; every earlier
   card result ran on a controller since replaced and is obsolete. No cloud-bill saving: Azure's bill on four workers
   read no difference beyond the noise (a fleet too small to give back one machine), and the larger fleet waits on
   Azure's capacity. More completed work at one fixed resource cap: the capacity test was built on 12 October and its
   tuning run made; its three counted runs come next.

## 2. Receipt by receipt

Newest first within each class. "In all three" means the same sign in runs A, B and C with every 95% interval clear of
zero; "noise" means an interval includes zero.

### Real software (L)

| Test | Engine | Native | What moved | Reading | It shows | It does not show | File |
|---|---|---|---|---|---|---|---|
| Capacity at a fixed cap (four cap levels, rising load) | v5 | Kubernetes HPA under a CPU quota | — | tuning run made 12 October (one cap, not counted); A, B, C next | — | anything yet | `docs/CAPACITY_PREREGISTRATION.md` |
| On top of KEDA's HTTP add-on | v3 | KEDA 2.21, HTTP add-on 0.16 | p95 −73% to −76%; machines −5.9% to −7.8%; idle-power energy +1.0% to +2.6% | p95 and machines better in all three; energy worse in all three (model) | faster service and fewer machines on top of a second autoscaler | a measured energy saving (the energy is a model) | `results/live/V3_KEDA_REQUESTS.md` |
| On top of KEDA on CPU and requests | v3 | KEDA 2.21 | p95 −51% to −53%; idle-power energy worse | as above | as above | as above | `results/live/V3_KEDA_CPU_REQUESTS.md` |
| The Google cluster trace of 2011, replayed | v3 | HPA | p95 −64% to −67%; failed requests −11% to −18%; machines −7% to −9% | better in all three | a public day of real demand served faster on fewer machines | a cloud bill | `results/live/V3_TRACE_GOOGLE2011.md` |
| All four at once | v3 | HPA | work inside the line +54% to +68%; p95 −57% to −63% | better in all three | more work in time on the same machines | energy (inside the noise, model) | `results/live/V3_ALL_FOUR.md` |
| Steady work in steps | v3 | HPA | p95 −64% to −66%; machines −1.7% to −2.0% | better in all three | a faster tail on fewer machines | a measured energy saving (model −1.3% to −1.8%) | `results/live/V3_STEADY.md` |
| Demand that wanders | v3 | HPA | p95 −57% to −64%; failed requests −12% to −13% | better in all three | service held as demand moves | machines (noise) | `results/live/V3_WANDERING.md` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | v3 | HPA | p95 −58% to −63%; failed requests −14% to −18% | better in all three | service held through faults | machines (noise) | `results/live/V3_FAULTS.md` |
| A queue of batch jobs | v3 | Jobs and HPA | machines −16% to −20% (−26% to −33% after the queue); standby-model energy −11% to −14%; queue finish noise | better in all three | the same queue on fewer machines | a measured energy saving (model) | `results/live/V3_BATCH.md` |
| A noisy neighbour | v3 | HPA | — | noise on every row | no harm beside a noisy neighbour | a gain there | `results/live/V3_FAIRNESS.md` |
| PostgreSQL behind PgBouncer | v3 | the operator's pool of 20 | connections −6% to −11% on `select`; the add above 20 refused on `simple_update` | better in all three on `select`; the rest noise | memory given back at the same service, proved on the stack first | more throughput | `results/live/V3_PGBENCH.md` |
| MySQL under sysbench | v3 | the operator's 512 MB buffer pool | pool −10% to −20% on `read_write` | better in all three; the rest noise | memory given back at the same service | more throughput | `results/live/V3_SYSBENCH.md` |
| MongoDB under YCSB | v3 | the operator's 512 MB cache | cache −3% to −13% on `f` | better in all three; the rest noise | memory given back at the same service | more throughput | `results/live/V3_YCSB.md` |
| Apache Kafka; Redis | v3 | the operator's settings | nothing judged | noise everywhere; every spend trial ended unjudged (our wiring, amendment 3) | no harm | a gain (none judged yet) | `results/live/V3_KAFKA.md`, `results/live/V3_REDIS.md` |
| The governor killed at 40% of the window | v3 | HPA | every setting back within 11 s (9 on average), 30 of 30; the window's p95 −27% to −48% | held in every repetition | the hand-back works under a crash | — | `results/live/V3_ROBUST_KILL.md` |
| The long run, two hours an arm | v3 | HPA | no leak; decisions valid; no slowing | held in every repetition | it runs for hours unchanged | — | `results/live/V3_ROBUST_LONG.md` |
| The six organisms with the real cluster inside, 10 and 100 copies | v3 | HPA | the cluster's p95 lower in all 12 cells (−1% to −52%); failed requests lower in 11 | per cell | the organisms and a real cluster on one clock | machines (6 in both arms under kind) | `results/live/V3_SIX_KUBE.md` |
| Azure's managed Kubernetes, its own bill, 4 workers | v1 | AKS with its cluster autoscaler | bill −4.7% steady, +5.0% burst | noise on every gauge (p99 −34% clear in one run) | the method on a real cloud bill | a bill saving (the fleet is too small to give back a machine) | `results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md` |

### Our own models (S)

| Test | Engine | Reading | File |
|---|---|---|---|
| The 1,107 muscles and the six organisms, preregistered seeds | v5 (digest 9be48445) | 517 better, 421 at their limit on native, 169 noise, 0 worse; every organism better under all three loads; 0 plants worse in any organism under any load | `results/realms_v5/REALMS_V5.md` |
| Power grids: 11 SimBench grids in pandapower | v3 | energy drawn and net import better in all 11; losses better in 7, worse in 4; tap operations fewer in 10, more in 1 | `results/live/V3_PANDAPOWER.md` |
| CityLearn districts | v3 | electricity bought, peak and unevenness better in all 11 battery districts; the bill worse in 7, ramping worse in 7 | `results/live/V3_CITYLEARN.md` |
| Robot arms, MuJoCo Menagerie | v3 | Gen3 and Panda peak torque −29% and −10%, tracking error −21%; the Panda's copper +14% worse; UR5e and iiwa left native | `results/live/V3_MUJOCO.md` |
| Drone swarms, 20 drones in three cells | v3 | energy a mission −7% to −20%, missions a charge +8% to +25%, better in all three; no late mission, reserve breach, near miss or collision | `results/live/V3_SWARM.md` |

### A physical meter (P)

| Test | Status |
|---|---|
| One card, the card inside the organisms, eight cards, on the current governor | to be run by the founder on rented cards, at one exact commit, after the CPU side (`docs/GPU_RUN_GUIDE.md`); every earlier card result is obsolete |

### The code (V)

The max's guarantees, one by one, with the code path that makes each one true: `docs/FORMAL_V5.md`. The budget law's
conservation and convergence, the safety shield's 2,000,000 adversarial cases, the C++ twins equal to the Python: 
`docs/STATE_OF_PLAY.md`, "Verified in code".

## 3. What would change these readings

- A P run on a real card that shows no difference in the card's own energy at the same work would leave the energy
  claim at "not shown"; it is not claimed now.
- An A, B or C run that disagrees with the others turns a row into "the runs disagree"; it is looked into, never
  dropped.
- A loss in all three runs is reported as it stands, its cause looked for in our own wiring, setup and scoring first,
  and the next set run on the fix.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.
Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any
outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
