# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.84 to 0.781 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0151 to 0.0134 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,540 | 2,510 | -1.2% | -199 to 138 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,765 | 3,595 | -4.5% | -750 to 410 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.89 | 8.67 | -2.5% | -0.617 to 0.17 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 380 | +0.2% | -4.07 to 5.49 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,647 | -0.5% | -103 to 86.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 165 | +0.1% | -1.62 to 2.09 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.302 | 0.299 | -1.1% | -0.0202 to 0.0135 | no difference beyond the noise |
| host CPU-seconds | 217 | 214 | -1.1% | -14.4 to 9.72 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.51 | 3.48 | -1.1% | -0.241 to 0.166 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
