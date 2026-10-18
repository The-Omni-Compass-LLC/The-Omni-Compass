# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -3.66 to 2.52 | no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00375 to 0.000242 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,386 | +0.2% | -437 to 448 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,683 | 3,717 | +0.9% | -120 to 189 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.15 | 8.13 | -0.2% | -0.0852 to 0.0459 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 315 | +0.6% | -35.3 to 38.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,682 | +0.3% | -189 to 199 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 139 | +0.4% | -15.2 to 16.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.294 | -0.4% | -0.00615 to 0.0039 | no difference beyond the noise |
| host CPU-seconds | 527 | 525 | -0.3% | -11.6 to 8.55 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.19 | 3.19 | -0.1% | -0.0839 to 0.0753 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
