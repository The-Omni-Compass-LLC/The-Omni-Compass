# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.21 to 0.544 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00448 to 0.00447 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,550 | +0.1% | -74.8 to 81.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,841 | 3,955 | +3.0% | -281 to 509 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.6 | -0.3% | -0.117 to 0.0417 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 348 | +2.1% | -20.8 to 35 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 711 | 732 | +2.9% | -10.4 to 51.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.5 | 63.5 | +1.6% | -3.46 to 5.47 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.289 | 0.284 | -1.6% | -0.0134 to 0.0041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 501 | -1.6% | -23.7 to 7.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 7.58 | -1.4% | -0.376 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
