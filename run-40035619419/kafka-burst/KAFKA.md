# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 339 | -0.4% | -5.41 to 2.86 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0362 to 0.0344 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,470 | 2,458 | -0.5% | -131 to 107 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,655 | -0.4% | -173 to 141 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.58 | +0.1% | -0.227 to 0.247 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 376 | 384 | +2.1% | -13.8 to 29.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,640 | 1,626 | -0.9% | -102 to 73.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 165 | +0.7% | -8.38 to 10.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -0.9% | -0.0162 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.8% | -10.9 to 7.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.33 | -0.5% | -0.192 to 0.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
