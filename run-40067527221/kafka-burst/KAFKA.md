# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 972 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -1.19 to -0.254 | LOSS |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0188 to 0.00901 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,408 | 2,435 | +1.1% | -456 to 510 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,588 | 3,500 | -2.5% | -413 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.6 | +0.0% | -0.0602 to 0.0635 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 366 | 366 | -0.0% | -37.6 to 37.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,597 | 1,604 | +0.4% | -49.2 to 63.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 158 | -0.3% | -16.6 to 15.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.283 | -0.7% | -0.00693 to 0.00308 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 203 | -0.6% | -4.84 to 2.31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.3 | -0.4% | -0.0726 to 0.0454 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
