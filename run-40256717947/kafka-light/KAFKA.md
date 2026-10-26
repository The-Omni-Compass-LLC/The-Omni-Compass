# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.1/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `a9f3cc761821`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -6.13 to 3.27 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.0194 to 0.0086 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,369 | 2,362 | -0.3% | -107 to 92.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,736 | 3,759 | +0.6% | -161 to 207 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.34 | 8.34 | -0.0% | -0.316 to 0.31 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 323 | +1.5% | -11.6 to 21 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,274 | 3,293 | +0.6% | -6.82 to 44.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 277 | 281 | +1.3% | -12.3 to 19.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.332 | 0.33 | -0.4% | -0.00493 to 0.00219 | EVEN, no difference beyond the noise |
| host CPU-seconds | 570 | 567 | -0.5% | -4.85 to -0.323 | GAIN |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | -0.3% | -0.0184 to 0.00933 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
