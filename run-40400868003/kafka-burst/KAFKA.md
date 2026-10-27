# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 347 | 347 | +0.1% | -0.906 to 1.92 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.00887 to 0.0304 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,706 | 1,711 | +0.3% | -66.6 to 75.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,500 | 2,497 | -0.1% | -205 to 198 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.83 | 9.83 | +0.0% | -0.804 to 0.804 | EVEN, the same |
| end-to-end latency, mean (ms) | 266 | 265 | -0.3% | -2 to 0.537 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,128 | 1,144 | +1.4% | -31.4 to 63.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 117 | 116 | -0.7% | -1.95 to 0.349 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.294 | -2.3% | -0.048 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 141 | 138 | -2.3% | -22.7 to 16.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.28 | -2.5% | -0.551 to 0.384 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
