# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.497 to 0.746 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000751 to 0.00134 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,382 | +0.3% | -91.3 to 106 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,793 | 3,651 | -3.7% | -586 to 302 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.2 | -0.7% | -0.264 to 0.116 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 317 | -2.0% | -27.5 to 14.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 688 | -2.3% | -22.6 to -9.43 | GAIN |
| consumer lag, mean messages waiting | 59.1 | 58.4 | -1.2% | -4.9 to 3.52 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.276 | 0.273 | -1.0% | -0.0103 to 0.00488 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 489 | -1.0% | -18.4 to 8.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.46 | 7.38 | -1.0% | -0.271 to 0.116 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
