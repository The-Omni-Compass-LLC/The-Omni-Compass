# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1939 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 727 | -0.1% | -1.46 to -0.718 | LOSS |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.037 to 0.0285 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,434 | +0.6% | -88.9 to 119 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,686 | 3,687 | +0.0% | -232 to 235 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.7 | 7.61 | -1.2% | -0.323 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 323 | +1.1% | 0.777 to 6.03 | LOSS |
| consumer lag, most messages waiting at once | 3,334 | 3,324 | -0.3% | -139 to 119 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 280 | +0.4% | -0.804 to 2.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.338 | 0.34 | +0.5% | -0.0105 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 604 | +0.5% | -16.8 to 22.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.85 | +0.7% | -0.0478 to 0.0719 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
