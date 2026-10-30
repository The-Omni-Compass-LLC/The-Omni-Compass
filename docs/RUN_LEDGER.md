# Run ledger: every chip, cloud and machine run, what it cost, and what came back

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read from GitHub's own run records on 27 October 2026 (the `lambda-gpu`, `aks-metered`, `cloud-check` and benchmark
workflows), not from memory; the chip and cloud rows brought up to 30 October, 00:22 UTC, from the same records. Dollar figures are the hours a machine was rented times the hourly price each launch printed
(`gpu_1x_a10`: $1.29 an hour). Lambda's own billing page is the exact figure; this page is the record of what each rental
was for, whether it finished, and where its receipt is.

## 1. GPU chips on Lambda

| GitHub run | Started (UTC) | What | Card | Hours rented | Cost | Finished? | What came back | Receipt |
|---|---|---|---|---:|---:|---|---|---|
| 40079073999 | 24 Oct 08:42 | one card, fast, omni-v18 | A10 | 0.4 | about $0.52 | No: the run refused to start (the copy shipped to the card had no git record) and the card went back | nothing; the shipping was fixed the same morning | none |
| 40079645681 | 24 Oct 08:51 | one card, omni-v18 | A100 SXM4 40 GB | 6.7 | at Lambda's A100 price (billing page) | **Yes**: one run, 10 paired repetitions | every service gauge STEADY; the governor wrote nothing in 3,050 decisions, both knobs already at their top on native (at its limit on native); wire check 7 of 7, fault drill 5 of 5 | `results/gpu/run-20261024T091235Z/GPU_REPS.md` |
| 40143765437, 40143770324, 40143775773 | 24 Oct 23:41 | the whole stacks with the card inside, A, B and C, omni-v18 | A10 ×3 | 25.1, 25.1, 25.0 | about $97 | **No**: each reached its 25-hour limit inside the stacks (1x copies done, 5 repetitions; 10x in its third) | the wire check and the smoke only: the stacks write each arm on the card and pack them only when they finish, and the watcher fetched only packed files, so every stacks arm stayed on the card when it was given back (fixed 26 October, commit `8e62252e1f`) | `raw` branch, `run-40143765437/` and the other two |
| 40218532131, 40218534998, 40218537259 | 25 Oct 17:52 | the stacks, A, B and C, omni-v21 | none | 0 | $0 | No: started as dry runs by mistake (priced, nothing rented) | the price only | none |
| 40393460334, 40393464531, 40393468676 | 26 Oct 20:11 | the stacks, A, B and C, omni-v21 | A10 ×3 | 0.1, 0.3, 0.3 | about $0.90 | Stopped on the founder's decision: they carried the watcher fault above | nothing | none |
| 40394988327, 40394992822, 40394997159 | 26 Oct 20:22 | the stacks, A, B and C, omni-v21, the watcher fixed | A10 ×3 | about 33 each, the budget | at most about $128 | **Yes**: all three finished on 28 Oct, 05:30 to 05:41 UTC | every run's files, on the `raw` branch; their three-run table is not yet written | `raw` branch, `run-40394988327/`, `run-40394992822/`, `run-40394997159/` |
| 40461604089 | 27 Oct 06:31 | one card, fast, omni-v21 | one card | about 7 | at the card's hourly price (billing page) | **Yes**, 13:36 UTC | its files, on the `raw` branch; no table yet | `raw` branch, `run-40461604089/` |
| 40485597269, 40485602065, 40485605739 | 27 Oct 10:04 | one card, fast, the saving dial, A, B and C, omni-v21 | one card ×3 | about 7 each | at the card's hourly price (billing page) | **Yes**, about 16:57 UTC | their files, on the `raw` branch; no three-run table yet | `raw` branch, `run-<id>/` |
| 40485609401, 40485613546, 40485617318 | 27 Oct 10:04 | one card, the operator's power cap underneath, A, B and C, omni-v21 | one card ×3 | about 4.6 each | at the card's hourly price (billing page) | **Yes**, 14:39 UTC | their files, on the `raw` branch; no three-run table yet | `raw` branch, `run-<id>/` |
| 14 runs, 24 Oct 02:57 to 08:41 | | launches that stopped before renting (the key and the shipping being set up) | none | 0 | $0 | No | nothing | none |
| 40400845313 | 26 Oct 21:01 | eight cards, pooled | none | 0 | $0 | dry run (priced only) | the price only | none |

**Rented so far:** about 175 A10 hours for the runs through 26 October (about $226), 6.7 A100 hours, and at most about 41 card hours on
27 October (the fast, saving-dial and cap runs). Lambda's billing page is the exact figure.

**What the record says about the chip:** one finished result on omni-v18 (the A100: STEADY, because native already ran both
knobs at their top). On omni-v21 the stacks' three runs and the one-card runs of 27 October all finished and their files are
on the `raw` branch; no three-run table has been written from them yet, so the page reads no chip result on omni-v21.

Older GPU results (2 October, `results/gpu/run-20261002T082232Z/`) are obsolete by the founder's order and stay as history.

## 2. CPU

| Benchmark | State | Why |
|---|---|---|
| The Linux CPU governor and its energy meter (`cpu-power`) | **Not run on real hardware** | GitHub's machines are virtual: no frequency governor and no energy meter. The three omni-v21 runs (A, B, C) are capability checks that read "cannot run here". It needs a bare-metal machine (a self-hosted runner). From 27 October the workflow fails if the harness's own tests or the probe fail, instead of hiding it. |
| Every Kubernetes benchmark | Run on GitHub's processors (class L) | see section 4 |

## 3. Clouds

| Cloud | State | Detail | Receipt |
|---|---|---|---|
| Azure | **On, running** | The omni-v18 100-repetition set (run 40069633316) ended on 29 October, 15:12 UTC, as a failure; the repair note of 29 October (`docs/REPAIR_20261029.md`) names its repetitions 90 and 91 as not validated, and it stays omni-v18's record. The $0 check passed on 29 October, 19:13 UTC (run 40938130483), and the omni-v21 steady set (run 40940616527, up to 100 repetitions under the stopping rule) started at 19:30: at 00:22 UTC on 30 October, 2 repetitions passed, repetition 3 failed in its measurement step (its files kept, artifact `aks-3`), repetition 4 running. | `results/live/AKS_BILL.md` (omni-v1: the bill STEADY) |
| Google Cloud | **Never run** | Its keys are not in the repository's secrets: `GCP_CREDENTIALS` and `GCP_PROJECT` (the $0 check, `cloud-check`, read them absent on 26 October and again on 27 October, run 40471452017). Wired; switched off. | none |
| Amazon | **Never run** | `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are not stored (the $0 check of 27 October, run 40471452017), and the account is on the Free plan. Wired; switched off. | none |
| Oracle, DigitalOcean, Alibaba, Linode, IBM, other | Never run | wired through `byoc-metered`, no cluster connected | none |

## 4. Kubernetes, the data stores and the outside simulators on omni-v21

23 of the 26 benchmarks on the benefit board read omni-v21's own three-run table (`docs/BENEFIT_SHEET.md`, written by
`tools/benefit_sheet.py`); every table names its three GitHub runs, and every run's files are on the `raw` branch.

| Still on an older engine | Its table | What it waits for |
|---|---|---|
| The six organisms with the real cluster inside, 10 and 100 copies | `results/live/V3_SIX_KUBE.md` (omni-v3) | the grid's omni-v21 runs |
| The big organisms with the real cluster inside, 1,000 copies on Azure | `results/live/V3_BIG_ORGANISM.md` (omni-v3) | an Azure set on omni-v21 |
| The 945 modelled muscles as one tower | `results/realms/REALMS.md` (omni-v3) | its table from the omni-v21 realms runs |

Every omni-v21 table was rebuilt on 27 October from its three archived runs by `tools/reproduce.py` (the recipes in
`results/live/RECIPES.json` and the front page's own for the five data stores): all 31 tables (18 Kubernetes and simulator
tables, 13 data-store tables; 58 files), identical to the byte, and every one names omni-v21 alone (the drone swarms' table names
omni-v12 only as the engine before whose runs its preregistration's amendment 2 was written).

## 5. Open, in one list

1. GPU: the three omni-v21 stacks runs finish by about 05:30 UTC on 28 October; then their three-run table. The one-card
   `cap` runs (an operator's power cap underneath, the cap alone against the cap with Omni-Compass on top) follow, A, B and C
   on A100s, since the A100's counted run read STEADY with no write (its limit already at the top on native).
   And the tune-down on the same card (`dial save`, A, B and C): the card averaged 253 W of its 400 W limit in that run, room
   the factory tune (the max, which never steps the clock below the top) leaves unused.
2. Azure: the omni-v18 set finishes; then the omni-v21 sets start.
3. Google and Amazon: their keys (`docs/GOOGLE_SETUP.md` section 4, `docs/AMAZON_SETUP.md` section 1a).
4. CPU: a bare-metal machine, or it stays not run.
5. The three tables above still on omni-v3.
6. The LOSS rows on omni-v21, each in `docs/LOSS_LEDGER.md`: the pod start wait on the Google day (more pods started; each
   starts as fast) and on Goldilocks (each pod slower too), CruiseKube's response time by the mean, and Kafka's.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
