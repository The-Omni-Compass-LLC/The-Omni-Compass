# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1937 messages a second; base rate 290.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 726 | +0.0% | -1.86 to 2.43 | no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0274 to 0.00906 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,428 | 2,441 | +0.5% | -50.3 to 75.1 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,968 | 3,728 | -6.0% | -493 to 12.8 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.19 | 8.16 | -0.3% | -0.542 to 0.492 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 329 | -1.1% | -12.3 to 4.85 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,400 | 3,367 | -1.0% | -178 to 114 | no difference beyond the noise |
| consumer lag, mean messages waiting | 289 | 286 | -1.0% | -10.7 to 4.75 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.341 | 0.336 | -1.3% | -0.0471 to 0.0384 | no difference beyond the noise |
| host CPU-seconds | 586 | 579 | -1.2% | -82.2 to 68.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.79 | 1.77 | -1.2% | -0.253 to 0.209 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
