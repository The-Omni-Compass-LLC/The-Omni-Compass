# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.1% | -4.89 to 5.47 | no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0117 to -0.002 | **WORSE** |
| end-to-end latency, 95th percentile (ms) | 2,551 | 2,540 | -0.4% | -59.2 to 36.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,770 | -5.4% | -472 to 44.6 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.49 | 9.36 | -1.4% | -0.544 to 0.28 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 395 | 389 | -1.4% | -33.1 to 22.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,673 | -2.5% | -163 to 78.5 | no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 168 | -1.9% | -13.2 to 6.72 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.292 | -0.9% | -0.0193 to 0.0139 | no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.8% | -13.1 to 9.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -0.9% | -0.21 to 0.148 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.957 to 0.563 | no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.000563 to 0.00186 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,185 | 2,144 | -1.9% | -190 to 108 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,389 | 3,466 | +2.3% | -87.2 to 240 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.1 | 11.1 | +0.1% | -0.0928 to 0.112 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 285 | 288 | +1.3% | -20 to 27.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 648 | 644 | -0.7% | -17.1 to 8.42 | no difference beyond the noise |
| consumer lag, mean messages waiting | 51.9 | 52.4 | +1.2% | -2.16 to 3.35 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.0115 to 0.00119 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.266 | 0.266 | -0.2% | -0.00584 to 0.00479 | no difference beyond the noise |
| host CPU-seconds | 478 | 477 | -0.2% | -10.3 to 8.49 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.21 | 7.21 | -0.1% | -0.157 to 0.15 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1949 messages a second; base rate 292.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 771 | +5.7% | -143 to 225 | no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0148 to 0.00251 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,455 | 1,736 | -29.3% | -4,323 to 2,885 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,754 | 2,608 | -30.5% | -6,419 to 4,127 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.42 | 7.13 | -3.9% | -1.82 to 1.24 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 233 | -29.3% | -574 to 380 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,369 | 2,353 | -30.2% | -5,548 to 3,516 | no difference beyond the noise |
| consumer lag, mean messages waiting | 288 | 204 | -29.3% | -497 to 328 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.17 | +8.5% | -0.591 to 0.932 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.315 | +0.6% | -0.00827 to 0.0122 | no difference beyond the noise |
| host CPU-seconds | 558 | 562 | +0.7% | -16.4 to 24 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.63 | -4.3% | -0.397 to 0.252 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -2.39 to 0.814 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0144 to 0.0121 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,342 | 2,413 | +3.1% | -61.7 to 205 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,696 | 3,672 | -0.6% | -369 to 322 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.6 | +0.3% | -0.0906 to 0.139 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 315 | 323 | +2.5% | -12.1 to 28 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,669 | 1,709 | +2.4% | -50.5 to 132 | no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 143 | +2.3% | -7.41 to 13.9 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.314 | 0.313 | -0.5% | -0.00998 to 0.00698 | no difference beyond the noise |
| host CPU-seconds | 547 | 543 | -0.6% | -15.7 to 9.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.3 | -0.4% | -0.0862 to 0.0606 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
