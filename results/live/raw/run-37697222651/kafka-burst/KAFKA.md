# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 419 | +20.5% | 70 to 72.5 | better |
| throughput (messages a second consumed) | 417 | 419 | +0.4% | 1.72 to 1.77 | better |
| end-to-end latency, 95th percentile (ms) | 1,671 | 10.9 | -99.3% | -1,747 to -1,574 | better |
| end-to-end latency, 99th percentile (ms) | 2,462 | 13.6 | -99.4% | -2,775 to -2,122 | better |
| end-to-end latency, median (ms) | 10.2 | 7.96 | -22.0% | -3.44 to -1.05 | better |
| end-to-end latency, mean (ms) | 262 | 9.11 | -96.5% | -261 to -245 | better |
| consumer lag, most messages waiting at once | 1,102 | 49.7 | -95.5% | -1,113 to -991 | better |
| consumer lag, mean messages waiting | 116 | 3.82 | -96.7% | -117 to -108 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.84 | +191.9% | 3.33 to 4.34 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.318 | +7.3% | -0.00359 to 0.0468 | no difference beyond the noise |
| host CPU-seconds | 138 | 148 | +6.7% | -2.43 to 21.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 2.94 | -11.0% | -0.653 to -0.0767 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
