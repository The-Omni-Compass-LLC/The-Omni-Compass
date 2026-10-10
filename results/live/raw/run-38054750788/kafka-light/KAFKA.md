# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 730 | +0.2% | -0.288 to 2.56 | no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.0176 to 0.0119 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,399 | 2,332 | -2.8% | -139 to 5.92 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,830 | 3,615 | -5.6% | -624 to 194 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.37 | -0.4% | -0.2 to 0.148 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 314 | -3.6% | -28.9 to 5.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,362 | 3,319 | -1.3% | -282 to 195 | no difference beyond the noise |
| consumer lag, mean messages waiting | 284 | 274 | -3.8% | -25 to 3.58 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.314 | 0.312 | -0.5% | -0.0103 to 0.00716 | no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.3% | -15.6 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | -0.5% | -0.053 to 0.036 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
