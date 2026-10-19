# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1953 messages a second; base rate 292.9/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 733 | -0.0% | -7.81 to 7.74 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 859 | 859 | +0.0% | -1.05 to 1.69 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,351 | 2,299 | -2.2% | -331 to 228 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,734 | 3,630 | -2.8% | -469 to 261 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.33 | 10.4 | +11.5% | -7.49 to 9.63 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 324 | 319 | -1.6% | -38.3 to 28.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,341 | 3,282 | -1.8% | -387 to 269 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 281 | -1.7% | -32.8 to 23.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.281 | 0.279 | -0.6% | -0.00994 to 0.00634 | EVEN, no difference beyond the noise |
| host CPU-seconds | 502 | 498 | -0.7% | -18.4 to 11.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.52 | 1.51 | -0.6% | -0.0672 to 0.0479 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
