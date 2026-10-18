# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 972 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 337 | -0.9% | -6.17 to 0.288 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0226 to 0.0298 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,477 | 2,548 | +2.9% | -78.9 to 220 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,616 | 3,787 | +4.7% | -321 to 663 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.75 | 9.53 | -2.3% | -0.967 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 393 | +4.2% | -11.1 to 42.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,628 | 1,651 | +1.4% | -29.8 to 76.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 169 | +2.9% | -6 to 15.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.305 | -2.0% | -0.03 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 213 | -1.9% | -21.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.5 | -1.1% | -0.313 to 0.236 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
