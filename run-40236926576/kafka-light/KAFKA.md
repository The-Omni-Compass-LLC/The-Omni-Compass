# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.1/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 716 | -1.3% | -22.5 to 3.83 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 846 | -0.2% | -9.92 to 6.18 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,272 | 2,293 | +0.9% | -136 to 179 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,679 | +4.4% | -296 to 607 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.45 | 8.14 | -3.7% | -1.04 to 0.409 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 321 | +5.4% | -29.5 to 62.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,226 | +0.8% | -41.5 to 94.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 266 | 277 | +4.0% | -29.4 to 51 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | +13.5% | -0.308 to 0.848 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3.67 | +83.3% | 0.232 to 3.1 | power given |
| host CPU busy (share of the run) | 0.329 | 0.331 | +0.6% | -0.0174 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 566 | 570 | +0.8% | -32.8 to 41.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.77 | +1.9% | -0.0656 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 11.3 | +466.7% | -6.64 to 25.3 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
