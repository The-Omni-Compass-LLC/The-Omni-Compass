# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 341 | +0.2% | -1.33 to 2.76 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 419 | -0.1% | -2.05 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,607 | 2,593 | -0.5% | -160 to 132 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,832 | 3,722 | -2.9% | -749 to 528 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.39 | 9.29 | -1.0% | -0.474 to 0.278 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 397 | 386 | -2.8% | -34.9 to 12.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 1,664 | -2.1% | -130 to 60.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 167 | -3.3% | -17.8 to 6.38 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.289 | -1.2% | -0.0175 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 202 | -1.2% | -12.3 to 7.54 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.29 | -1.5% | -0.184 to 0.0873 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
