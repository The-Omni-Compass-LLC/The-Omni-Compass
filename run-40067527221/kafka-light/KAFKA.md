# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1950 messages a second; base rate 292.5/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.1% | -4.53 to 2.65 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.0123 to 0.0082 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,301 | 2,323 | +1.0% | -36.2 to 80.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,621 | 3,567 | -1.5% | -172 to 62.5 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 16.6 | 11.6 | -30.4% | -20.3 to 10.2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 315 | -1.9% | -20.9 to 8.69 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,303 | 3,234 | -2.1% | -183 to 44.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 284 | 277 | -2.5% | -19.1 to 4.83 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.794 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.282 | +0.1% | -0.00515 to 0.00579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 503 | 504 | +0.1% | -9.38 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.53 | 1.53 | +0.3% | -0.0191 to 0.0276 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
