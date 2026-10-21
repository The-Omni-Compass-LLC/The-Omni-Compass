# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 726 | -0.1% | -1.85 to 0.272 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.0159 to 0.00409 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,294 | 2,332 | +1.6% | -247 to 322 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,648 | 3,563 | -2.3% | -199 to 28.3 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.77 | 7.63 | -1.9% | -0.785 to 0.497 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 309 | -0.6% | -5.02 to 1.57 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,282 | 3,271 | -0.3% | -152 to 129 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 269 | 267 | -0.9% | -5.43 to 0.708 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.34 | 0.34 | +0.0% | -0.0055 to 0.0058 | EVEN, no difference beyond the noise |
| host CPU-seconds | 590 | 591 | +0.2% | -8.35 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.81 | +0.4% | -0.0257 to 0.0385 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
