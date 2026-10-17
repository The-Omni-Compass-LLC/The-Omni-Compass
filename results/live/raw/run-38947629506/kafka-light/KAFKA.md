# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 730 | +0.4% | -8.78 to 14.2 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | +0.0% | -0.00516 to 0.00855 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,397 | 2,096 | -12.6% | -1,364 to 762 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,673 | 3,299 | -10.2% | -1,898 to 1,149 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.29 | -1.3% | -0.252 to 0.0544 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 277 | -11.8% | -162 to 88.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,305 | 2,985 | -9.7% | -1,439 to 798 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 271 | 240 | -11.7% | -139 to 74.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.13 | +6.3% | -0.445 to 0.697 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.345 | 0.345 | -0.1% | -0.013 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 614 | 614 | +0.0% | -21 to 21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.88 | 1.87 | -0.4% | -0.051 to 0.037 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
