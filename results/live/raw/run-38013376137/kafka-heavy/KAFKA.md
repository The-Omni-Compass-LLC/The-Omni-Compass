# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.767 to 0.794 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00331 to 0.00345 | same |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,349 | +0.7% | -76.3 to 107 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,701 | -1.0% | -103 to 28.5 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.2% | -0.318 to 0.272 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 315 | -1.3% | -20.8 to 12.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 681 | 689 | +1.1% | -17.3 to 32.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 57.9 | 57.8 | -0.1% | -4.52 to 4.36 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.274 | 0.274 | -0.0% | -0.0155 to 0.0153 | no difference beyond the noise |
| host CPU-seconds | 491 | 491 | -0.0% | -27.4 to 27.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.41 | -0.0% | -0.431 to 0.427 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
