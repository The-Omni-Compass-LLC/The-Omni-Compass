# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.2% | -1.56 to 0.196 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.0159 to 0.00754 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,593 | 2,483 | -4.2% | -318 to 98.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,968 | +8.7% | 94.6 to 542 | LOSS |
| end-to-end latency, median (ms) | 9.36 | 9.39 | +0.3% | -0.285 to 0.345 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 387 | 389 | +0.6% | -3.65 to 8.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,683 | +1.1% | -28.8 to 66.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 169 | +0.4% | -2.21 to 3.61 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.291 | -1.2% | -0.0173 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.2% | -11.7 to 6.83 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.31 | -1.0% | -0.175 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 156 | +5.7% | -27.9 to 44.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.336 to 0.209 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,423 | 1,575 | -35.0% | -4,101 to 2,407 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,823 | 2,625 | -31.3% | -6,649 to 4,253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.3 | -0.5% | -0.501 to 0.38 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 221 | -32.3% | -543 to 332 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 714 | 493 | -31.0% | -1,129 to 686 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 40.6 | -32.2% | -100 to 61.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.19 | +9.3% | -0.645 to 1.02 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.277 | 0.278 | +0.2% | -0.00689 to 0.00819 | EVEN, no difference beyond the noise |
| host CPU-seconds | 497 | 498 | +0.3% | -12.1 to 14.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.15 | -4.7% | -2.05 to 1.35 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1949 messages a second; base rate 292.3/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 771 | +5.9% | -139 to 225 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0123 to 0.00599 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,659 | 1,713 | -35.6% | -4,441 to 2,549 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,170 | 2,533 | -39.2% | -6,541 to 3,267 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.45 | 7.02 | -5.8% | -1.76 to 0.901 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 360 | 232 | -35.5% | -581 to 326 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,599 | 2,408 | -33.1% | -5,222 to 2,840 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 315 | 204 | -35.2% | -506 to 283 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.2 | +9.8% | -0.674 to 1.06 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.316 | +0.8% | -0.0117 to 0.0165 | EVEN, no difference beyond the noise |
| host CPU-seconds | 558 | 562 | +0.7% | -18.4 to 26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.63 | -4.4% | -0.408 to 0.257 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.7/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -3.11 to 0.916 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | -0.0% | -0.00608 to 0.00222 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,229 | 2,263 | +1.5% | 20.7 to 46.4 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,514 | 3,614 | +2.9% | 25.7 to 175 | LOSS |
| end-to-end latency, median (ms) | 8.59 | 8.56 | -0.3% | -0.0917 to 0.0417 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 297 | 303 | +2.1% | -8.37 to 21.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,615 | 1,621 | +0.4% | -44.7 to 56.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 131 | 133 | +1.8% | -3.9 to 8.66 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.31 | 0.316 | +2.0% | 0.000516 to 0.0116 | power given |
| host CPU-seconds | 537 | 550 | +2.4% | 2.03 to 23.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.35 | +2.7% | 0.00763 to 0.166 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
