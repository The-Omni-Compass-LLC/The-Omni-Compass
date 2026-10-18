# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.2% | -2.18 to 0.487 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | +0.0% | -0.0166 to 0.0263 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,542 | 2,570 | +1.1% | -127 to 183 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,618 | 3,615 | -0.1% | -458 to 453 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.65 | 9.5 | -1.5% | -1.56 to 1.26 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 388 | +1.0% | -3.17 to 10.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,672 | 1,654 | -1.1% | -89.6 to 52.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 170 | +0.8% | -3.07 to 5.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.271 | 0.267 | -1.3% | -0.0244 to 0.0176 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 192 | -1.2% | -17.4 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.14 | 3.11 | -1.0% | -0.275 to 0.213 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
