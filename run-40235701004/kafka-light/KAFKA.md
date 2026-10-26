# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.3% | -9.33 to 5.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.00557 to 0.0199 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,315 | 2,321 | +0.2% | -195 to 206 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,756 | 3,758 | +0.0% | -633 to 636 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.78 | 7.66 | -1.6% | -0.246 to 0.000486 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 314 | +1.2% | -6.85 to 14.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,289 | 3,279 | -0.3% | -44.5 to 25.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 269 | 272 | +0.9% | -5.1 to 10.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.8% | -0.38 to 0.61 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.344 | -2.2% | -0.0249 to 0.00914 | EVEN, no difference beyond the noise |
| host CPU-seconds | 624 | 611 | -2.1% | -46.4 to 19.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.87 | -1.9% | -0.156 to 0.0846 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -13.2 to 21.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
