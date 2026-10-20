# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 339 | -0.4% | -4.99 to 2.17 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | 0.000107 to 0.0104 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,505 | 2,512 | +0.3% | -196 to 209 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,616 | 3,663 | +1.3% | -152 to 247 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.52 | 9.47 | -0.5% | -0.494 to 0.39 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 375 | 383 | +2.3% | -18.1 to 35.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,637 | 1,629 | -0.5% | -91.8 to 76.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 165 | +0.9% | -7.06 to 10 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.295 | +0.1% | -0.014 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 206 | +0.0% | -9.74 to 9.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.36 | +0.5% | -0.158 to 0.189 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
