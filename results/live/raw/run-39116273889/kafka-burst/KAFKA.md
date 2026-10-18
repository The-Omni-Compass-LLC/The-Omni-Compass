# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.0% | -2.16 to 2.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0426 to 0.0292 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,600 | 2,459 | -5.4% | -174 to -109 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,913 | +2.9% | -379 to 599 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.38 | 9.44 | +0.7% | -0.884 to 1.01 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 386 | -0.7% | -33.8 to 28.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,652 | -0.7% | -87.8 to 63.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 166 | -0.7% | -13.3 to 10.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.291 | -1.3% | -0.021 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.3% | -14.5 to 9.26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.31 | -1.3% | -0.227 to 0.14 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
