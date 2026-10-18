# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -1.62 to 0.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -0.00593 to 0.0118 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,642 | 2,585 | -2.2% | -115 to 0.0358 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,769 | 3,692 | -2.0% | -657 to 503 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.5 | 9.37 | -1.3% | -0.591 to 0.34 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 391 | 391 | +0.0% | -6.54 to 6.84 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,682 | 1,676 | -0.3% | -15.7 to 4.37 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 170 | +0.4% | -2.66 to 3.98 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.293 | -0.5% | -0.00826 to 0.00515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.6% | -5.32 to 3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.33 | -0.4% | -0.082 to 0.054 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.497 to 0.746 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000751 to 0.00134 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,382 | +0.3% | -91.3 to 106 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,793 | 3,651 | -3.7% | -586 to 302 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.2 | -0.7% | -0.264 to 0.116 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 317 | -2.0% | -27.5 to 14.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 688 | -2.3% | -22.6 to -9.43 | GAIN |
| consumer lag, mean messages waiting | 59.1 | 58.4 | -1.2% | -4.9 to 3.52 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.276 | 0.273 | -1.0% | -0.0103 to 0.00488 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 489 | -1.0% | -18.4 to 8.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.46 | 7.38 | -1.0% | -0.271 to 0.116 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 727 | -0.3% | -6.16 to 1.31 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.00582 to 0.0022 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,278 | 2,310 | +1.4% | -133 to 196 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,529 | 3,664 | +3.8% | 54.6 to 216 | LOSS |
| end-to-end latency, median (ms) | 7.43 | 7.5 | +0.8% | -0.179 to 0.303 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 301 | 312 | +3.6% | -16.1 to 37.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,211 | 3,276 | +2.0% | -119 to 250 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 262 | 272 | +3.9% | -13.1 to 33.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | -0.6% | -0.0104 to 0.00638 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 557 | -0.5% | -15.2 to 9.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.7 | -0.2% | -0.0391 to 0.0328 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -4.55 to 3.02 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00459 to -0.000151 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,348 | 2,363 | +0.6% | -305 to 335 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,731 | 3,783 | +1.4% | -113 to 216 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.58 | 8.57 | -0.1% | -0.176 to 0.158 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 321 | +1.8% | -26.7 to 38.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,671 | 1,683 | +0.7% | -81.2 to 105 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 142 | +1.5% | -12 to 16.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.309 | -0.7% | -0.00827 to 0.004 | EVEN, no difference beyond the noise |
| host CPU-seconds | 541 | 537 | -0.7% | -16.3 to 8.59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.28 | 3.27 | -0.5% | -0.12 to 0.087 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
