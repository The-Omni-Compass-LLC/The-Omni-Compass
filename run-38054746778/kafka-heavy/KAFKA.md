# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 146 | -0.8% | -5.27 to 2.88 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00319 to 0.00249 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,406 | 2,540 | +5.6% | -401 to 670 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,960 | +3.6% | -183 to 455 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.4% | -0.18 to 0.0878 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 351 | +7.8% | -51.8 to 102 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 694 | 729 | +5.0% | -63.5 to 133 | no difference beyond the noise |
| consumer lag, mean messages waiting | 59.6 | 63.6 | +6.7% | -7.49 to 15.5 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.279 | 0.277 | -0.7% | -0.00865 to 0.00499 | no difference beyond the noise |
| host CPU-seconds | 491 | 488 | -0.6% | -15.5 to 9.66 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.4 | 7.42 | +0.2% | -0.31 to 0.344 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
