# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.0% | -0.84 to 0.781 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0151 to 0.0134 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,540 | 2,510 | -1.2% | -199 to 138 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,765 | 3,595 | -4.5% | -750 to 410 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.89 | 8.67 | -2.5% | -0.617 to 0.17 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 380 | +0.2% | -4.07 to 5.49 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,647 | -0.5% | -103 to 86.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 165 | +0.1% | -1.62 to 2.09 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.302 | 0.299 | -1.1% | -0.0202 to 0.0135 | no difference beyond the noise |
| host CPU-seconds | 217 | 214 | -1.1% | -14.4 to 9.72 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.51 | 3.48 | -1.1% | -0.241 to 0.166 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.474 to 0.193 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00437 to 0.00881 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,483 | 2,463 | -0.8% | -47 to 7.31 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,730 | 3,840 | +2.9% | -208 to 428 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | -0.5% | -0.15 to 0.0395 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 332 | 334 | +0.5% | -5.87 to 9.5 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 702 | 698 | -0.6% | -35 to 26.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 60.5 | 61.2 | +1.2% | -0.607 to 2.03 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.289 | 0.285 | -1.5% | -0.0168 to 0.0081 | no difference beyond the noise |
| host CPU-seconds | 511 | 503 | -1.5% | -29.3 to 14.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.71 | 7.6 | -1.4% | -0.443 to 0.229 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1946 messages a second; base rate 291.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.0% | -1.24 to 0.867 | no difference beyond the noise |
| throughput (messages a second consumed) | 856 | 856 | +0.0% | -0.0298 to 0.0317 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,339 | -1.7% | -107 to 24.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,674 | 3,677 | +0.1% | -35.9 to 42.2 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.15 | 7.05 | -1.4% | -0.346 to 0.139 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 308 | -0.9% | -4.46 to -1.28 | better |
| consumer lag, most messages waiting at once | 3,292 | 3,281 | -0.3% | -94.7 to 74 | no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 267 | -1.2% | -4.71 to -1.62 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.319 | 0.319 | -0.1% | -0.0119 to 0.0111 | no difference beyond the noise |
| host CPU-seconds | 569 | 569 | -0.0% | -21.9 to 21.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.73 | -0.0% | -0.066 to 0.0655 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | +0.0% | -1.94 to 1.98 | no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00812 to 0.00663 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,337 | 2,327 | -0.4% | -214 to 193 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,608 | 3,577 | -0.9% | -254 to 191 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.59 | 8.56 | -0.3% | -0.0701 to 0.0234 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 312 | 311 | -0.4% | -18.7 to 16 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,657 | 1,655 | -0.1% | -23.2 to 18.5 | no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 137 | -0.8% | -6.69 to 4.44 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.309 | 0.309 | +0.0% | -0.0122 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 535 | 537 | +0.3% | -20 to 23.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.27 | +0.3% | -0.135 to 0.157 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
