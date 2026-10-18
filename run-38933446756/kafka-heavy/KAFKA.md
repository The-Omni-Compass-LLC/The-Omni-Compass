# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 146 | -0.2% | -1.25 to 0.622 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00288 to 0.00193 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,249 | 2,351 | +4.5% | -138 to 341 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,633 | 3,619 | -0.4% | -615 to 587 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.5 | +0.8% | -0.301 to 0.493 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 314 | +2.4% | -24 to 39 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 674 | 670 | -0.6% | -94.3 to 85.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.4 | 56.7 | +0.4% | -4.5 to 5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.277 | 0.281 | +1.6% | -0.0171 to 0.0258 | EVEN, no difference beyond the noise |
| host CPU-seconds | 496 | 504 | +1.6% | -30.5 to 46.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.66 | +1.8% | -0.482 to 0.752 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
