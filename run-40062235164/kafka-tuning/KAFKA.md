# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -0.421 to -0.277 | LOSS |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0177 to 0.0173 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,311 | -0.9% | -150 to 108 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,674 | +0.1% | -231 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.85 | 8.76 | -1.0% | -0.58 to 0.401 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 307 | -1.2% | -17.5 to 10.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,646 | -0.5% | -74.5 to 57.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 135 | -1.0% | -6.5 to 3.69 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.339 | 0.331 | -2.3% | -0.0365 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 576 | -2.1% | -61.4 to 36.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.51 | -2.0% | -0.37 to 0.224 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
