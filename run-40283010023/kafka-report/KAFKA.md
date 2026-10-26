# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 985 messages a second; base rate 110.8/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 344 | 343 | -0.5% | -5.43 to 2.13 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 423 | 423 | +0.0% | -0.0637 to 0.0835 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,603 | 2,744 | +5.4% | -59.8 to 342 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,892 | 3,821 | -1.8% | -333 to 191 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 18.8 | 11.6 | -38.4% | -31.1 to 16.6 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 405 | 419 | +3.3% | -13.3 to 39.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,737 | 1,788 | +2.9% | 32.9 to 67.8 | LOSS |
| consumer lag, mean messages waiting | 180 | 185 | +2.4% | -7.96 to 16.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.26 | 0.266 | +2.2% | -0.0261 to 0.0376 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 191 | +2.2% | -18.6 to 26.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.01 | 3.09 | +2.6% | -0.251 to 0.409 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.36 to 0.72 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00219 to 0.00125 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,448 | 2,508 | +2.5% | -165 to 285 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,797 | 3,779 | -0.5% | -136 to 101 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.1% | -0.0453 to 0.0667 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 329 | 338 | +2.7% | -14.1 to 32.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 696 | 706 | +1.5% | -51.7 to 72.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.4 | 61.5 | +1.7% | -1.45 to 3.56 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.284 | -0.2% | -0.00855 to 0.0073 | EVEN, no difference beyond the noise |
| host CPU-seconds | 511 | 510 | -0.2% | -15 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.71 | 7.71 | -0.0% | -0.158 to 0.158 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1915 messages a second; base rate 287.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 720 | -0.4% | -16 to 9.73 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 842 | 842 | +0.0% | -0.0497 to 0.0939 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,100 | 2,098 | -0.1% | -54.4 to 50.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,386 | 3,338 | -1.4% | -478 to 382 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.2 | -0.6% | -0.47 to 0.374 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 275 | 280 | +1.8% | -20.9 to 30.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,045 | 3,019 | -0.9% | -55.3 to 3.29 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 236 | 240 | +1.7% | -17.2 to 25.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.1 | +4.9% | -0.308 to 0.503 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.378 | 0.372 | -1.5% | -0.014 to 0.00249 | EVEN, no difference beyond the noise |
| host CPU-seconds | 652 | 641 | -1.7% | -20.8 to -1.81 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 2 | 1.98 | -1.3% | -0.0753 to 0.0233 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -7.01 to 13.7 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.5/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | +0.1% | -1.61 to 2.27 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | +0.0% | -0.00638 to 0.00793 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,255 | 2,166 | -3.9% | -196 to 19.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,509 | 3,519 | +0.3% | -609 to 630 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.61 | 8.61 | -0.0% | -0.176 to 0.173 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 297 | 292 | -1.8% | -30 to 19.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,606 | 1,588 | -1.1% | -60.4 to 24.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 131 | 128 | -2.0% | -13.8 to 8.59 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.311 | -0.1% | -0.00985 to 0.00939 | EVEN, no difference beyond the noise |
| host CPU-seconds | 540 | 539 | -0.1% | -18 to 16.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | -0.2% | -0.128 to 0.114 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
