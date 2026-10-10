# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 959 messages a second; base rate 107.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 337 | -0.4% | -2.07 to -0.342 | **WORSE** |
| throughput (messages a second consumed) | 412 | 412 | -0.0% | -0.00844 to 0.00147 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,202 | +5.1% | -190 to 404 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,068 | 3,245 | +5.8% | 24.2 to 331 | **WORSE** |
| end-to-end latency, median (ms) | 8.87 | 8.78 | -1.0% | -0.292 to 0.116 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 334 | +5.2% | 0.381 to 32.7 | **WORSE** |
| consumer lag, most messages waiting at once | 1,367 | 1,443 | +5.6% | -40.4 to 192 | no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 143 | +4.5% | 0.165 to 12.2 | **WORSE** |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.281 | 0.282 | +0.3% | -0.00741 to 0.00892 | no difference beyond the noise |
| host CPU-seconds | 202 | 202 | +0.3% | -5.24 to 6.38 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.32 | +0.6% | -0.082 to 0.124 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
