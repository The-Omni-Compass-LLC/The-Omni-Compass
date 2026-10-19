# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 377 messages a second; base rate 56.6/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 150 | 147 | -1.6% | -13.1 to 8.27 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 166 | 166 | +0.0% | -0.000715 to 0.00147 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,208 | 1,905 | +57.7% | -2,248 to 3,642 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,155 | 3,126 | +45.1% | -3,014 to 4,956 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.1 | 11.1 | -0.3% | -0.151 to 0.0825 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 150 | 232 | +54.9% | -260 to 424 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 442 | 597 | +35.1% | -456 to 766 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 27.4 | 41.2 | +50.5% | -43.9 to 71.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.19 | +9.5% | -0.33 to 0.71 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.266 | 0.263 | -1.1% | -0.00407 to -0.00165 | GAIN |
| host CPU-seconds | 477 | 472 | -1.1% | -7.43 to -2.81 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 7.08 | 7.12 | +0.6% | -0.514 to 0.596 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 7.33 | +266.7% | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
