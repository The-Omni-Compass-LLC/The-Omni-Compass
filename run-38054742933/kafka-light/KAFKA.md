# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 723 | -0.3% | -8.53 to 3.91 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -1.01 to 1.66 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,368 | 2,372 | +0.1% | -343 to 350 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,789 | +4.1% | -94.3 to 392 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.26 | 7.99 | -3.3% | -1.04 to 0.491 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 323 | +2.1% | -36.6 to 50.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,283 | 3,313 | +0.9% | -138 to 197 | no difference beyond the noise |
| consumer lag, mean messages waiting | 275 | 280 | +1.9% | -36 to 46.7 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.336 | 0.336 | -0.1% | -0.032 to 0.031 | no difference beyond the noise |
| host CPU-seconds | 577 | 578 | +0.1% | -53.4 to 54.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.77 | +0.4% | -0.14 to 0.155 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
