# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.957 to 0.563 | no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.000563 to 0.00186 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,185 | 2,144 | -1.9% | -190 to 108 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,389 | 3,466 | +2.3% | -87.2 to 240 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.1 | 11.1 | +0.1% | -0.0928 to 0.112 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 285 | 288 | +1.3% | -20 to 27.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 648 | 644 | -0.7% | -17.1 to 8.42 | no difference beyond the noise |
| consumer lag, mean messages waiting | 51.9 | 52.4 | +1.2% | -2.16 to 3.35 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.0115 to 0.00119 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.266 | 0.266 | -0.2% | -0.00584 to 0.00479 | no difference beyond the noise |
| host CPU-seconds | 478 | 477 | -0.2% | -10.3 to 8.49 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.21 | 7.21 | -0.1% | -0.157 to 0.15 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
