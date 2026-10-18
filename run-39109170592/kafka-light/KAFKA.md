# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1917 messages a second; base rate 287.6/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 728 | -0.2% | -5.31 to 3.09 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 843 | 843 | -0.0% | -0.0294 to 0.0185 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,971 | 1,943 | -1.4% | -173 to 117 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,170 | 3,235 | +2.0% | -234 to 364 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.29 | 7.14 | -2.1% | -0.525 to 0.223 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 251 | 253 | +1.0% | -4.2 to 9.15 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,893 | 2,914 | +0.7% | -30.6 to 71.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 216 | 217 | +0.6% | -6.32 to 8.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | +19.3% | 0.383 to 0.39 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.332 | 0.334 | +0.6% | -0.00305 to 0.00681 | EVEN, no difference beyond the noise |
| host CPU-seconds | 592 | 596 | +0.7% | -6.43 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.82 | +0.8% | -0.0164 to 0.0464 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
