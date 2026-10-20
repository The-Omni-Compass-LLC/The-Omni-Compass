# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 721 | -0.8% | -22 to 10 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 849 | -0.0% | -1.66 to 1.03 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,260 | 2,968 | +31.4% | -2,353 to 3,769 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,631 | 4,479 | +23.4% | -2,461 to 4,157 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.51 | 7.51 | +0.0% | -0.259 to 0.26 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 300 | 386 | +28.8% | -282 to 454 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,197 | 3,836 | +20.0% | -2,034 to 3,313 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 332 | +28.5% | -238 to 385 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | +0.8% | -0.0752 to 0.106 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.347 | -1.3% | -0.0144 to 0.00554 | EVEN, no difference beyond the noise |
| host CPU-seconds | 624 | 617 | -1.1% | -24.2 to 9.96 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.9 | -0.4% | -0.0634 to 0.0498 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
