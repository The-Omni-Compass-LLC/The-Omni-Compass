# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -2.79 to 0.906 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.1% | -2.07 to 1.29 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,581 | 2,593 | +0.5% | -85.5 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,763 | 3,855 | +2.4% | -418 to 602 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.51 | 9.61 | +1.0% | -0.518 to 0.713 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 396 | 398 | +0.6% | -2.65 to 7.77 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,720 | +0.3% | -59.6 to 70.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 174 | +1.3% | -2.82 to 7.46 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.291 | -0.4% | -0.013 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 203 | -0.3% | -8.44 to 7.38 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.3 | -0.1% | -0.143 to 0.138 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
