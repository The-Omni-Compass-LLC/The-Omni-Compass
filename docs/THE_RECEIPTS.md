# The receipts, in their totality: what every result shows, and what it does not

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

A **receipt** here is a result file in this repository made by a paired run: the system as it runs on its own
(native) and the same system with Omni-Compass on top, the same work in both arms, the rules written down before the
counted runs, the engine identified by its fingerprint (`tools/omni_version.py --commit`), every row reported, losses
included. A receipt is read in the class of evidence it is: **P** a physical meter, **L** real software (a real
Kubernetes cluster, a real database), **S** our own models, **V** a property of the code. S is never presented as
proof of a physical saving. A result belongs to the engine it ran on and is never read across engines; every row below is the engine that stands, omni-v7, unless its Engine column says otherwise (the earlier engines' receipts are the road, in `docs/history`).
How to read a single table: `docs/HOW_TO_READ_THE_RESULTS.md`. The wording of every three-run row: `tools/readings.py`.

## 1. What the receipts say, read together

1. **More work in time, and a faster tail, on the same machines (L, omni-v7).** On a real Kubernetes cluster, Omni-Compass on
   top of the pod autoscaler cut the 95th-percentile response by 51% to 63% in the all-four, fault and public-trace tests,
   in all three runs each; where demand outran what native served in time, the work done inside the response line rose 41%
   to 61% (the all-four test); failed requests fell 9% to 17% and the alert minutes 16% to 67% where demand swung or machines
   failed. On top of Goldilocks the 95th percentile fell 60% to 62%, on top of KEDA 52% to 54%, and on top of KEDA's HTTP
   add-on 71% to 75%. Read together: the governor turns capacity the native controller leaves unused into service, on the
   same machines.
2. **The same work on less, where less is enough (L, omni-v7).** A queue of batch jobs ran on 12% to 15% fewer machines
   (19% to 22% fewer after it finished) with 8% to 11% less standby energy and a faster mean response, and the queue finished
   no later; Kafka held 0.3% to 0.8% fewer consumers; Redis's ceiling fell 2.5% on `burst`. PostgreSQL, MySQL and MongoDB read
   EVEN on every judged row: under the brain's verdict no give-back that would cost service was written.
3. **What it cost, shown beside it.** The pods the faster recovery took (faults: replicas +13% to +21%; the Google day: pods
   started +107% to +143%), the energy of workers left on at idle power on top of Goldilocks and KEDA (+1.1% to +2.3%, a
   declared model) and Redis's memory on `small` (+2.4%), each power given in all three runs, beside the service it bought.
4. **Everything handed back (L, omni-v7).** The long run (two hours an arm): no leak, every decision valid, no failed
   decision, every setting handed back. The kill test runs again on the fixed harness (its three omni-v7 runs of 16
   October were invalid: the restarted governor never began, `docs/ROBUSTNESS_PREREGISTRATION.md`, "On omni-v7").
5. **On our own models (S, omni-v7).** The 1,107 muscles each alone: 527 GAIN, 580 EVEN, none LOSS; every one of the
   seven organisms GAIN (fewer misses) under all three loads. The power grids: 67 gauge-rows GAIN, 14 power given, no LOSS.
   The robot arm the trial moved: torque −28.6%, tracking error −21.3%. The drone swarms: energy a mission −7% to −20%.
   **The buildings with batteries read LOSS in the seven 2023 districts** (energy not served +2.0% to +9.8%, discomfort,
   ramping and the highest peak), beside electricity bought and the daily peak GAIN in all ten battery districts; the cause
   is the battery wire (it did not see the outage hours those districts carry), and its fix is the next engine version.
6. **What is not yet shown.** No energy saving on a real chip: the physical receipt (P), the GPU's own meter on the
   current governor, is the decisive one still to be produced; every earlier card result is obsolete. No cloud-bill result
   on the engine that stands yet: the omni-v7 Azure sets run one at a time. More completed work at one fixed resource cap:
   the capacity test reads EVEN at all four caps (the quota blocks the one lever Omni-Compass has there).

## 2. Receipt by receipt

Newest first within each class. "In all three" means the same sign in runs A, B and C with every 95% interval clear of
zero; "noise" means an interval includes zero. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

### Real software (L)

| Test | Engine | Native | What moved | Reading | It shows | It does not show | File |
|---|---|---|---|---|---|---|---|
| All four at once | omni-v7 | HPA | work inside the line +41% to +61%; p95 −56% to −62%; failed requests −9% to −14%; alert minutes −20% to −35% | GAIN in all three | more work in time on the same machines | energy (noise, model) | `results/live/V7_ALL_FOUR.md` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | omni-v7 | HPA | p95 −51% to −63%; failed requests −11% to −17%; replicas +13% to +21% | GAIN in all three; replicas power given | service held through faults | machines (noise) | `results/live/V7_FAULTS.md` |
| The Google cluster trace of 2011, replayed | omni-v7 | HPA | p95 −54% to −58%; time over the line −72% to −74%; failed requests −12% to −14%; pods started +107% to +143% | GAIN in all three; pods power given | a public day of real demand served faster | machines (the same), a cloud bill | `results/live/V7_TRACE_GOOGLE2011.md` |
| A queue of batch jobs | omni-v7 | Jobs and HPA | machines −12% to −15% (−19% to −22% after the queue); standby-model energy −8% to −11%; queue finish noise | GAIN in all three | the same queue on fewer machines | a measured energy saving (model) | `results/live/V7_BATCH.md` |
| A noisy neighbour | omni-v7 | HPA | — | noise on every row | no harm beside a noisy neighbour | a gain there | `results/live/V7_FAIRNESS.md` |
| On top of Goldilocks and the VPA's recommender | omni-v7 | the service rightsized by Goldilocks, HPA | p95 −60% to −62%; time over the line −100%; energy +1.6% to +2.3% (model) | response times GAIN in all three; energy power given | a faster service on top of a rightsizer | a measured energy saving | `results/live/V7_GOLDILOCKS.md` |
| On top of KEDA's HTTP add-on | omni-v7 | KEDA 2.21, HTTP add-on 0.16 | p95 −71% to −75%; alert minutes −93% to −96%; replicas −15% to −19%; energy +2.2% to +2.3% (model) | GAIN in all three; energy power given | faster service on top of a second autoscaler | a measured energy saving | `results/live/V7_KEDA_REQUESTS.md` |
| On top of KEDA on CPU and requests | omni-v7 | KEDA 2.21 | p95 −52% to −54%; energy +1.1% to +1.7% (model) | as above | as above | as above | `results/live/V7_KEDA_CPU_REQUESTS.md` |
| On top of CruiseKube | omni-v7 | CruiseKube 0.3.4 | — | EVEN on every row; no command written | no harm on a rightsized service | a gain there | `results/live/V7_CRUISEKUBE.md` |
| Capacity at a fixed cap (four caps) | omni-v7 | HPA under a CPU quota | — | EVEN at every cap | no harm under a cap | more work under the cap | `results/live/V7_CAPACITY.md` |
| Redis | omni-v7 | the operator's 64 MB ceiling | work +1.2% to +1.7%, mean latency −1.8% to −7.9%; memory +2.4% on `small`, −2.5% on `burst` | GAIN in all three; memory power given on `small` | a faster cache, its price shown | a gain at the 95th percentile | `results/live/V7_REDIS.md` |
| Kafka | omni-v7 | the operator's 2 consumers | consumers −0.3% to −0.8% | GAIN in all three; the rest noise | no harm, a fraction given back | a service gain | `results/live/V7_KAFKA.md` |
| PostgreSQL, MySQL, MongoDB | omni-v7 | the operators' pool, buffer pool and cache | — | noise on every judged row (one MySQL row the runs disagree) | no harm under the verdict | memory given back (none passed its trial) | `results/live/V7_PGBENCH.md`, `V7_SYSBENCH.md`, `V7_YCSB.md` |
| The long run, two hours an arm | omni-v7 | HPA | no leak; decisions valid; none failed; every setting handed back | held in every repetition | it runs for hours unchanged | — | `results/live/V7_ROBUST_LONG.md` |
| Azure's managed Kubernetes, its own bill | v1 | AKS with its cluster autoscaler | bill −4.7% steady, +5.0% burst | noise on every gauge | the method on a real cloud bill | a bill saving (the omni-v7 sets run now) | `results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md` |

### Our own models (S)

| Test | Engine | Reading | File |
|---|---|---|---|
| The 1,107 muscles and the seven organisms, preregistered seeds | omni-v7 | 527 GAIN, 580 EVEN, none LOSS; every organism GAIN (fewer misses) under all three loads; reproduced exactly in three GitHub runs | `results/realms_v5/REALMS_V5.md` |
| Power grids: 11 SimBench grids in pandapower | omni-v7 | energy drawn and net import lower in all 11 (ZIP loads); losses lower in 7, power given in 4; tap operations fewer in 10, more in 1 | `results/live/V7_PANDAPOWER.md` |
| CityLearn districts | omni-v7 | electricity bought and the daily peak lower in all 10 battery districts; **LOSS** in the seven 2023 districts on energy not served, discomfort, ramping and the highest peak; monthly unevenness +0.11% in the 2022 robustness district | `results/live/V7_CITYLEARN.md` |
| Robot arms, MuJoCo Menagerie | omni-v7 | Gen3 peak torque −28.6%, tracking error −21.3%; UR5e and iiwa left native | `results/live/V7_MUJOCO.md` |
| Drone swarms, 20 drones in three cells | omni-v7 | energy a mission −7% to −20%, missions a charge +8% to +25%, GAIN in all three; no late mission, reserve breach, near miss or collision | `results/live/V7_SWARM.md` |

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
