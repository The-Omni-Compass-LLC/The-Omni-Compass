# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -2.56 to 2.15 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0129 to 0.00835 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,390 | 2,431 | +1.7% | -226 to 308 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,737 | 3,708 | -0.8% | -354 to 296 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.61 | 8.58 | -0.4% | -0.196 to 0.121 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 321 | +0.7% | -12.9 to 17.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,686 | +1.1% | -85 to 122 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 142 | +0.5% | -7.18 to 8.71 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.311 | -1.6% | -0.0288 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 539 | -1.6% | -54.4 to 37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.28 | -1.5% | -0.349 to 0.246 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
