# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1951 messages a second; base rate 292.7/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 731 | -0.1% | -1.2 to -0.58 | LOSS |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.023 to 0.00693 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,431 | 2,418 | -0.5% | -137 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,680 | -1.1% | -72.1 to -10.3 | GAIN |
| end-to-end latency, median (ms) | 8.15 | 8.56 | +5.1% | -1.07 to 1.89 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 329 | +1.2% | -9.33 to 17.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,348 | 3,342 | -0.2% | -40.1 to 29.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 289 | +0.9% | -8.94 to 13.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.306 | -3.2% | -0.0409 to 0.0206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 546 | -3.1% | -70.3 to 35.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.66 | -3.0% | -0.211 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
