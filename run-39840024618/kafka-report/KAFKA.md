# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -1.27 to -0.414 | LOSS |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0142 to 0.0132 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,505 | 2,522 | +0.7% | -220 to 256 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,646 | 3,642 | -0.1% | -426 to 417 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.54 | 9.4 | -1.5% | -0.579 to 0.297 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 380 | +0.9% | 1.46 to 5.19 | LOSS |
| consumer lag, most messages waiting at once | 1,627 | 1,647 | +1.2% | -52.6 to 91.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 165 | +1.2% | -1.2 to 5.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.29 | -1.3% | -0.0211 to 0.0137 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.2% | -15 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.3 | -1.0% | -0.236 to 0.171 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -1.2 to 1.13 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00229 to 0.00104 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,399 | 2,383 | -0.6% | -354 to 323 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,697 | 3,652 | -1.2% | -539 to 449 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.7 | -0.5% | -0.311 to 0.188 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 323 | +0.3% | -39 to 41 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 690 | 698 | +1.2% | -37.3 to 53.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.8 | 59.6 | +1.3% | -5.24 to 6.78 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.291 | 0.286 | -1.7% | -0.0233 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 513 | 505 | -1.7% | -41.4 to 24.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.77 | 7.64 | -1.7% | -0.685 to 0.427 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1966 messages a second; base rate 294.8/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 734 | 734 | +0.0% | -3.5 to 3.98 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 864 | 865 | +0.0% | -1.06 to 1.7 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,538 | -1.8% | -207 to 116 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,946 | 3,961 | +0.4% | -107 to 136 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.89 | 8.68 | -2.4% | -0.271 to -0.155 | GAIN |
| end-to-end latency, mean (ms) | 355 | 350 | -1.3% | -20.1 to 10.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,523 | 3,481 | -1.2% | -86.9 to 1.52 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 315 | 310 | -1.7% | -16 to 5.04 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.291 | 0.288 | -1.1% | -0.00831 to 0.00172 | EVEN, no difference beyond the noise |
| host CPU-seconds | 520 | 515 | -1.0% | -12.5 to 2.56 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.57 | 1.56 | -1.0% | -0.0413 to 0.0113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 954 messages a second; base rate 143.2/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 369 | +0.5% | -2.96 to 6.4 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00626 to 0.00343 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,670 | 1,641 | -1.7% | -157 to 98.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,878 | 2,707 | -5.9% | -482 to 142 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.1 | -1.8% | -0.358 to 0.0622 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 215 | 204 | -5.2% | -40.8 to 18.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,328 | 1,289 | -3.0% | -213 to 134 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 94.4 | 88.9 | -5.8% | -16.6 to 5.63 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.42 | +20.8% | 0.377 to 0.456 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.296 | 0.292 | -1.1% | -0.0171 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 526 | 521 | -1.0% | -29.6 to 19.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.18 | 3.13 | -1.4% | -0.153 to 0.0618 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
