# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 848 | +15.8% | 111 to 119 | better |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.055 to 0.0321 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,581 | 9.32 | -99.4% | -1,619 to -1,525 | better |
| end-to-end latency, 99th percentile (ms) | 2,440 | 10.7 | -99.6% | -2,573 to -2,285 | better |
| end-to-end latency, median (ms) | 8.36 | 6.03 | -27.9% | -2.35 to -2.31 | better |
| end-to-end latency, mean (ms) | 218 | 6.79 | -96.9% | -222 to -201 | better |
| consumer lag, most messages waiting at once | 2,189 | 128 | -94.1% | -2,099 to -2,022 | better |
| consumer lag, mean messages waiting | 191 | 5.9 | -96.9% | -191 to -179 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.5% | 5.93 to 5.93 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.34 | 0.405 | +19.2% | 0.0514 to 0.0789 | **WORSE** |
| host CPU-seconds | 390 | 466 | +19.5% | 59.5 to 92.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.83 | +3.2% | -0.00589 to 0.121 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
