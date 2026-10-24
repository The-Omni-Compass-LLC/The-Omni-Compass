# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.2% | 0.195 to 0.383 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00173 to 0.000386 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,493 | 2,462 | -1.2% | -157 to 95 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,896 | 3,674 | -5.7% | -439 to -6.11 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.0% | -0.0279 to 0.0239 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 330 | -3.1% | -16.1 to -4.87 | GAIN |
| consumer lag, most messages waiting at once | 718 | 696 | -3.1% | -90.7 to 46.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.5 | 61 | -2.5% | -4.29 to 1.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.281 | -0.0% | -0.00609 to 0.00593 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 494 | -0.0% | -11.1 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 7.46 | -0.2% | -0.181 to 0.151 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
