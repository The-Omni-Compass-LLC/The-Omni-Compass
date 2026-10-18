# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1952 messages a second; base rate 292.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 737 | 858 | +16.4% | 117 to 125 | better |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.0429 to -0.014 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 1,692 | 8.68 | -99.5% | -1,765 to -1,602 | better |
| end-to-end latency, 99th percentile (ms) | 2,605 | 9.91 | -99.6% | -2,801 to -2,389 | better |
| end-to-end latency, median (ms) | 6.96 | 5.56 | -20.1% | -1.49 to -1.3 | better |
| end-to-end latency, mean (ms) | 228 | 6.38 | -97.2% | -233 to -209 | better |
| consumer lag, most messages waiting at once | 2,325 | 133 | -94.3% | -2,350 to -2,032 | better |
| consumer lag, mean messages waiting | 200 | 5.45 | -97.3% | -204 to -184 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.72 | +285.9% | 5.38 to 6.05 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.339 | +10.4% | 0.0227 to 0.041 | **WORSE** |
| host CPU-seconds | 365 | 402 | +10.3% | 25.7 to 49.2 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.65 | 1.56 | -5.3% | -0.131 to -0.0436 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 2.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
