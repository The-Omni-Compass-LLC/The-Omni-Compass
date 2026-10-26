# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.5/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | +0.1% | -0.954 to 1.46 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | -0.0% | -0.0111 to 0.00959 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,197 | 2,181 | -0.7% | -40.2 to 8.62 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,595 | 3,519 | -2.1% | -198 to 47 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.56 | -0.1% | -0.115 to 0.0951 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 295 | 293 | -0.7% | -9.35 to 5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,613 | 1,590 | -1.4% | -70.2 to 24.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 130 | 129 | -0.5% | -3.86 to 2.58 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.306 | -0.5% | -0.0135 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 534 | 532 | -0.4% | -23.7 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.23 | -0.5% | -0.155 to 0.122 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
