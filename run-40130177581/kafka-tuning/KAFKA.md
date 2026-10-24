# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -1.51 to 0.0345 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0131 to 0.00704 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,276 | 2,276 | +0.0% | -314 to 314 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,563 | 3,688 | +3.5% | -138 to 387 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.06 | 8.01 | -0.6% | -0.251 to 0.148 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 309 | +1.4% | -16.1 to 24.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,642 | 1,653 | +0.7% | -81.9 to 105 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 136 | 137 | +1.1% | -7.96 to 11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% | -0.296 to 0.786 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.268 | 0.27 | +0.4% | -0.0093 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 480 | 482 | +0.5% | -15.8 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.9 | 2.92 | +0.7% | -0.0839 to 0.124 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
