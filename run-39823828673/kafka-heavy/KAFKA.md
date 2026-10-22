# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 145 | -1.9% | -7.16 to 1.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00361 to 0.00404 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,232 | +6.6% | 25.6 to 249 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,445 | 3,633 | +5.5% | -409 to 785 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% | -0.096 to 0.0433 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 280 | 314 | +12.0% | -3.34 to 70.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 653 | 643 | -1.6% | -69.9 to 49.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 51.2 | 57.6 | +12.7% | -1.77 to 14.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | -0.1% | -0.0129 to 0.00999 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.253 | 0.252 | -0.6% | -0.00759 to 0.00438 | EVEN, no difference beyond the noise |
| host CPU-seconds | 454 | 451 | -0.6% | -13.5 to 7.71 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.85 | 6.94 | +1.3% | -0.116 to 0.291 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
