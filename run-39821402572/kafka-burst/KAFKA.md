# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.0% | -7.3 to 7.18 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0219 to 0.0164 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,484 | 2,506 | +0.9% | -343 to 386 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,838 | 3,843 | +0.1% | -55.5 to 65.8 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.16 | 9.18 | +0.2% | -1.99 to 2.01 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 388 | +0.7% | -54.5 to 59.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,644 | 1,681 | +2.2% | -110 to 183 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 169 | +0.7% | -21.2 to 23.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | -0.6% | -0.0184 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 189 | -0.5% | -13 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 3.06 | -0.5% | -0.273 to 0.244 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
