# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | +0.0% | -0.341 to 0.383 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0291 to 0.0215 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,608 | 2,659 | +2.0% | -92.2 to 194 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,906 | 3,790 | -3.0% | -297 to 64.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.63 | -1.4% | -0.594 to 0.354 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 398 | 398 | -0.1% | -8.76 to 8.15 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,731 | 1,724 | -0.4% | -45 to 32.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 172 | -0.4% | -8.27 to 6.98 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.289 | 0.282 | -2.2% | -0.0187 to 0.00575 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 203 | -2.2% | -13.4 to 4.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.28 | -2.2% | -0.216 to 0.0675 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
