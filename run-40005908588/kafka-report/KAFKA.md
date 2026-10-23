# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 968 messages a second; base rate 108.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 364 | +7.4% | -75.2 to 126 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 416 | 416 | +0.0% | 0.000705 to 0.00816 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,508 | 1,592 | -36.5% | -3,848 to 2,017 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,822 | 2,548 | -33.3% | -4,926 to 2,377 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.66 | 8.46 | -2.3% | -1 to 0.594 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 244 | -35.9% | -542 to 269 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,622 | 1,179 | -27.3% | -1,757 to 871 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 105 | -35.6% | -230 to 114 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.882 to 1.37 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -2.2 to 3.54 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.293 | 0.293 | +0.1% | -0.00355 to 0.00436 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 210 | +0.2% | -2.65 to 3.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.23 | -6.0% | -1.07 to 0.661 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.21 to 0.544 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00448 to 0.00447 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,550 | +0.1% | -74.8 to 81.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,841 | 3,955 | +3.0% | -281 to 509 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.6 | -0.3% | -0.117 to 0.0417 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 348 | +2.1% | -20.8 to 35 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 711 | 732 | +2.9% | -10.4 to 51.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.5 | 63.5 | +1.6% | -3.46 to 5.47 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.289 | 0.284 | -1.6% | -0.0134 to 0.0041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 501 | -1.6% | -23.7 to 7.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 7.58 | -1.4% | -0.376 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.1/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724 | 724 | +0.0% | -4.99 to 5.53 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | +0.0% | -0.0159 to 0.0238 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,269 | 2,236 | -1.4% | -210 to 144 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,636 | 3,542 | -2.6% | -180 to -8.47 | GAIN |
| end-to-end latency, median (ms) | 8.13 | 8.11 | -0.4% | -0.882 to 0.825 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 302 | -1.5% | -25.9 to 16.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,259 | 3,170 | -2.8% | -248 to 69.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 266 | 261 | -1.6% | -24.1 to 15.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.301 to 0.798 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.347 | 0.337 | -2.7% | -0.0342 to 0.0156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 596 | 580 | -2.6% | -63.2 to 32.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.78 | -2.6% | -0.208 to 0.111 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -3.94 to 2.5 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.846 to 0.53 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,239 | 2,235 | -0.1% | -223 to 217 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,580 | 3,627 | +1.3% | -326 to 419 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.34 | 8.27 | -0.8% | -0.128 to -0.00389 | GAIN |
| end-to-end latency, mean (ms) | 295 | 298 | +1.1% | -28 to 34.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,608 | 1,614 | +0.4% | -84.6 to 96 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 130 | 131 | +1.2% | -11.3 to 14.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.31 | 0.308 | -0.5% | -0.00378 to 0.000697 | EVEN, no difference beyond the noise |
| host CPU-seconds | 553 | 551 | -0.3% | -5.78 to 2.38 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.35 | -0.1% | -0.0483 to 0.0383 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
