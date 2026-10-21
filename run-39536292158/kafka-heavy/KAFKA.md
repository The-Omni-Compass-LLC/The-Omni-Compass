# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.784 to 0.524 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00149 to 0.00121 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,424 | 2,459 | +1.5% | -263 to 334 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,760 | 3,720 | -1.1% | -226 to 146 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.1% | -0.069 to 0.0363 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 324 | 326 | +0.7% | -16.4 to 21.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 714 | 705 | -1.4% | -45.9 to 26.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 60.2 | +0.5% | -3.35 to 3.89 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.272 | 0.271 | -0.5% | -0.00586 to 0.00302 | EVEN, no difference beyond the noise |
| host CPU-seconds | 488 | 486 | -0.5% | -10.5 to 5.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.36 | 7.33 | -0.4% | -0.12 to 0.0596 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
