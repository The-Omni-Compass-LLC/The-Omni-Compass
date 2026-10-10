# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -1.62 to 1.49 | no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.000852 to 0.00114 | same |
| end-to-end latency, 95th percentile (ms) | 2,328 | 2,303 | -1.0% | -264 to 216 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,624 | 3,548 | -2.1% | -432 to 281 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% | -0.0537 to 0.0337 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 310 | -0.3% | -35.9 to 34.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 684 | 666 | -2.6% | -69.7 to 33.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 56.5 | 56.3 | -0.4% | -5.15 to 4.72 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.277 | 0.276 | -0.5% | -0.00936 to 0.00644 | no difference beyond the noise |
| host CPU-seconds | 489 | 487 | -0.4% | -15.7 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.38 | 7.36 | -0.4% | -0.309 to 0.255 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
