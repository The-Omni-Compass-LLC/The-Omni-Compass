# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 954 messages a second; base rate 143.2/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 369 | +0.5% | -2.96 to 6.4 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00626 to 0.00343 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,670 | 1,641 | -1.7% | -157 to 98.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,878 | 2,707 | -5.9% | -482 to 142 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.1 | -1.8% | -0.358 to 0.0622 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 215 | 204 | -5.2% | -40.8 to 18.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,328 | 1,289 | -3.0% | -213 to 134 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 94.4 | 88.9 | -5.8% | -16.6 to 5.63 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.42 | +20.8% | 0.377 to 0.456 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.296 | 0.292 | -1.1% | -0.0171 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 526 | 521 | -1.0% | -29.6 to 19.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.18 | 3.13 | -1.4% | -0.153 to 0.0618 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
