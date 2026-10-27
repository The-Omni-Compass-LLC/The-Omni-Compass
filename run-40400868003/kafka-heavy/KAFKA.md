# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.6% | -5.18 to 3.39 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00699 to 0.00556 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,567 | 1,543 | -1.6% | -206 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,435 | 2,433 | -0.1% | -551 to 547 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.7 | +0.4% | -0.0198 to 0.104 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 214 | 221 | +2.9% | -44.5 to 57.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 463 | 469 | +1.3% | -98 to 110 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 39.9 | 41.4 | +3.9% | -9.46 to 12.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.23 | +11.6% | -0.247 to 0.713 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.283 | 0.284 | +0.7% | -0.0113 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 334 | +0.7% | -13.1 to 18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.46 | 7.56 | +1.4% | -0.0438 to 0.247 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | -2.61 to 14.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
