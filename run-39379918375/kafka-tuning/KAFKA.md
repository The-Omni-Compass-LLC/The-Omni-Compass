# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -0.707 to 0.291 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00833 to 0.00379 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,431 | -1.2% | -127 to 69.5 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,781 | +0.4% | -311 to 340 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.48 | -0.1% | -0.111 to 0.0979 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 322 | -0.2% | -7.04 to 5.61 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,707 | 1,706 | -0.0% | -26.2 to 25.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 142 | -0.2% | -2.62 to 2.04 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.319 | 0.318 | -0.4% | -0.00749 to 0.00474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.3% | -12.2 to 8.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.38 | -0.3% | -0.0703 to 0.0532 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
