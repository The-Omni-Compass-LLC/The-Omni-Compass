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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
