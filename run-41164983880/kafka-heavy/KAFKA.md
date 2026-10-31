# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 174 | +17.9% | 25.7 to 26.9 | GAIN |
| throughput (messages a second consumed) | 174 | 174 | -0.0% | -0.00655 to 0.00312 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,654 | 12.5 | -99.5% | -2,772 to -2,512 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,978 | 34.5 | -99.1% | -3,996 to -3,890 | GAIN |
| end-to-end latency, median (ms) | 11.5 | 11.2 | -2.6% | -0.341 to -0.257 | GAIN |
| end-to-end latency, mean (ms) | 354 | 11.6 | -96.7% | -357 to -328 | GAIN |
| consumer lag, most messages waiting at once | 737 | 29.3 | -96.0% | -750 to -666 | GAIN |
| consumer lag, mean messages waiting | 65.1 | 2.02 | -96.9% | -64.4 to -61.8 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 4.79 | +139.4% | 2.31 to 3.27 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.288 | 0.295 | +2.3% | 0.000992 to 0.0124 | power given |
| host CPU-seconds | 509 | 520 | +2.2% | 1.24 to 21 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.68 | 6.65 | -13.3% | -1.17 to -0.876 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
