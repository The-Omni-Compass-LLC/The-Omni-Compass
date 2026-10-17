# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -2.77 to 1.38 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.00596 to 0.00665 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,215 | 2,248 | +1.5% | 19.1 to 46 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,587 | 3,573 | -0.4% | -109 to 81.1 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.12 | -1.0% | -0.211 to 0.0459 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 294 | 296 | +0.7% | -8.3 to 12.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,610 | 1,599 | -0.7% | -73 to 50.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 129 | 130 | +0.7% | -4.06 to 5.96 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.14 | +7.0% | -0.364 to 0.644 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.295 | 0.294 | -0.6% | -0.00665 to 0.00304 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 524 | -0.6% | -12.5 to 6.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.19 | 3.18 | -0.4% | -0.0796 to 0.0549 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
