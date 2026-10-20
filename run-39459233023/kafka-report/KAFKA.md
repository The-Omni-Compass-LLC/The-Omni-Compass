# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -1.09 to 0.095 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 420 | +0.1% | -1.3 to 2.07 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,590 | 2,533 | -2.2% | -247 to 133 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,746 | 3,802 | +1.5% | -400 to 511 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.46 | 9.53 | +0.8% | -0.518 to 0.661 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 391 | +0.5% | -5.56 to 9.38 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,676 | 1,690 | +0.8% | -42.2 to 70.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 169 | -0.3% | -5.34 to 4.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.302 | 0.3 | -0.8% | -0.00748 to 0.00256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 210 | -0.8% | -4.62 to 1.03 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.41 | -0.6% | -0.0844 to 0.0423 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.253 to -0.0998 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00402 to 0.00343 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,522 | +0.9% | -109 to 154 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,809 | 3,829 | +0.5% | -338 to 378 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.056 to 0.026 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 337 | +0.7% | -5 to 9.73 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 717 | 705 | -1.7% | -22.8 to -1.17 | GAIN |
| consumer lag, mean messages waiting | 61.6 | 61.7 | +0.1% | -1.42 to 1.57 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.291 | -0.4% | -0.00759 to 0.00498 | EVEN, no difference beyond the noise |
| host CPU-seconds | 516 | 514 | -0.4% | -13.5 to 8.89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.79 | 7.76 | -0.3% | -0.197 to 0.145 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 726 | -0.1% | -1.36 to 0.465 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.0386 to 0.036 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,399 | 2,373 | -1.1% | -117 to 66.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,678 | 3,650 | -0.8% | -241 to 185 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.54 | 7.55 | +0.1% | -0.144 to 0.16 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 312 | 310 | -0.7% | -6.4 to 2.31 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,289 | 3,265 | -0.7% | -42.5 to -4.86 | GAIN |
| consumer lag, mean messages waiting | 270 | 268 | -0.7% | -5.65 to 1.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.362 | 0.366 | +1.3% | -0.00575 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 646 | 655 | +1.4% | -9.09 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.98 | 2 | +1.4% | -0.0239 to 0.0807 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -1.28 to 1.15 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0219 to 0.00778 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,350 | 2,307 | -1.8% | -70.4 to -15 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,651 | 3,707 | +1.6% | -524 to 638 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.56 | 8.54 | -0.3% | -0.0565 to 0.0125 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 311 | -1.6% | -20.6 to 10.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,661 | 1,676 | +0.9% | -79.8 to 110 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 138 | -1.7% | -7.94 to 3.16 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.309 | 0.307 | -0.6% | -0.0109 to 0.00694 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 533 | -0.6% | -18.5 to 11.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.24 | -0.6% | -0.121 to 0.0799 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
