# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1926 messages a second; base rate 288.9/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 725 | +0.2% | -3.95 to 6.22 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | +0.0% | -0.021 to 0.0299 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,252 | 2,202 | -2.2% | -255 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,630 | 3,556 | -2.1% | -431 to 282 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.13 | 8.01 | -1.5% | -0.918 to 0.677 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 297 | -3.0% | -43.8 to 25.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,181 | -0.6% | -302 to 265 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 257 | -2.9% | -37.3 to 21.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.3 to 0.795 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.344 | 0.333 | -3.3% | -0.0373 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 592 | 572 | -3.5% | -66.3 to 25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.75 | -3.6% | -0.212 to 0.0798 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
