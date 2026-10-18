# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 727 | +0.1% | -6.96 to 7.93 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.0104 to 0.0118 | same |
| end-to-end latency, 95th percentile (ms) | 2,258 | 2,142 | -5.2% | -1,104 to 871 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,555 | 3,346 | -5.9% | -1,912 to 1,494 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.56 | 7.45 | -1.4% | -0.358 to 0.143 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 290 | -4.4% | -146 to 119 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,174 | 3,072 | -3.2% | -1,392 to 1,189 | no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 252 | -4.3% | -121 to 98.3 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.317 | 0.315 | -0.4% | -0.0112 to 0.00846 | no difference beyond the noise |
| host CPU-seconds | 564 | 562 | -0.4% | -20.4 to 15.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.72 | -0.5% | -0.0801 to 0.0634 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
