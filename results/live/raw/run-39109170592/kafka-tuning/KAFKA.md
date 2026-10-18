# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.2% | -2.93 to 1.23 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.013 to 0.00802 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,447 | +2.0% | -69.6 to 167 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,688 | 3,753 | +1.8% | -360 to 491 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.44 | 8.43 | -0.1% | -0.0662 to 0.0455 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 324 | +1.4% | -16.3 to 25.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,701 | 1,708 | +0.4% | -115 to 130 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 143 | +1.2% | -6.98 to 10.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | -0.5% | -0.011 to 0.0081 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.4% | -20.8 to 16.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | -0.1% | -0.135 to 0.127 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
