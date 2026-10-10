# Robot arms, MuJoCo Menagerie: the A/B/C confirmation (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the position servos it ships with as native. Omni sits on top of that servo on one knob, the speed override, inside the task's takt (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in both arms, with the standing draw charged for the whole takt. Three separate GitHub runs on the same frozen engine: MuJoCo is deterministic, so a gauge reads **confirmed better** or **confirmed WORSE** when all three runs give the same sign, **same** under one part in a million, and **the runs differ** when they do not reproduce. A robot whose paired physics trial found a slower cycle no cheaper is listed as nothing for Omni to move. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Robots in the run |
|---|---|---|---|---:|
| A | 37409198316 | `8d8766648865` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 1 |
| B | 37409860065 | `a91ed072b42a` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 1 |
| C | 37410022940 | `e5a6b10020e7` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 1 |

## Robots where Omni moved the override

### franka_emika_panda: 7 joints, planned 8 s, takt 12 s, 10 cycles per arm; handed back every cycle: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 1026 | 1021 | -0.50% | -0.50% | -0.50% | **confirmed better** |
| copper loss per cycle (J, declared model) | 98.61 | 112.7 | +14.28% | +14.28% | +14.28% | **confirmed WORSE** |
| mechanical work per cycle (J) | 207 | 187.8 | -9.26% | -9.26% | -9.26% | **confirmed better** |
| standing draw per takt (J, declared model; the same in both arms) | 720 | 720 | +0.00% | +0.00% | +0.00% | same |
| peak joint torque (N m) | 59.48 | 53.43 | -10.18% | -10.18% | -10.18% | **confirmed better** |
| mean |torque| (N m) | 8.064 | 7.511 | -6.86% | -6.86% | -6.86% | **confirmed better** |
| cycle time (s) | 8.01 | 10.21 | +27.47% | +27.47% | +27.47% | shown, not judged |
| cycles over the time line (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| tracking error, RMS (rad) | 0.04311 | 0.03408 | -20.96% | -20.96% | -20.96% | **confirmed better** |
| end-point error at the waypoints (rad) | 0.003741 | 0.002805 | -25.02% | -25.02% | -25.02% | **confirmed better** |
| speed override, mean | 1 | 0.7839 | -21.61% | -21.61% | -21.61% | shown, not judged |

## Across the robots Omni moved

| Gauge | Confirmed better | Confirmed worse | Same | The runs differ |
|---|---:|---|---:|---:|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 1 | 0 | 0 | 0 |
| copper loss per cycle (J, declared model) | 0 | 1 (franka_emika_panda) | 0 | 0 |
| mechanical work per cycle (J) | 1 | 0 | 0 | 0 |
| standing draw per takt (J, declared model; the same in both arms) | 0 | 0 | 1 | 0 |
| peak joint torque (N m) | 1 | 0 | 0 | 0 |
| mean |torque| (N m) | 1 | 0 | 0 | 0 |
| cycles over the time line (share) | 0 | 0 | 1 | 0 |
| tracking error, RMS (rad) | 1 | 0 | 0 | 0 |
| end-point error at the waypoints (rad) | 1 | 0 | 0 | 0 |

## Robots where the paired trial left the override native: nothing for Omni to move

In native mode, before the counted cycles, one cycle at full speed and one at override 0.8 showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so Omni left the override at 1.0 and both arms are the same. Reproduced over A, B, C is whether the three runs agree on every gauge.

| Robot | Full-speed cycle (J, motion) | Override 0.8 cycle (J, motion) | Reproduced over A, B, C |
|---|---:|---:|---|

## Robots the task could not be run on

| Robot | The runner's reason |
|---|---|

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
