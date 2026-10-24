# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.0% | -5.9 to 5.73 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0241 to 0.0158 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,508 | -2.9% | -337 to 186 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,728 | 3,796 | +1.8% | -399 to 535 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 15 | 11 | -26.7% | -19.1 to 11.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 397 | 395 | -0.5% | -57.6 to 53.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,707 | +1.1% | -69.4 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 174 | 172 | -1.3% | -30.3 to 25.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.268 | -0.3% | -0.0171 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 192 | -0.2% | -11.9 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.12 | 3.12 | -0.2% | -0.153 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
