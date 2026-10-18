# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.918 to 0.62 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.025 to 0.0263 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,549 | 2,556 | +0.3% | -122 to 136 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,628 | 3,691 | +1.8% | -223 to 351 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.63 | +0.7% | -0.305 to 0.426 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 380 | -0.5% | -15.7 to 11.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,658 | 1,655 | -0.2% | -77 to 69.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 163 | -1.3% | -4.93 to 0.617 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.291 | 0.289 | -0.7% | -0.013 to 0.00894 | no difference beyond the noise |
| host CPU-seconds | 209 | 208 | -0.7% | -9.43 to 6.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.38 | -0.6% | -0.151 to 0.107 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.767 to 0.794 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00331 to 0.00345 | same |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,349 | +0.7% | -76.3 to 107 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,701 | -1.0% | -103 to 28.5 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.2% | -0.318 to 0.272 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 315 | -1.3% | -20.8 to 12.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 681 | 689 | +1.1% | -17.3 to 32.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 57.9 | 57.8 | -0.1% | -4.52 to 4.36 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.274 | 0.274 | -0.0% | -0.0155 to 0.0153 | no difference beyond the noise |
| host CPU-seconds | 491 | 491 | -0.0% | -27.4 to 27.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.41 | -0.0% | -0.431 to 0.427 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1937 messages a second; base rate 290.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 726 | +0.0% | -1.86 to 2.43 | no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0274 to 0.00906 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,428 | 2,441 | +0.5% | -50.3 to 75.1 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,968 | 3,728 | -6.0% | -493 to 12.8 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.19 | 8.16 | -0.3% | -0.542 to 0.492 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 329 | -1.1% | -12.3 to 4.85 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,400 | 3,367 | -1.0% | -178 to 114 | no difference beyond the noise |
| consumer lag, mean messages waiting | 289 | 286 | -1.0% | -10.7 to 4.75 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.341 | 0.336 | -1.3% | -0.0471 to 0.0384 | no difference beyond the noise |
| host CPU-seconds | 586 | 579 | -1.2% | -82.2 to 68.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.79 | 1.77 | -1.2% | -0.253 to 0.209 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.2% | -3.66 to 2.52 | no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00375 to 0.000242 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,386 | +0.2% | -437 to 448 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,683 | 3,717 | +0.9% | -120 to 189 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.15 | 8.13 | -0.2% | -0.0852 to 0.0459 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 315 | +0.6% | -35.3 to 38.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,682 | +0.3% | -189 to 199 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 139 | +0.4% | -15.2 to 16.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.294 | -0.4% | -0.00615 to 0.0039 | no difference beyond the noise |
| host CPU-seconds | 527 | 525 | -0.3% | -11.6 to 8.55 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.19 | 3.19 | -0.1% | -0.0839 to 0.0753 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
