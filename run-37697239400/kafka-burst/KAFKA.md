# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 418 | +20.2% | 69.3 to 71.4 | better |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0253 to 0.0229 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,735 | 11 | -99.4% | -1,879 to -1,569 | better |
| end-to-end latency, 99th percentile (ms) | 2,538 | 13.7 | -99.5% | -2,641 to -2,407 | better |
| end-to-end latency, median (ms) | 9.87 | 8 | -18.9% | -2.33 to -1.41 | better |
| end-to-end latency, mean (ms) | 266 | 8.76 | -96.7% | -259 to -256 | better |
| consumer lag, most messages waiting at once | 1,122 | 42 | -96.3% | -1,159 to -1,001 | better |
| consumer lag, mean messages waiting | 117 | 3.65 | -96.9% | -114 to -112 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 6.15 | +207.5% | 1.89 to 6.41 | **WORSE** |
| consumers running, most at once | 2 | 7.33 | +266.7% | 2.46 to 8.2 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.32 | +8.3% | 0.0141 to 0.0346 | **WORSE** |
| host CPU-seconds | 138 | 149 | +8.0% | 6.13 to 16.1 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 2.96 | -10.1% | -0.491 to -0.176 | better |
| consumer changes written (the knob's moves) | 2 | 14.7 | +633.3% | 6.93 to 18.4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
