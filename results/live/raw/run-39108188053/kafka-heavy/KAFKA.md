# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.38 to 0.64 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00178 to 0.00121 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,354 | 2,348 | -0.3% | -125 to 112 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,647 | +0.2% | -80.8 to 96.1 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.2 | -0.3% | -0.102 to 0.0237 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 317 | +0.7% | -6.79 to 11.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 688 | 680 | -1.1% | -31.5 to 16.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57 | 58.1 | +2.0% | -2.23 to 4.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.6% | -0.0271 to 0.0493 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.275 | 0.272 | -0.9% | -0.0105 to 0.00564 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 488 | -0.9% | -18.4 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.38 | -0.6% | -0.208 to 0.119 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
