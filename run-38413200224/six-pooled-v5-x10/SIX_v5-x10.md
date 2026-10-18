# Six organisms at 10x size, work waiting in line (25% of the run's own work at the start), up to 100 runs (pooled from 12 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Engine omni-v5, commit(s) 148565d2550d, 6fdc678adb43. Native: each organism's own controllers. Omni: the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5). Each block is the first N runs (seeds 7000 on), so 1, 10 and 100 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5400 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.139 | +0.061% | -0.061% | True |
| 2 | Physics / Robotics / Autonomous | 4040 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.113 | +0.047% | -0.047% | True |
| 3 | Energy / Facility / Industrial | 4800 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.077 | +0.000% | -0.000% | True |
| 4 | Distribution / Specialized | 4840 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.064 | +0.014% | -0.014% | True |
| 5 | The four stacked, duplicates kept | 19080 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.099 | +0.000% | -0.000% | True |
| 6 | The whole tower, every muscle once | 11070 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.033 | +0.000% | -0.000% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5400 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.141 (-0.144 to -0.138) | +0.062% (+0.061 to +0.062) | -0.062% (-0.062 to -0.061) | True |
| 2 | Physics / Robotics / Autonomous | 4040 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.114 (-0.118 to -0.110) | +0.048% (+0.047 to +0.048) | -0.048% (-0.048 to -0.047) | True |
| 3 | Energy / Facility / Industrial | 4800 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.086 (-0.092 to -0.080) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 4840 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.068 (-0.071 to -0.065) | +0.015% (+0.014 to +0.015) | -0.015% (-0.015 to -0.014) | True |
| 5 | The four stacked, duplicates kept | 19080 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.103 (-0.106 to -0.099) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 11070 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.037 (-0.040 to -0.035) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 100 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5400 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.142 (-0.142 to -0.141) | +0.062% (+0.062 to +0.062) | -0.062% (-0.062 to -0.062) | True |
| 2 | Physics / Robotics / Autonomous | 4040 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.116 (-0.117 to -0.115) | +0.048% (+0.048 to +0.048) | -0.048% (-0.048 to -0.048) | True |
| 3 | Energy / Facility / Industrial | 4800 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.085 (-0.086 to -0.083) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 4840 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.069 (-0.070 to -0.068) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 19080 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.104 (-0.104 to -0.103) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 11070 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.037 (-0.037 to -0.036) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
