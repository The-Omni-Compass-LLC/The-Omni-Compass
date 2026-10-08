# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 172 | +16.0% | 22.2 to 25.3 | better |
| throughput (messages a second consumed) | 172 | 172 | -0.1% | -0.465 to 0.152 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,608 | 14.2 | -99.1% | -1,763 to -1,426 | better |
| end-to-end latency, 99th percentile (ms) | 2,545 | 18.4 | -99.3% | -2,817 to -2,236 | better |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -1.3% | -1.04 to 0.728 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 223 | 12.1 | -94.6% | -241 to -180 | better |
| consumer lag, most messages waiting at once | 487 | 27.3 | -94.4% | -494 to -426 | better |
| consumer lag, mean messages waiting | 42.1 | 2.1 | -95.0% | -45 to -35.1 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.83 | +191.7% | 3.8 to 3.86 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.324 | +9.4% | -0.0313 to 0.0872 | no difference beyond the noise |
| host CPU-seconds | 352 | 384 | +9.0% | -34.4 to 97.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.9 | 7.41 | -6.1% | -1.83 to 0.863 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 2.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
