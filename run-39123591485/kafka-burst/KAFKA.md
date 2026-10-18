# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 965 messages a second; base rate 108.6/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 339 | -0.3% | -1.76 to -0.101 | LOSS |
| throughput (messages a second consumed) | 415 | 415 | -0.0% | -0.0339 to 0.0233 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,232 | 2,222 | -0.4% | -277 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,346 | 3,361 | +0.5% | -420 to 450 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.59 | -1.8% | -0.631 to 0.31 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 337 | +0.5% | -2.31 to 5.42 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,472 | 1,476 | +0.3% | -20.2 to 28.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 144 | 144 | +0.1% | -3 to 3.32 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.2% | -0.0189 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 212 | -1.1% | -13.6 to 8.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.46 | -0.8% | -0.208 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
