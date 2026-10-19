# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 290.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 724 | -0.3% | -3.72 to -0.4 | LOSS |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0233 to 0.00788 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,329 | 2,315 | -0.6% | -312 to 284 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,574 | 3,725 | +4.2% | 70.2 to 232 | LOSS |
| end-to-end latency, median (ms) | 8.38 | 7.94 | -5.2% | -0.928 to 0.0503 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 316 | +1.0% | -11.5 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,227 | 3,270 | +1.3% | -83.2 to 168 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 274 | +0.9% | -10.9 to 15.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.325 | -0.2% | -0.00964 to 0.00857 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 559 | +0.0% | -18.6 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | +0.3% | -0.0536 to 0.0642 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
