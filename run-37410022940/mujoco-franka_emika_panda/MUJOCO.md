# Omni-Compass on top of a robot arm's own servos (MuJoCo, MuJoCo Menagerie)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the position servos the model ships with. Native: that servo tracks a pick-and-place cycle at its planned speed. Omni: the same servo and trajectory with the compass law on the speed override, inside the cycle's time line (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in both arms. Evidence class: S, our model on an independent simulator. Every row is shown, losses included.

## franka_emika_panda: 7 joints, 10 cycles per arm, planned 8 s (segment 2.0 s, the fastest the robot's own servo tracks within 0.05 rad: 0.0431), takt 12 s

The task: 4 segments between joint-space waypoints 25% of each joint's own range either side of home (at most 0.6 rad), a minimum-jerk trajectory; the same for both arms.

Paired physics trial (native mode, not counted): a cycle at full speed cost 1025.6 J, at override 0.8 1020.0 J, standing draw 60.0 W included: a slower cycle is cheaper, so omni moves the override.

Omni handed the override back at the end of every cycle: yes.

| Gauge | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 1026 | 1021 | -0.50% | better |
| copper loss per cycle (J, declared model) | 98.61 | 112.7 | +14.28% | WORSE |
| mechanical work per cycle (J) | 207 | 187.8 | -9.26% | better |
| standing draw per takt (J, declared model; the same in both arms) | 720 | 720 | +0.00% | same |
| peak joint torque (N m) | 59.48 | 53.43 | -10.18% | better |
| mean |torque| (N m) | 8.064 | 7.511 | -6.86% | better |
| cycle time (s) | 8.01 | 10.21 | +27.47% | shown |
| cycles over the time line (share) | 0 | 0 |  | same |
| tracking error, RMS (rad) | 0.04311 | 0.03408 | -20.96% | better |
| end-point error at the waypoints (rad) | 0.003741 | 0.002805 | -25.02% | better |
| speed override, mean | 1 | 0.7839 | -21.61% | shown |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
