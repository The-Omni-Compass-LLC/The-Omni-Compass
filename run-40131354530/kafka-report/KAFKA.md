# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -1.67 to -0.406 | LOSS |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0151 to 0.0117 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,592 | 2,571 | -0.8% | -280 to 238 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,694 | 3,729 | +0.9% | -609 to 678 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.72 | 8.64 | -0.9% | -0.539 to 0.38 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 383 | +0.4% | -5.05 to 8.07 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,651 | 1,660 | +0.5% | -45 to 61.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 164 | -0.2% | -5.52 to 4.88 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.303 | 0.301 | -0.8% | -0.0135 to 0.00883 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 216 | -0.7% | -9.43 to 6.25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.52 | 3.51 | -0.4% | -0.136 to 0.105 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 156 | +5.9% | -29.3 to 46.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00507 to 0.00369 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,615 | 1,684 | -35.6% | -4,682 to 2,821 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,041 | 2,576 | -36.2% | -6,478 to 3,548 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.7% | -0.225 to 0.0725 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 353 | 229 | -35.1% | -592 to 345 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 721 | 516 | -28.4% | -1,024 to 614 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.8 | 42.4 | -34.6% | -107 to 62.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.19 | +9.3% | -0.572 to 0.943 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.274 | 0.273 | -0.4% | -0.0112 to 0.00886 | EVEN, no difference beyond the noise |
| host CPU-seconds | 490 | 488 | -0.4% | -20 to 15.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.4 | 7 | -5.5% | -1.8 to 0.995 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1949 messages a second; base rate 292.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 729 | -0.3% | -2.57 to -1.3 | LOSS |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0144 to 0.00397 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,498 | 2,531 | +1.3% | -23.3 to 89.5 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,822 | 3,832 | +0.3% | -216 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.37 | 7.33 | -0.6% | -0.0964 to 0.0118 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 342 | +1.9% | -14.3 to 27.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,435 | 3,440 | +0.1% | -169 to 178 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 294 | 299 | +1.5% | -7.92 to 16.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.314 | 0.312 | -0.4% | -0.0131 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 558 | -0.2% | -22 to 19.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | +0.1% | -0.0613 to 0.0637 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.19 to 0.272 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0068 to 0.00587 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,394 | 2,331 | -2.6% | -332 to 207 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,770 | 3,732 | -1.0% | -333 to 256 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.25 | +0.1% | -0.146 to 0.168 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 313 | -2.0% | -27.5 to 14.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,708 | 1,663 | -2.6% | -211 to 121 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 138 | -2.1% | -13.5 to 7.49 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.301 | 0.304 | +1.0% | -0.0166 to 0.0227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 538 | 544 | +1.1% | -30 to 42.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.3 | +1.3% | -0.175 to 0.257 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
