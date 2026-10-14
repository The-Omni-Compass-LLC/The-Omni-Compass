# The next engine version: what goes in, and in what order

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 13 October 2026 (night), before any of it is built, on the founder's orders of 13 October. The engine that stands
is omni-v5, digest `6093b2b88aa911b9`. Everything below changes the engine, so it lands as the next declared version, and
every benchmark then runs again on it, A, B and C. Nothing here is a result.

## 1. GAIN, EVEN and LOSS as the code that steers the brain

Today the words are in every report (`tools/readings.py`) and the engine already acts on the same aims: the verdict
(`omnicompass/verdict.py`) keeps a step only where the muscle's own cost per piece of work is no higher, and the body's
guard refuses a step that pushes another part past its cushion. The next version makes the three words the brain's own
vocabulary: every gauge a muscle reports carries its declared aim (lower, higher, spent), and every trial is judged in the
words the reports use, GAIN, EVEN, LOSS or power given, for the muscle and for the body. A trial that reads LOSS anywhere is
undone; power given is kept only beside the work or speed it bought. One table of aims serves the brain and the reports, so
they can never disagree.

## 2. The muscles the catalog does not yet name

The catalog holds 1,107 muscles in 70 families. Read against the founder's list, these controls everybody runs are not yet
muscles of their own (each is a setting the native system already exposes to its operator):

| New family or addition | Muscles |
|---|---|
| SCADA and supervisory control | RTU and PLC polling interval (Modbus, DNP3), historian sampling rate, alarm-flood suppression window, supervisory setpoint push rate, OPC UA subscription rate |
| Control loops and estimation | PID gain schedule, setpoint ramp rate, controller output limit, anti-windup clamp, MPC prediction horizon, MPC move-suppression weight, MPC constraint softening, Kalman process-noise scale, estimator innovation gate, sensor-fusion rate |
| LLM and agent orchestration | agent concurrency, tool-call budget, token budget per task, model tier routing, context-cache budget, semantic-cache threshold, retry and timeout policy, parallel tool calls |
| ML optimizers and training schedule | learning-rate scale (Adam and its kin), warm-up steps, learning-rate schedule, gradient clipping, optimizer-state offload, ZeRO / FSDP sharding stage, evaluation interval |
| Cloud management and infrastructure as code | cloud quota guard, cost-budget gate, Terraform / OpenTofu apply parallelism, Crossplane reconcile rate, multi-cloud placement weight |
| Source control and developer platforms | GitLab and Bitbucket runner pools, Git LFS cache, repository mirror sync rate, code-review bot concurrency |

Each is added under the same rule as every muscle before it: tuned on development seeds only, kept only when it wins twice
and never falls behind native on any seed, and placed in every realm that runs that domain.

## 3. The whole tower at 100 copies

The long-window rerun on GitHub's four-core machine read the tower's 95th-percentile response time +45.9%, a LOSS (run
38423471888), while time over the line read GAIN (-14.9%) and failed requests GAIN (-8.8%). The machine was 87 to 89% busy
and Omni's arm made it 2.4% busier, its model 1.25 s further behind its clock. Two tests decide the cause before anything
in the engine is changed for it: protocol 3 on GitHub (the model on its own core, runs 38464343379 and 38462289297) and the
same tower at 100 copies on an eight-core Azure machine (three machines started 13 October, repetitions 1 to 10). If the
LOSS goes with the machine, it is the test rig and is reported so; if it stays, its cause is found inside the engine and
fixed there, never by going back to an older engine.

## 4. Also in this version (announced earlier)

- The GPU's heat line: never over 83 C, and the headroom under it used where it buys work.
- Micro steps inside each decision (fourth-order Runge-Kutta for the plants' motion, Monte Carlo over their uncertainty).
- The body's hormones and immune system carried into every organism.

## 5. Every LOSS that stands today, and what this version does about each

The founder's order of 13 October: a LOSS row is never cut; its cause is found and fixed and the test run again. These are
the LOSS rows on the newest tables (the grid page is the card version, digest `5648f290`; the grid on `6093b2b8` is
running now):

| Where | The LOSS | What it shows | In this version |
|---|---|---|---|
| The grid with the cluster inside (`results/grid_v5/GRID.md`) | the organism's work per energy, in 21 of 36 squares of 10 and 100 repetitions | the max gave the organism power (its energy reads power given) and the work waiting in line was done either way, so each unit of work took more energy; the power bought fewer misses (time over the line reads GAIN in all 36) | the decision code counts the body's work per energy as a gauge of its own: a power step that buys no work and no fewer misses is undone; where it buys fewer misses, the step stays only while the body's work per energy stays EVEN, so the row reads EVEN or GAIN |
| The four stacked at 100 copies, 100 repetitions | 95th and 99th percentile response time | the organism ran past its window in 49 of 100 repetitions (up to 635 s): GitHub's four-core machine could not step that many muscles in time | section 3: protocol 3 and the eight-core Azure machine decide whether it is the machine; if it stays, the cause is fixed in the engine |
| The whole tower at 100 copies, 100 repetitions | 95th and 99th percentile response time | the same machine; the long-window rerun read +45.9% at the 95th percentile | section 3 |
| CityLearn (`results/live/V1_CITYLEARN.md`, `V3_CITYLEARN.md`) | energy not served and time uncomfortable in several districts | older engines' tables; not yet run on omni-v5 | run on this version, A, B and C; a district that still reads LOSS has its cause found before the table goes up |

## 6. Order

1. The runs on the current engine that answer section 3 finish and are read.
2. The version is built and tested on development seeds; the founder is told what changed before it is declared.
3. Declared, then every benchmark runs again on it, A, B and C, on GitHub and on Azure; Google, Amazon and the GPU chips
   wait for the founder's word.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
