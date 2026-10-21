# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -2.54 to 0.377 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | +0.0% | -0.0978 to 0.153 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,459 | 2,655 | +8.0% | -256 to 648 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,864 | 4,041 | +4.6% | -1,076 to 1,431 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.18 | -0.3% | -0.137 to 0.0883 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 331 | 350 | +5.7% | -44 to 82 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,740 | 1,794 | +3.1% | -332 to 440 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 146 | 154 | +5.5% | -21.4 to 37.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.293 | -0.2% | -0.00508 to 0.0038 | EVEN, no difference beyond the noise |
| host CPU-seconds | 523 | 523 | -0.0% | -7.2 to 6.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 3.18 | +0.3% | -0.0331 to 0.05 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
