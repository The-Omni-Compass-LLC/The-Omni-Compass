# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.0% | -7.3 to 7.18 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0219 to 0.0164 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,484 | 2,506 | +0.9% | -343 to 386 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,838 | 3,843 | +0.1% | -55.5 to 65.8 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.16 | 9.18 | +0.2% | -1.99 to 2.01 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 388 | +0.7% | -54.5 to 59.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,644 | 1,681 | +2.2% | -110 to 183 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 169 | +0.7% | -21.2 to 23.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | -0.6% | -0.0184 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 189 | -0.5% | -13 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 3.06 | -0.5% | -0.273 to 0.244 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.798 to -0.0966 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00324 to 0.00286 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,470 | +3.2% | -59 to 212 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,784 | 3,821 | +1.0% | -48.5 to 123 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.2% | -0.0426 to -0.0127 | GAIN |
| end-to-end latency, mean (ms) | 325 | 334 | +2.9% | -10 to 28.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 693 | 709 | +2.3% | -91.2 to 123 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.8 | 61.3 | +2.6% | -3.88 to 6.94 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.288 | 0.287 | -0.5% | -0.00821 to 0.00525 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 506 | -0.5% | -14.4 to 9.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.68 | 7.66 | -0.2% | -0.178 to 0.148 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.3% | -6.03 to 2.07 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0691 to 0.0434 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,399 | +1.0% | 10.4 to 37.7 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,749 | +2.7% | -158 to 355 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.37 | 8.23 | -1.7% | -0.979 to 0.691 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 326 | +1.9% | -17.8 to 29.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,288 | 3,353 | +2.0% | -6.87 to 137 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 285 | +2.1% | -14.4 to 26.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.426 to 0.666 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.324 | 0.322 | -0.5% | -0.00851 to 0.00516 | EVEN, no difference beyond the noise |
| host CPU-seconds | 556 | 553 | -0.5% | -15.5 to 9.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.69 | -0.3% | -0.0334 to 0.0241 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -2.67 to 1.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -1.18 to 1.18 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,453 | +1.5% | -56.1 to 126 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,844 | +2.1% | -226 to 387 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.49 | 8.53 | +0.4% | -0.127 to 0.202 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 325 | +1.7% | -6.43 to 17.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,698 | 1,710 | +0.7% | -77.6 to 102 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 143 | +1.5% | -1.79 to 6.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.331 | +1.4% | -0.0108 to 0.0198 | EVEN, no difference beyond the noise |
| host CPU-seconds | 582 | 590 | +1.5% | -19 to 36.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.53 | 3.59 | +1.7% | -0.118 to 0.236 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
