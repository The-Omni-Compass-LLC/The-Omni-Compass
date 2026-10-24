# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.3/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.2% | -1.89 to 0.383 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.006 to 0.00507 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,623 | 2,654 | +1.2% | -200 to 262 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,845 | 3,721 | -3.2% | -327 to 79.2 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.52 | -0.5% | -0.373 to 0.283 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 387 | 390 | +0.8% | -0.185 to 6.22 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,689 | 1,700 | +0.6% | -0.536 to 21.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 169 | +0.9% | -1.61 to 4.79 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.284 | 0.281 | -0.8% | -0.0132 to 0.00841 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 202 | -0.8% | -9.53 to 6.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.27 | -0.6% | -0.139 to 0.101 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.553 to -0.252 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.213 to 0.335 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,385 | 2,441 | +2.3% | -92.9 to 205 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,685 | 3,766 | +2.2% | -329 to 492 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.1 | 11 | -1.1% | -0.748 to 0.502 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 329 | +3.1% | 2.93 to 16.6 | LOSS |
| consumer lag, most messages waiting at once | 679 | 693 | +2.0% | -26.5 to 53.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.3 | 60.1 | +3.2% | 0.359 to 3.33 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.27 | 0.263 | -2.4% | -0.0387 to 0.0255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 484 | 472 | -2.4% | -69.6 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.28 | 7.12 | -2.1% | -1.02 to 0.708 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1924 messages a second; base rate 288.5/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 716 | -1.4% | -31.7 to 11.8 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | +0.0% | -0.00907 to 0.0141 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,149 | 3,673 | +70.9% | -1,885 to 4,934 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,369 | 5,355 | +58.9% | -2,290 to 6,261 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.37 | 8.29 | -0.9% | -0.639 to 0.485 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 288 | 485 | +68.6% | -240 to 635 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,076 | 4,491 | +46.0% | -1,665 to 4,496 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 250 | 416 | +66.1% | -203 to 534 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.328 | 0.323 | -1.4% | -0.0124 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 556 | -1.1% | -21.3 to 8.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.73 | +0.2% | -0.0804 to 0.0881 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -1.51 to 0.0345 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0131 to 0.00704 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,276 | 2,276 | +0.0% | -314 to 314 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,563 | 3,688 | +3.5% | -138 to 387 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.06 | 8.01 | -0.6% | -0.251 to 0.148 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 309 | +1.4% | -16.1 to 24.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,642 | 1,653 | +0.7% | -81.9 to 105 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 136 | 137 | +1.1% | -7.96 to 11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% | -0.296 to 0.786 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.268 | 0.27 | +0.4% | -0.0093 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 480 | 482 | +0.5% | -15.8 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.9 | 2.92 | +0.7% | -0.0839 to 0.124 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
