# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 969 messages a second; base rate 145.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 426 | +15.4% | 53.6 to 59.8 | better |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.0291 to 0.0235 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,486 | 10.1 | -99.3% | -1,549 to -1,403 | better |
| end-to-end latency, 99th percentile (ms) | 2,356 | 11.9 | -99.5% | -2,518 to -2,170 | better |
| end-to-end latency, median (ms) | 8.59 | 7.3 | -15.1% | -1.36 to -1.23 | better |
| end-to-end latency, mean (ms) | 203 | 7.72 | -96.2% | -213 to -178 | better |
| consumer lag, most messages waiting at once | 1,072 | 45.7 | -95.7% | -1,090 to -963 | better |
| consumer lag, mean messages waiting | 91.3 | 3.34 | -96.3% | -94.4 to -81.4 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.5% | 5.92 to 5.93 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.334 | +8.6% | 0.0114 to 0.0417 | **WORSE** |
| host CPU-seconds | 355 | 386 | +8.7% | 14.1 to 47.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.02 | -5.8% | -0.345 to -0.0266 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
