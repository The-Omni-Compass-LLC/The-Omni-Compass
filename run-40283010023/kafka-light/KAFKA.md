# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1915 messages a second; base rate 287.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 720 | -0.4% | -16 to 9.73 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 842 | 842 | +0.0% | -0.0497 to 0.0939 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,100 | 2,098 | -0.1% | -54.4 to 50.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,386 | 3,338 | -1.4% | -478 to 382 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.2 | -0.6% | -0.47 to 0.374 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 275 | 280 | +1.8% | -20.9 to 30.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,045 | 3,019 | -0.9% | -55.3 to 3.29 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 236 | 240 | +1.7% | -17.2 to 25.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.1 | +4.9% | -0.308 to 0.503 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.378 | 0.372 | -1.5% | -0.014 to 0.00249 | EVEN, no difference beyond the noise |
| host CPU-seconds | 652 | 641 | -1.7% | -20.8 to -1.81 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 2 | 1.98 | -1.3% | -0.0753 to 0.0233 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -7.01 to 13.7 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
