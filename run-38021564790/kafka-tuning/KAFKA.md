# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.0% | -2.85 to 2.68 | no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0183 to 0.0149 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,355 | +2.2% | -218 to 321 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,641 | 3,589 | -1.4% | -443 to 339 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.73 | 8.71 | -0.2% | -0.298 to 0.261 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 311 | -0.6% | -29.3 to 25.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,656 | 1,657 | +0.1% | -57.2 to 59.2 | no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 137 | -0.4% | -13 to 11.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.323 | 0.325 | +0.5% | -0.00644 to 0.00967 | no difference beyond the noise |
| host CPU-seconds | 561 | 565 | +0.8% | -11.9 to 20.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.44 | +0.8% | -0.0908 to 0.147 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
