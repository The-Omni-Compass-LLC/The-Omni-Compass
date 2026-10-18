# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 344 | 343 | -0.2% | -3.16 to 2.12 | no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.1% | -2.07 to 1.3 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,605 | 2,539 | -2.5% | -213 to 80.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,805 | +1.5% | -433 to 549 | no difference beyond the noise |
| end-to-end latency, median (ms) | 12 | 9.95 | -17.0% | -11.7 to 7.66 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 395 | 389 | -1.3% | -16.9 to 6.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,710 | 1,678 | -1.9% | -142 to 77.8 | no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 169 | -2.2% | -14.1 to 6.35 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.286 | 0.265 | -7.1% | -0.0828 to 0.0423 | no difference beyond the noise |
| host CPU-seconds | 205 | 191 | -6.9% | -57.3 to 29.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.07 | -6.8% | -0.93 to 0.481 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
