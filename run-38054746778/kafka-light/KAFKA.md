# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 726 | -0.2% | -5.93 to 2.51 | no difference beyond the noise |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.033 to 0.026 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,466 | 2,503 | +1.5% | -10.9 to 84.7 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,831 | 3,886 | +1.4% | -101 to 211 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.28 | 8.21 | -0.8% | -0.985 to 0.844 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 336 | 343 | +2.0% | -4.79 to 18.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,417 | 3,435 | +0.5% | -156 to 191 | no difference beyond the noise |
| consumer lag, mean messages waiting | 293 | 299 | +2.1% | -0.744 to 13 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.332 | 0.332 | -0.0% | -0.0126 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 570 | 572 | +0.2% | -22 to 24.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.75 | +0.5% | -0.0708 to 0.0866 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
