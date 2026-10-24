# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1924 messages a second; base rate 288.5/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 716 | -1.4% | -31.7 to 11.8 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | +0.0% | -0.00907 to 0.0141 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,149 | 3,673 | +70.9% | -1,885 to 4,934 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,369 | 5,355 | +58.9% | -2,290 to 6,261 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.37 | 8.29 | -0.9% | -0.639 to 0.485 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 288 | 485 | +68.6% | -240 to 635 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,076 | 4,491 | +46.0% | -1,665 to 4,496 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 250 | 416 | +66.1% | -203 to 534 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.328 | 0.323 | -1.4% | -0.0124 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 556 | -1.1% | -21.3 to 8.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.73 | +0.2% | -0.0804 to 0.0881 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
