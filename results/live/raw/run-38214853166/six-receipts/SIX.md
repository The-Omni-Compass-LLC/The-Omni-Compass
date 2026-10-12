# Six organisms at 1x size, work waiting in line (25% of the run's own work at the start), up to 1000 runs (pooled from 60 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit(s) e29133537123. Native: each organism's own controllers. Omni: the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5). Each block is the first N runs (seeds 7000 on), so 1, 10, 100 and 1,000 are nested. Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 530 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.052 | +0.068% | -0.068% | True |
| 2 | Physics / Robotics / Autonomous | 394 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.047 | +0.053% | -0.053% | True |
| 3 | Energy / Facility / Industrial | 470 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.003 | +0.000% | -0.000% | True |
| 4 | Distribution / Specialized | 474 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.043 | +0.015% | -0.015% | True |
| 5 | The four stacked, duplicates kept | 1868 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.036 | +0.000% | -0.000% | True |
| 6 | The whole tower, every muscle once | 1097 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.001 | +0.000% | -0.000% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 530 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.053 (-0.055 to -0.052) | +0.068% (+0.068 to +0.068) | -0.068% (-0.068 to -0.068) | True |
| 2 | Physics / Robotics / Autonomous | 394 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.056 (-0.063 to -0.049) | +0.053% (+0.053 to +0.053) | -0.053% (-0.053 to -0.053) | True |
| 3 | Energy / Facility / Industrial | 470 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.008 (-0.014 to -0.002) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 474 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.045 (-0.050 to -0.041) | +0.015% (+0.015 to +0.016) | -0.015% (-0.016 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 1868 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.044 to -0.037) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 1097 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.003 (-0.006 to -0.001) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 100 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 530 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.053 (-0.053 to -0.052) | +0.068% (+0.068 to +0.068) | -0.068% (-0.068 to -0.068) | True |
| 2 | Physics / Robotics / Autonomous | 394 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.058 (-0.059 to -0.056) | +0.053% (+0.053 to +0.053) | -0.053% (-0.053 to -0.053) | True |
| 3 | Energy / Facility / Industrial | 470 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.010 (-0.012 to -0.009) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 474 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.046 (-0.047 to -0.045) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 1868 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.042 to -0.041) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 1097 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.005 (-0.005 to -0.004) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 1000 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 530 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.053 (-0.053 to -0.052) | +0.068% (+0.068 to +0.068) | -0.068% (-0.068 to -0.068) | True |
| 2 | Physics / Robotics / Autonomous | 394 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.056 (-0.057 to -0.056) | +0.053% (+0.053 to +0.053) | -0.053% (-0.053 to -0.053) | True |
| 3 | Energy / Facility / Industrial | 470 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.010 (-0.011 to -0.010) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 474 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.046 (-0.046 to -0.046) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 1868 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.041 to -0.041) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 1097 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.004 (-0.005 to -0.004) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
