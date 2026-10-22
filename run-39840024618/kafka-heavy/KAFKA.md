# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -1.2 to 1.13 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00229 to 0.00104 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,399 | 2,383 | -0.6% | -354 to 323 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,697 | 3,652 | -1.2% | -539 to 449 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.7 | -0.5% | -0.311 to 0.188 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 323 | +0.3% | -39 to 41 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 690 | 698 | +1.2% | -37.3 to 53.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.8 | 59.6 | +1.3% | -5.24 to 6.78 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.291 | 0.286 | -1.7% | -0.0233 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 513 | 505 | -1.7% | -41.4 to 24.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.77 | 7.64 | -1.7% | -0.685 to 0.427 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
