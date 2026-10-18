# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -9.59 to 7.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.00508 to 0.000495 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,433 | 2,382 | -2.1% | -446 to 344 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,560 | 3,582 | +0.6% | -525 to 568 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 21.9 | 15.5 | -29.1% | -21.5 to 8.76 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 380 | 381 | +0.3% | -45.3 to 47.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,584 | 1,607 | +1.4% | -111 to 156 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 167 | +1.3% | -13.6 to 17.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.257 | 0.255 | -0.5% | -0.00768 to 0.00493 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 183 | -0.5% | -5.29 to 3.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.99 | 2.99 | -0.1% | -0.027 to 0.0192 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
