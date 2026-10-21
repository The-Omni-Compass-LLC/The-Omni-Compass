# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 340 | -0.5% | -6.64 to 3.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 419 | -0.1% | -2.03 to 1.27 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,540 | 2,512 | -1.1% | -311 to 255 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,900 | +3.6% | -10.7 to 283 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.37 | 9.42 | +0.5% | -0.396 to 0.494 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 393 | +2.4% | -23.2 to 41.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,689 | +1.3% | -74.7 to 119 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 167 | 170 | +2.4% | -11.4 to 19.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.289 | -1.2% | -0.017 to 0.00994 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 202 | -1.1% | -12 to 7.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.29 | -0.8% | -0.193 to 0.143 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.784 to 0.524 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00149 to 0.00121 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,424 | 2,459 | +1.5% | -263 to 334 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,760 | 3,720 | -1.1% | -226 to 146 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.2 | -0.1% | -0.069 to 0.0363 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 324 | 326 | +0.7% | -16.4 to 21.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 714 | 705 | -1.4% | -45.9 to 26.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 60.2 | +0.5% | -3.35 to 3.89 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.272 | 0.271 | -0.5% | -0.00586 to 0.00302 | EVEN, no difference beyond the noise |
| host CPU-seconds | 488 | 486 | -0.5% | -10.5 to 5.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.36 | 7.33 | -0.4% | -0.12 to 0.0596 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.6/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | +0.0% | -2.53 to 2.72 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0274 to 0.0183 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,319 | 2,293 | -1.1% | -192 to 141 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,681 | 3,638 | -1.2% | -761 to 675 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.96 | 7.69 | -3.4% | -0.779 to 0.241 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 307 | -0.9% | -14.9 to 9.37 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,255 | 3,228 | -0.8% | -95 to 40.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 268 | 264 | -1.4% | -14.1 to 6.54 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.357 | 0.353 | -1.0% | -0.0247 to 0.0178 | EVEN, no difference beyond the noise |
| host CPU-seconds | 623 | 616 | -1.0% | -49.3 to 37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.89 | -1.0% | -0.144 to 0.106 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.4/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 363 | 366 | +0.8% | -7.22 to 12.7 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.0038 to 0.00146 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,127 | -17.6% | -1,794 to 883 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,974 | 3,457 | -13.0% | -1,982 to 948 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.18 | -0.7% | -0.118 to -0.00165 | GAIN |
| end-to-end latency, mean (ms) | 345 | 282 | -18.4% | -267 to 140 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,779 | 1,578 | -11.3% | -897 to 496 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 151 | 124 | -18.2% | -116 to 60.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | +13.5% | -0.192 to 0.732 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.294 | 0.296 | +0.7% | -0.000424 to 0.00466 | EVEN, no difference beyond the noise |
| host CPU-seconds | 524 | 528 | +0.9% | -1.18 to 10.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.21 | +0.1% | -0.113 to 0.121 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
