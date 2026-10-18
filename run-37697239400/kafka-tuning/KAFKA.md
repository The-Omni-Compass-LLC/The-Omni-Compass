# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 429 | +16.3% | 55.4 to 65.1 | better |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0163 to 0.00336 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,777 | 9.81 | -99.4% | -2,336 to -1,198 | better |
| end-to-end latency, 99th percentile (ms) | 2,729 | 12.8 | -99.5% | -3,367 to -2,066 | better |
| end-to-end latency, median (ms) | 8.17 | 7 | -14.3% | -1.3 to -1.03 | better |
| end-to-end latency, mean (ms) | 238 | 7.63 | -96.8% | -301 to -159 | better |
| consumer lag, most messages waiting at once | 1,231 | 49 | -96.0% | -1,441 to -923 | better |
| consumer lag, mean messages waiting | 106 | 3.32 | -96.9% | -134 to -71.3 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.6% | 5.93 to 5.94 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.31 | +5.1% | 0.00799 to 0.0223 | **WORSE** |
| host CPU-seconds | 351 | 368 | +4.9% | 10.2 to 24.3 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 2.86 | -9.8% | -0.351 to -0.271 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
