# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 983 messages a second; base rate 110.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 343 | -0.1% | -1.13 to 0.472 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 423 | 422 | -0.0% | -0.0112 to 0.00711 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,633 | 2,507 | -4.8% | -465 to 213 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,859 | 3,934 | +1.9% | -351 to 501 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 22.3 | 13.2 | -40.6% | -24.9 to 6.76 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 407 | 405 | -0.3% | -8.41 to 6.12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,725 | 1,734 | +0.5% | -111 to 130 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 179 | 178 | -0.8% | -4.94 to 2.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.259 | 0.258 | -0.5% | -0.00694 to 0.00445 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 185 | -0.5% | -4.9 to 3.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3 | 2.99 | -0.4% | -0.0827 to 0.061 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.21 to 0.447 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | 4.83e-05 to 0.0011 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,459 | 2,493 | +1.4% | -268 to 336 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,792 | 3,844 | +1.4% | -146 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.6 | +0.2% | -0.136 to 0.185 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 337 | +3.0% | -20.2 to 39.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 684 | 700 | +2.3% | -14 to 45.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.8 | 62 | +3.6% | -1.23 to 5.57 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.279 | +0.2% | -0.0175 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 493 | +0.4% | -30.4 to 34.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.46 | +0.6% | -0.472 to 0.567 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | -0.0% | -3.82 to 3.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0319 to 0.0228 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,432 | +1.7% | -122 to 201 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,862 | 3,623 | -6.2% | -648 to 170 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.21 | 8.12 | -1.2% | -0.542 to 0.351 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 331 | 327 | -1.1% | -19.3 to 12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,367 | 3,326 | -1.2% | -144 to 62.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 288 | 285 | -1.1% | -14.5 to 8.11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.331 | 0.332 | +0.3% | -0.00363 to 0.00533 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 571 | +0.3% | -7.78 to 11.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.75 | +0.3% | -0.0155 to 0.0272 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 984 messages a second; base rate 147.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.0% | -0.729 to 0.437 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | -0.0% | -0.00676 to 0.00261 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,491 | 2,461 | -1.2% | -159 to 100 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,811 | -1.5% | -221 to 105 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.04 | 8 | -0.5% | -0.157 to 0.0726 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 338 | 334 | -1.1% | -14.9 to 7.17 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,737 | 1,722 | -0.9% | -85.7 to 55.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 152 | 150 | -1.4% | -5.59 to 1.45 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.273 | 0.272 | -0.5% | -0.013 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 487 | 486 | -0.4% | -21.3 to 17.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.94 | 2.93 | -0.3% | -0.132 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
