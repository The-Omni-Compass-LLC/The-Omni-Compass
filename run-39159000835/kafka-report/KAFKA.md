# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.2% | -1.22 to 0.0772 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0053 to 0.00953 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,513 | 2,535 | +0.9% | -75.1 to 119 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,588 | 3,715 | +3.5% | -136 to 389 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.04 | -5.6% | -1.39 to 0.32 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 378 | +0.2% | -7.12 to 8.59 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,642 | 1,652 | +0.6% | -8.96 to 29.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 162 | -0.1% | -6.49 to 6.16 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.311 | -4.5% | -0.06 to 0.031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 223 | -4.4% | -43 to 22.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.79 | 3.63 | -4.3% | -0.687 to 0.363 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.06 to 0.867 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00275 to 0.0016 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,455 | 2,479 | +1.0% | -202 to 251 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,856 | 3,813 | -1.1% | -449 to 362 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | +0.2% | -0.045 to 0.093 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 334 | +0.5% | -27.9 to 31 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 706 | 703 | -0.3% | -71.9 to 67.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.9 | 61.2 | +0.4% | -4.6 to 5.13 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.288 | +0.2% | -0.00431 to 0.00532 | EVEN, no difference beyond the noise |
| host CPU-seconds | 506 | 507 | +0.2% | -7.42 to 9.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.65 | 7.67 | +0.3% | -0.0563 to 0.1 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1940 messages a second; base rate 291.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | +0.1% | -1.34 to 2.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0188 to 0.0112 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,500 | 2,413 | -3.5% | -267 to 94.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,808 | -1.6% | -455 to 333 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.34 | 8.3 | -0.5% | -0.637 to 0.553 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 337 | 330 | -2.3% | -28.3 to 12.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,399 | 3,319 | -2.4% | -196 to 35.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 295 | 287 | -2.5% | -25.4 to 10.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.326 | 0.325 | -0.5% | -0.00898 to 0.00549 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 557 | -0.6% | -18.3 to 12 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.7 | -0.6% | -0.0593 to 0.037 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 984 messages a second; base rate 147.6/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.1% | -1.99 to 1.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | -0.0% | -0.00704 to 0.00283 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,530 | +1.2% | -78.8 to 141 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,887 | 3,839 | -1.2% | -257 to 161 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.04 | 8.06 | +0.2% | -0.279 to 0.313 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 343 | +0.7% | -7.41 to 12.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,763 | 1,748 | -0.8% | -65.7 to 36.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 152 | 153 | +0.6% | -5.51 to 7.32 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.275 | 0.276 | +0.4% | -0.0168 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 494 | +0.5% | -28.7 to 33.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.97 | 2.99 | +0.6% | -0.16 to 0.196 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
