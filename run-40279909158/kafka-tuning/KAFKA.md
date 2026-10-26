# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 368 | +0.1% | -2.39 to 3.41 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | +0.0% | -0.0102 to 0.0139 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,363 | 2,389 | +1.1% | -310 to 364 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,748 | 3,666 | -2.2% | -141 to -24.5 | GAIN |
| end-to-end latency, median (ms) | 8.17 | 8.19 | +0.2% | -0.157 to 0.191 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 322 | -0.1% | -26.4 to 25.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,700 | 1,718 | +1.1% | -61.3 to 97.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 144 | 143 | -0.1% | -12.1 to 11.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.282 | -1.0% | -0.031 to 0.0254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 504 | -1.0% | -53.3 to 43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.04 | -1.2% | -0.345 to 0.274 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
