# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.1% | -1.42 to 0.851 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.0% | -0.00775 to 0.00098 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,754 | 2,606 | -5.3% | -546 to 251 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,005 | 4,040 | +0.9% | -206 to 276 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.7 | 8.49 | -2.4% | -0.975 to 0.555 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 407 | 398 | -2.3% | -39.2 to 20.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,791 | 1,742 | -2.7% | -227 to 130 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 177 | 173 | -2.4% | -17.6 to 9.19 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.284 | -0.7% | -0.0143 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 203 | -0.7% | -10.2 to 7.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.28 | -0.6% | -0.165 to 0.123 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.338 to 0.211 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00144 to 0.00365 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,589 | 2,559 | -1.2% | -77.8 to 17.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,944 | 3,909 | -0.9% | -255 to 184 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | +0.1% | -0.216 to 0.229 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 349 | 349 | -0.0% | -8 to 7.75 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 720 | 721 | +0.1% | -97.2 to 99.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 63.9 | 64 | +0.1% | -1.93 to 2.11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.286 | -0.4% | -0.016 to 0.0136 | EVEN, no difference beyond the noise |
| host CPU-seconds | 507 | 505 | -0.4% | -27.4 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.64 | 7.61 | -0.3% | -0.418 to 0.366 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.3/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 726 | -0.1% | -1.85 to 0.272 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.0159 to 0.00409 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,294 | 2,332 | +1.6% | -247 to 322 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,648 | 3,563 | -2.3% | -199 to 28.3 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.77 | 7.63 | -1.9% | -0.785 to 0.497 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 309 | -0.6% | -5.02 to 1.57 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,282 | 3,271 | -0.3% | -152 to 129 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 269 | 267 | -0.9% | -5.43 to 0.708 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.34 | 0.34 | +0.0% | -0.0055 to 0.0058 | EVEN, no difference beyond the noise |
| host CPU-seconds | 590 | 591 | +0.2% | -8.35 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.81 | +0.4% | -0.0257 to 0.0385 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.3% | -2.54 to 0.377 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | +0.0% | -0.0978 to 0.153 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,459 | 2,655 | +8.0% | -256 to 648 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,864 | 4,041 | +4.6% | -1,076 to 1,431 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.18 | -0.3% | -0.137 to 0.0883 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 331 | 350 | +5.7% | -44 to 82 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,740 | 1,794 | +3.1% | -332 to 440 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 146 | 154 | +5.5% | -21.4 to 37.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.293 | -0.2% | -0.00508 to 0.0038 | EVEN, no difference beyond the noise |
| host CPU-seconds | 523 | 523 | -0.0% | -7.2 to 6.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.17 | 3.18 | +0.3% | -0.0331 to 0.05 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
