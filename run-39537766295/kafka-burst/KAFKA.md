# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -3.34 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -2.88 to 2.88 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,562 | 2,570 | +0.3% | -83 to 99.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,769 | 3,886 | +3.1% | -21.8 to 255 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.08 | 9.08 | -0.0% | -0.971 to 0.966 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 389 | +0.9% | -7.25 to 14.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,663 | 1,697 | +2.0% | -30.8 to 98.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 168 | +0.9% | -3.5 to 6.46 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.3 | -0.4% | -0.0129 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 211 | -0.4% | -7.98 to 6.49 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.43 | -0.1% | -0.117 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
