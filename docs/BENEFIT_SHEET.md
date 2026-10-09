# The benefit sheet: one number per benchmark, plus always good for Omni

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


The founder's order of 9 October 2026: next to every benchmark, say whether Omni-Compass was a benefit and by how much, in one number whose sign always means the same thing. **Plus is good for Omni, minus is bad, whatever the gauge measures.** Less energy, fewer machines, less memory, a shorter wait and fewer failures are all plus here; more of any of them is minus. **0%** means nothing beyond the noise. The tables keep their raw signs (a response time that fell reads "-65%" in its table); this sheet turns every one the same way round, by one rule, from the tables themselves (`tools/benefit_sheet.py`, checked by `verify.py`).

The rule is the Omni index's (`results/OMNI_INDEX.md`): each judged gauge becomes a ratio oriented so that above one is good for Omni; it counts only where confirmed over all three runs, anything else counts as exactly one; the number is the geometric mean of the ratios, minus one, in percent. For the tests inside the index the number is the index's own resource reading of that test; for a stack with several workloads it is the stack's index category; for the simulators and the organisms the same arithmetic runs over every judged gauge of their tables.

**Benefit?** reads **yes** (a confirmed gain, no confirmed loss), **no** (a confirmed loss, no confirmed gain), **none** (nothing confirmed either way) or **trade** (gains and losses both; the number says which way the trade nets by this scoring, and the wiring page `docs/WIRING_VERDICTS.md` says what pays for what).

| Date | Benchmark | Benefit? | How much (plus is good) | Gauges better / worse | What the number is | Table |
|---|---|---|---:|---:|---|---|
| 2026-10-09 | Every real test together: the Omni index | **trade** | **+21%** | 82 / 16 | the headline: six real categories weighed the same (the index's resource reading) | `results/OMNI_INDEX.md` |
| 2026-10-09 | The big organisms with the real cluster inside, 1,000 copies on Azure | **yes** | **+155%** | 4 / 0 | the cluster's own gauges in both cells | `results/live/V3_BIG_ORGANISM.md` |
| 2026-10-09 | PostgreSQL, the pooler's pool size | **trade** | **+4.0%** | 1 / 1 | the index's category: its untouched workloads together (work, p95, the resource held, host CPU) | `results/live/V3_PGBENCH.md` |
| 2026-10-09 | MySQL, the buffer pool's size | **trade** | **+5.2%** | 4 / 1 | the index's category: its untouched workloads together (work, p95, the resource held, host CPU) | `results/live/V3_SYSBENCH.md` |
| 2026-10-09 | MongoDB, the storage engine's cache size | **yes** | **+8.5%** | 8 / 0 | the index's category: its untouched workloads together (work, p95, the resource held, host CPU) | `results/live/V3_YCSB.md` |
| 2026-10-08 | Robustness: the two-hour run | **none** | **0%** | 0 / 0 | the two-hour window; p95, machines, energy | `results/live/V3_ROBUST_LONG.md` |
| 2026-10-08 | Robustness: the governor killed outright mid-run | **yes** | **+9.4%** | 4 / 0 | the whole window, a kill and a restart inside it; p95, machines, energy | `results/live/V3_ROBUST_KILL.md` |
| 2026-10-08 | Redis, the cache's memory ceiling | **trade** | **-25%** | 12 / 6 | the index's category: its untouched workloads together (work, p95, the resource held, host CPU) | `results/live/V3_REDIS.md` |
| 2026-10-08 | Real Kubernetes, a public day of demand (Google 2011) | **yes** | **+50%** | 9 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_TRACE_GOOGLE2011.md` |
| 2026-10-08 | Kafka, the consumer group's size | **trade** | **+167%** | 21 / 8 | the index's category: its untouched workloads together (work, p95, the resource held, host CPU) | `results/live/V3_KAFKA.md` |
| 2026-10-07 | The six organisms with the real cluster inside, 10 and 100 copies | **yes** | **+3.7%** | 19 / 0 | the cluster's own gauges in every cell; the modelled organism is judged in the realms table | `results/live/V3_SIX_KUBE.md` |
| 2026-10-07 | The 945 modelled muscles as one tower, every muscle written at once | **yes** | **+0.3%** | 1 / 0 | the tower's work per energy over ten paired seeds; a model, evidence class S | `results/realms/REALMS.md` |
| 2026-10-07 | Robot arms (MuJoCo), the three untouched robots | **yes** | **+3.8%** | 6 / 0 | every judged gauge of each robot's table (energy, losses, torque, tracking); a robot the engine left native reads 0 | `results/live/V3_MUJOCO.md` |
| 2026-10-07 | Real Kubernetes, steady work | **yes** | **+31%** | 7 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_STEADY.md` |
| 2026-10-07 | Real Kubernetes, faults | **yes** | **+32%** | 4 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_FAULTS.md` |
| 2026-10-07 | Real Kubernetes, demand that wanders | **yes** | **+37%** | 5 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_WANDERING.md` |
| 2026-10-07 | Real Kubernetes, all four at once | **yes** | **+40%** | 5 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_ALL_FOUR.md` |
| 2026-10-07 | Real Kubernetes, a queue of jobs | **yes** | **+19%** | 6 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_BATCH.md` |
| 2026-10-07 | Real Kubernetes, a noisy neighbour | **none** | **0%** | 0 / 0 | the index's reading of this test: p95, machines, energy, and work where measured | `results/live/V3_FAIRNESS.md` |
| 2026-10-07 | Power grids (SimBench), both load models | **trade** | **+5.8%** | 63 / 14 | every judged gauge of every grid, then the grids together | `results/live/V3_PANDAPOWER.md` |
| 2026-10-07 | Drone swarms, the three untouched cells | **yes** | **+6.1%** | 9 / 0 | every judged gauge of every cell | `results/live/V3_SWARM.md` |
| 2026-10-07 | Buildings and batteries (CityLearn), the districts with batteries | **trade** | **+0.8%** | 71 / 33 | every CityLearn score of every district, then the districts together | `results/live/V3_CITYLEARN.md` |

## The parts behind a row

Where a row sums several workloads, grids, districts, cells or robots, each part with its own number, the same way round:

- **The big organisms with the real cluster inside, 1,000 copies on Azure**: tower at 1000 copies +159% (yes); stack at 1000 copies +151% (yes).
- **PostgreSQL, the pooler's pool size**: select +12% (yes); simple_update 0% (no); tpcb_hot 0% (none).
- **MySQL, the buffer pool's size**: burst +21% (yes); read_only 0% (none); read_write +1.2% (trade); update_index 0% (none).
- **MongoDB, the storage engine's cache size**: b +9.6% (yes); burst +6.8% (yes); c +7.1% (yes); f +11% (yes).
- **Redis, the cache's memory ceiling**: burst -22% (trade); large -27% (trade); small -26% (trade).
- **Kafka, the consumer group's size**: burst +182% (trade); heavy +156% (trade); light +163% (trade).
- **The six organisms with the real cluster inside, 10 and 100 copies**: compute_ai_cloud at 10 copies +3.6% (yes); physics_robotics_autonomous at 10 copies +4.5% (yes); energy_facility_industrial at 10 copies +4.3% (yes); distribution_specialized at 10 copies +3.1% (yes); tower at 10 copies +5.8% (yes); stack at 10 copies +6.2% (yes); compute_ai_cloud at 100 copies +3.7% (yes); physics_robotics_autonomous at 100 copies +2.5% (yes); energy_facility_industrial at 100 copies +6.1% (yes); distribution_specialized at 100 copies +0.1% (yes); tower at 100 copies +2.6% (yes); stack at 100 copies +1.6% (yes).
- **Robot arms (MuJoCo), the three untouched robots**: kinova_gen3 +12% (yes); kuka_iiwa_14 (left native by the engine's own trial) 0% (none); universal_robots_ur5e (left native by the engine's own trial) 0% (none).
- **Power grids (SimBench), both load models**: 1-MV-comm--0-sw (ZIP loads) +9.7% (yes); 1-MV-comm--1-sw (ZIP loads) +13% (yes); 1-MV-comm--2-sw (ZIP loads) +11% (yes); 1-MV-rural--1-sw (ZIP loads) -13% (trade); 1-MV-rural--2-sw (ZIP loads) +6.8% (trade); 1-MV-semiurb--0-sw (ZIP loads) +12% (yes); 1-MV-semiurb--1-sw (ZIP loads) +9.0% (trade); 1-MV-semiurb--2-sw (ZIP loads) +5.8% (trade); 1-MV-urban--0-sw (ZIP loads) +8.9% (yes); 1-MV-urban--1-sw (ZIP loads) +8.6% (yes); 1-MV-urban--2-sw (ZIP loads) +6.8% (yes); 1-MV-comm--0-sw (constant-power loads) +7.8% (yes); 1-MV-comm--1-sw (constant-power loads) +7.7% (yes); 1-MV-comm--2-sw (constant-power loads) +7.8% (yes); 1-MV-rural--1-sw (constant-power loads) -13% (no); 1-MV-rural--2-sw (constant-power loads) +3.3% (trade); 1-MV-semiurb--0-sw (constant-power loads) +7.4% (yes); 1-MV-semiurb--1-sw (constant-power loads) +7.6% (trade); 1-MV-semiurb--2-sw (constant-power loads) +4.7% (trade); 1-MV-urban--0-sw (constant-power loads) +7.7% (yes); 1-MV-urban--1-sw (constant-power loads) +6.8% (yes); 1-MV-urban--2-sw (constant-power loads) +5.4% (yes).
- **Drone swarms, the three untouched cells**: long +7.6% (yes); mixed +6.8% (yes); short +3.9% (yes).
- **Buildings and batteries (CityLearn), the districts with batteries**: ca_alameda_county_neighborhood +1.7% (yes); citylearn_challenge_2022_phase_all_robustness +8.3% (trade); citylearn_challenge_2023_phase_2_local_evaluation -0.7% (trade); citylearn_challenge_2023_phase_2_online_evaluation_1 -0.2% (trade); citylearn_challenge_2023_phase_2_online_evaluation_2 -0.3% (trade); citylearn_challenge_2023_phase_2_online_evaluation_3 -0.5% (trade); citylearn_challenge_2023_phase_3_1 -0.1% (trade); citylearn_challenge_2023_phase_3_2 -0.4% (trade); citylearn_challenge_2023_phase_3_3 -0.1% (trade); tx_travis_county_neighborhood +0.9% (yes); vt_chittenden_county_neighborhood +0.5% (yes).

## Not on the sheet, and why

- **Azure's managed Kubernetes, the bill** (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): Omni v1, a 4-worker fleet, every gauge inside the noise: 0%, and too small a fleet to show one machine.
- **The governor's own cost** (`results/live/V3_OWN_COST.md`): 0.6% to 1.3% of one core at every size; a cost shown, not a benchmark against native.
- **The card (NVIDIA)**: every earlier result is obsolete; the current governor has not run on a real card.
- **The index's second reading** (service alone, `results/OMNI_INDEX.md`): a second true number for the same tests, not repeated here; this sheet carries the preregistered one.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
