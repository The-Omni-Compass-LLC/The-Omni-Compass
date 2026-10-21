# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.2% | -2.94 to 1.33 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.1% | -2.05 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,549 | 2,542 | -0.2% | -223 to 210 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,649 | 3,761 | +3.1% | -471 to 694 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.2 | 9.28 | +0.9% | -0.131 to 0.297 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 386 | +0.7% | 1.09 to 4.58 | LOSS |
| consumer lag, most messages waiting at once | 1,684 | 1,679 | -0.3% | -48.4 to 39.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 167 | +0.3% | -0.196 to 1.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.303 | -0.8% | -0.0209 to 0.0159 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 213 | -0.7% | -14.8 to 12 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.48 | 3.46 | -0.5% | -0.245 to 0.21 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
