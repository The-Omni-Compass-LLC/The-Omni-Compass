# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 724 | -0.3% | -5.05 to 0.259 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | +0.0% | -0.0107 to 0.0123 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,291 | 2,305 | +0.6% | -78.3 to 105 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,620 | 3,636 | +0.4% | -222 to 253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.36 | 7.83 | -6.3% | -1.4 to 0.338 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 310 | +0.8% | -17.2 to 22.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,238 | 3,250 | +0.4% | -82.9 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 267 | 268 | +0.4% | -15.7 to 17.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.335 | 0.337 | +0.8% | -0.0052 to 0.0104 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 581 | +1.2% | -8.65 to 22.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.78 | +1.5% | -0.0179 to 0.071 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
