# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 964 messages a second; base rate 108.5/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 338 | 339 | +0.1% | -2.63 to 3.38 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 414 | 414 | +0.0% | -0.0134 to 0.0215 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,310 | 2,332 | +1.0% | -281 to 325 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,508 | 3,317 | -5.5% | -1,066 to 683 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.56 | -0.5% | -0.387 to 0.297 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 349 | 345 | -1.0% | -42.6 to 35.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,537 | 1,502 | -2.3% | -152 to 81.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 149 | 147 | -0.9% | -15.6 to 12.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.5% | -0.101 to 0.12 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.287 | 0.283 | -1.3% | -0.0281 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.2% | -19.7 to 14.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.32 | -1.3% | -0.298 to 0.207 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.883 to 1.09 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00327 to 0.00141 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,492 | 2,417 | -3.0% | -133 to -16.4 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,844 | 3,749 | -2.5% | -506 to 316 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.0% | -0.102 to 0.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 334 | 329 | -1.5% | -26.3 to 16.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 708 | 705 | -0.5% | -91.7 to 85 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.5 | 61.3 | -0.3% | -2.7 to 2.27 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.277 | -0.8% | -0.0114 to 0.00681 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 488 | -0.8% | -20.6 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.36 | -0.8% | -0.362 to 0.239 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1964 messages a second; base rate 294.7/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 734 | 733 | -0.1% | -3.32 to 1.26 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 864 | 864 | -0.0% | -1.68 to 1.01 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,628 | 2,569 | -2.3% | -240 to 121 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,941 | 3,974 | +0.8% | -304 to 370 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.86 | 7.8 | -0.7% | -0.897 to 0.793 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 353 | 352 | -0.2% | -17.3 to 15.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,537 | 3,545 | +0.2% | -245 to 260 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 311 | 310 | -0.3% | -16.4 to 14.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.287 | -1.1% | -0.00895 to 0.0025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 516 | 512 | -0.9% | -15 to 5.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.56 | 1.55 | -0.8% | -0.0424 to 0.017 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -3.6 to 2.23 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.00889 to 0.0115 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,321 | -0.9% | -290 to 247 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,719 | 3,777 | +1.6% | -185 to 300 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.53 | -0.2% | -0.0408 to 0.00542 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 318 | +1.0% | -25.2 to 31.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,670 | -0.4% | -69.3 to 54.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 141 | +1.1% | -10.3 to 13.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.306 | -0.5% | -0.0109 to 0.00774 | EVEN, no difference beyond the noise |
| host CPU-seconds | 534 | 531 | -0.5% | -20.1 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.23 | -0.3% | -0.141 to 0.123 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
