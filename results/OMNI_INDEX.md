# The Omni index: more for the same, or the same for less

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Every measure of every test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work (more is better), speed (a lower response time), machines (fewer), energy (less). A test's index is the geometric mean of its ratios; a category is the geometric mean of its tests; the headline is the geometric mean of the real categories, each weighted the same. Modelled muscles are shown beside it, never inside it. Every number is read from the test's own three-run table (`results/live/V1_*.json` and `results/live/V3_*.json`, made by `tools/confirm_abc.py` and `tools/pgbench_abc.py` from the three archived runs; `tools/omni_index.py`).

## Headline: Omni-Compass on top of native, real machines, confirmed three times: **+20.1%** (more for the same, or the same for less, across work, speed, machines and energy)

A measure enters only as its three-run reading allows (`docs/OMNI_V1.md`): confirmed better or confirmed worse in all three runs counts, as the geometric mean of the runs' ratios; no difference beyond the noise counts as exactly 1, so nothing inside the noise is claimed either way. Real Kubernetes (Omni v1) and the real database (Omni v3) are the real categories in; Azure and the card join as their three-run tables land. The law, controllers and runners are the same bytes in v1 and v3 (`docs/OMNI_V3.md`); each table names the engine it ran on.

| Category | Index | More work by | Faster by (native p95 / omni p95) | Fewer machines by | Less energy by | Tests |
|---|---:|---:|---:|---:|---:|---:|
| Real Kubernetes (GitHub) | **+26.2%** | +20.4% | +95.1% | +4.4% | +2.7% | 6 |
| Real database (PostgreSQL behind PgBouncer, GitHub) | **+14.2%** | +0.0% | +0.0% | +106.6% | -17.7% | 3 |
| Real cloud (Azure AKS, billed) | pending | | | | | the v1 steady and burst runs are in (`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`: on a 4-worker fleet every gauge inside the noise but the burst's p99, −34% in one run); both join as three-run tables, and a fleet big enough to see one machine is next (the earlier engine's +7.5% is in `docs/history/OMNI_INDEX_pre_v1.md`) |
| Real card (NVIDIA, its own meter) | pending | | | | | the rerun on the current card controller (the 2026-10-02 run used the replaced one) |

Read: every column points the same way, plus is good for Omni-Compass. "Fewer machines by +4%" means Omni did the same work on 4% fewer machine-hours; "less energy by +3%" means 3% less energy for the same work; "faster by +95%" means native's slowest-5% response is 1.95 times Omni's (Omni answers about twice as fast); "more work by +45%" means 45% more work inside the response line. The energy figure on GitHub's Kubernetes is a declared model, not a meter; the database's energy column is the host's CPU seconds (the compass's own cost, confirmed worse, counted against Omni); its machines column is the connections held open to the database; Azure's machines are its own billed count.

## Every test

| Category | Test | Index | More work by | Faster by | Fewer machines by | Less energy by | Source |
|---|---|---:|---:|---:|---:|---:|---|
| Real Kubernetes (GitHub) | Steady same work: the load in steps at a fixed rate, ten pairs, three runs | **+32.4%** | equal | +200.7% | +2.3% | no difference beyond the noise | `results/live/V1_STEADY.json` |
| Real Kubernetes (GitHub) | Demand that wanders: up and down one step at a time, ten pairs, three runs | **+34.1%** | not taken | +140.2% | no difference beyond the noise | +0.3% | `results/live/V1_WANDERING.json` |
| Real Kubernetes (GitHub) | All four in one run: load up and down one step at a time, ten pairs, three runs | **+38.3%** | +45.1% | +152.4% | no difference beyond the noise | no difference beyond the noise | `results/live/V1_ALL_FOUR.json` |
| Real Kubernetes (GitHub) | Fairness: a noisy neighbour, ten pairs, three runs | **+0.0%** | not taken | no difference beyond the noise | same | no difference beyond the noise | `results/live/V1_FAIRNESS.json` |
| Real Kubernetes (GitHub) | Faults: machine down, spike, runaway pod, blind probe, ten pairs, three runs | **+38.9%** | not taken | +168.0% | no difference beyond the noise | no difference beyond the noise | `results/live/V1_FAULTS.json` |
| Real Kubernetes (GitHub) | A queue of jobs: cruise, then the emergency brake, ten pairs, three runs | **+18.6%** | not taken | +13.0% | +26.3% | +17.0% | `results/live/V1_BATCH.json` |
| Real database (PostgreSQL behind PgBouncer, GitHub) | pgbench `select`: the pooler's pool size, three paired repetitions, three runs | **+21.2%** | no difference beyond the noise | no difference beyond the noise | +164.1% | -18.2% | `results/live/V3_PGBENCH.json` |
| Real database (PostgreSQL behind PgBouncer, GitHub) | pgbench `simple_update`: the pooler's pool size, three paired repetitions, three runs | **-5.3%** | no difference beyond the noise | no difference beyond the noise | no difference beyond the noise | -19.6% | `results/live/V3_PGBENCH.json` |
| Real database (PostgreSQL behind PgBouncer, GitHub) | pgbench `tpcb_hot`: the pooler's pool size, three paired repetitions, three runs | **+29.7%** | no difference beyond the noise | no difference beyond the noise | +233.9% | -15.3% | `results/live/V3_PGBENCH.json` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
