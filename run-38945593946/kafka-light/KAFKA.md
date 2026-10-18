# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 719 | -0.8% | -19.2 to 7.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.00643 to 0.00458 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,242 | 2,299 | +2.5% | -90.5 to 203 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,587 | 3,682 | +2.6% | -7.19 to 197 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.32 | 8.15 | -2.0% | -1.07 to 0.73 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 318 | +4.1% | 0.451 to 24.4 | LOSS |
| consumer lag, most messages waiting at once | 3,206 | 3,244 | +1.2% | -112 to 189 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 265 | 276 | +4.0% | -2.26 to 23.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.2% | -0.421 to 0.667 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.327 | -0.4% | -0.00314 to 0.00031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 563 | -0.4% | -5.38 to 1.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.5% | -0.0137 to 0.0306 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
