# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.21 to 0.447 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | 4.83e-05 to 0.0011 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,459 | 2,493 | +1.4% | -268 to 336 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,792 | 3,844 | +1.4% | -146 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.6 | +0.2% | -0.136 to 0.185 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 337 | +3.0% | -20.2 to 39.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 684 | 700 | +2.3% | -14 to 45.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.8 | 62 | +3.6% | -1.23 to 5.57 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.279 | +0.2% | -0.0175 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 493 | +0.4% | -30.4 to 34.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.46 | +0.6% | -0.472 to 0.567 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
