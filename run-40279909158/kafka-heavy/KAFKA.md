# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.41 to 0.382 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00262 to 0.00211 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,148 | 2,190 | +1.9% | -127 to 211 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,398 | 3,476 | +2.3% | -120 to 275 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.5% | -0.381 to 0.262 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 284 | 293 | +3.0% | -17 to 34.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 657 | 653 | -0.6% | -83.8 to 75.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52.1 | 53.8 | +3.1% | -2.73 to 6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.06 | +3.2% | 0.0604 to 0.0667 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.279 | 0.275 | -1.4% | -0.0183 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 492 | -1.4% | -32.5 to 19 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.53 | 7.45 | -1.0% | -0.51 to 0.358 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
