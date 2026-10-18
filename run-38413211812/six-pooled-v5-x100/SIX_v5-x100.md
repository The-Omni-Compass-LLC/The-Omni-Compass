# Six organisms at 100x size, work waiting in line (25% of the run's own work at the start), up to 100 runs (pooled from 23 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Engine omni-v5, commit(s) 148565d2550d, 57115a31c11d. Native: each organism's own controllers. Omni: the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5). Each block is the first N runs (seeds 7000 on), so 1, 10 and 100 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 54000 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.135 | +0.065% | -0.065% | True |
| 2 | Physics / Robotics / Autonomous | 40400 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.107 | +0.051% | -0.051% | True |
| 3 | Energy / Facility / Industrial | 48000 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.087 | +0.000% | -0.000% | True |
| 4 | Distribution / Specialized | 48400 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.058 | +0.015% | -0.015% | True |
| 5 | The four stacked, duplicates kept | 190800 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.098 | +0.000% | -0.000% | True |
| 6 | The whole tower, every muscle once | 110700 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.038 | +0.000% | -0.000% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 54000 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.135 (-0.135 to -0.134) | +0.065% (+0.065 to +0.065) | -0.065% (-0.065 to -0.065) | True |
| 2 | Physics / Robotics / Autonomous | 40400 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.107 (-0.108 to -0.106) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |
| 3 | Energy / Facility / Industrial | 48000 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.086 (-0.088 to -0.084) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 48400 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.059 (-0.059 to -0.058) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 190800 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.097 (-0.098 to -0.097) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 110700 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.037 (-0.038 to -0.037) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 100 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 54000 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.135 (-0.135 to -0.135) | +0.065% (+0.065 to +0.065) | -0.065% (-0.065 to -0.065) | True |
| 2 | Physics / Robotics / Autonomous | 40400 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.107 (-0.107 to -0.107) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |
| 3 | Energy / Facility / Industrial | 48000 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.085 (-0.085 to -0.085) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 48400 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.059 (-0.059 to -0.059) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 190800 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.097 (-0.097 to -0.097) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 110700 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.037 (-0.037 to -0.037) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
