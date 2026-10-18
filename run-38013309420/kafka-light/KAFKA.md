# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | +0.0% | -4.29 to 4.78 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0256 to 0.017 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,306 | 2,305 | -0.1% | -301 to 298 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,623 | 3,540 | -2.3% | -447 to 280 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.23 | -1.0% | -0.425 to 0.26 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 310 | -0.9% | -30.4 to 24.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,231 | 3,249 | +0.5% | -143 to 178 | no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 269 | -0.8% | -25.4 to 21.2 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.331 | 0.327 | -1.4% | -0.0164 to 0.007 | no difference beyond the noise |
| host CPU-seconds | 570 | 563 | -1.3% | -28.4 to 13.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.72 | -1.3% | -0.0876 to 0.0415 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
