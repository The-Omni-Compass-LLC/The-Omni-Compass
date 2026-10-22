# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 156 | +5.7% | -27.9 to 44.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.336 to 0.209 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,423 | 1,575 | -35.0% | -4,101 to 2,407 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,823 | 2,625 | -31.3% | -6,649 to 4,253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.3 | -0.5% | -0.501 to 0.38 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 221 | -32.3% | -543 to 332 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 714 | 493 | -31.0% | -1,129 to 686 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 40.6 | -32.2% | -100 to 61.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.19 | +9.3% | -0.645 to 1.02 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.277 | 0.278 | +0.2% | -0.00689 to 0.00819 | EVEN, no difference beyond the noise |
| host CPU-seconds | 497 | 498 | +0.3% | -12.1 to 14.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.15 | -4.7% | -2.05 to 1.35 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
