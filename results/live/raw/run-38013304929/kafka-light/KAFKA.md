# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1937 messages a second; base rate 290.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 729 | +0.0% | -12.3 to 13 | no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0109 to 0.0024 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,129 | -7.6% | -1,018 to 668 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,267 | -10.5% | -1,457 to 690 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.45 | 7.41 | -0.5% | -0.335 to 0.265 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 289 | -6.9% | -125 to 82.5 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,306 | 3,054 | -7.6% | -1,074 to 571 | no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 251 | -6.9% | -109 to 71.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.0115 to 0.00119 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.312 | -0.3% | -0.00633 to 0.0044 | no difference beyond the noise |
| host CPU-seconds | 558 | 556 | -0.3% | -14.9 to 12 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | -0.3% | -0.0576 to 0.0472 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
