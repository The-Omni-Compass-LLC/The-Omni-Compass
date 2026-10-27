# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.8/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 371 | 366 | -1.4% | -22.6 to 12.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.014 to 0.00727 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,612 | 1,704 | +5.7% | -242 to 426 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,450 | 2,674 | +9.1% | -397 to 844 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.14 | 8.15 | +0.2% | -0.215 to 0.244 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 219 | 244 | +11.3% | -63.4 to 113 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,130 | 1,192 | +5.5% | -130 to 254 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 98.8 | 110 | +11.3% | -27.9 to 50.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.00732 to 0.0117 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.286 | +1.4% | -0.0109 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 341 | +1.4% | -12.4 to 22.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.01 | 3.1 | +2.9% | -0.214 to 0.387 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2.67 | +33.3% | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
