# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.2% | -1.79 to 0.434 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0279 to 0.0125 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,524 | +2.6% | -109 to 238 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,707 | 3,514 | -5.2% | -822 to 436 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.5 | -0.7% | -0.636 to 0.502 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 380 | +0.6% | -1.5 to 5.95 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,632 | 1,624 | -0.5% | -62.5 to 46.5 | no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 163 | -0.7% | -4.73 to 2.3 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% | -0.0182 to 0.0121 | no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.0% | -12.8 to 8.57 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.38 | -0.8% | -0.196 to 0.141 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
