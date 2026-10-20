# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 365 | -0.3% | -3.08 to 0.883 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.1% | -0.996 to 0.364 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,296 | 2,310 | +0.6% | -12.2 to 38.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,565 | 3,580 | +0.4% | -149 to 178 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.26 | 8.18 | -0.9% | -0.276 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 302 | 306 | +1.6% | -18.7 to 28.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,626 | 1,643 | +1.0% | -37.1 to 69.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 133 | 135 | +1.3% | -7.89 to 11.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.307 | 0.305 | -0.5% | -0.0108 to 0.00753 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 547 | -0.3% | -17.9 to 14.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.32 | -0.1% | -0.103 to 0.0966 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
