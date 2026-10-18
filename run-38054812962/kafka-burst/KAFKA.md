# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 338 | -0.5% | -5.44 to 1.73 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.00662 to 0.018 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,480 | 2,494 | +0.5% | -183 to 210 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,666 | 3,922 | +7.0% | -358 to 868 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.58 | 9.21 | -3.8% | -0.87 to 0.138 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 392 | +2.6% | -16.3 to 36.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,650 | 1,666 | +0.9% | -84.2 to 115 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 168 | +1.9% | -7.46 to 13.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.291 | -1.0% | -0.0248 to 0.0192 | no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.9% | -17.2 to 13.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.34 | -0.3% | -0.281 to 0.258 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
