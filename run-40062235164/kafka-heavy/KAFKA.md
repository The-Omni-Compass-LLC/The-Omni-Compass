# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.56 to 0.607 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00147 to 0.0047 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,538 | +3.2% | 33.4 to 126 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,843 | 3,824 | -0.5% | -494 to 456 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.3% | -0.0697 to 0.00636 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 344 | +3.4% | -11.6 to 34.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 711 | 720 | +1.2% | -38.6 to 56 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61 | 63.1 | +3.4% | -0.517 to 4.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.281 | -1.2% | -0.0131 to 0.00632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 502 | 496 | -1.2% | -24 to 11.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.5 | -0.9% | -0.283 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
