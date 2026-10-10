# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.918 to 0.62 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.025 to 0.0263 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,549 | 2,556 | +0.3% | -122 to 136 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,628 | 3,691 | +1.8% | -223 to 351 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.63 | +0.7% | -0.305 to 0.426 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 380 | -0.5% | -15.7 to 11.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,658 | 1,655 | -0.2% | -77 to 69.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 163 | -1.3% | -4.93 to 0.617 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.291 | 0.289 | -0.7% | -0.013 to 0.00894 | no difference beyond the noise |
| host CPU-seconds | 209 | 208 | -0.7% | -9.43 to 6.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.38 | -0.6% | -0.151 to 0.107 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
