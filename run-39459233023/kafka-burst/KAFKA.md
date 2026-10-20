# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -1.09 to 0.095 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 420 | +0.1% | -1.3 to 2.07 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,590 | 2,533 | -2.2% | -247 to 133 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,746 | 3,802 | +1.5% | -400 to 511 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.46 | 9.53 | +0.8% | -0.518 to 0.661 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 391 | +0.5% | -5.56 to 9.38 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,676 | 1,690 | +0.8% | -42.2 to 70.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 169 | -0.3% | -5.34 to 4.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.302 | 0.3 | -0.8% | -0.00748 to 0.00256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 210 | -0.8% | -4.62 to 1.03 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.41 | -0.6% | -0.0844 to 0.0423 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
