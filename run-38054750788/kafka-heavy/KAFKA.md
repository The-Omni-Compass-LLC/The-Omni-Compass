# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.847 to 0.571 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00192 to 0.00214 | same |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,501 | -0.6% | -172 to 144 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,867 | 3,780 | -2.2% | -567 to 394 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | +0.0% | -0.0635 to 0.0708 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 339 | -0.6% | -21.2 to 16.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 722 | 720 | -0.2% | -20.3 to 17.6 | no difference beyond the noise |
| consumer lag, mean messages waiting | 63.2 | 62 | -2.0% | -4.43 to 1.85 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.5% | -0.00445 to 0.00166 | no difference beyond the noise |
| host CPU-seconds | 497 | 495 | -0.4% | -7.61 to 3.38 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.51 | 7.48 | -0.3% | -0.118 to 0.0685 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
