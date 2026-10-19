# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -1.12 to -0.862 | LOSS |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -0.00465 to 0.00917 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,501 | -1.8% | -186 to 94.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,713 | +1.7% | -291 to 417 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.76 | 8.69 | -0.8% | -0.123 to -0.00955 | GAIN |
| end-to-end latency, mean (ms) | 376 | 378 | +0.6% | -4.45 to 8.82 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,662 | 1,649 | -0.8% | -53 to 27 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 163 | -0.1% | -5.17 to 5.01 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.298 | -0.9% | -0.0138 to 0.00845 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 214 | -0.9% | -9.85 to 6.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.47 | -0.6% | -0.148 to 0.109 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
