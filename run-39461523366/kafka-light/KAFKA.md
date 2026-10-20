# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -2.89 to 2.28 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 850 | +0.0% | -1.04 to 1.66 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,330 | 2,318 | -0.5% | -40.7 to 16.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,571 | -3.2% | -325 to 85.5 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.93 | 7.73 | -2.5% | -0.592 to 0.2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 312 | 309 | -0.8% | -16.9 to 12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,256 | 3,220 | -1.1% | -128 to 56 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 268 | -0.8% | -12.9 to 8.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.346 | 0.346 | -0.0% | -0.0194 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 601 | +0.1% | -36.8 to 37.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.84 | +0.1% | -0.113 to 0.118 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
