# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.3% | -7.06 to 3.12 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -1.7 to 1.06 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,311 | 2,379 | +2.9% | -100 to 236 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,697 | -0.9% | -286 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.44 | 8.11 | -3.9% | -0.938 to 0.282 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 324 | +2.0% | -31.2 to 44.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,253 | 3,308 | +1.7% | -202 to 313 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 278 | 281 | +1.1% | -29.4 to 35.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.426 to 0.666 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.325 | 0.331 | +1.8% | -0.00318 to 0.0151 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 570 | +2.1% | -5.13 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.75 | +2.4% | -0.00826 to 0.0892 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
