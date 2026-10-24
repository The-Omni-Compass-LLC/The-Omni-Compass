# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -1.25 to -0.148 | LOSS |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0135 to 0.0127 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,300 | 2,267 | -1.4% | -142 to 77.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,469 | 3,620 | +4.3% | -379 to 680 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.41 | 8.54 | +1.5% | -0.0656 to 0.31 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 296 | 301 | +1.7% | -0.167 to 10.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,629 | 1,628 | -0.1% | -39.2 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 130 | 133 | +1.7% | 0.325 to 4.07 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.317 | 0.328 | +3.3% | -0.00878 to 0.0296 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 583 | +3.3% | -15.1 to 52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.55 | +3.5% | -0.0865 to 0.324 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
