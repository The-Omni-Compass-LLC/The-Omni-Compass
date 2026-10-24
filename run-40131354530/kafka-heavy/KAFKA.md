# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 156 | +5.9% | -29.3 to 46.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00507 to 0.00369 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,615 | 1,684 | -35.6% | -4,682 to 2,821 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,041 | 2,576 | -36.2% | -6,478 to 3,548 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.7% | -0.225 to 0.0725 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 353 | 229 | -35.1% | -592 to 345 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 721 | 516 | -28.4% | -1,024 to 614 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.8 | 42.4 | -34.6% | -107 to 62.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.19 | +9.3% | -0.572 to 0.943 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.274 | 0.273 | -0.4% | -0.0112 to 0.00886 | EVEN, no difference beyond the noise |
| host CPU-seconds | 490 | 488 | -0.4% | -20 to 15.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.4 | 7 | -5.5% | -1.8 to 0.995 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
