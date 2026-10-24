# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 972 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -1.19 to -0.254 | LOSS |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0188 to 0.00901 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,408 | 2,435 | +1.1% | -456 to 510 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,588 | 3,500 | -2.5% | -413 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.6 | +0.0% | -0.0602 to 0.0635 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 366 | 366 | -0.0% | -37.6 to 37.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,597 | 1,604 | +0.4% | -49.2 to 63.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 158 | -0.3% | -16.6 to 15.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.283 | -0.7% | -0.00693 to 0.00308 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 203 | -0.6% | -4.84 to 2.31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.3 | -0.4% | -0.0726 to 0.0454 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.672 to 0.71 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00377 to 0.00478 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,599 | 2,532 | -2.6% | -250 to 115 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,962 | 3,905 | -1.5% | -422 to 307 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.193 to 0.175 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 351 | 345 | -1.5% | -27 to 16.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 742 | 730 | -1.7% | -61.4 to 36 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.4 | 63.2 | -1.9% | -3.71 to 1.23 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.285 | -0.7% | -0.0115 to 0.00761 | EVEN, no difference beyond the noise |
| host CPU-seconds | 505 | 502 | -0.6% | -20.5 to 14.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.63 | 7.58 | -0.6% | -0.343 to 0.253 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1950 messages a second; base rate 292.5/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.1% | -4.53 to 2.65 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.0123 to 0.0082 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,301 | 2,323 | +1.0% | -36.2 to 80.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,621 | 3,567 | -1.5% | -172 to 62.5 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 16.6 | 11.6 | -30.4% | -20.3 to 10.2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 315 | -1.9% | -20.9 to 8.69 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,303 | 3,234 | -2.1% | -183 to 44.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 284 | 277 | -2.5% | -19.1 to 4.83 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.794 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.282 | +0.1% | -0.00515 to 0.00579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 503 | 504 | +0.1% | -9.38 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.53 | 1.53 | +0.3% | -0.0191 to 0.0276 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 983 messages a second; base rate 147.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 369 | +0.1% | -0.0832 to 0.893 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | +0.0% | -0.00502 to 0.00507 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,437 | 2,412 | -1.0% | -87.2 to 37.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,758 | +0.8% | -104 to 163 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.01 | 8 | -0.2% | -0.0496 to 0.0236 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 327 | -0.8% | -14 to 8.64 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,735 | 1,710 | -1.4% | -99.5 to 50.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 147 | 147 | -0.6% | -4.56 to 2.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.267 | 0.266 | -0.5% | -0.00501 to 0.00231 | EVEN, no difference beyond the noise |
| host CPU-seconds | 478 | 476 | -0.4% | -7.5 to 3.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.88 | 2.87 | -0.6% | -0.0466 to 0.0146 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
