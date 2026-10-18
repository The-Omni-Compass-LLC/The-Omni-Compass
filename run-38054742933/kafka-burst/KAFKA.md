# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.0% | -1.06 to 1.18 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0246 to 0.0219 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,525 | 2,503 | -0.9% | -234 to 190 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,776 | 3,763 | -0.3% | -332 to 306 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.68 | 9.58 | -1.1% | -2.03 to 1.81 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 384 | +0.3% | -10.9 to 13 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,650 | 1,644 | -0.3% | -69.2 to 57.9 | no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 166 | -0.1% | -5.6 to 5.13 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -1.0% | -0.0201 to 0.0142 | no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.0% | -13.8 to 9.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -1.0% | -0.214 to 0.148 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
