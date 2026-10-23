# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1949 messages a second; base rate 292.3/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 733 | +0.1% | -3.14 to 3.97 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0366 to 0.0308 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,310 | 2,255 | -2.4% | -228 to 118 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,599 | 3,524 | -2.1% | -442 to 290 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.52 | 10 | +5.2% | -7.96 to 8.95 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 307 | -3.0% | -29.5 to 10.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,278 | 3,221 | -1.7% | -223 to 111 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 271 | -2.8% | -21.8 to 6.42 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.284 | 0.283 | -0.4% | -0.0122 to 0.00992 | EVEN, no difference beyond the noise |
| host CPU-seconds | 507 | 505 | -0.4% | -20.6 to 16.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.54 | 1.53 | -0.5% | -0.0634 to 0.0485 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
