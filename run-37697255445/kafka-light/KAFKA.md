# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1937 messages a second; base rate 290.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 851 | +16.2% | 111 to 127 | better |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0209 to -0.0114 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 1,636 | 9.19 | -99.4% | -1,758 to -1,496 | better |
| end-to-end latency, 99th percentile (ms) | 2,587 | 10.6 | -99.6% | -2,903 to -2,250 | better |
| end-to-end latency, median (ms) | 8.34 | 6.08 | -27.1% | -2.36 to -2.16 | better |
| end-to-end latency, mean (ms) | 230 | 6.67 | -97.1% | -250 to -197 | better |
| consumer lag, most messages waiting at once | 2,279 | 90.3 | -96.0% | -2,367 to -2,011 | better |
| consumer lag, mean messages waiting | 203 | 5.88 | -97.1% | -222 to -173 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.1 | +255.0% | 3.17 to 7.03 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.325 | 0.377 | +16.0% | 0.0275 to 0.0762 | **WORSE** |
| host CPU-seconds | 371 | 433 | +16.5% | 32.1 to 90.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.69 | +0.3% | -0.118 to 0.127 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
