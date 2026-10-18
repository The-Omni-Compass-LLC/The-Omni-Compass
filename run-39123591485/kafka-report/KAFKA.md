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

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.93 to 0.62 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000137 to 0.00119 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,323 | 2,381 | +2.5% | -9.73 to 125 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,735 | 3,657 | -2.1% | -285 to 128 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.9 | 10.7 | -1.3% | -0.615 to 0.327 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 318 | +0.7% | -8.9 to 13.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 692 | 690 | -0.3% | -80.1 to 76.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.2 | 58.2 | -0.0% | -2.16 to 2.13 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.261 | 0.256 | -1.8% | -0.0181 to 0.0089 | EVEN, no difference beyond the noise |
| host CPU-seconds | 468 | 459 | -1.8% | -32.4 to 16 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.05 | 6.93 | -1.6% | -0.485 to 0.253 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1921 messages a second; base rate 288.1/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 719 | -0.9% | -17.7 to 4.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 845 | 845 | +0.0% | -0.0149 to 0.0157 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,098 | 2,191 | +4.4% | 18.6 to 168 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,360 | 3,520 | +4.8% | -142 to 462 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.53 | 8.25 | -3.2% | -1.26 to 0.711 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 284 | 301 | +6.2% | -6.89 to 42.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,057 | 3,160 | +3.4% | -80.2 to 286 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 247 | 261 | +5.9% | -8.51 to 37.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.2% | -0.426 to 0.675 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.322 | 0.322 | +0.1% | -0.0118 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 552 | 554 | +0.3% | -18.6 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.71 | +1.2% | -0.0492 to 0.0893 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.4/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -3.12 to 1.49 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.841 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,442 | 2,476 | +1.4% | -154 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,746 | 3,782 | +1.0% | -470 to 542 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.89 | 7.91 | +0.2% | -0.113 to 0.146 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.5% | -31.2 to 40.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,710 | 1,721 | +0.6% | -67.7 to 88.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 145 | +1.2% | -14.6 to 17.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.283 | -0.6% | -0.00735 to 0.00421 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 507 | -0.6% | -14.9 to 8.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.07 | -0.4% | -0.0725 to 0.0466 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
