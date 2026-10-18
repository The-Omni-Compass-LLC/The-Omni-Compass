# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1921 messages a second; base rate 288.1/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 719 | -0.9% | -17.7 to 4.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 845 | 845 | +0.0% | -0.0149 to 0.0157 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,098 | 2,191 | +4.4% | 18.6 to 168 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,360 | 3,520 | +4.8% | -142 to 462 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.53 | 8.25 | -3.2% | -1.26 to 0.711 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 284 | 301 | +6.2% | -6.89 to 42.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,057 | 3,160 | +3.4% | -80.2 to 286 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 247 | 261 | +5.9% | -8.51 to 37.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.2% | -0.426 to 0.675 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.322 | 0.322 | +0.1% | -0.0118 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 552 | 554 | +0.3% | -18.6 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.71 | +1.2% | -0.0492 to 0.0893 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
