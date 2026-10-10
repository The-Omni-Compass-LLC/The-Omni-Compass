# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.4% | -2.23 to -0.215 | **WORSE** |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0184 to 0.0145 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,471 | 2,474 | +0.1% | -110 to 114 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,768 | 3,732 | -1.0% | -368 to 296 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.47 | 9.28 | -2.0% | -0.826 to 0.448 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 379 | 380 | +0.5% | -3.9 to 7.6 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,641 | 1,633 | -0.4% | -21.5 to 6.79 | no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.5% | -5.22 to 6.91 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.293 | -0.7% | -0.0145 to 0.0102 | no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.7% | -9.87 to 7.11 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.34 | -0.3% | -0.143 to 0.122 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 148 | +0.1% | -0.765 to 0.941 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00143 to 0.00181 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,350 | 2,370 | +0.8% | -257 to 295 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,738 | 3,672 | -1.8% | -342 to 209 | no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.7 | -0.2% | -0.0667 to 0.0294 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 313 | -1.9% | -34 to 21.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 696 | 675 | -3.1% | -75 to 32.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 58.7 | 57 | -2.9% | -9.34 to 5.91 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.257 | 0.256 | -0.5% | -0.00604 to 0.00361 | no difference beyond the noise |
| host CPU-seconds | 460 | 458 | -0.5% | -10.6 to 6.48 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.94 | 6.9 | -0.5% | -0.15 to 0.0792 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 728 | -0.2% | -5.22 to 1.82 | no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0156 to 0.0133 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,474 | 2,503 | +1.2% | -77.5 to 136 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,743 | -2.1% | -712 to 548 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.45 | +0.8% | -0.152 to 0.274 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 333 | +1.5% | -17.2 to 27.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,394 | 3,433 | +1.2% | -13.8 to 93.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 291 | +1.6% | -13.4 to 22.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.32 | 0.319 | -0.2% | -0.00656 to 0.00499 | no difference beyond the noise |
| host CPU-seconds | 570 | 568 | -0.3% | -9.26 to 6.09 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.73 | -0.0% | -0.0173 to 0.0157 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `0a74e9a66193`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.0% | -2.85 to 2.68 | no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0183 to 0.0149 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,355 | +2.2% | -218 to 321 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,641 | 3,589 | -1.4% | -443 to 339 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.73 | 8.71 | -0.2% | -0.298 to 0.261 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 311 | -0.6% | -29.3 to 25.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,656 | 1,657 | +0.1% | -57.2 to 59.2 | no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 137 | -0.4% | -13 to 11.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.323 | 0.325 | +0.5% | -0.00644 to 0.00967 | no difference beyond the noise |
| host CPU-seconds | 561 | 565 | +0.8% | -11.9 to 20.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.44 | +0.8% | -0.0908 to 0.147 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
