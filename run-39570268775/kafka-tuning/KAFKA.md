# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.1/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -1.51 to 0.0138 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.837 to 0.517 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,448 | 2,470 | +0.9% | -89.7 to 133 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,815 | 3,769 | -1.2% | -134 to 41.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.14 | 8.1 | -0.5% | -0.21 to 0.128 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.5% | -10.5 to 20.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,711 | +0.4% | -49.8 to 64.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 145 | +1.3% | -5.38 to 9.18 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.304 | 0.303 | -0.4% | -0.0083 to 0.0057 | EVEN, no difference beyond the noise |
| host CPU-seconds | 547 | 545 | -0.3% | -14.2 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.3 | -0.1% | -0.0855 to 0.0788 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
