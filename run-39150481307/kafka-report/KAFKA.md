# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.1% | -3.16 to 3.68 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0279 to 0.0063 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,520 | 2,482 | -1.5% | -206 to 132 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,877 | 3,663 | -5.5% | -686 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.83 | 9.28 | -5.7% | -1.71 to 0.588 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 383 | -1.4% | -41.9 to 30.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,661 | 1,664 | +0.2% | -94.2 to 99.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 165 | -2.1% | -22.7 to 15.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% | -0.0203 to 0.0141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.0% | -14.3 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.37 | -1.1% | -0.204 to 0.13 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -0.819 to 0.267 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00074 to 0.00209 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,403 | 2,450 | +1.9% | -255 to 348 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,767 | 3,826 | +1.6% | -256 to 373 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% | -0.0659 to 0.0712 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 331 | +2.0% | -4.34 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 693 | 691 | -0.3% | -50.4 to 46.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.6 | 60.6 | +1.7% | -2.89 to 4.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.284 | +0.1% | -0.00859 to 0.00889 | EVEN, no difference beyond the noise |
| host CPU-seconds | 508 | 509 | +0.0% | -15.4 to 15.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 7.69 | +0.2% | -0.194 to 0.23 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 290.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 724 | -0.3% | -3.72 to -0.4 | LOSS |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0233 to 0.00788 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,329 | 2,315 | -0.6% | -312 to 284 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,574 | 3,725 | +4.2% | 70.2 to 232 | LOSS |
| end-to-end latency, median (ms) | 8.38 | 7.94 | -5.2% | -0.928 to 0.0503 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 316 | +1.0% | -11.5 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,227 | 3,270 | +1.3% | -83.2 to 168 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 274 | +0.9% | -10.9 to 15.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.325 | -0.2% | -0.00964 to 0.00857 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 559 | +0.0% | -18.6 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | +0.3% | -0.0536 to 0.0642 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -2.29 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.00677 to 0.00817 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,395 | 2,372 | -1.0% | -397 to 351 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,675 | 3,776 | +2.8% | -79 to 282 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.54 | -0.2% | -0.163 to 0.133 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 320 | +0.9% | -21.1 to 26.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,685 | 1,681 | -0.3% | -97.6 to 88.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 142 | +0.7% | -8.28 to 10.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | +0.3% | -0.00694 to 0.00871 | EVEN, no difference beyond the noise |
| host CPU-seconds | 534 | 538 | +0.6% | -11.1 to 17.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.27 | +0.7% | -0.0492 to 0.0954 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
