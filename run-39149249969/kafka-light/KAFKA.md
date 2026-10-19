# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.1% | -7.58 to 6.48 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0172 to 0.0149 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,250 | 2,242 | -0.4% | -318 to 301 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,564 | 3,544 | -0.6% | -227 to 187 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.38 | 7.86 | -6.2% | -1.28 to 0.243 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 303 | -0.5% | -32.6 to 29.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,212 | 3,206 | -0.2% | -190 to 178 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 265 | 263 | -0.7% | -28.3 to 24.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.325 | 0.327 | +0.6% | -0.013 to 0.0172 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 562 | +0.9% | -25.7 to 35.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | +1.0% | -0.0784 to 0.111 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
