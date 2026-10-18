# The referee's summary: what Omni-Compass claims, what has been measured, and what is undetermined

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Two pages for a CTO, an engineer, a CFO or an attorney who needs the standing of every claim before reading anything else.
Every number names its engine and its evidence class: L is live software, the real thing; S is our own models, never
proof; P is a physical meter, and there is none yet. Every reading is GAIN, EVEN or LOSS, decided by what the gauge is for,
and holds only when all three of our runs (A, B and C) agree with every 95% interval clear of zero
(`docs/HOW_TO_READ_THE_RESULTS.md`). Beside every gain stands what it cost. Where no proof exists yet, the word is
**undetermined**.

## 1. What it is

A supervisory governor. It sits on top of a system's own controller (Kubernetes' autoscaler, a database's pool, a battery's
controller), reads the system, and moves the same settings native moves, inside bounds the system and its operator set. It
hands every setting back to native's value when it stops, dies or is switched off (`docs/SAFETY_CASE.md`).

## 2. Each claim and its standing

| Claim | Standing | Evidence |
|---|---|---|
| It sits on top of native and never replaces it | **Shown** | Every live test runs native, and Omni-Compass on top of the same native; the setting is read back at native's value at the end of every arm |
| It does no harm: never a LOSS against native | **Shown on what has run** | 0 LOSS rows in the seven database tables (omni-v10, L); the one Kubernetes LOSS (the pod start wait under KEDA's HTTP add-on) traces to the test machine, not the governor (`docs/POD_START_WAIT.md`) |
| More work, faster, on real Kubernetes | **Shown** (L, omni-v7) | See section 3 |
| More work, faster, on databases and caches | **Small or EVEN** (L, omni-v10) | Redis: work inside the line +1.3%, hit rate +1.3%, for +2.3% memory; Kafka: 1 to 2 gauges GAIN; PostgreSQL 1, MongoDB 1, MySQL 0 of their gauges GAIN; every other gauge EVEN. MySQL, MongoDB and PostgreSQL ran at the tune-down alone, where the governor refuses most trials; their runs at the max are queued (18 October) |
| Fewer machines | **Shown in one test** (L, omni-v7) | A queue of jobs: machines in service and node-hours cut 11.5% to 15.2%, the queue finished EVEN |
| A smaller cloud bill | **Undetermined** | Azure, the engine of 13 October: no difference in the bill (`results/live/AKS_BILL.md`); omni-v11's Azure sets are running; Google and Amazon have not run |
| Less energy | **Undetermined** | No physical meter yet; every energy figure in a live test is a declared model, not a measurement |
| More work per watt on a GPU | **Undetermined** | No run on the engine that stands |
| One governor over every muscle and organism | **Modelled** (S) | 1,107 muscles in our own models: 527 GAIN, 580 EVEN, 0 LOSS (`results/realms_v5/REALMS_V5.md`); a few dozen knobs on real systems |
| Its mathematics | **Partly proved** | Theorems 1 to 4 hold for the compass law's channel; global stability of the full six-state system is open (`docs/FORMAL_STATUS.md`) |

## 3. Real Kubernetes, each gain beside its cost (L, omni-v7, three runs of ten pairs, kind on one GitHub runner)

| Test | Gain, the same in all three of our runs | What it cost |
|---|---|---|
| The load stepping up and down (all four at once) | Work inside the response line +41% to +61%; 95th percentile cut 56% to 62% | Machines and node-hours EVEN; CPU used, the governor's own included, −0.8% to −3.2% |
| A public day of demand (Google 2011) | 95th percentile cut 54% to 58% | Machines EVEN; CPU used, the governor's own included, −2.6% to −3.9% |
| Faults injected | 95th percentile cut 51% to 63% | Replicas +13% to +21% (power given) |
| KEDA's HTTP add-on underneath | 95th percentile cut 71% to 75%; time over the line cut 94% to 95% | CPU used, the governor's own included, +54% to +57% (shown, not judged: idle processor given to the service) |
| KEDA on CPU and requests underneath | 95th percentile cut 52% to 54% | CPU used, the governor's own included, +29% to +34% (shown, not judged) |
| Goldilocks and the VPA underneath | 95th percentile cut 60% to 62% | CPU used, the governor's own included, +42% to +47% (shown, not judged) |
| A queue of jobs | Machines cut 11.5% to 15.2% | Queue finish time EVEN |
| A noisy neighbour; fixed capacity; CruiseKube underneath | EVEN | — |

The processor given in the add-on tests was idle on machines already running. Where machines are billed by the hour, idle
processor put to work costs nothing more unless it raises the machine count, and in these tests the machine count did not
rise. Where processor is billed by use, it is a cost, and the table shows it.

## 4. What is undetermined, and what decides it

- **The cloud bill**: omni-v11's Azure sets (running); Google once its key is stored whole; Amazon once its account is on the
  Paid plan.
- **Energy**: a rented machine with the processor's own energy counters and a wall meter.
- **The GPU**: the Lambda runs from one exact commit.
- **Production**: a deployment on a customer's system with their sign-off.
- **Outside review**: no outside party has reviewed, replicated or approved any result here.

## 5. How to check any number yourself

Every table names its runs; `scripts/raw_archive.sh open /run-<id>/` places the run's raw files at the path the table
names, with their SHA-256 sums, and the table's own tool rebuilds the table from them (`tools/confirm_abc.py`,
`tools/redis_abc.py`, and the like). `python3 tools/omni_version.py --commit <sha>` names the engine a run's commit carries.
`python3 verify.py` runs every test and check the repository holds.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
