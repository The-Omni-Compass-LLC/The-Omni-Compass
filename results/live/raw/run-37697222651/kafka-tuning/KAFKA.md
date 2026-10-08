# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 428 | +16.0% | 56 to 62.3 | better |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00576 to 0.00206 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,617 | 10.2 | -99.4% | -1,742 to -1,471 | better |
| end-to-end latency, 99th percentile (ms) | 2,500 | 12.1 | -99.5% | -2,676 to -2,300 | better |
| end-to-end latency, median (ms) | 8.52 | 7.31 | -14.2% | -1.43 to -0.992 | better |
| end-to-end latency, mean (ms) | 221 | 7.92 | -96.4% | -237 to -188 | better |
| consumer lag, most messages waiting at once | 1,142 | 67 | -94.1% | -1,153 to -996 | better |
| consumer lag, mean messages waiting | 98.6 | 3.47 | -96.5% | -105 to -85.5 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.27 | +263.5% | 2.43 to 8.11 | **WORSE** |
| consumers running, most at once | 2 | 7.33 | +266.7% | 2.46 to 8.2 | **WORSE** |
| host CPU busy (share of the run) | 0.308 | 0.329 | +6.9% | 0.0144 to 0.0282 | **WORSE** |
| host CPU-seconds | 357 | 381 | +6.9% | 17.4 to 31.7 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 2.97 | -7.9% | -0.35 to -0.157 | better |
| consumer changes written (the knob's moves) | 2 | 14.7 | +633.3% | 6.93 to 18.4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
