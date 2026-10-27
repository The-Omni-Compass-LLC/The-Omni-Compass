# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1925 messages a second; base rate 288.8/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 727 | -0.8% | -15.7 to 3.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0103 to 0.00549 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,515 | 1,716 | +13.2% | -410 to 810 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,394 | 2,611 | +9.1% | -337 to 772 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.22 | 7.92 | -3.7% | -0.829 to 0.217 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 211 | 235 | +11.8% | -29.3 to 78.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,195 | 2,276 | +3.7% | -383 to 546 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 185 | 205 | +11.2% | -24.2 to 65.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.29 | +14.5% | -0.115 to 0.694 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3.67 | +83.3% | 0.232 to 3.1 | power given |
| host CPU busy (share of the run) | 0.331 | 0.331 | +0.0% | -0.011 to 0.011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 380 | 380 | +0.0% | -11 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.9% | -0.046 to 0.0756 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 9.33 | +366.7% | -0.256 to 14.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
