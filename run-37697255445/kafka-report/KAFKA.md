# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 420 | +20.8% | 71.8 to 72.7 | better |
| throughput (messages a second consumed) | 419 | 421 | +0.4% | 1.72 to 1.76 | better |
| end-to-end latency, 95th percentile (ms) | 1,701 | 11 | -99.4% | -1,804 to -1,575 | better |
| end-to-end latency, 99th percentile (ms) | 2,515 | 13.2 | -99.5% | -2,617 to -2,388 | better |
| end-to-end latency, median (ms) | 10 | 7.97 | -20.7% | -3.09 to -1.08 | better |
| end-to-end latency, mean (ms) | 267 | 8.85 | -96.7% | -264 to -253 | better |
| consumer lag, most messages waiting at once | 1,129 | 42.3 | -96.3% | -1,140 to -1,034 | better |
| consumer lag, mean messages waiting | 118 | 3.71 | -96.9% | -121 to -108 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.67 | +183.3% | 3.06 to 4.27 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.314 | +6.4% | -0.00484 to 0.0426 | no difference beyond the noise |
| host CPU-seconds | 138 | 146 | +5.7% | -3.07 to 18.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 2.89 | -12.1% | -0.655 to -0.139 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 149 | 172 | +15.8% | 23 to 23.9 | better |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00561 to 0.00522 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,639 | 22.3 | -98.6% | -1,716 to -1,517 | better |
| end-to-end latency, 99th percentile (ms) | 2,424 | 285 | -88.3% | -2,298 to -1,981 | better |
| end-to-end latency, median (ms) | 11.2 | 11.1 | -1.1% | -0.299 to 0.0633 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 221 | 18.1 | -91.8% | -209 to -197 | better |
| consumer lag, most messages waiting at once | 465 | 125 | -73.2% | -378 to -303 | better |
| consumer lag, mean messages waiting | 41.2 | 3.41 | -91.7% | -39.8 to -35.7 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.17 | +158.3% | 3 to 3.34 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.272 | 0.279 | +2.3% | -0.0082 to 0.0208 | no difference beyond the noise |
| host CPU-seconds | 325 | 332 | +2.2% | -9.9 to 24.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.28 | 6.43 | -11.7% | -1.2 to -0.503 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1937 messages a second; base rate 290.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 851 | +16.2% | 111 to 127 | better |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0209 to -0.0114 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 1,636 | 9.19 | -99.4% | -1,758 to -1,496 | better |
| end-to-end latency, 99th percentile (ms) | 2,587 | 10.6 | -99.6% | -2,903 to -2,250 | better |
| end-to-end latency, median (ms) | 8.34 | 6.08 | -27.1% | -2.36 to -2.16 | better |
| end-to-end latency, mean (ms) | 230 | 6.67 | -97.1% | -250 to -197 | better |
| consumer lag, most messages waiting at once | 2,279 | 90.3 | -96.0% | -2,367 to -2,011 | better |
| consumer lag, mean messages waiting | 203 | 5.88 | -97.1% | -222 to -173 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.1 | +255.0% | 3.17 to 7.03 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.325 | 0.377 | +16.0% | 0.0275 to 0.0762 | **WORSE** |
| host CPU-seconds | 371 | 433 | +16.5% | 32.1 to 90.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.69 | +0.3% | -0.118 to 0.127 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 969 messages a second; base rate 145.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 426 | +15.4% | 53.6 to 59.8 | better |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.0291 to 0.0235 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,486 | 10.1 | -99.3% | -1,549 to -1,403 | better |
| end-to-end latency, 99th percentile (ms) | 2,356 | 11.9 | -99.5% | -2,518 to -2,170 | better |
| end-to-end latency, median (ms) | 8.59 | 7.3 | -15.1% | -1.36 to -1.23 | better |
| end-to-end latency, mean (ms) | 203 | 7.72 | -96.2% | -213 to -178 | better |
| consumer lag, most messages waiting at once | 1,072 | 45.7 | -95.7% | -1,090 to -963 | better |
| consumer lag, mean messages waiting | 91.3 | 3.34 | -96.3% | -94.4 to -81.4 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.5% | 5.92 to 5.93 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.334 | +8.6% | 0.0114 to 0.0417 | **WORSE** |
| host CPU-seconds | 355 | 386 | +8.7% | 14.1 to 47.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.02 | -5.8% | -0.345 to -0.0266 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
