# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 290.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | +0.0% | -1.42 to 1.42 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.0178 to 0.0256 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,328 | 2,328 | +0.0% | -43.2 to 45.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,799 | 3,716 | -2.2% | -493 to 327 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.23 | 8.04 | -2.3% | -1.11 to 0.726 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 317 | -0.5% | -6.09 to 3.16 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,307 | 3,275 | -1.0% | -150 to 85.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 277 | 275 | -0.5% | -4.26 to 1.41 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.342 | 0.338 | -1.3% | -0.0302 to 0.0211 | EVEN, no difference beyond the noise |
| host CPU-seconds | 588 | 581 | -1.2% | -57.3 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.78 | -1.2% | -0.178 to 0.136 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
