# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 339 | -0.4% | -4.73 to 2.24 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.00113 to 0.000325 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,466 | 2,532 | +2.6% | -86.1 to 217 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,752 | 3,716 | -1.0% | -344 to 271 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.39 | 9.37 | -0.3% | -0.245 to 0.198 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 378 | 387 | +2.4% | -25 to 42.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,647 | 1,640 | -0.4% | -92.9 to 79.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 167 | +1.6% | -9.87 to 15.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.291 | -0.8% | -0.0179 to 0.0133 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 204 | -0.8% | -12.5 to 9.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.32 | -0.4% | -0.158 to 0.132 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 146 | -0.2% | -1.25 to 0.622 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00288 to 0.00193 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,249 | 2,351 | +4.5% | -138 to 341 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,633 | 3,619 | -0.4% | -615 to 587 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.5 | +0.8% | -0.301 to 0.493 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 314 | +2.4% | -24 to 39 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 674 | 670 | -0.6% | -94.3 to 85.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.4 | 56.7 | +0.4% | -4.5 to 5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.277 | 0.281 | +1.6% | -0.0171 to 0.0258 | EVEN, no difference beyond the noise |
| host CPU-seconds | 496 | 504 | +1.6% | -30.5 to 46.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.52 | 7.66 | +1.8% | -0.482 to 0.752 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.1/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 723 | -0.2% | -4.53 to 1.16 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.0125 to 0.00652 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,237 | 2,275 | +1.7% | -95.6 to 171 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,526 | 3,536 | +0.3% | -201 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.16 | -3.8% | -1.42 to 0.768 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 301 | 306 | +1.7% | -12.7 to 22.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,171 | 3,181 | +0.3% | -53.1 to 71.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 262 | 266 | +1.2% | -13.8 to 20 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.3 to 0.795 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.335 | 0.334 | -0.3% | -0.00632 to 0.00425 | EVEN, no difference beyond the noise |
| host CPU-seconds | 575 | 574 | -0.2% | -11.6 to 9.25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.76 | +0.0% | -0.0365 to 0.0374 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -2.64 to 2.11 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0123 to 0.00686 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,306 | 2,189 | -5.1% | -292 to 58.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,536 | 3,559 | +0.7% | -521 to 568 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.16 | 8.14 | -0.3% | -0.201 to 0.158 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 299 | 293 | -2.2% | -33.5 to 20.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,640 | 1,607 | -2.0% | -104 to 38.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 132 | 129 | -2.0% | -13 to 7.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.293 | -0.3% | -0.00985 to 0.00794 | EVEN, no difference beyond the noise |
| host CPU-seconds | 524 | 522 | -0.3% | -18.9 to 16.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 3.17 | -0.2% | -0.131 to 0.118 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
