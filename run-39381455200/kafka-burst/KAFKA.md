# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.97 to -0.233 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0178 to 0.018 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,570 | 2,568 | -0.1% | -218 to 214 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,694 | 3,744 | +1.4% | -215 to 315 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.28 | 9.24 | -0.5% | -0.523 to 0.427 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 384 | +0.6% | -2.16 to 6.42 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,651 | 1,663 | +0.8% | -34.3 to 59.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 166 | +0.2% | -3.81 to 4.49 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.289 | -0.6% | -0.0188 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 202 | -0.6% | -13.4 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | -0.3% | -0.202 to 0.185 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
