# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1948 messages a second; base rate 292.2/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 728 | -0.1% | -7.19 to 5.48 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0194 to 0.0183 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,544 | 2,522 | -0.8% | -439 to 396 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,925 | 3,949 | +0.6% | -496 to 545 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.31 | 7.27 | -0.5% | -0.153 to 0.0755 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 339 | 340 | +0.3% | -60.1 to 62.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,445 | 3,479 | +1.0% | -403 to 470 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 295 | 296 | +0.4% | -50.8 to 53 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.418 to 0.654 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.3% | -0.00534 to 0.00699 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 564 | +0.4% | -9.07 to 14.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | +0.6% | -0.035 to 0.0542 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
