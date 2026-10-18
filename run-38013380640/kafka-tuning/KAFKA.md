# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.05 to 0.0225 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00451 to 0.00169 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,303 | 2,304 | +0.0% | -154 to 156 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,561 | 3,685 | +3.5% | -128 to 375 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.43 | 8.41 | -0.2% | -0.117 to 0.076 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 309 | +1.3% | -9.48 to 17.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,646 | 1,642 | -0.2% | -47.4 to 40.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 136 | +1.0% | -4.78 to 7.38 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.315 | 0.314 | -0.5% | -0.00858 to 0.00522 | no difference beyond the noise |
| host CPU-seconds | 562 | 559 | -0.5% | -14.6 to 8.88 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.4 | -0.4% | -0.0794 to 0.0543 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
