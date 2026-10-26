# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.4% | -4.75 to 2.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.019 to 0.0172 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | -0.7% | -150 to 115 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,432 | 3,678 | +7.1% | -52.6 to 543 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.86 | 12 | +21.5% | -3.01 to 7.25 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 362 | 371 | +2.5% | -16.4 to 34.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,565 | 1,574 | +0.5% | -101 to 118 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 163 | +2.9% | -6.5 to 15.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.3% | -0.021 to 0.00881 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 187 | -2.3% | -14.8 to 6.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.09 | 3.03 | -1.9% | -0.205 to 0.0886 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
