# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -5.74 to 5.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0174 to 0.00759 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,328 | -0.8% | -161 to 126 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,666 | 3,612 | -1.5% | -362 to 253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.21 | 8.03 | -2.2% | -0.639 to 0.282 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 308 | -1.8% | -33.3 to 22.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,277 | 3,225 | -1.6% | -211 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 267 | -2.1% | -34 to 22.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% | -0.296 to 0.786 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.343 | 0.347 | +1.4% | -0.00673 to 0.0163 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 597 | +1.3% | -11 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.83 | +1.3% | -0.0314 to 0.0789 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
