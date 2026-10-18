# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.3/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.3% | -2.61 to 0.408 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0156 to 0.00473 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,532 | 2,549 | +0.7% | -258 to 293 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,825 | 3,749 | -2.0% | -734 to 582 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.22 | 8.29 | +0.8% | -0.0579 to 0.192 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 384 | +0.5% | 0.00408 to 3.87 | LOSS |
| consumer lag, most messages waiting at once | 1,699 | 1,667 | -1.9% | -45.8 to -17.5 | GAIN |
| consumer lag, mean messages waiting | 165 | 167 | +0.7% | -2.2 to 4.51 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.278 | 0.278 | -0.3% | -0.0112 to 0.00958 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 200 | -0.3% | -8.11 to 6.91 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.23 | +0.0% | -0.13 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146 | 147 | +0.4% | -0.0204 to 1.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00281 to 0.00168 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,629 | 2,389 | -9.1% | -908 to 428 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,979 | 3,701 | -7.0% | -975 to 420 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.4% | -0.185 to 0.0946 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 354 | 320 | -9.6% | -86.1 to 18.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 738 | 689 | -6.6% | -195 to 97.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 65.2 | 59 | -9.4% | -14.4 to 2.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.276 | -1.2% | -0.00638 to -4.38e-05 | GAIN |
| host CPU-seconds | 500 | 494 | -1.1% | -11.4 to 0.177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.46 | -1.5% | -0.202 to -0.0301 | GAIN |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.2/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 727 | +0.0% | -2.48 to 3.12 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 854 | 854 | +0.0% | -0.0269 to 0.0297 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,438 | 2,372 | -2.7% | -131 to -0.479 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,926 | 3,906 | -0.5% | -130 to 90.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.28 | 8.1 | -2.2% | -1.26 to 0.898 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 329 | -1.9% | -19.8 to 7.24 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,406 | 3,345 | -1.8% | -175 to 53 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 293 | 287 | -1.9% | -16.7 to 5.85 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.325 | -0.3% | -0.0126 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 558 | -0.3% | -27 to 24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.7 | -0.3% | -0.0872 to 0.0763 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 985 messages a second; base rate 147.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.1% | -2.96 to 2.24 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | -0.0% | -0.00605 to 0.00224 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,552 | 2,615 | +2.4% | -72.5 to 197 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,978 | 3,936 | -1.0% | -494 to 410 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.07 | 8.03 | -0.5% | -0.146 to 0.0612 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 350 | 352 | +0.7% | -26.1 to 30.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,785 | 1,796 | +0.6% | -85.4 to 106 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 157 | 157 | +0.3% | -9.65 to 10.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.272 | 0.274 | +0.8% | -0.00827 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 486 | 490 | +0.9% | -13.3 to 22.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.93 | 2.96 | +1.0% | -0.058 to 0.119 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
