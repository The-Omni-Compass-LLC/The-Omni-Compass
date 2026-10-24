# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 341 | -0.5% | -7.71 to 4.01 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.0% | -0.0317 to 0.0183 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,646 | +3.2% | -1.18 to 163 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,787 | -4.9% | -1,030 to 637 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.9 | 10 | -16.2% | -6.5 to 2.63 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 408 | +2.3% | -27.6 to 46.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,733 | 1,730 | -0.2% | -177 to 171 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 175 | 179 | +2.2% | -10.6 to 18.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.27 | +0.7% | -0.0135 to 0.0174 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +0.8% | -9.51 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.11 | 3.15 | +1.3% | -0.0813 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
