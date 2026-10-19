# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.1% | -3.16 to 3.68 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0279 to 0.0063 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,520 | 2,482 | -1.5% | -206 to 132 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,877 | 3,663 | -5.5% | -686 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.83 | 9.28 | -5.7% | -1.71 to 0.588 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 383 | -1.4% | -41.9 to 30.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,661 | 1,664 | +0.2% | -94.2 to 99.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 165 | -2.1% | -22.7 to 15.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% | -0.0203 to 0.0141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.0% | -14.3 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.37 | -1.1% | -0.204 to 0.13 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
