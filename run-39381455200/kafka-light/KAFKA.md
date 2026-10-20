# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1924 messages a second; base rate 288.6/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 764 | +5.3% | -150 to 228 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | -0.0% | -0.0296 to 0.0167 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,151 | 1,595 | -25.9% | -4,347 to 3,234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,444 | 2,501 | -27.4% | -6,503 to 4,617 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.51 | 7.16 | -4.7% | -1.58 to 0.875 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 289 | 211 | -26.9% | -578 to 423 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,083 | 2,328 | -24.5% | -5,297 to 3,787 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 250 | 181 | -27.8% | -497 to 358 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.43 | +21.6% | 0.152 to 0.712 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.32 | 0.333 | +4.1% | -0.00842 to 0.0346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 593 | +3.9% | -15 to 59.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | -0.9% | -0.45 to 0.42 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
