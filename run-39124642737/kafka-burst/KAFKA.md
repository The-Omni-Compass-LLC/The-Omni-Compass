# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -1.62 to 0.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -0.00593 to 0.0118 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,642 | 2,585 | -2.2% | -115 to 0.0358 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,769 | 3,692 | -2.0% | -657 to 503 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.5 | 9.37 | -1.3% | -0.591 to 0.34 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 391 | 391 | +0.0% | -6.54 to 6.84 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,682 | 1,676 | -0.3% | -15.7 to 4.37 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 170 | +0.4% | -2.66 to 3.98 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.293 | -0.5% | -0.00826 to 0.00515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.6% | -5.32 to 3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.33 | -0.4% | -0.082 to 0.054 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
