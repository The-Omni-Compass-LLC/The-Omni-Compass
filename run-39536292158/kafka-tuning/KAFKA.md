# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.4/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 363 | 366 | +0.8% | -7.22 to 12.7 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.0038 to 0.00146 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,127 | -17.6% | -1,794 to 883 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,974 | 3,457 | -13.0% | -1,982 to 948 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.18 | -0.7% | -0.118 to -0.00165 | GAIN |
| end-to-end latency, mean (ms) | 345 | 282 | -18.4% | -267 to 140 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,779 | 1,578 | -11.3% | -897 to 496 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 151 | 124 | -18.2% | -116 to 60.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | +13.5% | -0.192 to 0.732 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.294 | 0.296 | +0.7% | -0.000424 to 0.00466 | EVEN, no difference beyond the noise |
| host CPU-seconds | 524 | 528 | +0.9% | -1.18 to 10.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.21 | +0.1% | -0.113 to 0.121 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
