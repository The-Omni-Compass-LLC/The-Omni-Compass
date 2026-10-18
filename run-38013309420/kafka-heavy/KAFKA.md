# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.619 to -0.189 | **WORSE** |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00315 to 0.00201 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,594 | 2,628 | +1.3% | -50.3 to 117 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,000 | 4,069 | +1.7% | -478 to 615 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.0% | -0.102 to 0.0993 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 350 | 357 | +1.9% | -7.97 to 20.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 739 | 737 | -0.3% | -30.7 to 26.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 65.1 | 65.7 | +0.8% | -0.209 to 1.31 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.282 | 0.282 | -0.2% | -0.0105 to 0.00933 | no difference beyond the noise |
| host CPU-seconds | 497 | 497 | -0.1% | -17.9 to 16.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.5 | +0.1% | -0.238 to 0.257 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
