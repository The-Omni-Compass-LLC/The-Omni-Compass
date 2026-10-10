# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -1.93 to 1.12 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00207 to 0.00458 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,477 | 2,520 | +1.8% | -115 to 202 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,664 | 3,735 | +2.0% | -42.6 to 186 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.73 | -0.2% | -0.0645 to 0.0265 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 374 | 378 | +1.2% | -0.348 to 9.41 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,651 | 1,640 | -0.6% | -18.3 to -2.35 | better |
| consumer lag, mean messages waiting | 161 | 163 | +0.9% | -0.696 to 3.6 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.304 | 0.303 | -0.3% | -0.0186 to 0.0168 | no difference beyond the noise |
| host CPU-seconds | 218 | 217 | -0.3% | -13.4 to 12.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.53 | -0.2% | -0.199 to 0.187 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 146 | -0.8% | -5.27 to 2.88 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00319 to 0.00249 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,406 | 2,540 | +5.6% | -401 to 670 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,960 | +3.6% | -183 to 455 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.4% | -0.18 to 0.0878 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 351 | +7.8% | -51.8 to 102 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 694 | 729 | +5.0% | -63.5 to 133 | no difference beyond the noise |
| consumer lag, mean messages waiting | 59.6 | 63.6 | +6.7% | -7.49 to 15.5 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.279 | 0.277 | -0.7% | -0.00865 to 0.00499 | no difference beyond the noise |
| host CPU-seconds | 491 | 488 | -0.6% | -15.5 to 9.66 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.4 | 7.42 | +0.2% | -0.31 to 0.344 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 726 | -0.2% | -5.93 to 2.51 | no difference beyond the noise |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.033 to 0.026 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,466 | 2,503 | +1.5% | -10.9 to 84.7 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,831 | 3,886 | +1.4% | -101 to 211 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.28 | 8.21 | -0.8% | -0.985 to 0.844 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 336 | 343 | +2.0% | -4.79 to 18.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,417 | 3,435 | +0.5% | -156 to 191 | no difference beyond the noise |
| consumer lag, mean messages waiting | 293 | 299 | +2.1% | -0.744 to 13 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.332 | 0.332 | -0.0% | -0.0126 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 570 | 572 | +0.2% | -22 to 24.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.75 | +0.5% | -0.0708 to 0.0866 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -3.12 to 0.719 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00285 to -0.000739 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 2,344 | 2,424 | +3.4% | -172 to 332 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,647 | 3,792 | +4.0% | -57.8 to 348 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.68 | 8.67 | -0.1% | -0.388 to 0.37 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 329 | +4.4% | -22.3 to 50.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,678 | 1,724 | +2.8% | -81.7 to 174 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 145 | +4.2% | -9.77 to 21.5 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.321 | 0.32 | -0.3% | -0.0232 to 0.0215 | no difference beyond the noise |
| host CPU-seconds | 558 | 556 | -0.2% | -40 to 37.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | +0.1% | -0.243 to 0.249 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
