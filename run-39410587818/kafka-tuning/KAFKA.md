# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 388 | +5.8% | -68.8 to 111 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00769 to 0.00314 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 1,619 | -33.9% | -4,173 to 2,512 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,872 | 2,569 | -33.6% | -6,225 to 3,620 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.27 | 8.13 | -1.7% | -0.641 to 0.359 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 219 | -33.4% | -531 to 311 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,719 | 1,180 | -31.3% | -2,762 to 1,685 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 96.7 | -33.5% | -235 to 138 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.18 | +9.2% | -0.638 to 1.01 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.306 | 0.309 | +0.9% | -0.0038 to 0.00952 | EVEN, no difference beyond the noise |
| host CPU-seconds | 545 | 549 | +0.8% | -8.43 to 17.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.17 | -4.1% | -0.815 to 0.545 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
