# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.0% | -5.9 to 5.73 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.0% | -0.0241 to 0.0158 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,508 | -2.9% | -337 to 186 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,728 | 3,796 | +1.8% | -399 to 535 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 15 | 11 | -26.7% | -19.1 to 11.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 397 | 395 | -0.5% | -57.6 to 53.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,707 | +1.1% | -69.4 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 174 | 172 | -1.3% | -30.3 to 25.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.268 | -0.3% | -0.0171 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 192 | -0.2% | -11.9 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.12 | 3.12 | -0.2% | -0.153 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.629 to -0.153 | LOSS |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00249 to 0.00328 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,499 | +1.6% | -87.4 to 168 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,845 | 3,859 | +0.4% | -169 to 198 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | +0.0% | -0.0468 to 0.0501 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 332 | 338 | +1.9% | -9.99 to 22.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 703 | 717 | +1.9% | -21.2 to 48.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.8 | 62.2 | +2.3% | -1.47 to 4.28 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | -0.7% | -0.00911 to 0.00507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 490 | -0.7% | -15.2 to 8.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.42 | -0.4% | -0.222 to 0.163 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1951 messages a second; base rate 292.7/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 731 | -0.2% | -6.08 to 2.63 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 858 | 858 | +0.0% | -1.05 to 1.69 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,293 | 2,319 | +1.1% | -69.2 to 121 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,605 | -2.3% | -358 to 187 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 15.4 | 11.2 | -27.2% | -17.3 to 8.9 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 324 | +0.5% | -12.7 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,305 | 3,332 | +0.8% | -154 to 208 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 286 | 285 | -0.3% | -14.2 to 12.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.286 | 0.283 | -1.0% | -0.0211 to 0.0156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 506 | -0.9% | -35 to 25.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.54 | -0.7% | -0.0935 to 0.0734 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.1/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.0% | -2.7 to 2.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0102 to 0.00665 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,329 | -0.6% | -222 to 193 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,642 | 3,704 | +1.7% | -342 to 466 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.52 | +0.1% | -0.112 to 0.126 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 312 | -0.2% | -35.3 to 34.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,664 | 1,654 | -0.6% | -113 to 93.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 138 | -0.5% | -14 to 12.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.306 | +0.2% | -0.00202 to 0.00346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 532 | +0.3% | -4.77 to 7.89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | +0.3% | -0.0304 to 0.0506 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
