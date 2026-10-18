# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 420 | +20.8% | 71.8 to 72.7 | better |
| throughput (messages a second consumed) | 419 | 421 | +0.4% | 1.72 to 1.76 | better |
| end-to-end latency, 95th percentile (ms) | 1,701 | 11 | -99.4% | -1,804 to -1,575 | better |
| end-to-end latency, 99th percentile (ms) | 2,515 | 13.2 | -99.5% | -2,617 to -2,388 | better |
| end-to-end latency, median (ms) | 10 | 7.97 | -20.7% | -3.09 to -1.08 | better |
| end-to-end latency, mean (ms) | 267 | 8.85 | -96.7% | -264 to -253 | better |
| consumer lag, most messages waiting at once | 1,129 | 42.3 | -96.3% | -1,140 to -1,034 | better |
| consumer lag, mean messages waiting | 118 | 3.71 | -96.9% | -121 to -108 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.67 | +183.3% | 3.06 to 4.27 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.314 | +6.4% | -0.00484 to 0.0426 | no difference beyond the noise |
| host CPU-seconds | 138 | 146 | +5.7% | -3.07 to 18.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 2.89 | -12.1% | -0.655 to -0.139 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
