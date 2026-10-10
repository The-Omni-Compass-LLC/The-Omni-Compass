# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 983 messages a second; base rate 147.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -2.56 to 0.855 | no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 432 | -0.0% | -0.853 to 0.541 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,425 | 2,492 | +2.8% | 48.7 to 85.1 | **WORSE** |
| end-to-end latency, 99th percentile (ms) | 3,891 | 3,847 | -1.1% | -554 to 465 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.05 | 8.01 | -0.5% | -0.147 to 0.0588 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 339 | +1.7% | -12.6 to 24.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,734 | 1,746 | +0.7% | -90 to 115 | no difference beyond the noise |
| consumer lag, mean messages waiting | 150 | 152 | +1.3% | -8.27 to 12.1 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.272 | 0.271 | -0.6% | -0.00696 to 0.00355 | no difference beyond the noise |
| host CPU-seconds | 487 | 484 | -0.5% | -12.9 to 8.19 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.93 | 2.93 | -0.3% | -0.0631 to 0.0459 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
