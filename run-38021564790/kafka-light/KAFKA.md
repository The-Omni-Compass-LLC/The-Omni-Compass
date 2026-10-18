# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 728 | -0.2% | -5.22 to 1.82 | no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0156 to 0.0133 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,474 | 2,503 | +1.2% | -77.5 to 136 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,743 | -2.1% | -712 to 548 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.45 | +0.8% | -0.152 to 0.274 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 333 | +1.5% | -17.2 to 27.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,394 | 3,433 | +1.2% | -13.8 to 93.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 291 | +1.6% | -13.4 to 22.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.32 | 0.319 | -0.2% | -0.00656 to 0.00499 | no difference beyond the noise |
| host CPU-seconds | 570 | 568 | -0.3% | -9.26 to 6.09 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.73 | -0.0% | -0.0173 to 0.0157 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
