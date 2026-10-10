# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1931 messages a second; base rate 289.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -2.74 to 2.41 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0179 to 0.00711 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,302 | -1.7% | -153 to 72.2 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,672 | 3,595 | -2.1% | -247 to 94.2 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.3 | 8.09 | -2.6% | -0.612 to 0.188 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 310 | -1.0% | -20.7 to 14.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,271 | 3,254 | -0.5% | -166 to 133 | no difference beyond the noise |
| consumer lag, mean messages waiting | 273 | 270 | -1.1% | -16.6 to 10.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.338 | 0.339 | +0.2% | -0.00679 to 0.0081 | no difference beyond the noise |
| host CPU-seconds | 581 | 583 | +0.3% | -8.68 to 12.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.78 | 1.78 | +0.3% | -0.0319 to 0.0441 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
