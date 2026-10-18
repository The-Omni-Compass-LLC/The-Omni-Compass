# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -2.39 to 0.814 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0144 to 0.0121 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,342 | 2,413 | +3.1% | -61.7 to 205 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,696 | 3,672 | -0.6% | -369 to 322 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.6 | +0.3% | -0.0906 to 0.139 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 323 | +2.5% | -12.1 to 28 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,669 | 1,709 | +2.4% | -50.5 to 132 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 143 | +2.3% | -7.41 to 13.9 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.314 | 0.313 | -0.5% | -0.00998 to 0.00698 | no difference beyond the noise |
| host CPU-seconds | 547 | 543 | -0.6% | -15.7 to 9.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.3 | -0.4% | -0.0862 to 0.0606 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
