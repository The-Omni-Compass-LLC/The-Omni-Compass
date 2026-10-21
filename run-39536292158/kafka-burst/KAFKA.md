# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 340 | -0.5% | -6.64 to 3.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 419 | -0.1% | -2.03 to 1.27 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,540 | 2,512 | -1.1% | -311 to 255 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,900 | +3.6% | -10.7 to 283 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.37 | 9.42 | +0.5% | -0.396 to 0.494 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 393 | +2.4% | -23.2 to 41.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,689 | +1.3% | -74.7 to 119 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 170 | +2.4% | -11.4 to 19.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.289 | -1.2% | -0.017 to 0.00994 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 202 | -1.1% | -12 to 7.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.29 | -0.8% | -0.193 to 0.143 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
