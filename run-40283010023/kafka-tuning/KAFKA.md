# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

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
