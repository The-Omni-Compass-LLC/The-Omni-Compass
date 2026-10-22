# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 983 messages a second; base rate 110.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 343 | -0.1% | -1.13 to 0.472 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 423 | 422 | -0.0% | -0.0112 to 0.00711 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,633 | 2,507 | -4.8% | -465 to 213 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,859 | 3,934 | +1.9% | -351 to 501 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 22.3 | 13.2 | -40.6% | -24.9 to 6.76 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 407 | 405 | -0.3% | -8.41 to 6.12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,725 | 1,734 | +0.5% | -111 to 130 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 179 | 178 | -0.8% | -4.94 to 2.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.259 | 0.258 | -0.5% | -0.00694 to 0.00445 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 185 | -0.5% | -4.9 to 3.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3 | 2.99 | -0.4% | -0.0827 to 0.061 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
