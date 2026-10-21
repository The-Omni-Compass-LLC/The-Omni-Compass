# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -1.46 to 0.614 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0147 to 0.00782 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,604 | 2,575 | -1.1% | -259 to 201 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,755 | 3,849 | +2.5% | -440 to 628 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.15 | 8.96 | -2.1% | -1.09 to 0.699 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 387 | 390 | +0.7% | -3.31 to 8.92 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,698 | 1,693 | -0.3% | -68.7 to 58.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 168 | +0.8% | -3.4 to 6.07 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.307 | -0.4% | -0.0135 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 219 | -0.4% | -9.63 to 8.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.57 | 3.57 | -0.2% | -0.163 to 0.145 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
