# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1951 messages a second; base rate 292.7/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 731 | -0.2% | -6.08 to 2.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 858 | 858 | +0.0% | -1.05 to 1.69 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,293 | 2,319 | +1.1% | -69.2 to 121 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,605 | -2.3% | -358 to 187 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 15.4 | 11.2 | -27.2% | -17.3 to 8.9 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 324 | +0.5% | -12.7 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,305 | 3,332 | +0.8% | -154 to 208 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 285 | -0.3% | -14.2 to 12.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.286 | 0.283 | -1.0% | -0.0211 to 0.0156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 506 | -0.9% | -35 to 25.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.54 | -0.7% | -0.0935 to 0.0734 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
