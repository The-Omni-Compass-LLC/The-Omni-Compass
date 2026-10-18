# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1946 messages a second; base rate 291.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.0% | -1.24 to 0.867 | no difference beyond the noise |
| throughput (messages a second consumed) | 856 | 856 | +0.0% | -0.0298 to 0.0317 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,339 | -1.7% | -107 to 24.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,674 | 3,677 | +0.1% | -35.9 to 42.2 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.15 | 7.05 | -1.4% | -0.346 to 0.139 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 308 | -0.9% | -4.46 to -1.28 | better |
| consumer lag, most messages waiting at once | 3,292 | 3,281 | -0.3% | -94.7 to 74 | no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 267 | -1.2% | -4.71 to -1.62 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.319 | 0.319 | -0.1% | -0.0119 to 0.0111 | no difference beyond the noise |
| host CPU-seconds | 569 | 569 | -0.0% | -21.9 to 21.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.73 | -0.0% | -0.066 to 0.0655 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
