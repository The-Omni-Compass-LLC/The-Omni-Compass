# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.1% | -3.21 to 3.72 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0247 to 0.0308 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,457 | -1.7% | -154 to 70 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,675 | 3,598 | -2.1% | -577 to 424 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.66 | 9.35 | -3.2% | -0.609 to -0.00603 | better |
| end-to-end latency, mean (ms) | 381 | 375 | -1.5% | -35.4 to 23.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,623 | 1,613 | -0.6% | -148 to 130 | no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 162 | -2.1% | -15.1 to 8.09 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.29 | -1.3% | -0.0249 to 0.0174 | no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.3% | -17.6 to 12.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.3 | -1.4% | -0.276 to 0.182 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
