# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.0% | -2.16 to 2.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0426 to 0.0292 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,600 | 2,459 | -5.4% | -174 to -109 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,913 | +2.9% | -379 to 599 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.38 | 9.44 | +0.7% | -0.884 to 1.01 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 389 | 386 | -0.7% | -33.8 to 28.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,652 | -0.7% | -87.8 to 63.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 166 | -0.7% | -13.3 to 10.9 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.291 | -1.3% | -0.021 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.3% | -14.5 to 9.26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.31 | -1.3% | -0.227 to 0.14 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.582 to 0.279 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00342 to 0.00394 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,369 | 2,381 | +0.5% | -101 to 126 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,741 | 3,759 | +0.5% | -256 to 292 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.0% | -0.0766 to 0.0666 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 326 | +0.9% | -6.37 to 12.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 693 | 686 | -1.1% | -56.4 to 41.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.9 | 59.8 | +1.5% | 0.458 to 1.3 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.279 | -0.7% | -0.0106 to 0.00658 | EVEN, no difference beyond the noise |
| host CPU-seconds | 495 | 492 | -0.7% | -19.4 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.48 | 7.44 | -0.6% | -0.302 to 0.218 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 768 | +5.4% | -132 to 210 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.0329 to 0.0539 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,198 | 1,464 | -33.4% | -3,583 to 2,115 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,624 | 2,514 | -30.6% | -5,915 to 3,694 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.52 | 7.09 | -5.7% | -1.52 to 0.67 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 298 | 204 | -31.5% | -477 to 289 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,213 | 2,253 | -29.9% | -4,582 to 2,661 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 178 | -31.4% | -413 to 250 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +16.2% | -0.442 to 1.09 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.316 | +0.9% | 0.000294 to 0.00548 | power given |
| host CPU-seconds | 556 | 563 | +1.2% | 0.969 to 11.9 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.64 | -3.6% | -0.426 to 0.305 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.6/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.2% | -3.07 to 1.79 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | +0.0% | -0.00414 to 0.00848 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,214 | 2,236 | +1.0% | -27.3 to 73.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,479 | 3,501 | +0.6% | -457 to 501 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.56 | -0.1% | -0.0444 to 0.0217 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 294 | 299 | +1.6% | -25.9 to 35 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,599 | 1,609 | +0.6% | -32.9 to 53.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 130 | 131 | +1.3% | -11.8 to 15.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.31 | -0.6% | -0.0144 to 0.0104 | EVEN, no difference beyond the noise |
| host CPU-seconds | 541 | 539 | -0.4% | -27.1 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.29 | -0.2% | -0.139 to 0.124 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
