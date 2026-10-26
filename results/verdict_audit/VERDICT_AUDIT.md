# The verdict audit: every row recomputed from its stored values, every count from one selection

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Written by `tools/verdict_audit.py` from the three-run tables as they stand (digest `365e2448ee446c5c`). The engine that stands is omni-v20. The rule: tools/readings.py three_run_reading: a change of 0.5% or more, the mean of the three runs' changes in percent of native, reads by the gauge's aim; under it STEADY, under the floor; every run's two values equal to 1e-09 of the value, STEADY, the same; runs that moved 0.5% or more in opposite directions, the runs disagree. Evidence strength is shown beside the word and never changes it: strong, every run the mean's way and beyond its noise (its 95% interval clear of zero); moderate, all but one; weak, one run beyond its noise; inconclusive, no run beyond its noise (a mean of 0.5% or more, not a change any one run could tell from its noise). STEADY is of three kinds: exactly the same (every run's values equal to nine decimal places), under the floor (a measured change, the three runs' mean under 0.5%) and no difference beyond the noise (a table read by an older key). The runs disagree is unresolved, never a final word: opposite directions each beyond its noise, or opposite directions inside overlapping noise.

## The counts

| What | Count |
|---|---|
| Three-run tables | 205: 85 standing, 59 superseded, 60 the road, 1 taken out |
| Standing tables, Omni-Compass against its native | 55 |
| Standing tables on the engine that stands (omni-v20) | 0 |
| Standing tables not yet run again on omni-v20 | 85 |
| Rows recomputed from their stored values | 6460 of 8940 |
| Stored readings the key reads otherwise | 0 |
| Markdown readings unlike their JSON twin | 0 |

### Standing tables: Omni-Compass against its native (the readings do no harm is judged by)

Every word: 412 GAIN, 116 power given, 555 STEADY, 164 LOSS, 286 the runs disagree, 9 the runs differ, 478 shown, 164 tuning. The four categories are exclusive: each row has one word.

| Engine | Words |
|---|---|
| omni-v17 | 28 GAIN, 7 power given, 37 STEADY, 9 LOSS, 47 the runs disagree, 22 shown, 27 tuning |
| omni-v16 | 63 GAIN, 47 power given, 162 STEADY, 28 LOSS, 112 the runs disagree, 62 shown, 126 tuning |
| omni-v12 | 139 GAIN, 31 power given, 136 STEADY, 113 LOSS, 96 the runs disagree, 216 shown |
| omni-v11 | 131 GAIN, 21 power given, 172 STEADY, 6 LOSS, 13 the runs disagree, 9 the runs differ, 106 shown, 11 tuning |
| omni-v10 | 51 GAIN, 10 power given, 48 STEADY, 8 LOSS, 18 the runs disagree, 72 shown |

| Evidence class | Words |
|---|---|
| L (the real software) | 315 GAIN, 106 power given, 409 STEADY, 164 LOSS, 286 the runs disagree, 424 shown, 153 tuning |
| S (an outside simulator driven by our own runner) | 97 GAIN, 10 power given, 146 STEADY, 9 the runs differ, 54 shown, 11 tuning |

Useful work, time waited and resources apart (item 8 of the work order): a resource spent or held that rose is power given, shown beside what it bought, never a gain in work.

| The gauge's direction | Words |
|---|---|
| a count that must never rise | 6 GAIN, 73 STEADY, 14 tuning |
| resource spent or held | 240 GAIN, 116 power given, 206 STEADY, 105 the runs disagree, 57 tuning |
| shown | 7 the runs differ, 478 shown, 25 tuning |
| time waited, missed or failed | 150 GAIN, 184 STEADY, 157 LOSS, 173 the runs disagree, 2 the runs differ, 39 tuning |
| work done | 16 GAIN, 92 STEADY, 7 LOSS, 8 the runs disagree, 29 tuning |

Evidence strength beside the word (it never changes the word):

| Word | Strength |
|---|---|
| GAIN | 141 strong, 91 inconclusive, 88 deterministic, reproduced in all three runs, 48 weak, 35 moderate, 9 not recomputable from runs |
| LOSS | 94 inconclusive, 40 weak, 23 moderate, 7 strong |
| power given | 39 inconclusive, 27 weak, 23 strong, 17 moderate, 10 deterministic, reproduced in all three runs |

| STEADY of each kind | 315 exactly the same, 240 under the floor |
|---|---|
| The runs disagree, by cause | 285 opposite directions inside overlapping noise, 1 opposite directions, each beyond its noise |

### Every comparison and status

| Status, comparison | Words |
|---|---|
| standing | against its native | 412 GAIN, 116 power given, 555 STEADY, 164 LOSS, 286 the runs disagree, 9 the runs differ, 478 shown, 164 tuning |
| standing | in place of a controller | 109 GAIN, 9 power given, 44 STEADY, 27 LOSS, 24 the runs disagree, 90 shown |
| standing | the orchestrator's own | 31 GAIN, 12 power given, 78 STEADY, 66 LOSS, 26 the runs disagree, 90 shown |
| standing | two changes at once | 57 GAIN, 22 power given, 42 STEADY, 78 LOSS, 14 the runs disagree, 90 shown |
| superseded | against its native | 528 GAIN, 206 power given, 906 STEADY, 114 LOSS, 547 the runs disagree, 10 the runs differ, 399 shown, 556 tuning |
| taken out | against its native | 9 GAIN, 3 power given |
| the road | against its native | 590 GAIN, 114 power given, 949 STEADY, 55 LOSS, 133 the runs disagree, 17 the runs differ, 519 shown, 192 tuning |

The orchestrator's own rows (ORCH) carry no Omni-Compass in either arm; two changes at once (BOTH) and in place of a controller (VS) are shown, never a reading of Omni-Compass against its native.

## Every LOSS row of Omni-Compass against its native (164)

| Table | Engine | Class | Gauge | Native → Omni-Compass, raw change, each run | Evidence |
|---|---|---|---|---|---|
| `results/live/V10_BATCH.md` | omni-v10 | L | pod start wait, total (s) | 3.3 → 8 (+142.4%); 18.0; 0.1 → 0.1 (±0.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V10_BATCH.md` | omni-v10 | L | pod start wait, mean (s) | 3.3 → 4.2 (+27.3%); 13.1; 0.1 → 0.1 (±0.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V10_BATCH.md` | omni-v10 | L | batch: queue finished (s) | 582.1 → 585.3 (+0.5%); 625.6 → 631.4 (+0.9%); 592.9 → 597.6 (+0.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V10_CRUISEKUBE.md` | omni-v10 | L | response time (ms), mean | 84.66 → 85.86 (+1.4%); 73.3 → 73.97 (+0.9%); 85.71 → 86.91 (+1.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V10_CRUISEKUBE.md` | omni-v10 | L | response time (ms), 95th percentile | 129.8 → 131.8 (+1.5%); 108.6 → 111.9 (+3.0%); 132.7 → 133.5 (+0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V10_CRUISEKUBE.md` | omni-v10 | L | response time (ms), 99th percentile | 146.9 → 148.8 (+1.3%); 122.6 → 126.3 (+3.1%); 152.8 → 156.9 (+2.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V10_TRACE_GOOGLE2011.md` | omni-v10 | L | pod start wait, total (s) | 21.3 → 37.5 (+76.1%); 16 → 34.6 (+116.3%); 22.4 → 32.5 (+45.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V10_WANDERING.md` | omni-v10 | L | pod start wait, total (s) | 11.9 → 15.8 (+32.8%); 11.1 → 11.6 (+4.5%); 17.7 → 20.3 (+14.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_CAPACITY.md` | omni-v11 | L | 1000:work | 3399 → 3168 (−6.8%); 4693 → 4618 (−1.6%); 4006 → 3927 (−2.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_CAPACITY.md` | omni-v11 | L | 2000:capacity | 16.4 → 16.4 (±0.0%); 10 → 10 (±0.0%); 12.4 → 11.6 (−6.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_CAPACITY.md` | omni-v11 | L | 3000:work | 1.21e+04 → 1.19e+04 (−1.7%); 1.22e+04 → 1.216e+04 (−0.3%); 1.233e+04 → 1.216e+04 (−1.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_CAPACITY.md` | omni-v11 | L | 3000:capacity | 14.8 → 14.4 (−2.7%); 14.8 → 14 (−5.4%); 15.2 → 14.8 (−2.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_KEDA_REQUESTS.md` | omni-v11 | L | failed requests (%) | 0.011976047904191617; 0.0; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V11_ROBUST_LONG.md` | omni-v11 | L | pod start wait, total (s) | 7.333 → 27 (+268.2%); 9.333 → 22 (+135.7%); 7 → 16.67 (+138.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 2452 → 2510 (+2.4%); 2697 → 2871 (+6.5%); 1422 → 1533 (+7.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 3425 → 3535 (+3.2%); 3778 → 4014 (+6.3%); 1972 → 2162 (+9.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | failed requests (%) | 0.006817 → 0.007637 (+12.0%); 0.0; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 → 12.33 (+2.8%); 13 → 14 (+7.7%); 6.8 → 8.2 (+20.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 0.4444 → 1 (+125.0%); 0.3 → 2.3 (+666.7%); 0.3 → 1 (+233.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | pod start wait, mean (s) | 0.2222 → 0.8333 (+275.0%); 0.3 → 1.083 (+261.1%); 0.15 → 0.65 (+333.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | batch: queue finished (s) | 872.8 → 885.1 (+1.4%); 892.4 → 912.5 (+2.3%); 806 → 818.8 (+1.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 184.4 → 193.8 (+5.1%); 203.2 → 221.3 (+8.9%); 115.3 → 125.8 (+9.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_ARMADA_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 0.4444 → 2.222 (+400.0%); 2.3; 1.5 → 1.6 (+6.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | response time (ms), 99th percentile | 427.2 → 439.5 (+2.9%); 415.6 → 425.7 (+2.4%); 419.3 → 430.5 (+2.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | time over the response line (% of samples) | 0.7443 → 1.042 (+40.0%); 0.5461 → 0.6976 (+27.7%); 0.7367 → 0.8459 (+14.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 → 2.1 (+75.0%); 0.9 → 1.3 (+44.4%); 1.7 → 1.7 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | pod start wait, total (s) | 0.1 → 0.6 (+500.0%); 0.2 → 1 (+400.0%); 0.1 → 0.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | pod start wait, mean (s) | 0.1 → 0.5 (+400.0%); 0.2 → 0.75 (+275.0%); 0.1 → 0.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 → 0.1 (±0.0%); 0.2 → 0.2 (±0.0%); 0.1 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 26.6 → 26.97 (+1.4%); 26.39 → 26.66 (+1.0%); 26.58 → 26.89 (+1.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 1397 → 1463 (+4.7%); 866.2 → 923.9 (+6.7%); 827.2 → 872.2 (+5.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 2014 → 2059 (+2.3%); 1230 → 1274 (+3.5%); 1250 → 1246 (−0.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 → 10.9 (+0.9%); 6.9 → 7.7 (+11.6%); 8.3 → 8.6 (+3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 102.4 → 106.9 (+4.4%); 63.56 → 65.83 (+3.6%); 58.77 → 61.3 (+4.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 0.5 → 0.9 (+80.0%); 0.5 → 1 (+100.0%); 0.6 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 0.25 → 0.9 (+260.0%); 0.4 → 0.65 (+62.5%); 0.6 | weak; 1 of 3 beyond the noise |
| `results/live/V12_BINPACK_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 106.1 → 108.4 (+2.2%); 63.75 → 65.27 (+2.4%); 58.35 → 61.38 (+5.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_CRANE_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 6.8 → 10.9 (+60.3%); 8 → 10.3 (+28.7%); 7.1 → 12 (+69.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_CRANE_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 6.8 → 12.3 (+80.9%); 6.6 → 13.5 (+104.5%); 7.9 → 12.2 (+54.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_CRANE_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 1.492 → 1.62 (+8.6%); 1.325 → 1.607 (+21.3%); 1.58 → 1.594 (+0.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KAI.md` | omni-v12 | L | response time (ms), 99th percentile | 484.3 → 487.6 (+0.7%); 519.6 → 569.8 (+9.7%); 565.6 → 598.1 (+5.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI.md` | omni-v12 | L | time over the response line (% of samples) | 1.003 → 1.091 (+8.8%); 1.527 → 2.172 (+42.3%); 2.335 → 2.487 (+6.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.4 → 1.8 (+28.6%); 1.8 → 2.9 (+61.1%); 3.5 → 3.5 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 → 1 (±0.0%); 1 → 1 (±0.0%); 1 → 1.2 (+20.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 29.85 → 30.29 (+1.5%); 30.8 → 32.45 (+5.3%); 32.25 → 32.97 (+2.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KAI_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 1070 → 1095 (+2.3%); 1366 → 1450 (+6.2%); 1135 → 1150 (+1.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI_4W_BARE.md` | omni-v12 | L | batch: queue finished (s) | 771.5 → 775.5 (+0.5%); 790 → 797.8 (+1.0%); 772.7 → 773.3 (+0.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KAI_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 78.3 → 81.36 (+3.9%); 98.16 → 106.2 (+8.2%); 82.27 → 82.29 (+0.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | response time (ms), 95th percentile | 1478 → 1519 (+2.8%); 1927 → 1992 (+3.4%); 1712 → 1788 (+4.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | response time (ms), 99th percentile | 2206 → 2288 (+3.7%); 2841 → 2937 (+3.4%); 2761 → 2775 (+0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 0.15 → 0.8 (+433.3%); 0.15 → 0.4 (+166.7%); 0.4 → 0.5 (+25.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 804.2 → 810.9 (+0.8%); 835 → 844.2 (+1.1%); 807.9 → 812.4 (+0.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 → 2.6 (+62.5%); 2.6 → 3 (+15.4%); 1.4 → 1.6 (+14.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 109.7 → 115.9 (+5.6%); 139.5 → 148.6 (+6.5%); 119.4 → 125.4 (+5.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 2164 → 2439 (+12.7%); 2260 → 2366 (+4.6%); 2707 → 2815 (+4.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 3077 → 3538 (+15.0%); 3117 → 3349 (+7.4%); 3712 → 3925 (+5.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.33 → 13 (+14.7%); 11.3 → 12.3 (+8.8%); 10.4 → 10.9 (+4.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 0.5556 → 2.222 (+300.0%); 1.2; 1.9 | weak; 1 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | pod start wait, mean (s) | 0.5556 → 1.389 (+150.0%); 0.95; 1.25 | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | batch: queue finished (s) | 852.7 → 875.9 (+2.7%); 856.4 → 866.9 (+1.2%); 909.9 → 928.2 (+2.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.07407 → 0.1019 (+37.5%); 0.1042 → 0.1083 (+4.0%); 0.0875 → 0.1 (+14.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 → 0.6667 (+20.0%); 0.6 → 0.8 (+33.3%); 0.5 → 0.5 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 163.2 → 182 (+11.6%); 167.6 → 171.2 (+2.2%); 216.2 → 228.7 (+5.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | response time (ms), mean | 709.8 → 808.5 (+13.9%); 691.8 → 764.6 (+10.5%); 844.3 → 867.4 (+2.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | response time (ms), 95th percentile | 3269 → 3923 (+20.0%); 3140 → 3665 (+16.7%); 3666 → 3759 (+2.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | response time (ms), 99th percentile | 4767 → 5337 (+12.0%); 4602 → 5114 (+11.1%); 4876 → 5069 (+4.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | time over the response line (% of samples) | 24.64 → 25.85 (+4.9%); 23.99 → 25.28 (+5.4%); 25.85 → 28 (+8.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | failed requests (%) | 0.08233 → 0.159 (+93.2%); 0.0524 → 0.1452 (+177.2%); 0.06374 → 0.1831 (+187.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 1.111 → 3.889 (+250.0%); 1.1 → 1.9 (+72.7%); 1.1 → 2.2 (+100.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 0.8333 → 1.101 (+32.1%); 0.65 → 1.033 (+59.0%); 0.85 → 1.225 (+44.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 952.2 → 993.1 (+4.3%); 952.2 → 991 (+4.1%); 1010 → 1040 (+3.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 258.1 → 298.7 (+15.7%); 261.5 → 298.5 (+14.2%); 311.6 → 341.4 (+9.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR.md` | omni-v12 | L | pod start wait, total (s) | 0.2 → 0.8 (+300.0%); 0.2 → 0.8 (+300.0%); 0.2 → 0.9 (+350.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR.md` | omni-v12 | L | pod start wait, mean (s) | 0.2 → 0.6 (+200.0%); 0.2 → 0.8 (+300.0%); 0.2 → 0.65 (+225.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 536.2 → 567.1 (+5.8%); 1283 → 1372 (+6.9%); 863.2 → 913.5 (+5.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 767.9 → 818.7 (+6.6%); 1874 → 2010 (+7.3%); 1252 → 1296 (+3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 38.07 → 40.1 (+5.3%); 85.79 → 89.12 (+3.9%); 55.45 → 59.44 (+7.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.0; 0.1 → 0.2 (+100.0%); 0.1 → 0.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 1290 → 1313 (+1.8%); 1421 → 1421 (−0.0%); 1396 → 1421 (+1.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 614 → 650.2 (+5.9%); 799.3 → 814.5 (+1.9%); 763.3 → 789 (+3.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 1132 → 1204 (+6.3%); 1090 → 1166 (+7.0%); 1496 → 1547 (+3.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 1583 → 1738 (+9.8%); 1617 → 1688 (+4.4%); 2030 → 2294 (+13.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 0.5555555555555556; 0.5; 0.6 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | pod start wait, mean (s) | 0.5555555555555556; 0.35; 0.6 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | batch: queue finished (s) | 774.1 → 780.1 (+0.8%); 775.3 → 780.5 (+0.7%); 802.6 → 807.7 (+0.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.03241 → 0.05093 (+57.1%); 0.04167 → 0.09167 (+120.0%); 0.05417 → 0.09583 (+76.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 → 0.3333 (+200.0%); 0.4 → 0.4 (±0.0%); 0.4 → 0.6 (+50.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 81.79 → 87.35 (+6.8%); 83.3 → 87.46 (+5.0%); 107.6 → 114.2 (+6.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_TOP.md` | omni-v12 | L | response time (ms), 95th percentile | 1305 → 1356 (+3.9%); 1271 → 1343 (+5.6%); 1432 → 1440 (+0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUBERAY_4W_TOP.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, mean (s) | 635 → 637.5 (+0.4%); 533.6 → 536.6 (+0.6%); 670.7 → 677.6 (+1.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 1006 → 1044 (+3.8%); 1151 → 1169 (+1.6%); 1278 → 1334 (+4.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 0.0; 0.3; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | L | pod start wait, mean (s) | 0.0; 0.3; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 73.89 → 79.93 (+8.2%); 81.23 → 83.89 (+3.3%); 87.61 → 92.22 (+5.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | L | failed requests (%) | 0.0; 0.009302325581395349; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 → 8 (+2.6%); 10.3 → 10.6 (+2.9%); 11.11 → 11.33 (+2.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1625 → 0.1667 (+2.6%); 0.2 → 0.2 (−0.0%); 0.2361 → 0.2361 (−0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 82.38 → 83.16 (+0.9%); 88.75 → 92.45 (+4.2%); 98.69 → 102.1 (+3.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 2969 → 3098 (+4.3%); 2682 → 2784 (+3.8%); 2493 → 2538 (+1.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 4041 → 4247 (+5.1%); 3704 → 3891 (+5.1%); 3409 → 3512 (+3.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.9 → 15.3 (+2.7%); 12.4 → 12.7 (+2.4%); 10.1 → 11.2 (+10.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | pod start wait, total (s) | 0.8 → 1.7 (+112.5%); 0.2 → 2.4 (+1100.0%); 0.6 → 1.3 (+116.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | pod start wait, mean (s) | 0.55 → 1.1 (+100.0%); 0.2 → 1.25 (+525.0%); 0.4 → 0.8 (+100.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | batch: queue finished (s) | 911.9 → 932.9 (+2.3%); 885.4 → 898.2 (+1.4%); 881.5 → 890.5 (+1.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 222.3 → 236.9 (+6.5%); 194.8 → 204.3 (+4.9%); 190.6 → 195 (+2.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | response time (ms), 95th percentile | 4119 → 4499 (+9.2%); 4095 → 4162 (+1.6%); 2738 → 3866 (+41.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | response time (ms), 99th percentile | 5429 → 6036 (+11.2%); 5491 → 5867 (+6.9%); 3776 → 5213 (+38.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | failed requests (%) | 0.3539 → 0.4937 (+39.5%); 0.05059 → 0.1132 (+123.7%); 0.01653 → 0.05082 (+207.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 → 18.6 (+5.7%); 14.8 → 15.7 (+6.1%); 12.1 → 17.6 (+45.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 0.3 → 2.9 (+866.7%); 2.9; 5.0 | moderate; 2 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 0.3 → 1.55 (+416.7%); 1.6166666666666665; 2.466666666666667 | moderate; 2 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 1049 → 1107 (+5.5%); 1026 → 1058 (+3.0%); 1023 → 1050 (+2.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, mean (s) | 7.229 → 22.47 (+210.8%); 6.929 → 18.62 (+168.7%); 3.13 → 14.34 (+358.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 39.4 → 159.5 (+304.8%); 55.9 → 105.6 (+88.9%); 6.333 → 94.33 (+1389.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 328.8 → 380 (+15.6%); 305.8 → 326.8 (+6.9%); 258.9 → 309.6 (+19.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_VANILLA.md` | omni-v12 | L | response time (ms), 95th percentile | 523.3 → 522.3 (−0.2%); 417.2 → 455 (+9.1%); 469.7 → 494.8 (+5.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_VANILLA.md` | omni-v12 | L | response time (ms), 99th percentile | 672.1 → 678.9 (+1.0%); 553.2 → 584.8 (+5.7%); 621.8 → 650.1 (+4.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_VANILLA.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 → 9.7 (±0.0%); 4.5 → 5.8 (+28.9%); 6.8 → 8.3 (+22.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_VANILLA.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 28.22 → 28.48 (+0.9%); 25.72 → 25.95 (+0.9%); 27.32 → 27.65 (+1.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 926.1 → 996.5 (+7.6%); 1133 → 1167 (+2.9%); 1065 → 1145 (+7.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 1337 → 1467 (+9.7%); 1627 → 1620 (−0.4%); 1483 → 1638 (+10.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 → 0.3 (±0.0%); 0.4 → 0.5 (+25.0%); 0.2 → 0.5 (+150.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 65.63 → 70.4 (+7.3%); 85.9 → 87.21 (+1.5%); 75.65 → 82.43 (+9.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | L | response time (ms), 95th percentile | 517.4 → 518.9 (+0.3%); 884.6 → 1003 (+13.4%); 758.9 → 839.4 (+10.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | L | pod start wait, total (s) | 0.2 → 0.4 (+100.0%); 0.1 → 1.4 (+1300.0%); 1.2 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | L | pod start wait, mean (s) | 0.2 → 0.4 (+100.0%); 0.1 → 0.7 (+600.0%); 1.2 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 81.51 → 86.72 (+6.4%); 101 → 102.8 (+1.8%); 93.17 → 95.34 (+2.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V16_KAFKA.md` | omni-v16 | L | burst: p99_ms | 3838 → 3843 (+0.1%); 3646 → 3642 (−0.1%); 3859 → 3934 (+1.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_KAFKA.md` | omni-v16 | L | burst: lag_max | 1644 → 1681 (+2.2%); 1627 → 1647 (+1.2%); 1725 → 1734 (+0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_KAFKA.md` | omni-v16 | L | heavy: mean_ms | 325 → 334.4 (+2.9%); 321.9 → 322.9 (+0.3%); 327.7 → 337.4 (+3.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_KAFKA.md` | omni-v16 | L | heavy: lag_max | 693.3 → 709.3 (+2.3%); 690.3 → 698.3 (+1.2%); 684 → 699.7 (+2.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_KAFKA.md` | omni-v16 | L | heavy: lag_mean | 59.78 → 61.32 (+2.6%); 58.8 → 59.57 (+1.3%); 59.83 → 62.01 (+3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_KAFKA_SERVICE.md` | omni-v16 | L | burst: mean_ms | 376.4 → 380.1 (+1.0%); 386.6 → 388.9 (+0.6%); 365.3 → 368.2 (+0.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_PGBENCH.md` | omni-v16 | L | select: p50_ms | 0.1593 → 0.1603 (+0.6%); 0.36 → 0.3643 (+1.2%); 0.2757 → 0.2757 (±0.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V16_PGBENCH.md` | omni-v16 | L | tpcb_hot: work_inside_line_tps | 1324 → 1237 (−6.5%); 747.3 → 737.7 (−1.3%); 818.8 → 817.8 (−0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_PGBENCH.md` | omni-v16 | L | tpcb_hot: p95_ms | 56.55 → 299.9 (+430.3%); 622.3 → 1091 (+75.3%); 6.154 → 6.142 (−0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_REDIS_SERVICE.md` | omni-v16 | L | small: p99_ms | 5.327 → 5.446 (+2.2%); 5.756 → 5.766 (+0.2%); 5.696 → 5.701 (+0.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V16_REDIS_SHIPPED.md` | omni-v16 | L | large: p95_ms | 0.165 → 0.1673 (+1.4%); 0.2303 → 0.2341 (+1.7%); 0.1129 → 0.1142 (+1.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_SYSBENCH.md` | omni-v16 | L | read_write: work_inside_line_tps | 157.3 → 148.3 (−5.7%); 191.6 → 191.6 (+0.0%); 197.2 → 196.7 (−0.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V16_SYSBENCH.md` | omni-v16 | L | read_write: mean_ms | 20.1 → 25.82 (+28.5%); 5.368 → 5.361 (−0.1%); 2.578 → 2.756 (+6.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V16_SYSBENCH_SHIPPED.md` | omni-v16 | L | read_only: mean_ms | 3.01 → 3.056 (+1.5%); 1.275 → 1.283 (+0.6%); 2.771 → 2.766 (−0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | b: p95_ms | 0.3497 → 0.361 (+3.2%); 0.3377 → 0.3463 (+2.6%); 0.1577 → 0.1663 (+5.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | b: p99_ms | 0.5383 → 0.5543 (+3.0%); 0.5873 → 0.5887 (+0.2%); 0.3453 → 0.3527 (+2.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | b: mean_ms | 0.201 → 0.2051 (+2.1%); 0.2005 → 0.2009 (+0.2%); 0.06931 → 0.07076 (+2.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | burst: p99_ms | 0.502 → 0.5003 (−0.3%); 0.49 → 0.4973 (+1.5%); 0.6837 → 0.6897 (+0.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | c: p95_ms | 0.2803 → 0.2797 (−0.2%); 0.1893 → 0.1887 (−0.4%); 0.086 → 0.093 (+8.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | c: p99_ms | 0.4463 → 0.4447 (−0.4%); 0.36 → 0.365 (+1.4%); 0.2817 → 0.286 (+1.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | c: mean_ms | 0.1471 → 0.1487 (+1.1%); 0.1417 → 0.1468 (+3.6%); 0.05555 → 0.05942 (+7.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB.md` | omni-v16 | L | f: p95_ms | 0.318 → 0.319 (+0.3%); 0.3547 → 0.353 (−0.5%); 0.1673 → 0.1867 (+11.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | burst: p95_ms | 0.468 → 0.4737 (+1.2%); 0.2473 → 0.2563 (+3.6%); 0.2283 → 0.2303 (+0.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | burst: p99_ms | 0.644 → 0.6537 (+1.5%); 0.3797 → 0.3993 (+5.2%); 0.3547 → 0.355 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | burst: mean_ms | 0.215 → 0.2166 (+0.8%); 0.0753 → 0.07704 (+2.3%); 0.06965 → 0.06964 (−0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | c: p95_ms | 0.092 → 0.09233 (+0.4%); 0.2027 → 0.206 (+1.6%); 0.175 → 0.175 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | c: p99_ms | 0.3007 → 0.315 (+4.8%); 0.3803 → 0.3803 (±0.0%); 0.3513 → 0.356 (+1.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | L | c: mean_ms | 0.05656 → 0.05705 (+0.9%); 0.1482 → 0.152 (+2.5%); 0.1253 → 0.1255 (+0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_PGBENCH_SERVICE.md` | omni-v17 | L | simple_update: p50_ms | 1.518 → 1.522 (+0.3%); 1.397 → 1.917 (+37.2%); 1.634 → 30.65 (+1776.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_PGBENCH_SERVICE.md` | omni-v17 | L | tpcb_hot: work_inside_line_tps | 1007 → 1007 (−0.0%); 839.7 → 839.9 (+0.0%); 554.8 → 536.1 (−3.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | b: p95_ms | 0.149 → 0.166 (+11.4%); 0.3417 → 0.351 (+2.7%); 0.3107 → 0.3147 (+1.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | b: p99_ms | 0.354 → 0.364 (+2.8%); 0.527 → 0.5417 (+2.8%); 0.469 → 0.4697 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | b: mean_ms | 0.06809 → 0.06967 (+2.3%); 0.1989 → 0.2021 (+1.6%); 0.1907 → 0.1915 (+0.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | burst: p95_ms | 0.5033 → 0.5067 (+0.7%); 0.4557 → 0.4597 (+0.9%); 0.4003 → 0.4007 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | burst: mean_ms | 0.2228 → 0.2244 (+0.7%); 0.2162 → 0.2194 (+1.5%); 0.2089 → 0.2104 (+0.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | c: p95_ms | 0.3017 → 0.3057 (+1.3%); 0.3107 → 0.3137 (+1.0%); 0.31 → 0.3163 (+2.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | L | c: mean_ms | 0.1898 → 0.189 (−0.5%); 0.1915 → 0.1935 (+1.0%); 0.192 → 0.196 (+2.1%) | inconclusive; 0 of 3 beyond the noise |

## Stored readings the key reads otherwise (0)

None: every stored reading is the key's reading of its stored values, and every Markdown table prints its JSON's.

## Every table

| Table | Engine | Status | Comparison | Class | Runs |
|---|---|---|---|---|---|
| `results/live/V10_ALL_FOUR.md` | omni-v10 | standing | against its native | L | A 39107187219 (10 reps, `6d871e2baad1`), B 39114214725 (10 reps, `3b9fc76017ad`), C 39122525181 (10 reps, `faaaff3142e1`) |
| `results/live/V10_BATCH.md` | omni-v10 | standing | against its native | L | A 39107196814 (10 reps, `6d871e2baad1`), B 39115235566 (10 reps, `f09db2756842`), C 39122536157 (10 reps, `faaaff3142e1`) |
| `results/live/V10_CAPACITY.md` | omni-v10 | superseded | against its native | L | in its own Markdown |
| `results/live/V10_CITYLEARN.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_CRUISEKUBE.md` | omni-v10 | standing | against its native | L | A 39102512170 (10 reps, `959cb4725a7e`), B 39113183694 (10 reps, `3b9fc76017ad`), C 39120444653 (10 reps, `faaaff3142e1`) |
| `results/live/V10_FAIRNESS.md` | omni-v10 | standing | against its native | L | A 39107190192 (10 reps, `6d871e2baad1`), B 39114217887 (10 reps, `3b9fc76017ad`), C 39122528801 (10 reps, `faaaff3142e1`) |
| `results/live/V10_FAULTS.md` | omni-v10 | standing | against its native | L | A 39107193417 (10 reps, `6d871e2baad1`), B 39115232348 (10 reps, `f09db2756842`), C 39122532509 (10 reps, `faaaff3142e1`) |
| `results/live/V10_GOLDILOCKS.md` | omni-v10 | superseded | against its native | L | A 39106189778 (10 reps, `0454fdb0089f`), B 39113187123 (10 reps, `3b9fc76017ad`), C 39120448390 (10 reps, `faaaff3142e1`) |
| `results/live/V10_KAFKA.md` | omni-v10 | superseded | against its native | L | A 39108188053 (? reps, `6d871e2baad1`), B 39116273889 (? reps, `f09db2756842`), C 39123591485 (? reps, `faaaff3142e1`) |
| `results/live/V10_KAFKA_SERVICE.md` | omni-v10 | superseded | against its native | L | A 39109170592 (? reps, `6d871e2baad1`), B 39116292836 (? reps, `f09db2756842`), C 39124642737 (? reps, `8b902df8d857`) |
| `results/live/V10_KEDA_CPU_REQUESTS.md` | omni-v10 | superseded | against its native | L | A 39108180989 (10 reps, `6d871e2baad1`), B 39115242861 (10 reps, `f09db2756842`), C 39123583570 (10 reps, `faaaff3142e1`) |
| `results/live/V10_KEDA_REQUESTS.md` | omni-v10 | superseded | against its native | L | A 39108180989 (10 reps, `6d871e2baad1`), B 39115242861 (10 reps, `f09db2756842`), C 39123583570 (10 reps, `faaaff3142e1`) |
| `results/live/V10_MUJOCO.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_PANDAPOWER.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_PGBENCH.md` | omni-v10 | superseded | against its native | L | A 39108191914 (? reps, `6d871e2baad1`), B 39116277778 (? reps, `f09db2756842`), C 39123595298 (? reps, `faaaff3142e1`) |
| `results/live/V10_REDIS.md` | omni-v10 | superseded | against its native | L | A 39108184403 (? reps, `6d871e2baad1`), B 39115246841 (? reps, `f09db2756842`), C 39123587108 (? reps, `faaaff3142e1`) |
| `results/live/V10_REDIS_SERVICE.md` | omni-v10 | superseded | against its native | L | A 39109167603 (? reps, `6d871e2baad1`), B 39116289213 (? reps, `f09db2756842`), C 39124638850 (? reps, `8b902df8d857`) |
| `results/live/V10_ROBUST_LONG.md` | omni-v10 | superseded | against its native | L | A 39111154503 (3 reps, `13f22e8141c4`), B 39119406616 (3 reps, `faaaff3142e1`), C 39126745660 (3 reps, `56e00223da79`) |
| `results/live/V10_STEADY.md` | omni-v10 | standing | against its native | L | A 39107180703 (10 reps, `6d871e2baad1`), B 39114207589 (10 reps, `3b9fc76017ad`), C 39121472594 (10 reps, `faaaff3142e1`) |
| `results/live/V10_SWARM.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_SYSBENCH.md` | omni-v10 | superseded | against its native | L | A 39108195807 (? reps, `6d871e2baad1`), B 39116281643 (? reps, `f09db2756842`), C 39123599130 (? reps, `faaaff3142e1`) |
| `results/live/V10_TRACE_GOOGLE2011.md` | omni-v10 | standing | against its native | L | A 39108177259 (10 reps, `6d871e2baad1`), B 39115239009 (10 reps, `f09db2756842`), C 39122539586 (10 reps, `faaaff3142e1`) |
| `results/live/V10_WANDERING.md` | omni-v10 | standing | against its native | L | A 39107183748 (10 reps, `6d871e2baad1`), B 39114211206 (10 reps, `3b9fc76017ad`), C 39122521784 (10 reps, `faaaff3142e1`) |
| `results/live/V10_YCSB.md` | omni-v10 | superseded | against its native | L | A 39109164668 (? reps, `6d871e2baad1`), B 39116285471 (? reps, `f09db2756842`), C 39124635012 (? reps, `8b902df8d857`) |
| `results/live/V11_CAPACITY.md` | omni-v11 | standing | against its native | L | in its own Markdown |
| `results/live/V11_CITYLEARN.md` | omni-v11 | standing | against its native | S | in its own Markdown |
| `results/live/V11_GOLDILOCKS.md` | omni-v11 | standing | against its native | L | A 39171064099 (10 reps, `f445e205073f`), B 39175675418 (10 reps, `df871e4396dc`), C 39177950720 (10 reps, `0d11e5ab281c`) |
| `results/live/V11_KAFKA.md` | omni-v11 | superseded | against its native | L | A 39149249969 (? reps, `d44261ca0c5c`), B 39157787056 (? reps, `5031411ae285`), C 39166374877 (? reps, `8472aaad2bf4`) |
| `results/live/V11_KAFKA_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39150481307 (? reps, `c1c1b59711b1`), B 39159000835 (? reps, `3cb376bb3284`), C 39167574190 (? reps, `e2d5958834f5`) |
| `results/live/V11_KEDA_CPU_REQUESTS.md` | omni-v11 | standing | against its native | L | A 39173411511 (10 reps, `8de24035ac07`), B 39176842679 (10 reps, `2a2cfc67147e`), C 39180252225 (10 reps, `7b7dd69870e7`) |
| `results/live/V11_KEDA_REQUESTS.md` | omni-v11 | standing | against its native | L | A 39173411511 (10 reps, `8de24035ac07`), B 39176842679 (10 reps, `2a2cfc67147e`), C 39180252225 (10 reps, `7b7dd69870e7`) |
| `results/live/V11_MUJOCO.md` | omni-v11 | standing | against its native | S | in its own Markdown |
| `results/live/V11_PANDAPOWER.md` | omni-v11 | standing | against its native | S | in its own Markdown |
| `results/live/V11_PGBENCH.md` | omni-v11 | superseded | against its native | L | A 39149254727 (? reps, `d44261ca0c5c`), B 39157791268 (? reps, `5031411ae285`), C 39166378754 (? reps, `8472aaad2bf4`) |
| `results/live/V11_PGBENCH_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182915425 (? reps, `bc2eb38f4ca8`), B 39184166001 (? reps, `75478eb28444`), C 39185403353 (? reps, `ce92ff888e73`) |
| `results/live/V11_REDIS.md` | omni-v11 | superseded | against its native | L | A 39149244903 (? reps, `d44261ca0c5c`), B 39157782849 (? reps, `5031411ae285`), C 39166371110 (? reps, `8472aaad2bf4`) |
| `results/live/V11_REDIS_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39149267883 (? reps, `d44261ca0c5c`), B 39158996767 (? reps, `3cb376bb3284`), C 39167569649 (? reps, `e2d5958834f5`) |
| `results/live/V11_REDIS_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150490855 (? reps, `c1c1b59711b1`), B 39159008310 (? reps, `3cb376bb3284`), C 39167582853 (? reps, `e2d5958834f5`) |
| `results/live/V11_ROBUST_KILL.md` | omni-v11 | standing | against its native | L | A 39173416105 (10 reps, `8de24035ac07`), B 39177935888 (10 reps, `0d11e5ab281c`), C 39182898753 (10 reps, `bc2eb38f4ca8`) |
| `results/live/V11_ROBUST_LONG.md` | omni-v11 | standing | against its native | L | A 39173420146 (3 reps, `8de24035ac07`), B 39177939062 (3 reps, `0d11e5ab281c`), C 39182902844 (3 reps, `bc2eb38f4ca8`) |
| `results/live/V11_SWARM.md` | omni-v11 | standing | against its native | S | in its own Markdown |
| `results/live/V11_SYSBENCH.md` | omni-v11 | superseded | against its native | L | A 39149259396 (? reps, `d44261ca0c5c`), B 39157795408 (? reps, `5031411ae285`), C 39166382450 (? reps, `8472aaad2bf4`) |
| `results/live/V11_SYSBENCH_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182906799 (? reps, `bc2eb38f4ca8`), B 39184157413 (? reps, `75478eb28444`), C 39184175254 (? reps, `75478eb28444`) |
| `results/live/V11_SYSBENCH_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150486066 (? reps, `c1c1b59711b1`), B 39159004803 (? reps, `3cb376bb3284`), C 39167578494 (? reps, `e2d5958834f5`) |
| `results/live/V11_YCSB.md` | omni-v11 | superseded | against its native | L | A 39149263618 (? reps, `d44261ca0c5c`), B 39158992412 (? reps, `3cb376bb3284`), C 39167564949 (? reps, `e2d5958834f5`) |
| `results/live/V11_YCSB_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182911063 (? reps, `bc2eb38f4ca8`), B 39184161631 (? reps, `75478eb28444`), C 39184179710 (? reps, `75478eb28444`) |
| `results/live/V11_YCSB_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150495654 (? reps, `c1c1b59711b1`), B 39160201436 (? reps, `773cd59cfdd2`), C 39169863638 (? reps, `2b4c11e3aee0`) |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_BINPACK.md` | omni-v12 | standing | against its native | L | A 39356578556 (10 reps, `1ca982cf97db`), B 39356594135 (10 reps, `1ca982cf97db`), C 39356608147 (10 reps, `1ca982cf97db`) |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_CRANE_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_KAFKA.md` | omni-v12 | superseded | against its native | L | A 39379918375 (? reps, `690b955b1c2a`), B 39410587818 (? reps, `690b955b1c2a`), C 39459233023 (? reps, `6f4be24ffb43`) |
| `results/live/V12_KAFKA_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39381455200 (? reps, `690b955b1c2a`), B 39412428649 (? reps, `690b955b1c2a`), C 39461523366 (? reps, `6f4be24ffb43`) |
| `results/live/V12_KAI.md` | omni-v12 | standing | against its native | L | A 39350900880 (10 reps, `7dee891c54d1`), B 39350907916 (10 reps, `7dee891c54d1`), C 39350915166 (10 reps, `7dee891c54d1`) |
| `results/live/V12_KAI_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KOORDINATOR.md` | omni-v12 | standing | against its native | L | A 39359085965 (10 reps, `28a65e160d68`), B 39359094679 (10 reps, `28a65e160d68`), C 39359103518 (10 reps, `28a65e160d68`) |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_PGBENCH.md` | omni-v12 | superseded | against its native | L | A 39379923601 (? reps, `690b955b1c2a`), B 39410594381 (? reps, `690b955b1c2a`), C 39459241206 (? reps, `6f4be24ffb43`) |
| `results/live/V12_PGBENCH_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39473169216 (? reps, `ac0eeaef8ecc`), B 39477818906 (? reps, `fb90309cad0d`), C 39491674383 (? reps, `de8da62736d4`) |
| `results/live/V12_REDIS.md` | omni-v12 | superseded | against its native | L | A 39367385496 (? reps, `15654388e112`), B 39408770553 (? reps, `690b955b1c2a`), C 39459224023 (? reps, `6f4be24ffb43`) |
| `results/live/V12_REDIS_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39381449955 (? reps, `690b955b1c2a`), B 39412421481 (? reps, `690b955b1c2a`), C 39461515383 (? reps, `6f4be24ffb43`) |
| `results/live/V12_REDIS_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39382995467 (? reps, `690b955b1c2a`), B 39414279979 (? reps, `690b955b1c2a`), C 39461540163 (? reps, `6f4be24ffb43`) |
| `results/live/V12_SYSBENCH.md` | omni-v12 | superseded | against its native | L | A 39379929041 (? reps, `690b955b1c2a`), B 39410600428 (? reps, `690b955b1c2a`), C 39461498952 (? reps, `6f4be24ffb43`) |
| `results/live/V12_SYSBENCH_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39468576581 (? reps, `80843e7684b3`), B 39473186537 (? reps, `ac0eeaef8ecc`), C 39477834359 (? reps, `fb90309cad0d`) |
| `results/live/V12_SYSBENCH_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39382990197 (? reps, `690b955b1c2a`), B 39412436421 (? reps, `690b955b1c2a`), C 39461531771 (? reps, `6f4be24ffb43`) |
| `results/live/V12_VANILLA.md` | omni-v12 | standing | against its native | L | A 39356571014 (10 reps, `1ca982cf97db`), B 39356586356 (10 reps, `1ca982cf97db`), C 39356601235 (10 reps, `1ca982cf97db`) |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_YCSB.md` | omni-v12 | superseded | against its native | L | A 39379934444 (? reps, `690b955b1c2a`), B 39410606870 (? reps, `690b955b1c2a`), C 39461506751 (? reps, `6f4be24ffb43`) |
| `results/live/V12_YCSB_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39470845655 (? reps, `ac0eeaef8ecc`), B 39475514914 (? reps, `fb90309cad0d`), C 39477842603 (? reps, `fb90309cad0d`) |
| `results/live/V12_YCSB_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39383000915 (? reps, `690b955b1c2a`), B 39414286889 (? reps, `690b955b1c2a`), C 39463721089 (? reps, `6f4be24ffb43`) |
| `results/live/V14_PGBENCH_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39625603596 (? reps, `e32bbb605501`), B 39628245625 (? reps, `990711a99dc4`), C 39630669154 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_SYSBENCH_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39623235693 (? reps, `e32bbb605501`), B 39625624640 (? reps, `e32bbb605501`), C 39630651710 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_YCSB_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39623244880 (? reps, `e32bbb605501`), B 39628035584 (? reps, `990711a99dc4`), C 39630660108 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_YCSB_SHIPPED.md` | omni-v14 | superseded | against its native | L | A 39562510452 (? reps, `418f860a4da6`), B 39590117126 (? reps, `e997ca0d9f65`), C 39616239634 (? reps, `63a093f13de0`) |
| `results/live/V16_KAFKA.md` | omni-v16 | standing | against its native | L | A 39821402572 (? reps, `611aad4666db`), B 39840024618 (? reps, `d27db5f66c71`), C 39860244280 (? reps, `15915c961cd2`) |
| `results/live/V16_KAFKA_SERVICE.md` | omni-v16 | standing | against its native | L | A 39823828673 (? reps, `611aad4666db`), B 39844651167 (? reps, `d27db5f66c71`), C 39864227589 (? reps, `681ff70efadd`) |
| `results/live/V16_PGBENCH.md` | omni-v16 | standing | against its native | L | A 39842347137 (? reps, `d27db5f66c71`), B 39851575564 (? reps, `36cb1cc37947`), C 39860251731 (? reps, `15915c961cd2`) |
| `results/live/V16_PGBENCH_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869913163 (? reps, `464fb9e27535`), B 39871667274 (? reps, `464fb9e27535`), C 39873437772 (? reps, `a9694fbc7d2a`) |
| `results/live/V16_REDIS.md` | omni-v16 | standing | against its native | L | A 39821393310 (? reps, `611aad4666db`), B 39840016313 (? reps, `d27db5f66c71`), C 39860237154 (? reps, `15915c961cd2`) |
| `results/live/V16_REDIS_SERVICE.md` | omni-v16 | standing | against its native | L | A 39823820262 (? reps, `611aad4666db`), B 39844642925 (? reps, `d27db5f66c71`), C 39862248686 (? reps, `681ff70efadd`) |
| `results/live/V16_REDIS_SHIPPED.md` | omni-v16 | standing | against its native | L | A 39826081107 (? reps, `611aad4666db`), B 39846960314 (? reps, `d27db5f66c71`), C 39866161041 (? reps, `5f430c111d90`) |
| `results/live/V16_SYSBENCH.md` | omni-v16 | standing | against its native | L | A 39823802516 (? reps, `611aad4666db`), B 39842355356 (? reps, `d27db5f66c71`), C 39862234914 (? reps, `15915c961cd2`) |
| `results/live/V16_SYSBENCH_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869901058 (? reps, `464fb9e27535`), B 39869925397 (? reps, `464fb9e27535`), C 39871679567 (? reps, `464fb9e27535`) |
| `results/live/V16_SYSBENCH_SHIPPED.md` | omni-v16 | standing | against its native | L | A 39826073316 (? reps, `611aad4666db`), B 39846952545 (? reps, `d27db5f66c71`), C 39864234559 (? reps, `681ff70efadd`) |
| `results/live/V16_YCSB.md` | omni-v16 | standing | against its native | L | A 39823811507 (? reps, `611aad4666db`), B 39842363997 (? reps, `d27db5f66c71`), C 39862241743 (? reps, `681ff70efadd`) |
| `results/live/V16_YCSB_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869906902 (? reps, `464fb9e27535`), B 39871660953 (? reps, `464fb9e27535`), C 39871685303 (? reps, `464fb9e27535`) |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | standing | against its native | L | A 39826088859 (? reps, `611aad4666db`), B 39846968680 (? reps, `d27db5f66c71`), C 39866167058 (? reps, `5f430c111d90`) |
| `results/live/V17_KAFKA.md` | omni-v17 | superseded | against its native | L | A 40003710547 (? reps, `b525b7a07a0c`), B 40020507060 (? reps, `6fcdf41aad34`), C 40035619419 (? reps, `6e4b64630bfc`) |
| `results/live/V17_KAFKA_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40005908588 (? reps, `b525b7a07a0c`), B 40022521256 (? reps, `6fcdf41aad34`), C 40037209884 (? reps, `6e4b64630bfc`) |
| `results/live/V17_PGBENCH.md` | omni-v17 | superseded | against its native | L | A 40003718316 (? reps, `b525b7a07a0c`), B 40022493643 (? reps, `6fcdf41aad34`), C 40037187971 (? reps, `6e4b64630bfc`) |
| `results/live/V17_PGBENCH_SERVICE.md` | omni-v17 | standing | against its native | L | A 40043218026 (? reps, `f22776e60a87`), B 40044599601 (? reps, `0d532c7a2dbd`), C 40045930230 (? reps, `e4a97f22dce1`) |
| `results/live/V17_REDIS.md` | omni-v17 | superseded | against its native | L | A 39999416157 (? reps, `9678c8ad4325`), B 40020500663 (? reps, `6fcdf41aad34`), C 40035613178 (? reps, `6e4b64630bfc`) |
| `results/live/V17_REDIS_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40005899721 (? reps, `b525b7a07a0c`), B 40022515018 (? reps, `6fcdf41aad34`), C 40037204297 (? reps, `6e4b64630bfc`) |
| `results/live/V17_REDIS_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40005925354 (? reps, `b525b7a07a0c`), B 40024478954 (? reps, `6fcdf41aad34`), C 40038802348 (? reps, `d02c7052ae50`) |
| `results/live/V17_SYSBENCH.md` | omni-v17 | superseded | against its native | L | A 40003726359 (? reps, `b525b7a07a0c`), B 40022500639 (? reps, `6fcdf41aad34`), C 40037193927 (? reps, `6e4b64630bfc`) |
| `results/live/V17_SYSBENCH_SERVICE.md` | omni-v17 | standing | against its native | L | A 40043207507 (? reps, `f22776e60a87`), B 40044589141 (? reps, `0d532c7a2dbd`), C 40045921684 (? reps, `e4a97f22dce1`) |
| `results/live/V17_SYSBENCH_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40005917048 (? reps, `b525b7a07a0c`), B 40024472453 (? reps, `6fcdf41aad34`), C 40038796458 (? reps, `d02c7052ae50`) |
| `results/live/V17_YCSB.md` | omni-v17 | superseded | against its native | L | A 40003734350 (? reps, `b525b7a07a0c`), B 40022507977 (? reps, `6fcdf41aad34`), C 40037199208 (? reps, `6e4b64630bfc`) |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | standing | against its native | L | A 40043212711 (? reps, `f22776e60a87`), B 40044594345 (? reps, `0d532c7a2dbd`), C 40045925918 (? reps, `e4a97f22dce1`) |
| `results/live/V17_YCSB_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40008048292 (? reps, `b525b7a07a0c`), B 40024485005 (? reps, `6fcdf41aad34`), C 40038808111 (? reps, `d02c7052ae50`) |
| `results/live/V1_ALL_FOUR.md` | omni-v1 | the road | against its native | L | A 37384945573 (10 reps, `f162ce8d74e8`), B 37385646550 (10 reps, `f162ce8d74e8`), C 37394444337 (10 reps, `68d9bd172605`) |
| `results/live/V1_BATCH.md` | omni-v1 | the road | against its native | L | A 37385637932 (10 reps, `f162ce8d74e8`), B 37385654462 (10 reps, `f162ce8d74e8`), C 37394452486 (10 reps, `68d9bd172605`) |
| `results/live/V1_CITYLEARN.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_FAIRNESS.md` | omni-v1 | the road | against its native | L | A 37384948340 (10 reps, `f162ce8d74e8`), B 37385649261 (10 reps, `f162ce8d74e8`), C 37391303438 (10 reps, `029340abf30c`) |
| `results/live/V1_FAULTS.md` | omni-v1 | the road | against its native | L | A 37384951397 (10 reps, `f162ce8d74e8`), B 37385651747 (10 reps, `f162ce8d74e8`), C 37391310157 (10 reps, `029340abf30c`) |
| `results/live/V1_MUJOCO.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_MUJOCO_PANDA.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_PANDAPOWER.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_STEADY.md` | omni-v1 | the road | against its native | L | A 37384939815 (10 reps, `f162ce8d74e8`), B 37385640601 (10 reps, `f162ce8d74e8`), C 37391296025 (10 reps, `029340abf30c`) |
| `results/live/V1_WANDERING.md` | omni-v1 | the road | against its native | L | A 37384942870 (10 reps, `f162ce8d74e8`), B 37385643291 (10 reps, `f162ce8d74e8`), C 37394436586 (10 reps, `68d9bd172605`) |
| `results/live/V3_ALL_FOUR.md` | omni-v3 | the road | against its native | L | A 38013221512 (10 reps, `3aac0ab7d384`), B 38013226173 (10 reps, `3aac0ab7d384`), C 38013230522 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_BATCH.md` | omni-v3 | the road | against its native | L | A 38013261196 (10 reps, `3aac0ab7d384`), B 38013265986 (10 reps, `3aac0ab7d384`), C 38013269850 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_CITYLEARN.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_FAIRNESS.md` | omni-v3 | the road | against its native | L | A 38013235441 (10 reps, `3aac0ab7d384`), B 38013239864 (10 reps, `3aac0ab7d384`), C 38013244591 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_FAULTS.md` | omni-v3 | the road | against its native | L | A 38013248544 (10 reps, `3aac0ab7d384`), B 38013252615 (10 reps, `3aac0ab7d384`), C 38013257029 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_KAFKA.md` | omni-v3 | the road | against its native | L | A 38054742933 (? reps, `ca745467845c`), B 38054746778 (? reps, `ca745467845c`), C 38054750788 (? reps, `ca745467845c`) |
| `results/live/V3_KAFKA_SERVICE.md` | omni-v3 | the road | against its native | L | A 38054804459 (? reps, `ca745467845c`), B 38054808912 (? reps, `ca745467845c`), C 38054812962 (? reps, `ca745467845c`) |
| `results/live/V3_KEDA_CPU_REQUESTS.md` | omni-v3 | the road | against its native | L | A 38096663118 (9 reps, `175cc0feda00`), B 38099655092 (10 reps, `85b150889152`), C 38099656930 (10 reps, `85b150889152`) |
| `results/live/V3_KEDA_REQUESTS.md` | omni-v3 | the road | against its native | L | A 38096663118 (10 reps, `175cc0feda00`), B 38099655092 (10 reps, `85b150889152`), C 38099656930 (10 reps, `85b150889152`) |
| `results/live/V3_MUJOCO.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_PANDAPOWER.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_PGBENCH.md` | omni-v3 | the road | against its native | L | A 38054754511 (? reps, `ca745467845c`), B 38054758150 (? reps, `ca745467845c`), C 38054761503 (? reps, `ca745467845c`) |
| `results/live/V3_REDIS.md` | omni-v3 | the road | against its native | L | A 38054731163 (? reps, `ca745467845c`), B 38054735302 (? reps, `ca745467845c`), C 38054739168 (? reps, `ca745467845c`) |
| `results/live/V3_REDIS_SERVICE.md` | omni-v3 | the road | against its native | L | A 38054791688 (? reps, `ca745467845c`), B 38054795871 (? reps, `ca745467845c`), C 38054800068 (? reps, `ca745467845c`) |
| `results/live/V3_ROBUST_KILL.md` | omni-v3 | the road | against its native | L | A 38013447217 (10 reps, `3aac0ab7d384`), B 38013451990 (10 reps, `3aac0ab7d384`), C 38013456955 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_ROBUST_LONG.md` | omni-v3 | the road | against its native | L | A 38013462081 (3 reps, `3aac0ab7d384`), B 38013467123 (3 reps, `3aac0ab7d384`), C 38013471943 (3 reps, `3aac0ab7d384`) |
| `results/live/V3_STEADY.md` | omni-v3 | the road | against its native | L | A 38013195851 (10 reps, `3aac0ab7d384`), B 38013200499 (10 reps, `3aac0ab7d384`), C 38013204648 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_SWARM.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_SYSBENCH.md` | omni-v3 | the road | against its native | L | A 38054765202 (? reps, `ca745467845c`), B 38054768832 (? reps, `ca745467845c`), C 38054773573 (? reps, `ca745467845c`) |
| `results/live/V3_TRACE_GOOGLE2011.md` | omni-v3 | the road | against its native | L | A 38013274685 (10 reps, `3aac0ab7d384`), B 38013279107 (10 reps, `3aac0ab7d384`), C 38013283518 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_WANDERING.md` | omni-v3 | the road | against its native | L | A 38013208955 (10 reps, `3aac0ab7d384`), B 38013212780 (10 reps, `3aac0ab7d384`), C 38013217100 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_YCSB.md` | omni-v3 | the road | against its native | L | A 38054777807 (? reps, `ca745467845c`), B 38054782696 (? reps, `ca745467845c`), C 38054787517 (? reps, `ca745467845c`) |
| `results/live/V5_CAPACITY.md` | omni-v5 | the road | against its native | L | in its own Markdown |
| `results/live/V5_GOLDILOCKS.md` | omni-v5 | the road | against its native | L | A 38339821941 (10 reps, `148565d2550d`), B 38339828150 (10 reps, `148565d2550d`), C 38339834658 (10 reps, `148565d2550d`) |
| `results/live/V6_CRUISEKUBE.md` | omni-v6 | the road | against its native | L | A 38695794476 (10 reps, `9a499b137e78`), B 38708509996 (10 reps, `afbac134f8a1`), C 38721988615 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_GOLDILOCKS.md` | omni-v6 | the road | against its native | L | A 38697567716 (10 reps, `9a499b137e78`), B 38708517967 (10 reps, `afbac134f8a1`), C 38721995611 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_KEDA_CPU_REQUESTS.md` | omni-v6 | the road | against its native | L | A 38701101796 (10 reps, `9a499b137e78`), B 38712444594 (10 reps, `afbac134f8a1`), C 38725705826 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_KEDA_REQUESTS.md` | omni-v6 | the road | against its native | L | A 38701101796 (10 reps, `9a499b137e78`), B 38712444594 (10 reps, `afbac134f8a1`), C 38725705826 (10 reps, `63f29c3e20a5`) |
| `results/live/V7_ALL_FOUR.md` | omni-v7 | the road | against its native | L | A 38931373773 (10 reps, `ccce256f4079`), B 38943562450 (10 reps, `cf8dccec0604`), C 38953643978 (10 reps, `cf8dccec0604`) |
| `results/live/V7_BATCH.md` | omni-v7 | the road | against its native | L | A 38933427756 (10 reps, `1ccba53a74fe`), B 38943582904 (10 reps, `cf8dccec0604`), C 38955582904 (10 reps, `cf8dccec0604`) |
| `results/live/V7_CAPACITY.md` | omni-v7 | the road | against its native | L | in its own Markdown |
| `results/live/V7_CITYLEARN.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_CRUISEKUBE.md` | omni-v7 | the road | against its native | L | A 38843284578 (10 reps, `b1eb8294f4a7`), B 38843287341 (10 reps, `b1eb8294f4a7`), C 38843289946 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_FAIRNESS.md` | omni-v7 | the road | against its native | L | A 38933412682 (10 reps, `1ccba53a74fe`), B 38943569010 (10 reps, `cf8dccec0604`), C 38955570717 (10 reps, `cf8dccec0604`) |
| `results/live/V7_FAULTS.md` | omni-v7 | the road | against its native | L | A 38933419908 (10 reps, `1ccba53a74fe`), B 38943575598 (10 reps, `cf8dccec0604`), C 38955576606 (10 reps, `cf8dccec0604`) |
| `results/live/V7_GOLDILOCKS.md` | omni-v7 | the road | against its native | L | A 38843260818 (10 reps, `b1eb8294f4a7`), B 38843263401 (10 reps, `b1eb8294f4a7`), C 38843266098 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_KAFKA.md` | omni-v7 | the road | against its native | L | A 38933446756 (? reps, `1ccba53a74fe`), B 38945593946 (? reps, `cf8dccec0604`), C 38955602669 (? reps, `cf8dccec0604`) |
| `results/live/V7_KAFKA_SERVICE.md` | omni-v7 | the road | against its native | L | A 38935449417 (? reps, `1ccba53a74fe`), B 38947629506 (? reps, `cf8dccec0604`), C 38957543812 (? reps, `cf8dccec0604`) |
| `results/live/V7_KEDA_CPU_REQUESTS.md` | omni-v7 | the road | against its native | L | A 38843268161 (10 reps, `b1eb8294f4a7`), B 38843270386 (10 reps, `b1eb8294f4a7`), C 38843272786 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_KEDA_REQUESTS.md` | omni-v7 | the road | against its native | L | A 38843268161 (10 reps, `b1eb8294f4a7`), B 38843270386 (10 reps, `b1eb8294f4a7`), C 38843272786 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_MUJOCO.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_PANDAPOWER.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_PGBENCH.md` | omni-v7 | the road | against its native | L | A 38935420705 (? reps, `1ccba53a74fe`), B 38945602041 (? reps, `cf8dccec0604`), C 38957516288 (? reps, `cf8dccec0604`) |
| `results/live/V7_REDIS.md` | omni-v7 | the road | against its native | L | A 38933440763 (? reps, `1ccba53a74fe`), B 38945586160 (? reps, `cf8dccec0604`), C 38955596458 (? reps, `cf8dccec0604`) |
| `results/live/V7_REDIS_SERVICE.md` | omni-v7 | the road | against its native | L | A 38935442398 (? reps, `1ccba53a74fe`), B 38947622681 (? reps, `cf8dccec0604`), C 38957537624 (? reps, `cf8dccec0604`) |
| `results/live/V7_ROBUST_LONG.md` | omni-v7 | the road | against its native | L | A 38937561382 (3 reps, `1ccba53a74fe`), B 38949637918 (3 reps, `cf8dccec0604`), C 38961359324 (3 reps, `cf8dccec0604`) |
| `results/live/V7_SWARM.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_SYSBENCH.md` | omni-v7 | the road | against its native | L | A 38935427838 (? reps, `1ccba53a74fe`), B 38945609870 (? reps, `cf8dccec0604`), C 38957523334 (? reps, `cf8dccec0604`) |
| `results/live/V7_TRACE_GOOGLE2011.md` | omni-v7 | the road | against its native | L | A 38933435153 (10 reps, `1ccba53a74fe`), B 38945578014 (10 reps, `cf8dccec0604`), C 38955589372 (10 reps, `cf8dccec0604`) |
| `results/live/V7_YCSB.md` | omni-v7 | the road | against its native | L | A 38935435045 (? reps, `1ccba53a74fe`), B 38947615453 (? reps, `cf8dccec0604`), C 38957530830 (? reps, `cf8dccec0604`) |
| `results/orchestrator/V18_THREE_ARMS_ABC.md` | omni-v18 | taken out | against its native | L | in its own Markdown |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
