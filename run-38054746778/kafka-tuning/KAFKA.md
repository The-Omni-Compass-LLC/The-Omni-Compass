# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -3.12 to 0.719 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00285 to -0.000739 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 2,344 | 2,424 | +3.4% | -172 to 332 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,647 | 3,792 | +4.0% | -57.8 to 348 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.68 | 8.67 | -0.1% | -0.388 to 0.37 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 329 | +4.4% | -22.3 to 50.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,678 | 1,724 | +2.8% | -81.7 to 174 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 145 | +4.2% | -9.77 to 21.5 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.321 | 0.32 | -0.3% | -0.0232 to 0.0215 | no difference beyond the noise |
| host CPU-seconds | 558 | 556 | -0.2% | -40 to 37.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | +0.1% | -0.243 to 0.249 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
