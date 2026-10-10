# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.1% | -4.89 to 5.47 | no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0117 to -0.002 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 2,551 | 2,540 | -0.4% | -59.2 to 36.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,770 | -5.4% | -472 to 44.6 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.49 | 9.36 | -1.4% | -0.544 to 0.28 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 395 | 389 | -1.4% | -33.1 to 22.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,673 | -2.5% | -163 to 78.5 | no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 168 | -1.9% | -13.2 to 6.72 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.292 | -0.9% | -0.0193 to 0.0139 | no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.8% | -13.1 to 9.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -0.9% | -0.21 to 0.148 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
