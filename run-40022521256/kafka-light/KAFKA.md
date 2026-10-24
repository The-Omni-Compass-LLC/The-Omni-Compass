# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1907 messages a second; base rate 286.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 732 | +0.0% | -6.53 to 7.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 839 | 839 | -0.0% | -0.0432 to 0.0297 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,802 | 1,801 | -0.1% | -72 to 69.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,025 | 2,971 | -1.8% | -280 to 171 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.29 | 7.19 | -1.3% | -0.179 to -0.0139 | GAIN |
| end-to-end latency, mean (ms) | 231 | 228 | -1.2% | -23.7 to 18.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,770 | 2,733 | -1.3% | -147 to 72.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 197 | 195 | -1.5% | -19.3 to 13.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.26 | +13.0% | -0.313 to 0.832 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.335 | 0.334 | -0.3% | -0.0199 to 0.0178 | EVEN, no difference beyond the noise |
| host CPU-seconds | 596 | 595 | -0.2% | -33.9 to 32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.81 | 1.81 | -0.2% | -0.12 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
