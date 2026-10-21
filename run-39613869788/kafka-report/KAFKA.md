# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.2% | -1.21 to 0.0553 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0271 to 0.0362 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,565 | +2.7% | -64.1 to 197 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,898 | 3,836 | -1.6% | -531 to 408 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10 | 9.49 | -5.0% | -1.52 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 391 | 391 | -0.1% | -2.69 to 2.06 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,677 | 1,689 | +0.7% | -69.6 to 92.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 169 | 169 | +0.2% | -4.49 to 5.29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.304 | 0.301 | -1.2% | -0.0261 to 0.0189 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 211 | -1.2% | -18.3 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.46 | 3.42 | -1.0% | -0.289 to 0.22 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.2% | -0.782 to 0.153 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00542 to 0.00188 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,408 | +0.4% | -123 to 142 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,725 | 3,878 | +4.1% | -32.8 to 339 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11 | 11 | -0.5% | -0.282 to 0.18 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.8% | -15.1 to 26.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 679 | 702 | +3.3% | -35.2 to 80.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 58.4 | 60.3 | +3.1% | -2.93 to 6.55 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.27 | 0.266 | -1.3% | -0.00817 to 0.00132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 482 | 476 | -1.2% | -14 to 2.09 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.26 | 7.19 | -1.0% | -0.179 to 0.029 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1928 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 724 | -0.1% | -5.03 to 3.93 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.0318 to 0.0116 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,280 | 2,281 | +0.1% | -174 to 177 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,574 | 3,610 | +1.0% | -371 to 444 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.59 | 7.49 | -1.3% | -0.298 to 0.099 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 298 | 300 | +0.7% | -27.1 to 31.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,200 | 3,208 | +0.2% | -235 to 250 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 257 | 258 | +0.5% | -22.7 to 25.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.37 | +18.6% | 0.369 to 0.376 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.363 | 0.366 | +1.0% | -0.00194 to 0.00907 | EVEN, no difference beyond the noise |
| host CPU-seconds | 644 | 652 | +1.2% | -5.63 to 21.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.97 | 2 | +1.3% | -0.0264 to 0.0769 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.1% | -1.56 to 0.752 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.0113 to 0.00686 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,349 | 2,357 | +0.3% | -33.1 to 48.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,610 | 3,604 | -0.2% | -127 to 113 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.1 | 8.07 | -0.4% | -0.185 to 0.124 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 313 | +0.7% | -5.21 to 9.42 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,659 | 1,674 | +0.9% | -60.8 to 90.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 138 | 139 | +0.7% | -2.2 to 4.19 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.285 | -1.8% | -0.0468 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 517 | 509 | -1.6% | -82.4 to 65.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.12 | 3.08 | -1.5% | -0.502 to 0.407 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
