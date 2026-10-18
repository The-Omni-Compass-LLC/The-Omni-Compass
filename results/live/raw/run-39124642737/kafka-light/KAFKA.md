# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 727 | -0.3% | -6.16 to 1.31 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.00582 to 0.0022 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,278 | 2,310 | +1.4% | -133 to 196 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,529 | 3,664 | +3.8% | 54.6 to 216 | LOSS |
| end-to-end latency, median (ms) | 7.43 | 7.5 | +0.8% | -0.179 to 0.303 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 301 | 312 | +3.6% | -16.1 to 37.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,211 | 3,276 | +2.0% | -119 to 250 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 262 | 272 | +3.9% | -13.1 to 33.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | -0.6% | -0.0104 to 0.00638 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 557 | -0.5% | -15.2 to 9.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.7 | -0.2% | -0.0391 to 0.0328 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
