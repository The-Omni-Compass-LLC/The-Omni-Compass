# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 418 | +20.2% | 69.3 to 71.4 | better |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0253 to 0.0229 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,735 | 11 | -99.4% | -1,879 to -1,569 | better |
| end-to-end latency, 99th percentile (ms) | 2,538 | 13.7 | -99.5% | -2,641 to -2,407 | better |
| end-to-end latency, median (ms) | 9.87 | 8 | -18.9% | -2.33 to -1.41 | better |
| end-to-end latency, mean (ms) | 266 | 8.76 | -96.7% | -259 to -256 | better |
| consumer lag, most messages waiting at once | 1,122 | 42 | -96.3% | -1,159 to -1,001 | better |
| consumer lag, mean messages waiting | 117 | 3.65 | -96.9% | -114 to -112 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 6.15 | +207.5% | 1.89 to 6.41 | **WORSE** |
| consumers running, most at once | 2 | 7.33 | +266.7% | 2.46 to 8.2 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.32 | +8.3% | 0.0141 to 0.0346 | **WORSE** |
| host CPU-seconds | 138 | 149 | +8.0% | 6.13 to 16.1 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 2.96 | -10.1% | -0.491 to -0.176 | better |
| consumer changes written (the knob's moves) | 2 | 14.7 | +633.3% | 6.93 to 18.4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 149 | 172 | +15.8% | 22.5 to 24.5 | better |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00324 to 0.0021 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,549 | 11.9 | -99.2% | -1,605 to -1,470 | better |
| end-to-end latency, 99th percentile (ms) | 2,470 | 16.2 | -99.3% | -2,642 to -2,265 | better |
| end-to-end latency, median (ms) | 10.8 | 10.7 | -0.6% | -0.496 to 0.364 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 212 | 11.9 | -94.4% | -215 to -184 | better |
| consumer lag, most messages waiting at once | 460 | 45.7 | -90.1% | -519 to -309 | better |
| consumer lag, mean messages waiting | 39.9 | 2.09 | -94.8% | -41.2 to -34.4 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.69 | +184.4% | 2.42 to 4.95 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.259 | 0.27 | +4.2% | -0.00986 to 0.0315 | no difference beyond the noise |
| host CPU-seconds | 309 | 322 | +4.0% | -11.9 to 36.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.92 | 6.22 | -10.1% | -1.21 to -0.199 | better |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1952 messages a second; base rate 292.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 737 | 858 | +16.4% | 117 to 125 | better |
| throughput (messages a second consumed) | 858 | 858 | -0.0% | -0.0429 to -0.014 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 1,692 | 8.68 | -99.5% | -1,765 to -1,602 | better |
| end-to-end latency, 99th percentile (ms) | 2,605 | 9.91 | -99.6% | -2,801 to -2,389 | better |
| end-to-end latency, median (ms) | 6.96 | 5.56 | -20.1% | -1.49 to -1.3 | better |
| end-to-end latency, mean (ms) | 228 | 6.38 | -97.2% | -233 to -209 | better |
| consumer lag, most messages waiting at once | 2,325 | 133 | -94.3% | -2,350 to -2,032 | better |
| consumer lag, mean messages waiting | 200 | 5.45 | -97.3% | -204 to -184 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.72 | +285.9% | 5.38 to 6.05 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.339 | +10.4% | 0.0227 to 0.041 | **WORSE** |
| host CPU-seconds | 365 | 402 | +10.3% | 25.7 to 49.2 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.65 | 1.56 | -5.3% | -0.131 to -0.0436 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 2.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 429 | +16.3% | 55.4 to 65.1 | better |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0163 to 0.00336 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,777 | 9.81 | -99.4% | -2,336 to -1,198 | better |
| end-to-end latency, 99th percentile (ms) | 2,729 | 12.8 | -99.5% | -3,367 to -2,066 | better |
| end-to-end latency, median (ms) | 8.17 | 7 | -14.3% | -1.3 to -1.03 | better |
| end-to-end latency, mean (ms) | 238 | 7.63 | -96.8% | -301 to -159 | better |
| consumer lag, most messages waiting at once | 1,231 | 49 | -96.0% | -1,441 to -923 | better |
| consumer lag, mean messages waiting | 106 | 3.32 | -96.9% | -134 to -71.3 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.6% | 5.93 to 5.94 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.295 | 0.31 | +5.1% | 0.00799 to 0.0223 | **WORSE** |
| host CPU-seconds | 351 | 368 | +4.9% | 10.2 to 24.3 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 2.86 | -9.8% | -0.351 to -0.271 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
