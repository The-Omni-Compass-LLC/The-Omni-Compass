# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -1.26 to 1.16 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00297 to 0.0024 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,420 | 2,431 | +0.5% | -106 to 129 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,733 | 3,719 | -0.4% | -714 to 686 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.104 to 0.0507 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 325 | -0.3% | -30.4 to 28.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 689 | 691 | +0.2% | -22.7 to 26.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 59.7 | 59.1 | -1.1% | -5.31 to 4.04 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.282 | 0.278 | -1.3% | -0.0162 to 0.00878 | no difference beyond the noise |
| host CPU-seconds | 497 | 491 | -1.2% | -28.2 to 16 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.41 | -1.2% | -0.415 to 0.236 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
