# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1936 messages a second; base rate 290.5/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | +0.0% | -2.6 to 3.24 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.00853 to 0.000355 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,419 | 2,383 | -1.5% | -173 to 101 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,830 | 3,709 | -3.2% | -783 to 540 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.4 | 8.41 | +0.0% | -0.684 to 0.687 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 322 | -2.4% | -32.4 to 16.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,396 | 3,305 | -2.7% | -206 to 23.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 287 | 281 | -2.4% | -27.1 to 13.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.333 | 0.328 | -1.5% | -0.0215 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 572 | 563 | -1.6% | -38.5 to 20 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.72 | -1.7% | -0.126 to 0.0675 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
