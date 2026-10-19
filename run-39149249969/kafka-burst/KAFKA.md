# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.471 to 0.251 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.00472 to 0.00216 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,515 | 2,536 | +0.9% | -179 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,727 | -3.8% | -698 to 404 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.96 | 8.77 | -2.2% | -0.674 to 0.283 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 382 | +0.8% | -4.45 to 10.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,661 | -0.2% | -72.8 to 67.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 165 | +0.8% | -1.6 to 4.16 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.304 | -1.1% | -0.0243 to 0.0173 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 218 | -1.1% | -17.3 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.55 | -1.1% | -0.276 to 0.197 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
