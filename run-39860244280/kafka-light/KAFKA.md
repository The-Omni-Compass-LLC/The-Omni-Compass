# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | -0.0% | -3.82 to 3.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0319 to 0.0228 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,432 | +1.7% | -122 to 201 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,862 | 3,623 | -6.2% | -648 to 170 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.21 | 8.12 | -1.2% | -0.542 to 0.351 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 331 | 327 | -1.1% | -19.3 to 12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,367 | 3,326 | -1.2% | -144 to 62.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 288 | 285 | -1.1% | -14.5 to 8.11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.331 | 0.332 | +0.3% | -0.00363 to 0.00533 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 571 | +0.3% | -7.78 to 11.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.75 | +0.3% | -0.0155 to 0.0272 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
