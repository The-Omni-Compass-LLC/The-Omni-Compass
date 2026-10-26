# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.4% | -4.75 to 2.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.019 to 0.0172 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | -0.7% | -150 to 115 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,432 | 3,678 | +7.1% | -52.6 to 543 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.86 | 12 | +21.5% | -3.01 to 7.25 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 362 | 371 | +2.5% | -16.4 to 34.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,565 | 1,574 | +0.5% | -101 to 118 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 163 | +2.9% | -6.5 to 15.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.3% | -0.021 to 0.00881 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 187 | -2.3% | -14.8 to 6.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.09 | 3.03 | -1.9% | -0.205 to 0.0886 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.22 to 0.732 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -9.57e-05 to 0.00015 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,205 | 2,168 | -1.6% | -117 to 44.3 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,404 | 3,415 | +0.3% | -213 to 235 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11 | 10.9 | -0.3% | -0.16 to 0.0983 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 289 | 288 | -0.4% | -6.93 to 4.45 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 646 | 654 | +1.2% | -90.5 to 106 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52.7 | 52.4 | -0.5% | -4.31 to 3.79 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | +1.1% | -0.0708 to 0.114 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.262 | 0.261 | -0.5% | -0.00653 to 0.00412 | EVEN, no difference beyond the noise |
| host CPU-seconds | 470 | 468 | -0.5% | -11.3 to 7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.09 | 7.07 | -0.3% | -0.178 to 0.137 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2.67 | +33.3% | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1927 messages a second; base rate 289.1/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 716 | -1.3% | -22.5 to 3.83 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 846 | -0.2% | -9.92 to 6.18 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,272 | 2,293 | +0.9% | -136 to 179 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,679 | +4.4% | -296 to 607 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.45 | 8.14 | -3.7% | -1.04 to 0.409 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 321 | +5.4% | -29.5 to 62.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,226 | +0.8% | -41.5 to 94.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 266 | 277 | +4.0% | -29.4 to 51 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | +13.5% | -0.308 to 0.848 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3.67 | +83.3% | 0.232 to 3.1 | power given |
| host CPU busy (share of the run) | 0.329 | 0.331 | +0.6% | -0.0174 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 566 | 570 | +0.8% | -32.8 to 41.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.77 | +1.9% | -0.0656 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 11.3 | +466.7% | -6.64 to 25.3 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 6.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 969 messages a second; base rate 145.3/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 363 | -0.7% | -10.3 to 4.91 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.00406 to 0.0022 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,092 | 2,185 | +4.4% | -133 to 319 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,428 | 3,392 | -1.1% | -178 to 106 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.58 | 8.55 | -0.4% | -0.079 to 0.017 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 281 | 293 | +4.1% | -24.7 to 47.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,568 | 1,564 | -0.3% | -108 to 98.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 124 | 129 | +4.0% | -10.8 to 20.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.07 | +3.4% | -0.0901 to 0.225 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.305 | 0.303 | -0.5% | -0.0137 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 529 | 527 | -0.4% | -26.2 to 22.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.23 | +0.4% | -0.149 to 0.173 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
