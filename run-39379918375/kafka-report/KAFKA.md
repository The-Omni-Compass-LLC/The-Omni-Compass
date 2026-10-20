# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.3/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.3% | -7.64 to 5.62 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.133 to 0.089 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,564 | 2,603 | +1.5% | -336 to 414 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,717 | 3,762 | +1.2% | -707 to 797 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.3 | 12 | +17.0% | -3.99 to 7.47 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 394 | 404 | +2.5% | -57.7 to 77.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,741 | +3.1% | -193 to 299 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 177 | +2.1% | -21.8 to 28.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.267 | 0.264 | -1.0% | -0.0254 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 190 | -1.0% | -18.1 to 14.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.1 | 3.08 | -0.7% | -0.242 to 0.197 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.07 to 0.666 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00183 to -8.62e-05 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,519 | 2,528 | +0.3% | -233 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,918 | -0.8% | -407 to 346 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.8 | +0.4% | -0.105 to 0.199 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 342 | 346 | +1.0% | -26.9 to 33.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 720 | 732 | +1.7% | -26.7 to 50.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.8 | 63.5 | +1.1% | -5.56 to 6.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.292 | +0.7% | -0.0095 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 514 | +0.8% | -15.9 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.7 | 7.77 | +0.9% | -0.222 to 0.359 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 725 | -0.4% | -6.35 to 1.09 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.0101 to 0.00282 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,364 | 2,451 | +3.7% | 56.4 to 119 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,749 | 3,797 | +1.3% | -5.12 to 99.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.29 | 8.09 | -2.5% | -1.29 to 0.878 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 335 | +3.9% | 2.76 to 22.3 | LOSS |
| consumer lag, most messages waiting at once | 3,374 | 3,389 | +0.4% | -114 to 144 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 283 | 293 | +3.4% | 0.867 to 18.6 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.32 | 0.32 | -0.0% | -0.00781 to 0.00753 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 549 | +0.1% | -14.8 to 16.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.67 | 1.68 | +0.5% | -0.031 to 0.0477 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -0.707 to 0.291 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00833 to 0.00379 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,431 | -1.2% | -127 to 69.5 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,781 | +0.4% | -311 to 340 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.48 | -0.1% | -0.111 to 0.0979 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 322 | -0.2% | -7.04 to 5.61 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,707 | 1,706 | -0.0% | -26.2 to 25.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 142 | -0.2% | -2.62 to 2.04 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.319 | 0.318 | -0.4% | -0.00749 to 0.00474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.3% | -12.2 to 8.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.38 | -0.3% | -0.0703 to 0.0532 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
