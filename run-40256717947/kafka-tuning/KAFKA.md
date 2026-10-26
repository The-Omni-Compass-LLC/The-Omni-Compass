# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `a9f3cc761821`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -6.83 to 5.57 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 428 | +0.0% | -0.513 to 0.832 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,208 | 2,265 | +2.6% | -161 to 275 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,496 | 3,506 | +0.3% | -97.4 to 118 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.42 | 8.39 | -0.4% | -0.0382 to -0.0325 | GAIN |
| end-to-end latency, mean (ms) | 293 | 296 | +0.9% | -27.4 to 32.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,603 | 1,604 | +0.1% | -91 to 93.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 129 | 130 | +1.0% | -11.9 to 14.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | +1.1% | -0.0732 to 0.118 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.317 | 0.313 | -1.0% | -0.00781 to 0.0012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 560 | -1.0% | -12.8 to 1.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.4 | -0.8% | -0.095 to 0.0423 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2.67 | +33.3% | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
