# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1964 messages a second; base rate 294.7/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 734 | 733 | -0.1% | -3.32 to 1.26 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 864 | 864 | -0.0% | -1.68 to 1.01 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,628 | 2,569 | -2.3% | -240 to 121 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,941 | 3,974 | +0.8% | -304 to 370 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.86 | 7.8 | -0.7% | -0.897 to 0.793 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 353 | 352 | -0.2% | -17.3 to 15.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,537 | 3,545 | +0.2% | -245 to 260 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 311 | 310 | -0.3% | -16.4 to 14.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.287 | -1.1% | -0.00895 to 0.0025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 516 | 512 | -0.9% | -15 to 5.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.56 | 1.55 | -0.8% | -0.0424 to 0.017 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
