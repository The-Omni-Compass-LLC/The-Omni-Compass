# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 971 messages a second; base rate 109.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.0% | -0.91 to 0.899 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | -0.0% | -0.0102 to 0.00595 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,355 | 2,397 | +1.8% | -76.4 to 160 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,605 | 3,453 | -4.2% | -240 to -62.9 | GAIN |
| end-to-end latency, median (ms) | 8.66 | 8.7 | +0.5% | -0.157 to 0.243 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 357 | 359 | +0.5% | -0.25 to 3.64 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,560 | 1,581 | +1.3% | -4.21 to 46.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 154 | 154 | +0.3% | -0.0966 to 1.05 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -0.9% | -0.0204 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 212 | -1.0% | -14.6 to 10.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.45 | -1.0% | -0.234 to 0.167 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
