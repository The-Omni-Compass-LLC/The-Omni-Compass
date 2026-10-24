# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 948 messages a second; base rate 106.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 336 | 336 | -0.0% | -10.6 to 10.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 407 | 407 | +0.0% | -0.00612 to 0.0107 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,043 | 2,661 | +30.3% | -1,855 to 3,092 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,890 | 3,716 | +28.6% | -1,737 to 3,390 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.8 | 8.7 | -1.0% | -0.572 to 0.389 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 375 | +23.3% | -165 to 308 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,274 | 1,568 | +23.0% | -788 to 1,375 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 128 | 157 | +22.9% | -68.6 to 127 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.7% | -0.0227 to -0.00681 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.291 | +2.0% | -0.0142 to 0.0257 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 208 | +2.0% | -9.88 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.43 | +2.0% | -0.136 to 0.27 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
