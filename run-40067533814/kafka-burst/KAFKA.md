# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.2% | -2.15 to 0.983 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.01 to 0.00908 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,535 | 2,462 | -2.9% | -175 to 28.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,659 | 3,679 | +0.5% | -228 to 267 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.46 | 8.51 | +0.5% | -0.251 to 0.336 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 373 | 376 | +0.8% | 1.51 to 4.66 | LOSS |
| consumer lag, most messages waiting at once | 1,656 | 1,663 | +0.4% | 4.52 to 9.48 | LOSS |
| consumer lag, mean messages waiting | 162 | 163 | +0.6% | -2.93 to 5.01 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.282 | -0.6% | -0.00994 to 0.00677 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 202 | -0.6% | -7.1 to 4.77 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | -0.4% | -0.124 to 0.0974 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
