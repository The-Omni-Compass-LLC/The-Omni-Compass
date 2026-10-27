# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 347 | 347 | +0.1% | -0.906 to 1.92 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.00887 to 0.0304 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,706 | 1,711 | +0.3% | -66.6 to 75.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,500 | 2,497 | -0.1% | -205 to 198 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.83 | 9.83 | +0.0% | -0.804 to 0.804 | EVEN, the same |
| end-to-end latency, mean (ms) | 266 | 265 | -0.3% | -2 to 0.537 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,128 | 1,144 | +1.4% | -31.4 to 63.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 117 | 116 | -0.7% | -1.95 to 0.349 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.294 | -2.3% | -0.048 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 141 | 138 | -2.3% | -22.7 to 16.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.28 | -2.5% | -0.551 to 0.384 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.6% | -5.18 to 3.39 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00699 to 0.00556 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,567 | 1,543 | -1.6% | -206 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,435 | 2,433 | -0.1% | -551 to 547 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.7 | +0.4% | -0.0198 to 0.104 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 214 | 221 | +2.9% | -44.5 to 57.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 463 | 469 | +1.3% | -98 to 110 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 39.9 | 41.4 | +3.9% | -9.46 to 12.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.23 | +11.6% | -0.247 to 0.713 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.283 | 0.284 | +0.7% | -0.0113 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 334 | +0.7% | -13.1 to 18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.46 | 7.56 | +1.4% | -0.0438 to 0.247 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | -2.61 to 14.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 6.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1925 messages a second; base rate 288.8/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 727 | -0.8% | -15.7 to 3.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0103 to 0.00549 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,515 | 1,716 | +13.2% | -410 to 810 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,394 | 2,611 | +9.1% | -337 to 772 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.22 | 7.92 | -3.7% | -0.829 to 0.217 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 211 | 235 | +11.8% | -29.3 to 78.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,195 | 2,276 | +3.7% | -383 to 546 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 185 | 205 | +11.2% | -24.2 to 65.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.29 | +14.5% | -0.115 to 0.694 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3.67 | +83.3% | 0.232 to 3.1 | power given |
| host CPU busy (share of the run) | 0.331 | 0.331 | +0.0% | -0.011 to 0.011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 380 | 380 | +0.0% | -11 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.9% | -0.046 to 0.0756 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 9.33 | +366.7% | -0.256 to 14.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.8/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 371 | 366 | -1.4% | -22.6 to 12.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.014 to 0.00727 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,612 | 1,704 | +5.7% | -242 to 426 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,450 | 2,674 | +9.1% | -397 to 844 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.14 | 8.15 | +0.2% | -0.215 to 0.244 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 219 | 244 | +11.3% | -63.4 to 113 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,130 | 1,192 | +5.5% | -130 to 254 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 98.8 | 110 | +11.3% | -27.9 to 50.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.00732 to 0.0117 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.286 | +1.4% | -0.0109 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 341 | +1.4% | -12.4 to 22.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.01 | 3.1 | +2.9% | -0.214 to 0.387 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2.67 | +33.3% | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
