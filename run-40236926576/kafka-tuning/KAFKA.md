# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 969 messages a second; base rate 145.3/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 363 | -0.7% | -10.3 to 4.91 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.00406 to 0.0022 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,092 | 2,185 | +4.4% | -133 to 319 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,428 | 3,392 | -1.1% | -178 to 106 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.58 | 8.55 | -0.4% | -0.079 to 0.017 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 281 | 293 | +4.1% | -24.7 to 47.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,568 | 1,564 | -0.3% | -108 to 98.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 124 | 129 | +4.0% | -10.8 to 20.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.07 | +3.4% | -0.0901 to 0.225 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.305 | 0.303 | -0.5% | -0.0137 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 529 | 527 | -0.4% | -26.2 to 22.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.23 | +0.4% | -0.149 to 0.173 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
