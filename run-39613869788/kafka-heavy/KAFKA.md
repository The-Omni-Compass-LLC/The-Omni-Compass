# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.2% | -0.782 to 0.153 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00542 to 0.00188 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,408 | +0.4% | -123 to 142 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,725 | 3,878 | +4.1% | -32.8 to 339 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11 | 11 | -0.5% | -0.282 to 0.18 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.8% | -15.1 to 26.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 679 | 702 | +3.3% | -35.2 to 80.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.4 | 60.3 | +3.1% | -2.93 to 6.55 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.27 | 0.266 | -1.3% | -0.00817 to 0.00132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 482 | 476 | -1.2% | -14 to 2.09 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.26 | 7.19 | -1.0% | -0.179 to 0.029 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
