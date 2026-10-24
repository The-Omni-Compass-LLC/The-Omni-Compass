# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -1.67 to -0.406 | LOSS |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0151 to 0.0117 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,592 | 2,571 | -0.8% | -280 to 238 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,694 | 3,729 | +0.9% | -609 to 678 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.72 | 8.64 | -0.9% | -0.539 to 0.38 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 383 | +0.4% | -5.05 to 8.07 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,651 | 1,660 | +0.5% | -45 to 61.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 164 | -0.2% | -5.52 to 4.88 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.303 | 0.301 | -0.8% | -0.0135 to 0.00883 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 216 | -0.7% | -9.43 to 6.25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.52 | 3.51 | -0.4% | -0.136 to 0.105 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
