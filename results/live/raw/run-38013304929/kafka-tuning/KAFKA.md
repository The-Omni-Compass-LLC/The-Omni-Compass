# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -1.45 to 1.21 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00826 to 0.000224 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,395 | 2,401 | +0.3% | -133 to 146 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,720 | 3,766 | +1.2% | -338 to 429 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.54 | +0.0% | -0.0411 to 0.0451 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 322 | +0.7% | -13.5 to 17.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,695 | +1.5% | -11.6 to 60.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 142 | +0.3% | -5.42 to 6.33 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.308 | 0.307 | -0.4% | -0.0145 to 0.0122 | no difference beyond the noise |
| host CPU-seconds | 535 | 532 | -0.5% | -27.6 to 22.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.23 | -0.4% | -0.16 to 0.131 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
