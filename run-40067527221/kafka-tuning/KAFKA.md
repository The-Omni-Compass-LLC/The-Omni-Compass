# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 983 messages a second; base rate 147.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 369 | +0.1% | -0.0832 to 0.893 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | +0.0% | -0.00502 to 0.00507 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,437 | 2,412 | -1.0% | -87.2 to 37.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,758 | +0.8% | -104 to 163 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.01 | 8 | -0.2% | -0.0496 to 0.0236 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 327 | -0.8% | -14 to 8.64 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,735 | 1,710 | -1.4% | -99.5 to 50.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 147 | 147 | -0.6% | -4.56 to 2.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.267 | 0.266 | -0.5% | -0.00501 to 0.00231 | EVEN, no difference beyond the noise |
| host CPU-seconds | 478 | 476 | -0.4% | -7.5 to 3.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.88 | 2.87 | -0.6% | -0.0466 to 0.0146 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
