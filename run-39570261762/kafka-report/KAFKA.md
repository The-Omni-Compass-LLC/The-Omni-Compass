# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -1.46 to 0.614 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0147 to 0.00782 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,604 | 2,575 | -1.1% | -259 to 201 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,755 | 3,849 | +2.5% | -440 to 628 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.15 | 8.96 | -2.1% | -1.09 to 0.699 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 387 | 390 | +0.7% | -3.31 to 8.92 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,698 | 1,693 | -0.3% | -68.7 to 58.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 168 | +0.8% | -3.4 to 6.07 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.307 | -0.4% | -0.0135 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 219 | -0.4% | -9.63 to 8.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.57 | 3.57 | -0.2% | -0.163 to 0.145 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.199 to -0.101 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00544 to 0.00216 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,561 | 2,519 | -1.6% | -90.4 to 6.39 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,854 | 3,877 | +0.6% | -452 to 498 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.172 to 0.122 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 342 | 343 | +0.2% | -4.22 to 5.41 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 724 | 714 | -1.3% | -42.5 to 23.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 63.2 | 63.5 | +0.4% | -0.172 to 0.672 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.282 | 0.28 | -0.7% | -0.0112 to 0.007 | EVEN, no difference beyond the noise |
| host CPU-seconds | 497 | 494 | -0.7% | -20.2 to 13.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.45 | -0.6% | -0.295 to 0.207 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.2% | -5.41 to 2.88 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0238 to 0.0101 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,286 | 2,293 | +0.3% | -167 to 181 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,646 | 3,696 | +1.4% | -293 to 392 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.8 | 7.79 | -0.0% | -0.247 to 0.246 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 311 | +1.6% | -5.96 to 15.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,228 | 3,243 | +0.5% | -88.9 to 118 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 266 | 269 | +1.1% | -4.79 to 10.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.344 | 0.345 | +0.4% | -0.0176 to 0.0206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 596 | 600 | +0.7% | -31.3 to 39.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.84 | +0.9% | -0.097 to 0.129 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 147.0/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.1% | -1.2 to 0.671 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00945 to 0.00634 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,390 | 2,349 | -1.7% | -173 to 90.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,731 | 3,737 | +0.2% | -79.2 to 90.6 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.03 | 7.96 | -0.9% | -0.264 to 0.113 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 315 | -0.4% | -11.1 to 8.65 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,674 | -1.7% | -84.4 to 25.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 139 | -0.5% | -3.71 to 2.29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.31 | -0.3% | -0.00555 to 0.0036 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 570 | -0.1% | -8.94 to 7.52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.45 | 3.45 | -0.1% | -0.06 to 0.0564 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
