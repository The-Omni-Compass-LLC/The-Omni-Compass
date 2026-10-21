# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -3.34 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | -2.88 to 2.88 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,562 | 2,570 | +0.3% | -83 to 99.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,769 | 3,886 | +3.1% | -21.8 to 255 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.08 | 9.08 | -0.0% | -0.971 to 0.966 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 385 | 389 | +0.9% | -7.25 to 14.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,663 | 1,697 | +2.0% | -30.8 to 98.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 168 | +0.9% | -3.5 to 6.46 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.301 | 0.3 | -0.4% | -0.0129 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 211 | -0.4% | -7.98 to 6.49 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.43 | -0.1% | -0.117 to 0.11 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.4% | -1.53 to 0.435 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00219 to 0.00887 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,544 | 2,577 | +1.3% | -241 to 307 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,808 | 3,973 | +4.3% | -72.2 to 401 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.7 | -0.9% | -0.33 to 0.129 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 338 | 350 | +3.5% | -12.7 to 36.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 713 | 735 | +3.1% | -19 to 63 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62 | 63.9 | +3.1% | -1.56 to 5.34 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.287 | -2.4% | -0.0267 to 0.0124 | EVEN, no difference beyond the noise |
| host CPU-seconds | 518 | 506 | -2.4% | -48 to 22.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.81 | 7.65 | -2.1% | -0.68 to 0.359 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1936 messages a second; base rate 290.5/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | +0.0% | -2.6 to 3.24 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.00853 to 0.000355 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,419 | 2,383 | -1.5% | -173 to 101 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,830 | 3,709 | -3.2% | -783 to 540 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.4 | 8.41 | +0.0% | -0.684 to 0.687 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 330 | 322 | -2.4% | -32.4 to 16.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,396 | 3,305 | -2.7% | -206 to 23.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 287 | 281 | -2.4% | -27.1 to 13.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.333 | 0.328 | -1.5% | -0.0215 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 572 | 563 | -1.6% | -38.5 to 20 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.72 | -1.7% | -0.126 to 0.0675 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 985 messages a second; base rate 147.8/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 368 | -0.2% | -4.57 to 3.11 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | +0.0% | -0.0226 to 0.0248 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,492 | 2,560 | +2.7% | -115 to 249 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,754 | -3.0% | -895 to 665 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.05 | 7.96 | -1.1% | -0.223 to 0.0425 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 344 | +0.9% | -43.1 to 49.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,751 | 1,757 | +0.4% | -259 to 271 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 153 | 154 | +0.9% | -20.1 to 22.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.27 | 0.268 | -0.5% | -0.00832 to 0.00563 | EVEN, no difference beyond the noise |
| host CPU-seconds | 482 | 480 | -0.4% | -14.9 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.91 | 2.9 | -0.2% | -0.0917 to 0.0797 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
