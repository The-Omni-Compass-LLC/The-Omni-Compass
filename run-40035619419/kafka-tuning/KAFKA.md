# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 964 messages a second; base rate 144.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.3% | -8.25 to 5.71 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 424 | 424 | +0.0% | -0.00572 to 0.00888 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,902 | 1,938 | +1.9% | -264 to 335 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,127 | 3,143 | +0.5% | -383 to 416 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.18 | 8.11 | -0.8% | -0.565 to 0.438 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 246 | 251 | +2.0% | -40.9 to 50.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,469 | 1,467 | -0.2% | -160 to 155 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 108 | 110 | +1.7% | -16.1 to 19.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.38 | +19.1% | 0.377 to 0.388 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.298 | 0.292 | -2.1% | -0.0322 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 521 | -2.1% | -56.2 to 33.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.16 | -1.8% | -0.391 to 0.277 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
