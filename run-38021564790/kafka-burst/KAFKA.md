# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -2.23 to -0.215 | **WORSE** |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0184 to 0.0145 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,471 | 2,474 | +0.1% | -110 to 114 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,768 | 3,732 | -1.0% | -368 to 296 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.47 | 9.28 | -2.0% | -0.826 to 0.448 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 380 | +0.5% | -3.9 to 7.6 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,641 | 1,633 | -0.4% | -21.5 to 6.79 | no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.5% | -5.22 to 6.91 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.293 | -0.7% | -0.0145 to 0.0102 | no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.7% | -9.87 to 7.11 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.34 | -0.3% | -0.143 to 0.122 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
