# Six organisms at 1x size, work waiting in line (25% of the run's own work at the start), up to 100 runs (pooled from 12 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Engine omni-v5, commit(s) 148565d2550d. Native: each organism's own controllers. Omni: the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5). Each block is the first N runs (seeds 7000 on), so 1, 10 and 100 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 540 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.181 | +0.032% | -0.032% | True |
| 2 | Physics / Robotics / Autonomous | 404 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.230 | +0.029% | -0.029% | True |
| 3 | Energy / Facility / Industrial | 480 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.078 | +0.000% | -0.000% | True |
| 4 | Distribution / Specialized | 484 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.106 | +0.005% | -0.005% | True |
| 5 | The four stacked, duplicates kept | 1908 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.146 | +0.000% | -0.000% | True |
| 6 | The whole tower, every muscle once | 1107 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.034 | +0.000% | -0.000% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 540 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.191 (-0.210 to -0.172) | +0.041% (+0.036 to +0.047) | -0.041% (-0.047 to -0.036) | True |
| 2 | Physics / Robotics / Autonomous | 404 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.242 (-0.272 to -0.212) | +0.029% (+0.025 to +0.032) | -0.029% (-0.032 to -0.025) | True |
| 3 | Energy / Facility / Industrial | 480 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.096 (-0.123 to -0.069) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 484 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.135 (-0.159 to -0.110) | +0.005% (+0.004 to +0.006) | -0.005% (-0.006 to -0.004) | True |
| 5 | The four stacked, duplicates kept | 1908 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.164 (-0.183 to -0.145) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 1107 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.042 (-0.053 to -0.030) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 100 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 540 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.204 (-0.209 to -0.200) | +0.045% (+0.044 to +0.046) | -0.045% (-0.046 to -0.044) | True |
| 2 | Physics / Robotics / Autonomous | 404 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.249 (-0.257 to -0.241) | +0.030% (+0.029 to +0.031) | -0.030% (-0.031 to -0.029) | True |
| 3 | Energy / Facility / Industrial | 480 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.108 (-0.114 to -0.102) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 484 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.152 (-0.161 to -0.143) | +0.006% (+0.006 to +0.007) | -0.006% (-0.007 to -0.006) | True |
| 5 | The four stacked, duplicates kept | 1908 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.176 (-0.181 to -0.171) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 1107 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.047 (-0.049 to -0.044) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
