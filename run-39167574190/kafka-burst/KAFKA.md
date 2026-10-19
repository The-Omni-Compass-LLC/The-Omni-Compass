# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.0% | -4.67 to 4.65 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0208 to 0.0212 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,468 | 2,493 | +1.0% | -212 to 261 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,852 | 3,598 | -6.6% | -694 to 186 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.61 | 9.41 | -2.1% | -0.706 to 0.306 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 378 | -1.5% | -32.7 to 21.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,654 | 1,625 | -1.7% | -119 to 61.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 163 | -2.0% | -18.5 to 11.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.298 | 0.292 | -1.9% | -0.0162 to 0.00471 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 204 | -2.0% | -11.4 to 3.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.33 | -2.0% | -0.145 to 0.0124 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
