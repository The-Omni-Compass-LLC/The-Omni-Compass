# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 150 | +1.8% | -8.63 to 13.8 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00393 to 0.00452 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,374 | 2,430 | +2.4% | -326 to 437 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,663 | 3,843 | +4.9% | -792 to 1,153 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% | -0.128 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 308 | -3.4% | -52.5 to 30.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 698 | 729 | +4.4% | -83.4 to 145 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59 | 56.2 | -4.7% | -12.9 to 7.39 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.279 | 0.28 | +0.2% | -0.00578 to 0.00684 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 493 | +0.3% | -10.2 to 13.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.31 | -1.4% | -0.748 to 0.544 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
