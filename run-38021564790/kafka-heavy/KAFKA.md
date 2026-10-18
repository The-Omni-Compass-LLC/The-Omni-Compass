# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 148 | +0.1% | -0.765 to 0.941 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00143 to 0.00181 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,350 | 2,370 | +0.8% | -257 to 295 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,672 | -1.8% | -342 to 209 | no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% | -0.0667 to 0.0294 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 313 | -1.9% | -34 to 21.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 696 | 675 | -3.1% | -75 to 32.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 58.7 | 57 | -2.9% | -9.34 to 5.91 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.257 | 0.256 | -0.5% | -0.00604 to 0.00361 | no difference beyond the noise |
| host CPU-seconds | 460 | 458 | -0.5% | -10.6 to 6.48 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.94 | 6.9 | -0.5% | -0.15 to 0.0792 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
