# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -1.12 to -0.862 | LOSS |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -0.00465 to 0.00917 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,501 | -1.8% | -186 to 94.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,713 | +1.7% | -291 to 417 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.76 | 8.69 | -0.8% | -0.123 to -0.00955 | GAIN |
| end-to-end latency, mean (ms) | 376 | 378 | +0.6% | -4.45 to 8.82 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,662 | 1,649 | -0.8% | -53 to 27 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 163 | -0.1% | -5.17 to 5.01 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.298 | -0.9% | -0.0138 to 0.00845 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 214 | -0.9% | -9.85 to 6.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.47 | -0.6% | -0.148 to 0.109 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.2% | -0.76 to 1.36 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00382 to 0.00534 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,563 | 2,518 | -1.8% | -177 to 85.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,001 | 3,797 | -5.1% | -517 to 108 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% | -0.121 to 0.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 349 | 339 | -3.0% | -36.9 to 15.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 731 | 713 | -2.4% | -57.6 to 22.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.3 | 62.5 | -2.8% | -6.08 to 2.49 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.8% | -0.0112 to 0.00687 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 490 | -0.8% | -20 to 12.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 7.4 | -1.0% | -0.296 to 0.153 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.3% | -7.06 to 3.12 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -1.7 to 1.06 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,311 | 2,379 | +2.9% | -100 to 236 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,729 | 3,697 | -0.9% | -286 to 222 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.44 | 8.11 | -3.9% | -0.938 to 0.282 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 324 | +2.0% | -31.2 to 44.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,253 | 3,308 | +1.7% | -202 to 313 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 278 | 281 | +1.1% | -29.4 to 35.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.426 to 0.666 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.325 | 0.331 | +1.8% | -0.00318 to 0.0151 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 570 | +2.1% | -5.13 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.75 | +2.4% | -0.00826 to 0.0892 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.4% | -4.06 to 1.16 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.843 to 0.525 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,396 | 2,420 | +1.0% | -168 to 216 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,705 | 3,803 | +2.6% | -18.2 to 214 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.52 | 8.51 | -0.1% | -0.0915 to 0.0822 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 329 | +3.2% | -18.8 to 39.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,695 | +1.1% | -122 to 157 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 146 | +2.7% | -9.15 to 16.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.306 | -0.4% | -0.013 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 532 | -0.1% | -20.5 to 19.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | +0.3% | -0.114 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
