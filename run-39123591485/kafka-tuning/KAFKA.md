# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.4/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -3.12 to 1.49 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.841 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,442 | 2,476 | +1.4% | -154 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,746 | 3,782 | +1.0% | -470 to 542 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.89 | 7.91 | +0.2% | -0.113 to 0.146 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.5% | -31.2 to 40.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,710 | 1,721 | +0.6% | -67.7 to 88.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 145 | +1.2% | -14.6 to 17.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.283 | -0.6% | -0.00735 to 0.00421 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 507 | -0.6% | -14.9 to 8.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.07 | -0.4% | -0.0725 to 0.0466 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
