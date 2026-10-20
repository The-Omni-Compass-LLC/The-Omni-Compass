# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 969 messages a second; base rate 109.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 337 | -0.9% | -12.7 to 6.43 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.00352 to 0.00801 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,406 | 2,577 | +7.1% | -36.3 to 378 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,762 | 3,788 | +0.7% | -206 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.63 | -1.4% | -0.558 to 0.32 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 372 | 394 | +5.9% | -8.17 to 52.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,686 | 1,665 | -1.3% | -220 to 177 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 162 | 169 | +4.6% | -9.03 to 24.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.1 | +5.1% | -0.158 to 0.363 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.284 | 0.283 | -0.4% | -0.0134 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 202 | -0.4% | -9.51 to 8.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.32 | +0.6% | -0.0296 to 0.0666 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
