# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1963 messages a second; base rate 294.5/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.2% | -5.91 to 3.53 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 864 | 864 | +0.0% | -0.117 to 0.137 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,641 | 2,644 | +0.1% | -277 to 282 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,061 | 4,011 | -1.2% | -295 to 196 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.91 | 8.24 | -7.6% | -1.02 to -0.329 | GAIN |
| end-to-end latency, mean (ms) | 362 | 363 | +0.1% | -39.5 to 40.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,609 | 3,582 | -0.8% | -203 to 149 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 321 | 320 | -0.3% | -34.4 to 32.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.321 | +7.5% | -0.0169 to 0.0615 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 571 | +7.3% | -29.8 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.61 | 1.73 | +7.5% | -0.0924 to 0.333 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
