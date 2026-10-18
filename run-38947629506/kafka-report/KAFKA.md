# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.2% | -1.9 to 0.816 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0118 to -0.000673 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,556 | 2,575 | +0.7% | -48 to 85.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,716 | 3,818 | +2.7% | -422 to 626 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.06 | 8.82 | -2.6% | -0.873 to 0.396 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 385 | +0.4% | -0.00893 to 3.02 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,667 | -0.2% | -62.3 to 57 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 165 | +0.2% | -1.91 to 2.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.306 | 0.305 | -0.5% | -0.0184 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 219 | 218 | -0.4% | -13 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.55 | -0.3% | -0.214 to 0.193 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 389 messages a second; base rate 58.4/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 154 | +5.1% | -28 to 43.1 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00326 to 0.00368 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,107 | 1,424 | -32.4% | -3,519 to 2,152 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,393 | 2,272 | -33.0% | -5,549 to 3,307 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.5% | -0.42 to 0.313 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 282 | 196 | -30.3% | -454 to 283 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 637 | 448 | -29.8% | -970 to 590 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 51.7 | 36.2 | -30.0% | -82.5 to 51.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.3 | +15.1% | -0.372 to 0.977 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.279 | 0.281 | +0.5% | -0.00857 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 494 | +0.6% | -15.2 to 21.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.43 | 7.15 | -3.8% | -2.03 to 1.48 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 730 | +0.4% | -8.78 to 14.2 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | +0.0% | -0.00516 to 0.00855 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,397 | 2,096 | -12.6% | -1,364 to 762 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,673 | 3,299 | -10.2% | -1,898 to 1,149 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.29 | -1.3% | -0.252 to 0.0544 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 277 | -11.8% | -162 to 88.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,305 | 2,985 | -9.7% | -1,439 to 798 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 271 | 240 | -11.7% | -139 to 74.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.13 | +6.3% | -0.445 to 0.697 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.345 | 0.345 | -0.1% | -0.013 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 614 | 614 | +0.0% | -21 to 21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.88 | 1.87 | -0.4% | -0.051 to 0.037 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -2.94 to 3.24 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00653 to 0.00173 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,390 | 2,351 | -1.6% | -159 to 81.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,800 | 3,680 | -3.2% | -908 to 668 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.49 | -0.2% | -0.0822 to 0.0562 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 316 | -2.2% | -41.7 to 27.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,680 | 1,658 | -1.3% | -144 to 100 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 140 | -2.5% | -17.6 to 10.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.306 | 0.305 | -0.3% | -0.00521 to 0.00351 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 531 | -0.1% | -5.27 to 4.73 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.22 | -0.1% | -0.0547 to 0.0487 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
