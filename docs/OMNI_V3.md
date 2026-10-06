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
| The organisms at 1 / 10 / 100 / 1,000 copies ([`results/scale/GRID.md`](../results/scale/GRID.md)) | not run | **1 and 10 copies done** (runs 37430723080, 37433972731; 1,000 paired runs per organism each; every organism superior within guardrails at 10, 100 and 1,000 runs); 100 copies running (37501765605); 1,000 to follow |
| Kubernetes: the six organisms with the real cluster inside | not run | running at 10 and 100 copies (37501769448); 1,000 copies of the stack does not fit a six-hour GitHub job (the v1 run showed it) and waits for a detached run |
| Kubernetes: the big organisms on Azure | not run | the stack at 1,000 copies runs detached from the GitHub job (workflow `big-organism-detached`: one rented machine runs the three repetitions on its own, about eight hours each; a look every two hours collects the files when done and deletes the machine); the tower at 1,000 copies follows in the `big-organism` workflow (the v1 tower finished 3 of 3 there; the v1 stack never fit the six-hour job and runs detached too) |
| Databases: PostgreSQL behind PgBouncer, the untouched workloads on amendment 1 | the first untouched run (a loss, kept) | **A, B, C done** (runs 37435740735, 37435751322, 37435761371): [`results/live/V3_PGBENCH.md`](../results/live/V3_PGBENCH.md); connections held open confirmed better on two workloads (−61% to −72%), the runs disagree on the third; host CPU-seconds confirmed worse on all three (+14% to +28%); work and latency no difference beyond the noise |
| Kubernetes alone, Azure alone, CityLearn, the grid, the robots | not run on v2 | the controllers and runners are v1's byte for byte; run again as the queue allows |

## How each result is confirmed

Exactly as v1 and v2: three separate GitHub runs on the same frozen bytes; every judged row reads confirmed better,
confirmed worse, no difference beyond the noise, or the runs disagree; every row is reported, losses included; the
tables are made by rule and refuse to mix engines.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone.
