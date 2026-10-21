# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

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
