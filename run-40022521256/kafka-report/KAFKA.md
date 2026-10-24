# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 948 messages a second; base rate 106.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 336 | 336 | -0.0% | -10.6 to 10.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 407 | 407 | +0.0% | -0.00612 to 0.0107 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,043 | 2,661 | +30.3% | -1,855 to 3,092 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,890 | 3,716 | +28.6% | -1,737 to 3,390 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.8 | 8.7 | -1.0% | -0.572 to 0.389 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 375 | +23.3% | -165 to 308 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,274 | 1,568 | +23.0% | -788 to 1,375 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 128 | 157 | +22.9% | -68.6 to 127 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.7% | -0.0227 to -0.00681 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.291 | +2.0% | -0.0142 to 0.0257 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 208 | +2.0% | -9.88 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.43 | +2.0% | -0.136 to 0.27 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.947 to 1.04 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00313 to 0.00313 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,495 | 2,449 | -1.9% | -321 to 228 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,752 | 3,775 | +0.6% | -412 to 459 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.0976 to 0.0496 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 331 | -1.3% | -35.9 to 26.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 706 | 712 | +0.9% | -51 to 63.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.4 | 60.6 | -1.4% | -7.33 to 5.63 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.281 | -0.9% | -0.0125 to 0.00721 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 494 | -1.0% | -22.4 to 12.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.54 | 7.46 | -1.0% | -0.371 to 0.218 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1907 messages a second; base rate 286.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 732 | +0.0% | -6.53 to 7.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 839 | 839 | -0.0% | -0.0432 to 0.0297 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,802 | 1,801 | -0.1% | -72 to 69.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,025 | 2,971 | -1.8% | -280 to 171 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.29 | 7.19 | -1.3% | -0.179 to -0.0139 | GAIN |
| end-to-end latency, mean (ms) | 231 | 228 | -1.2% | -23.7 to 18.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,770 | 2,733 | -1.3% | -147 to 72.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 197 | 195 | -1.5% | -19.3 to 13.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.26 | +13.0% | -0.313 to 0.832 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.335 | 0.334 | -0.3% | -0.0199 to 0.0178 | EVEN, no difference beyond the noise |
| host CPU-seconds | 596 | 595 | -0.2% | -33.9 to 32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.81 | 1.81 | -0.2% | -0.12 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -1.25 to -0.148 | LOSS |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0135 to 0.0127 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,300 | 2,267 | -1.4% | -142 to 77.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,469 | 3,620 | +4.3% | -379 to 680 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.41 | 8.54 | +1.5% | -0.0656 to 0.31 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 296 | 301 | +1.7% | -0.167 to 10.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,629 | 1,628 | -0.1% | -39.2 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 130 | 133 | +1.7% | 0.325 to 4.07 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.317 | 0.328 | +3.3% | -0.00878 to 0.0296 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 583 | +3.3% | -15.1 to 52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.55 | +3.5% | -0.0865 to 0.324 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
