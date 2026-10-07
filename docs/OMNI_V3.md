# Omni v3: the frozen engine, and every result checked against it

> © 2026 The Omni-Compass LLC. Evaluation and simulation use only. See LICENSE.

## What is frozen

Omni v3 is the engine as it stands at the commit that carries `OMNI_V3.json`. Against v2 (`docs/OMNI_V2.md`) two things
changed, both in the modelled realms and nowhere else:

- **The slack gate on speed knobs** (`realms/compass_arm.py`, `speed_slack`): on a motion axis the compass is offered the
  speed knob only where the axis at full speed is busy at most half the time (task rate × (move time + dwell) ≤ 0.5,
  from the plant's own figures, before any decision). A train on its timetable, a lift at rush hour, a robot joint at
  its takt have no slack for a slower move, and there the knob stays native, as the robot benchmark's paired physics
  trial leaves it (`docs/ROBOTICS_PREREGISTRATION.md`).
- **The marine propulsion preset** (`realms/presets.py`): twelve speed changes an hour of 200 rad instead of four of 600,
  so a one-hour run holds enough moves to count; its deadline 1,200 s.

The compass law, the live controllers, the catalog (945 muscles), every other preset and the runners are v2's byte for
byte. `OMNI_V3.json` holds one SHA-256 for each of the 40 files, plus one digest over all of them.

```
python3 tools/omni_version.py                    # this checkout: omni-v3, omni-v2, omni-v1, or every file that differs from v3
python3 tools/omni_version.py --commit <sha>     # the engine at the commit any result ran on
```

A result counts as a v3 result only if the commit it ran on carries exactly these bytes. Nothing is read across versions.

## Why there is a v3

The v2 realms table (`results/realms/REALMS.md`, three runs reproduced) put Physics and the whole tower at "energy
improvement with a service tradeoff" where v1 had every organism superior. The rows that carried it were new: three
rail traction speed muscles where Omni's slowing added 1.6 to 2.7 points of lateness on a train already near its
timetable's capacity, and two marine and two elevator speed muscles where a slower cycle finished fewer moves in the
hour. By the honesty rule the first suspect is our own wiring, and it was: the realm harness had no do-no-harm gate on
speed knobs, so it slowed an axis with no slack. The gate is an engine change, so it is a new version, declared in
`docs/REALMS_PREREGISTRATION.md` before any v3 run. The v2 table stays published as it is.

## Every result, by version

| Result | v2 | v3 |
|---|---|---|
| The muscles and six organisms, modelled | A, B, C done ([`results/realms/v2/REALMS.md`](../results/realms/v2/REALMS.md)), 0 worse, Physics and the tower a service tradeoff | **A, B, C done** (runs 37429141430, 37429151263, 37429161515; reproduced to the last digit in 3 of 3): [`results/realms/REALMS.md`](../results/realms/REALMS.md); 945 muscles, 0 worse, **every organism superior within guardrails** (work per energy +0.1% to +0.3%, work unchanged, time over the line not above native's) |
| The organisms at 1 / 10 / 100 / 1,000 copies ([`results/scale/GRID.md`](../results/scale/GRID.md)) | not run | **1, 10, 100 and 1,000 copies done, 84 of 90 cells** (runs 37430723080, 37433972731, 37501765605, 37578946088): 1,000 paired runs per organism at 1, 10 and 100 copies, 10 at 1,000 copies (1.7 million muscles for the four stacked); every organism superior within guardrails in every cell of 10 runs or more, work per energy +0.07% (Physics) to +0.37% (Energy, the four stacked, the tower), the same figure at every size, work unchanged, every knob handed back; the six cells left (100 and 1,000 runs at 1,000 copies) are beyond the machines available, as declared |
| Kubernetes: the six organisms with the real cluster inside | not run | **done at 10 and 100 copies: [`V3_SIX_KUBE.md`](../results/live/V3_SIX_KUBE.md)** (run 37501769448 on `33b15eb`, 12 cells, 5 pairs each): every cell better on 4 to 6 gauges (response time, time over the line, the organism's energy and time over its line), worse on none beyond the noise except a rounding-level work loss (6 to 11 parts in a million) in 4 cells; the stack at 100 copies ran off the clock in 4 of 5 repetitions (up to 277 s past its 1,440 s window; marked, the pairing stands); the machines stay at 6 in both arms (no autoscaler under kind); the 1,000-copy cells run on Azure (next row) |
| Kubernetes: the big organisms on Azure | not run | the stack at 1,000 copies runs detached from the GitHub job (workflow `big-organism-detached`: one rented machine runs the three repetitions on its own; the first machine stepped 1.7 million muscles in 31 s against a 12 s step and fell 4,628 s behind its window, so it was stopped and started again with a 10,800 s window, 45 s steps, about seven hours a repetition; a look every two hours collects the files when done and deletes the machine); the tower at 1,000 copies follows in the `big-organism` workflow (the v1 tower finished 3 of 3 there; the v1 stack never fit the six-hour job and runs detached too) |
| Databases: PostgreSQL behind PgBouncer, the untouched workloads on amendment 1 | the first untouched run (a loss, kept) | **A, B, C done** (runs 37435740735, 37435751322, 37435761371): [`results/live/V3_PGBENCH.md`](../results/live/V3_PGBENCH.md); connections held open confirmed better on two workloads (−61% to −72%), the runs disagree on the third; host CPU-seconds confirmed worse on all three (+14% to +28%); work and latency no difference beyond the noise |
| Robot arms, MuJoCo Menagerie | not run on v2 | **done, A/B/C: [`V3_MUJOCO.md`](../results/live/V3_MUJOCO.md)** (runs 37568387334, 37568405026, 37568422829; the three untouched robots): Gen3 moved, 7 gauges confirmed better (peak torque −29%, tracking error −21%, copper −11%, energy per takt −0.8%), 0 worse; UR5e and iiwa 14 nothing to move; the same readings as v1 (the runner is the same bytes) |
| CityLearn, every district | not run on v2 | **done, A/B/C: [`V3_CITYLEARN.md`](../results/live/V3_CITYLEARN.md)** (runs 37568381751, 37568399439, 37568416917): 11 battery districts; electricity bought, daily peak and daily unevenness confirmed better in all 11, carbon in 8; the bill worse in 7 (the 2023 districts) and ramping worse in 7, as on v1; 71 score-rows better, 33 worse, 1 where the runs differ (CityLearn's own variation); 3 districts with nothing to move; 8 CityLearn cannot run |
| Kubernetes: steady, fairness, faults (10 pairs × 3 runs) | not run on v2 | **A, B, C done**: [`V3_STEADY.md`](../results/live/V3_STEADY.md) (p95 −65% to −66%, p99 −68% to −72%, machines −1.5% to −2.9%, standby-model energy −1.3% to −2.1%, time over the line −97% to −99%, all confirmed better, failed requests 0 in both arms), [`V3_FAIRNESS.md`](../results/live/V3_FAIRNESS.md) (no difference beyond the noise on every row, the neighbour included), [`V3_FAULTS.md`](../results/live/V3_FAULTS.md) (p95 −47% to −62%, p99 −39% to −63%, time over the line −22% to −42% confirmed better; machines and energy no difference beyond the noise); the same readings as v1 (the controllers are v1's bytes) |
| Kubernetes: batch queue (10 pairs × 3 runs) | not run on v2 | **A, B, C done**: [`V3_BATCH.md`](../results/live/V3_BATCH.md) (runs 37568459663, 37573759437, 37581021752): machines −19% to −23%, machines after the queue −29% to −35%, standby-model energy −13% to −16%, mean response −10% to −14%, time over the line −2% to −4%, all confirmed better; the queue finished no difference beyond the noise in all three (on v1 it read 0.7% to 0.9% later) |
| Kubernetes: wandering, all-four (10 pairs × 3 runs) | not run on v2 | **A, B, C done**: [`V3_WANDERING.md`](../results/live/V3_WANDERING.md) (p95 −57% to −63%, p99 −40% to −51%, mean response −46% to −49%, time over the line −39% to −40%, failed requests −9% to −12%, all confirmed better; machines and energy inside the noise), [`V3_ALL_FOUR.md`](../results/live/V3_ALL_FOUR.md) (work inside the line **+35% to +49%**, p95 −61% to −66%, failed requests −11% to −14%, all confirmed better; machines and energy inside the noise). **All six Kubernetes tests are now confirmed on v3; the Omni index reads from the v3 tables: +19.7% (Kubernetes +25.5%, the database +14.2%)** |
| Power grid, pandapower and SimBench, 11 untouched grids | not run on v2 | **A, B, C done**: [`V3_PANDAPOWER.md`](../results/live/V3_PANDAPOWER.md) (runs 37568375564, 37568393269, 37568411160): the same table as v1 to the digit (the runner is v1's bytes, the simulator deterministic): with ZIP loads energy drawn and net import confirmed better in all 11 grids, losses better in 7 and worse in 4, tap operations fewer in 10 and 4 → 8 a year in one (worse, the declared cost); 67 gauge-rows better, 14 worse, 0 where the runs differ |
| Azure, the fleet that can show one machine | not run on v2 | two dispatches refused by Azure's family allowance before any arm ran (DASv4 held by the detached machine; DAv4 "remaining 0"); the survey of what holds the allowance runs first, then the fleet is dispatched again |

## How each result is confirmed

Exactly as v1 and v2: three separate GitHub runs on the same frozen bytes; every judged row reads confirmed better,
confirmed worse, no difference beyond the noise, or the runs disagree; every row is reported, losses included; the
tables are made by rule and refuse to mix engines.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
