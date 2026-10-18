# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 768 | +5.4% | -132 to 210 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.0329 to 0.0539 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,198 | 1,464 | -33.4% | -3,583 to 2,115 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,624 | 2,514 | -30.6% | -5,915 to 3,694 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.52 | 7.09 | -5.7% | -1.52 to 0.67 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 298 | 204 | -31.5% | -477 to 289 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,213 | 2,253 | -29.9% | -4,582 to 2,661 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 178 | -31.4% | -413 to 250 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +16.2% | -0.442 to 1.09 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.316 | +0.9% | 0.000294 to 0.00548 | power given |
| host CPU-seconds | 556 | 563 | +1.2% | 0.969 to 11.9 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.64 | -3.6% | -0.426 to 0.305 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
