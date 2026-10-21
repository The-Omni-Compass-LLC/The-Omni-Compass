# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -1.68 to 0.00184 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00965 to 0.00664 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,381 | 2,413 | +1.3% | -167 to 230 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,731 | 3,730 | -0.0% | -432 to 431 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.52 | +0.1% | -0.176 to 0.189 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 322 | +1.3% | -8.59 to 17.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,677 | -0.6% | -60.9 to 39.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 142 | +1.4% | -4.01 to 8.03 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.317 | -0.5% | -0.0115 to 0.00827 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 554 | -0.5% | -23.6 to 18.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.37 | -0.2% | -0.137 to 0.12 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
