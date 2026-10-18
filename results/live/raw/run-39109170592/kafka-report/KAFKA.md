# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.2% | -2.18 to 0.487 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | +0.0% | -0.0166 to 0.0263 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,542 | 2,570 | +1.1% | -127 to 183 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,618 | 3,615 | -0.1% | -458 to 453 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.65 | 9.5 | -1.5% | -1.56 to 1.26 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 388 | +1.0% | -3.17 to 10.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,672 | 1,654 | -1.1% | -89.6 to 52.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 170 | +0.8% | -3.07 to 5.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.271 | 0.267 | -1.3% | -0.0244 to 0.0176 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 192 | -1.2% | -17.4 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.14 | 3.11 | -1.0% | -0.275 to 0.213 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.03 to 0.739 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00509 to 0.00457 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,528 | 2,515 | -0.5% | -213 to 188 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,813 | 3,816 | +0.1% | -52.1 to 58.3 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% | -0.0755 to 0.0495 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 340 | 340 | +0.1% | -18.4 to 18.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 719 | 718 | -0.1% | -52.9 to 50.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.4 | 62.3 | -0.2% | -2.4 to 2.11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.5% | -0.00976 to 0.00698 | EVEN, no difference beyond the noise |
| host CPU-seconds | 493 | 491 | -0.5% | -17.3 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.44 | 7.41 | -0.4% | -0.27 to 0.211 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1917 messages a second; base rate 287.6/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 728 | -0.2% | -5.31 to 3.09 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 843 | 843 | -0.0% | -0.0294 to 0.0185 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,971 | 1,943 | -1.4% | -173 to 117 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,170 | 3,235 | +2.0% | -234 to 364 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.29 | 7.14 | -2.1% | -0.525 to 0.223 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 251 | 253 | +1.0% | -4.2 to 9.15 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,893 | 2,914 | +0.7% | -30.6 to 71.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 216 | 217 | +0.6% | -6.32 to 8.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | +19.3% | 0.383 to 0.39 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.332 | 0.334 | +0.6% | -0.00305 to 0.00681 | EVEN, no difference beyond the noise |
| host CPU-seconds | 592 | 596 | +0.7% | -6.43 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.82 | +0.8% | -0.0164 to 0.0464 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.2% | -2.93 to 1.23 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.013 to 0.00802 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,447 | +2.0% | -69.6 to 167 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,688 | 3,753 | +1.8% | -360 to 491 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.44 | 8.43 | -0.1% | -0.0662 to 0.0455 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 324 | +1.4% | -16.3 to 25.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,701 | 1,708 | +0.4% | -115 to 130 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 143 | +1.2% | -6.98 to 10.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | -0.5% | -0.011 to 0.0081 | EVEN, no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.4% | -20.8 to 16.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | -0.1% | -0.135 to 0.127 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
