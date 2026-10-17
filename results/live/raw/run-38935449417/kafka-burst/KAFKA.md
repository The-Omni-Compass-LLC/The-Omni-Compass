# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.0% | -5.55 to 5.46 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0153 to 0.0204 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,522 | 2,504 | -0.7% | -254 to 218 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,733 | -1.8% | -528 to 388 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.86 | 8.9 | +0.5% | -0.0816 to 0.163 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 380 | -0.8% | -31.6 to 25.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,640 | -0.9% | -46.8 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 163 | -0.8% | -13.3 to 10.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.306 | 0.303 | -0.9% | -0.0151 to 0.00928 | EVEN, no difference beyond the noise |
| host CPU-seconds | 219 | 217 | -1.0% | -10.8 to 6.65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.53 | -0.9% | -0.159 to 0.0917 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
