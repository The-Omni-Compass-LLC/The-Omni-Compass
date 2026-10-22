# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.7/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -3.11 to 0.916 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | -0.0% | -0.00608 to 0.00222 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,229 | 2,263 | +1.5% | 20.7 to 46.4 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,514 | 3,614 | +2.9% | 25.7 to 175 | LOSS |
| end-to-end latency, median (ms) | 8.59 | 8.56 | -0.3% | -0.0917 to 0.0417 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 297 | 303 | +2.1% | -8.37 to 21.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,615 | 1,621 | +0.4% | -44.7 to 56.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 131 | 133 | +1.8% | -3.9 to 8.66 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.31 | 0.316 | +2.0% | 0.000516 to 0.0116 | power given |
| host CPU-seconds | 537 | 550 | +2.4% | 2.03 to 23.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.35 | +2.7% | 0.00763 to 0.166 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
