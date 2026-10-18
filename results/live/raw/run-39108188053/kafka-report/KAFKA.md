# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 339 | -0.5% | -3.19 to -0.316 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00262 to 0.00608 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,517 | 2,555 | +1.5% | -124 to 200 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,785 | +1.0% | -531 to 606 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.45 | 9.57 | +1.2% | -0.313 to 0.549 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 392 | +2.5% | -20.6 to 40 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,659 | 1,670 | +0.6% | -42.4 to 63.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 169 | +1.5% | -12 to 17.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.294 | -1.1% | -0.0241 to 0.0174 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 206 | -1.1% | -17.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.36 | -0.6% | -0.246 to 0.209 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.38 to 0.64 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00178 to 0.00121 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,354 | 2,348 | -0.3% | -125 to 112 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,647 | +0.2% | -80.8 to 96.1 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.2 | -0.3% | -0.102 to 0.0237 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 317 | +0.7% | -6.79 to 11.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 688 | 680 | -1.1% | -31.5 to 16.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57 | 58.1 | +2.0% | -2.23 to 4.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.6% | -0.0271 to 0.0493 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.275 | 0.272 | -0.9% | -0.0105 to 0.00564 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 488 | -0.9% | -18.4 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.38 | -0.6% | -0.208 to 0.119 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1951 messages a second; base rate 292.7/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 731 | -0.1% | -1.2 to -0.58 | LOSS |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.023 to 0.00693 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,431 | 2,418 | -0.5% | -137 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,680 | -1.1% | -72.1 to -10.3 | GAIN |
| end-to-end latency, median (ms) | 8.15 | 8.56 | +5.1% | -1.07 to 1.89 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 329 | +1.2% | -9.33 to 17.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,348 | 3,342 | -0.2% | -40.1 to 29.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 289 | +0.9% | -8.94 to 13.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.306 | -3.2% | -0.0409 to 0.0206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 563 | 546 | -3.1% | -70.3 to 35.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.66 | -3.0% | -0.211 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -2.29 to 0.523 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0135 to 0.0063 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,387 | +1.7% | -59.5 to 140 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,617 | 3,610 | -0.2% | -224 to 210 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.56 | 8.5 | -0.6% | -0.189 to 0.0799 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 317 | +1.2% | -11.6 to 18.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,668 | 1,670 | +0.1% | -60.3 to 64.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 140 | +1.0% | -4.48 to 7.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.306 | -0.4% | -0.0094 to 0.00688 | EVEN, no difference beyond the noise |
| host CPU-seconds | 532 | 532 | -0.1% | -16.4 to 15.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | +0.2% | -0.0796 to 0.0902 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
