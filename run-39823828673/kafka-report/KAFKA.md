# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -2.78 to 1.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0184 to 0.0245 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,502 | -2.5% | -343 to 216 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,763 | 3,696 | -1.8% | -289 to 155 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.05 | 8.88 | -2.0% | -0.845 to 0.492 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 376 | 380 | +1.0% | -7.04 to 14.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,658 | 1,639 | -1.1% | -76.4 to 39.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 163 | -0.0% | -4.77 to 4.74 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | +0.1% | -0.0224 to 0.0229 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 221 | +0.1% | -15.9 to 16.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.6 | +0.2% | -0.25 to 0.267 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 145 | -1.9% | -7.16 to 1.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00361 to 0.00404 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,232 | +6.6% | 25.6 to 249 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,445 | 3,633 | +5.5% | -409 to 785 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% | -0.096 to 0.0433 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 280 | 314 | +12.0% | -3.34 to 70.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 653 | 643 | -1.6% | -69.9 to 49.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 51.2 | 57.6 | +12.7% | -1.77 to 14.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | -0.1% | -0.0129 to 0.00999 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.253 | 0.252 | -0.6% | -0.00759 to 0.00438 | EVEN, no difference beyond the noise |
| host CPU-seconds | 454 | 451 | -0.6% | -13.5 to 7.71 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.85 | 6.94 | +1.3% | -0.116 to 0.291 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -3.07 to 0.679 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.011 to 0.0239 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,298 | 2,297 | -0.0% | -235 to 234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,658 | 3,775 | +3.2% | -284 to 517 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.86 | 7.78 | -1.1% | -0.329 to 0.161 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 310 | +1.5% | -7.85 to 17 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,222 | 3,287 | +2.0% | -13.4 to 143 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 268 | +1.5% | -5.89 to 14.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.346 | 0.342 | -1.2% | -0.0116 to 0.00321 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 595 | -1.0% | -19.8 to 8.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.82 | -0.8% | -0.0592 to 0.0293 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | +0.1% | -1.04 to 1.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00219 to 0.00144 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,357 | 2,237 | -5.1% | -223 to -18.5 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,506 | 3,594 | +2.5% | -193 to 371 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.56 | 8.51 | -0.6% | -0.161 to 0.0604 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 308 | 301 | -2.4% | -22.5 to 8.03 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,637 | 1,615 | -1.3% | -104 to 60.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 133 | -3.0% | -9.75 to 1.55 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% | -0.296 to 0.786 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.305 | 0.305 | -0.0% | -0.0117 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 530 | 530 | +0.1% | -22.2 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.22 | +0.0% | -0.141 to 0.144 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
