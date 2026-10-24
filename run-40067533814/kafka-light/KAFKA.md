# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1940 messages a second; base rate 291.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 725 | -0.4% | -8.02 to 1.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0251 to 0.00677 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,387 | 2,607 | +9.2% | -254 to 694 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 4,062 | +7.9% | -177 to 774 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.45 | 7.51 | +0.8% | -0.152 to 0.276 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 355 | +10.6% | -18.6 to 86.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,354 | 3,447 | +2.8% | -380 to 566 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 280 | 307 | +9.7% | -16.6 to 71.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.323 | +2.4% | -0.00132 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 576 | +2.5% | -2.35 to 30.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.77 | +3.0% | 0.00628 to 0.0954 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
