# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.0% | -3.17 to 3.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | 0.000764 to 0.0238 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,641 | 2,591 | -1.9% | -148 to 48 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,985 | 3,987 | +0.0% | -441 to 445 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.31 | 9.02 | -3.1% | -1.07 to 0.5 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 393 | -1.4% | -42.3 to 30.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,724 | 1,711 | -0.8% | -55 to 28.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 170 | -1.6% | -17.8 to 12.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.309 | -0.5% | -0.0224 to 0.0193 | EVEN, no difference beyond the noise |
| host CPU-seconds | 219 | 218 | -0.4% | -15.6 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.54 | -0.4% | -0.248 to 0.216 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
