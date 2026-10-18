# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -9.59 to 7.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.00508 to 0.000495 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,433 | 2,382 | -2.1% | -446 to 344 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,560 | 3,582 | +0.6% | -525 to 568 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 21.9 | 15.5 | -29.1% | -21.5 to 8.76 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 380 | 381 | +0.3% | -45.3 to 47.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,584 | 1,607 | +1.4% | -111 to 156 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 167 | +1.3% | -13.6 to 17.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.257 | 0.255 | -0.5% | -0.00768 to 0.00493 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 183 | -0.5% | -5.29 to 3.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.99 | 2.99 | -0.1% | -0.027 to 0.0192 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.844 to 0.788 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00408 to 0.0073 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,448 | 2,470 | +0.9% | -71.1 to 116 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,848 | 3,759 | -2.3% | -405 to 227 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.3% | -0.11 to 0.0497 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 334 | 331 | -0.9% | -26.8 to 20.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 696 | -1.0% | -45.8 to 31.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.1 | 60.1 | -1.5% | -5.35 to 3.49 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.28 | -0.5% | -0.00676 to 0.00387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 495 | 493 | -0.5% | -11.4 to 6.06 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.48 | 7.45 | -0.5% | -0.141 to 0.0631 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1926 messages a second; base rate 288.9/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 725 | +0.2% | -3.95 to 6.22 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | +0.0% | -0.021 to 0.0299 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,252 | 2,202 | -2.2% | -255 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,630 | 3,556 | -2.1% | -431 to 282 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.13 | 8.01 | -1.5% | -0.918 to 0.677 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 297 | -3.0% | -43.8 to 25.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,181 | -0.6% | -302 to 265 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 257 | -2.9% | -37.3 to 21.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.3 to 0.795 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.344 | 0.333 | -3.3% | -0.0373 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 592 | 572 | -3.5% | -66.3 to 25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.75 | -3.6% | -0.212 to 0.0798 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -2.77 to 1.38 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.00596 to 0.00665 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,215 | 2,248 | +1.5% | 19.1 to 46 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,587 | 3,573 | -0.4% | -109 to 81.1 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.12 | -1.0% | -0.211 to 0.0459 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 294 | 296 | +0.7% | -8.3 to 12.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,610 | 1,599 | -0.7% | -73 to 50.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 129 | 130 | +0.7% | -4.06 to 5.96 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.14 | +7.0% | -0.364 to 0.644 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.295 | 0.294 | -0.6% | -0.00665 to 0.00304 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 524 | -0.6% | -12.5 to 6.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.19 | 3.18 | -0.4% | -0.0796 to 0.0549 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
