# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | +0.0% | -0.341 to 0.383 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0291 to 0.0215 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,608 | 2,659 | +2.0% | -92.2 to 194 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,906 | 3,790 | -3.0% | -297 to 64.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.63 | -1.4% | -0.594 to 0.354 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 398 | 398 | -0.1% | -8.76 to 8.15 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,731 | 1,724 | -0.4% | -45 to 32.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 172 | -0.4% | -8.27 to 6.98 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.289 | 0.282 | -2.2% | -0.0187 to 0.00575 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 203 | -2.2% | -13.4 to 4.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.28 | -2.2% | -0.216 to 0.0675 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.41 to 0.382 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00262 to 0.00211 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,148 | 2,190 | +1.9% | -127 to 211 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,398 | 3,476 | +2.3% | -120 to 275 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.5% | -0.381 to 0.262 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 284 | 293 | +3.0% | -17 to 34.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 657 | 653 | -0.6% | -83.8 to 75.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52.1 | 53.8 | +3.1% | -2.73 to 6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.06 | +3.2% | 0.0604 to 0.0667 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.279 | 0.275 | -1.4% | -0.0183 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 492 | -1.4% | -32.5 to 19 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.53 | 7.45 | -1.0% | -0.51 to 0.358 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1951 messages a second; base rate 292.7/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 730 | -0.3% | -12.3 to 7.94 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.0286 to 0.0231 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,359 | -0.7% | -319 to 285 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,649 | 3,679 | +0.8% | -138 to 198 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.3 | 10.4 | +1.2% | -11.1 to 11.3 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 327 | +0.1% | -35.1 to 35.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,348 | 3,316 | -1.0% | -344 to 280 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 287 | 288 | +0.1% | -29.5 to 30.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.34 | +16.9% | -0.49 to 1.17 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3.33 | +66.7% | -2.46 to 5.13 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.288 | 0.286 | -1.0% | -0.0222 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 515 | 510 | -1.0% | -38.5 to 28 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.56 | 1.55 | -0.7% | -0.132 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 10.7 | +433.3% | -10.1 to 27.5 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 6.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 368 | +0.1% | -2.39 to 3.41 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | +0.0% | -0.0102 to 0.0139 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,363 | 2,389 | +1.1% | -310 to 364 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,748 | 3,666 | -2.2% | -141 to -24.5 | GAIN |
| end-to-end latency, median (ms) | 8.17 | 8.19 | +0.2% | -0.157 to 0.191 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 322 | -0.1% | -26.4 to 25.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,700 | 1,718 | +1.1% | -61.3 to 97.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 144 | 143 | -0.1% | -12.1 to 11.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.282 | -1.0% | -0.031 to 0.0254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 504 | -1.0% | -53.3 to 43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.04 | -1.2% | -0.345 to 0.274 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
