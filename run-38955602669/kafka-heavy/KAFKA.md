# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 147 | +0.4% | -0.0204 to 1.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00281 to 0.00168 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,629 | 2,389 | -9.1% | -908 to 428 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,979 | 3,701 | -7.0% | -975 to 420 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.4% | -0.185 to 0.0946 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 354 | 320 | -9.6% | -86.1 to 18.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 738 | 689 | -6.6% | -195 to 97.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 65.2 | 59 | -9.4% | -14.4 to 2.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.276 | -1.2% | -0.00638 to -4.38e-05 | GAIN |
| host CPU-seconds | 500 | 494 | -1.1% | -11.4 to 0.177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.46 | -1.5% | -0.202 to -0.0301 | GAIN |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
