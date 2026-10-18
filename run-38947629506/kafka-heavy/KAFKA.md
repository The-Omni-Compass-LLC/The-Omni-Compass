# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 389 messages a second; base rate 58.4/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 154 | +5.1% | -28 to 43.1 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00326 to 0.00368 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,107 | 1,424 | -32.4% | -3,519 to 2,152 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,393 | 2,272 | -33.0% | -5,549 to 3,307 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.5% | -0.42 to 0.313 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 282 | 196 | -30.3% | -454 to 283 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 637 | 448 | -29.8% | -970 to 590 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 51.7 | 36.2 | -30.0% | -82.5 to 51.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.3 | +15.1% | -0.372 to 0.977 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.279 | 0.281 | +0.5% | -0.00857 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 494 | +0.6% | -15.2 to 21.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.43 | 7.15 | -3.8% | -2.03 to 1.48 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
