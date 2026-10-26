# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `a9f3cc761821`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 342 | +0.7% | 1.7 to 3.11 | GAIN |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00104 to 0.000777 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,626 | 2,531 | -3.6% | -332 to 140 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,966 | 3,898 | -1.7% | -374 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.83 | 9.4 | -4.3% | -1.91 to 1.06 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 407 | 386 | -5.1% | -29.4 to -12.2 | GAIN |
| consumer lag, most messages waiting at once | 1,720 | 1,684 | -2.1% | -108 to 36.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 178 | 167 | -6.0% | -18.9 to -2.38 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.289 | -1.2% | -0.0201 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 202 | -1.3% | -14.1 to 8.94 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.28 | -2.0% | -0.252 to 0.122 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
