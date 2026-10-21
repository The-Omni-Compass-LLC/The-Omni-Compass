# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -1.21 to 0.0553 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0271 to 0.0362 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,565 | +2.7% | -64.1 to 197 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,898 | 3,836 | -1.6% | -531 to 408 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10 | 9.49 | -5.0% | -1.52 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 391 | 391 | -0.1% | -2.69 to 2.06 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,689 | +0.7% | -69.6 to 92.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 169 | +0.2% | -4.49 to 5.29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.304 | 0.301 | -1.2% | -0.0261 to 0.0189 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 211 | -1.2% | -18.3 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.46 | 3.42 | -1.0% | -0.289 to 0.22 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
