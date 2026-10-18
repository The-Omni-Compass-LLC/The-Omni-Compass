# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.45 to 1.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00419 to 0.00419 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,411 | 2,407 | -0.2% | -225 to 216 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,730 | 3,778 | +1.3% | -528 to 624 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.121 to 0.0873 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 327 | +0.4% | -33.9 to 36.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 708 | 694 | -1.9% | -80.2 to 52.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 59.7 | -0.3% | -6.06 to 5.73 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.284 | 0.282 | -0.6% | -0.00971 to 0.00632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 497 | -0.6% | -16.8 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.55 | 7.51 | -0.5% | -0.257 to 0.178 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
