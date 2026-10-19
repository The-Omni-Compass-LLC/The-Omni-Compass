# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.471 to 0.251 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.00472 to 0.00216 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,515 | 2,536 | +0.9% | -179 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,727 | -3.8% | -698 to 404 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.96 | 8.77 | -2.2% | -0.674 to 0.283 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 382 | +0.8% | -4.45 to 10.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,661 | -0.2% | -72.8 to 67.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 165 | +0.8% | -1.6 to 4.16 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.304 | -1.1% | -0.0243 to 0.0173 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 218 | -1.1% | -17.3 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.55 | -1.1% | -0.276 to 0.197 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 150 | +1.8% | -8.63 to 13.8 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00393 to 0.00452 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,374 | 2,430 | +2.4% | -326 to 437 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,663 | 3,843 | +4.9% | -792 to 1,153 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% | -0.128 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 308 | -3.4% | -52.5 to 30.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 698 | 729 | +4.4% | -83.4 to 145 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59 | 56.2 | -4.7% | -12.9 to 7.39 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.279 | 0.28 | +0.2% | -0.00578 to 0.00684 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 493 | +0.3% | -10.2 to 13.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.31 | -1.4% | -0.748 to 0.544 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.1% | -7.58 to 6.48 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0172 to 0.0149 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,250 | 2,242 | -0.4% | -318 to 301 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,564 | 3,544 | -0.6% | -227 to 187 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.38 | 7.86 | -6.2% | -1.28 to 0.243 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 303 | -0.5% | -32.6 to 29.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,212 | 3,206 | -0.2% | -190 to 178 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 265 | 263 | -0.7% | -28.3 to 24.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.325 | 0.327 | +0.6% | -0.013 to 0.0172 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 562 | +0.9% | -25.7 to 35.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | +1.0% | -0.0784 to 0.111 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -2.72 to 1.18 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0128 to 0.00937 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,178 | 2,249 | +3.3% | -240 to 383 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,424 | 3,465 | +1.2% | -227 to 309 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.19 | -0.2% | -0.235 to 0.206 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 285 | 292 | +2.7% | -31.1 to 46.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,588 | 1,588 | +0.0% | -44.7 to 44.7 | EVEN, the same |
| consumer lag, mean messages waiting | 126 | 129 | +2.4% | -13.1 to 19.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.297 | 0.296 | -0.2% | -0.00796 to 0.00674 | EVEN, no difference beyond the noise |
| host CPU-seconds | 530 | 529 | -0.1% | -11.7 to 10.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.21 | +0.1% | -0.0527 to 0.0597 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
