# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.1/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 721 | -0.6% | -20.1 to 10.9 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | +0.0% | -0.0145 to 0.0194 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,181 | 2,238 | +2.6% | -15.1 to 128 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,548 | 3,593 | +1.2% | -36.5 to 125 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.36 | 8.03 | -4.0% | -1.05 to 0.38 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 299 | 310 | +3.9% | -11.7 to 34.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,177 | 3,186 | +0.3% | -231 to 250 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 269 | +3.7% | -11.4 to 30.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.16 | +8.0% | -0.245 to 0.564 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.334 | 0.332 | -0.5% | -0.016 to 0.0129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 571 | -0.5% | -27.1 to 21.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.76 | +0.1% | -0.0342 to 0.0384 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | -11.2 to 23.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
