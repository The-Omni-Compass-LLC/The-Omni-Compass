# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 968 messages a second; base rate 108.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 364 | +7.4% | -75.2 to 126 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 416 | 416 | +0.0% | 0.000705 to 0.00816 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,508 | 1,592 | -36.5% | -3,848 to 2,017 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,822 | 2,548 | -33.3% | -4,926 to 2,377 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.66 | 8.46 | -2.3% | -1 to 0.594 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 244 | -35.9% | -542 to 269 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,622 | 1,179 | -27.3% | -1,757 to 871 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 105 | -35.6% | -230 to 114 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.882 to 1.37 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -2.2 to 3.54 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.293 | 0.293 | +0.1% | -0.00355 to 0.00436 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 210 | +0.2% | -2.65 to 3.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.23 | -6.0% | -1.07 to 0.661 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
