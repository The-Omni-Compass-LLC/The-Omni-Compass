# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 984 messages a second; base rate 147.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.0% | -0.729 to 0.437 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | -0.0% | -0.00676 to 0.00261 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,491 | 2,461 | -1.2% | -159 to 100 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,811 | -1.5% | -221 to 105 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.04 | 8 | -0.5% | -0.157 to 0.0726 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 338 | 334 | -1.1% | -14.9 to 7.17 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,737 | 1,722 | -0.9% | -85.7 to 55.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 152 | 150 | -1.4% | -5.59 to 1.45 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.273 | 0.272 | -0.5% | -0.013 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 487 | 486 | -0.4% | -21.3 to 17.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.94 | 2.93 | -0.3% | -0.132 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
