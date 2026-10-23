# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.0% | -3.05 to 3.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0104 to 0.0086 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,547 | 2,529 | -0.7% | -262 to 226 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,688 | 3,670 | -0.5% | -441 to 405 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.73 | 8.49 | -2.8% | -1.02 to 0.537 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 378 | -0.7% | -6.05 to 0.413 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,656 | 1,650 | -0.3% | -57 to 45.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 163 | -1.0% | -6.4 to 2.94 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.282 | -1.0% | -0.0152 to 0.00973 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 202 | -0.9% | -10.7 to 6.85 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.28 | -1.0% | -0.17 to 0.105 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.557 to 0.649 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00162 to 0.00347 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,465 | 2,395 | -2.9% | -176 to 35.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,945 | +3.7% | -124 to 407 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11 | 10.9 | -1.3% | -0.743 to 0.453 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 327 | -0.9% | -19.4 to 13.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 706 | 710 | +0.5% | -29.9 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.8 | 60.4 | -0.7% | -2.15 to 1.35 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.261 | -1.3% | -0.0188 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 474 | 468 | -1.3% | -33.2 to 20.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.14 | 7.04 | -1.3% | -0.503 to 0.311 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1949 messages a second; base rate 292.3/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 733 | +0.1% | -3.14 to 3.97 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0366 to 0.0308 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,310 | 2,255 | -2.4% | -228 to 118 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,599 | 3,524 | -2.1% | -442 to 290 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.52 | 10 | +5.2% | -7.96 to 8.95 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 307 | -3.0% | -29.5 to 10.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,278 | 3,221 | -1.7% | -223 to 111 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 271 | -2.8% | -21.8 to 6.42 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.284 | 0.283 | -0.4% | -0.0122 to 0.00992 | EVEN, no difference beyond the noise |
| host CPU-seconds | 507 | 505 | -0.4% | -20.6 to 16.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.54 | 1.53 | -0.5% | -0.0634 to 0.0485 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -2.37 to 1.17 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.847 to 0.527 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,357 | 2,395 | +1.6% | -151 to 226 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,679 | 3,825 | +4.0% | -276 to 569 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.21 | 8.18 | -0.4% | -0.0769 to 0.0122 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 321 | +1.9% | -23.2 to 35.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,683 | 1,681 | -0.1% | -139 to 135 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 142 | +1.9% | -9.95 to 15.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.298 | 0.296 | -0.8% | -0.00727 to 0.00279 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 528 | -0.6% | -11.3 to 5.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.21 | -0.4% | -0.0727 to 0.0453 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
