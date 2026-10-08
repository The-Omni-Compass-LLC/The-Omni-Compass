# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 419 | +20.5% | 70 to 72.5 | better |
| throughput (messages a second consumed) | 417 | 419 | +0.4% | 1.72 to 1.77 | better |
| end-to-end latency, 95th percentile (ms) | 1,671 | 10.9 | -99.3% | -1,747 to -1,574 | better |
| end-to-end latency, 99th percentile (ms) | 2,462 | 13.6 | -99.4% | -2,775 to -2,122 | better |
| end-to-end latency, median (ms) | 10.2 | 7.96 | -22.0% | -3.44 to -1.05 | better |
| end-to-end latency, mean (ms) | 262 | 9.11 | -96.5% | -261 to -245 | better |
| consumer lag, most messages waiting at once | 1,102 | 49.7 | -95.5% | -1,113 to -991 | better |
| consumer lag, mean messages waiting | 116 | 3.82 | -96.7% | -117 to -108 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.84 | +191.9% | 3.33 to 4.34 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.318 | +7.3% | -0.00359 to 0.0468 | no difference beyond the noise |
| host CPU-seconds | 138 | 148 | +6.7% | -2.43 to 21.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 2.94 | -11.0% | -0.653 to -0.0767 | better |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 172 | +16.0% | 22.2 to 25.3 | better |
| throughput (messages a second consumed) | 172 | 172 | -0.1% | -0.465 to 0.152 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,608 | 14.2 | -99.1% | -1,763 to -1,426 | better |
| end-to-end latency, 99th percentile (ms) | 2,545 | 18.4 | -99.3% | -2,817 to -2,236 | better |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -1.3% | -1.04 to 0.728 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 223 | 12.1 | -94.6% | -241 to -180 | better |
| consumer lag, most messages waiting at once | 487 | 27.3 | -94.4% | -494 to -426 | better |
| consumer lag, mean messages waiting | 42.1 | 2.1 | -95.0% | -45 to -35.1 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 5.83 | +191.7% | 3.8 to 3.86 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.324 | +9.4% | -0.0313 to 0.0872 | no difference beyond the noise |
| host CPU-seconds | 352 | 384 | +9.0% | -34.4 to 97.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.9 | 7.41 | -6.1% | -1.83 to 0.863 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 2.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732 | 848 | +15.8% | 111 to 119 | better |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.055 to 0.0321 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,581 | 9.32 | -99.4% | -1,619 to -1,525 | better |
| end-to-end latency, 99th percentile (ms) | 2,440 | 10.7 | -99.6% | -2,573 to -2,285 | better |
| end-to-end latency, median (ms) | 8.36 | 6.03 | -27.9% | -2.35 to -2.31 | better |
| end-to-end latency, mean (ms) | 218 | 6.79 | -96.9% | -222 to -201 | better |
| consumer lag, most messages waiting at once | 2,189 | 128 | -94.1% | -2,099 to -2,022 | better |
| consumer lag, mean messages waiting | 191 | 5.9 | -96.9% | -191 to -179 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.5% | 5.93 to 5.93 | **WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | **WORSE** |
| host CPU busy (share of the run) | 0.34 | 0.405 | +19.2% | 0.0514 to 0.0789 | **WORSE** |
| host CPU-seconds | 390 | 466 | +19.5% | 59.5 to 92.6 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.83 | +3.2% | -0.00589 to 0.121 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 14 to 14 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a0b5d2381e9e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 428 | +16.0% | 56 to 62.3 | better |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00576 to 0.00206 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,617 | 10.2 | -99.4% | -1,742 to -1,471 | better |
| end-to-end latency, 99th percentile (ms) | 2,500 | 12.1 | -99.5% | -2,676 to -2,300 | better |
| end-to-end latency, median (ms) | 8.52 | 7.31 | -14.2% | -1.43 to -0.992 | better |
| end-to-end latency, mean (ms) | 221 | 7.92 | -96.4% | -237 to -188 | better |
| consumer lag, most messages waiting at once | 1,142 | 67 | -94.1% | -1,153 to -996 | better |
| consumer lag, mean messages waiting | 98.6 | 3.47 | -96.5% | -105 to -85.5 | better |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 7.27 | +263.5% | 2.43 to 8.11 | **WORSE** |
| consumers running, most at once | 2 | 7.33 | +266.7% | 2.46 to 8.2 | **WORSE** |
| host CPU busy (share of the run) | 0.308 | 0.329 | +6.9% | 0.0144 to 0.0282 | **WORSE** |
| host CPU-seconds | 357 | 381 | +6.9% | 17.4 to 31.7 | **WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 2.97 | -7.9% | -0.35 to -0.157 | better |
| consumer changes written (the knob's moves) | 2 | 14.7 | +633.3% | 6.93 to 18.4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
