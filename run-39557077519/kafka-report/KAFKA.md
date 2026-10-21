# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.2% | -0.926 to -0.558 | LOSS |
| throughput (messages a second consumed) | 422 | 422 | +0.0% | -0.00662 to 0.0115 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,588 | 2,583 | -0.2% | -217 to 209 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,749 | 3,843 | +2.5% | -467 to 656 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.88 | 9.11 | +2.6% | -0.935 to 1.4 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 387 | 392 | +1.3% | -1.15 to 11.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,682 | 1,687 | +0.3% | -51 to 62.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 168 | 171 | +1.7% | -1.03 to 6.88 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.274 | -3.2% | -0.0583 to 0.0401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 196 | -3.1% | -41.2 to 28.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.27 | 3.18 | -2.9% | -0.66 to 0.47 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.69 to 1.37 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00982 to 0.00323 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,536 | 2,526 | -0.4% | -192 to 171 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,936 | 3,957 | +0.5% | -314 to 357 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | +0.2% | -0.0509 to 0.0982 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 344 | 345 | +0.4% | -39 to 41.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 725 | 728 | +0.4% | -81.1 to 87.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 63.1 | 63.2 | +0.2% | -7.44 to 7.69 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.295 | +1.2% | -0.00933 to 0.0161 | EVEN, no difference beyond the noise |
| host CPU-seconds | 516 | 522 | +1.2% | -17 to 29.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.79 | 7.89 | +1.3% | -0.31 to 0.513 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 720 | -0.8% | -18.2 to 7.22 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.0476 to 0.0377 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,278 | 2,321 | +1.9% | -69 to 155 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,593 | 3,639 | +1.3% | -266 to 357 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.93 | 7.99 | +0.7% | -0.192 to 0.305 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 303 | 315 | +3.7% | -10.8 to 33.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,244 | 3,219 | -0.8% | -199 to 150 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 262 | 272 | +3.6% | -11.4 to 30.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | -0.2% | -0.014 to 0.00511 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.357 | 0.352 | -1.3% | -0.0165 to 0.00719 | EVEN, no difference beyond the noise |
| host CPU-seconds | 621 | 612 | -1.4% | -30.9 to 13.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.9 | 1.89 | -0.6% | -0.0624 to 0.0384 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 147.0/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 367 | -0.1% | -1.66 to 0.656 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00929 to 0.00524 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,489 | 2,480 | -0.4% | -279 to 260 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,745 | 3,879 | +3.6% | -222 to 490 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.24 | 8.24 | -0.0% | -0.0938 to 0.0858 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 327 | 330 | +1.1% | -18.7 to 25.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,718 | 1,716 | -0.1% | -69.4 to 66.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 146 | +0.9% | -8.41 to 11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.302 | 0.303 | +0.4% | -0.0121 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 540 | +0.5% | -21.7 to 27.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.27 | +0.6% | -0.12 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
