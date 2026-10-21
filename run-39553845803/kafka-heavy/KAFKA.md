# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.929 to -0.0832 | LOSS |
| throughput (messages a second consumed) | 174 | 174 | -0.0% | -0.0022 to 0.00138 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,617 | 2,719 | +3.9% | -12.3 to 217 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,975 | 4,040 | +1.6% | -59.4 to 190 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.155 to 0.13 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 352 | 365 | +3.8% | 9.24 to 17.1 | LOSS |
| consumer lag, most messages waiting at once | 744 | 749 | +0.7% | -42.3 to 52.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.8 | 66.8 | +3.0% | 0.69 to 3.21 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.292 | -0.7% | -0.014 to 0.00983 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 524 | -0.7% | -24.7 to 17.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.94 | 7.91 | -0.3% | -0.362 to 0.307 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
