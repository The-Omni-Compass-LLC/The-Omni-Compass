# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -2.36 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00666 to 0.0121 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,433 | 2,507 | +3.0% | -224 to 372 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,615 | 3,511 | -2.9% | -723 to 514 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.5 | 8.62 | +1.4% | -0.193 to 0.429 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 365 | 368 | +0.8% | -0.447 to 6.18 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,605 | 1,592 | -0.8% | -55.4 to 30.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 159 | +0.2% | -0.981 to 1.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.284 | -0.7% | -0.0135 to 0.00922 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.7% | -9.68 to 6.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.31 | -0.6% | -0.164 to 0.123 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
