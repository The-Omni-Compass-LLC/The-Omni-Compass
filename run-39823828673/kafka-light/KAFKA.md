# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -3.07 to 0.679 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.011 to 0.0239 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,298 | 2,297 | -0.0% | -235 to 234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,658 | 3,775 | +3.2% | -284 to 517 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.86 | 7.78 | -1.1% | -0.329 to 0.161 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 310 | +1.5% | -7.85 to 17 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,222 | 3,287 | +2.0% | -13.4 to 143 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 268 | +1.5% | -5.89 to 14.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.346 | 0.342 | -1.2% | -0.0116 to 0.00321 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 595 | -1.0% | -19.8 to 8.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.82 | -0.8% | -0.0592 to 0.0293 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
