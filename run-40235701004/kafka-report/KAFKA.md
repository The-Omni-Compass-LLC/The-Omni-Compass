# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 971 messages a second; base rate 109.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.0% | -0.91 to 0.899 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | -0.0% | -0.0102 to 0.00595 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,355 | 2,397 | +1.8% | -76.4 to 160 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,605 | 3,453 | -4.2% | -240 to -62.9 | GAIN |
| end-to-end latency, median (ms) | 8.66 | 8.7 | +0.5% | -0.157 to 0.243 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 357 | 359 | +0.5% | -0.25 to 3.64 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,560 | 1,581 | +1.3% | -4.21 to 46.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 154 | 154 | +0.3% | -0.0966 to 1.05 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -0.9% | -0.0204 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 212 | -1.0% | -14.6 to 10.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.45 | -1.0% | -0.234 to 0.167 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.0% | -0.667 to 0.797 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00137 to 0.00166 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,486 | 2,498 | +0.5% | -271 to 295 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,892 | +0.6% | -437 to 483 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.2% | -0.0522 to 0.00822 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 340 | 339 | -0.2% | -19.2 to 18 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 718 | 705 | -1.8% | -65.8 to 40.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.5 | 62.1 | -0.6% | -3.39 to 2.64 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.279 | 0.277 | -0.7% | -0.00887 to 0.00525 | EVEN, no difference beyond the noise |
| host CPU-seconds | 491 | 488 | -0.7% | -15.6 to 9.03 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.37 | -0.7% | -0.275 to 0.17 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1935 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 725 | -0.3% | -9.33 to 5.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.00557 to 0.0199 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,315 | 2,321 | +0.2% | -195 to 206 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,756 | 3,758 | +0.0% | -633 to 636 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.78 | 7.66 | -1.6% | -0.246 to 0.000486 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 314 | +1.2% | -6.85 to 14.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,289 | 3,279 | -0.3% | -44.5 to 25.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 269 | 272 | +0.9% | -5.1 to 10.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.8% | -0.38 to 0.61 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.344 | -2.2% | -0.0249 to 0.00914 | EVEN, no difference beyond the noise |
| host CPU-seconds | 624 | 611 | -2.1% | -46.4 to 19.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.87 | -1.9% | -0.156 to 0.0846 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -13.2 to 21.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 5.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -0.628 to 0.0297 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00343 to 0.00202 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,371 | 2,394 | +1.0% | -96.6 to 143 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,653 | 3,705 | +1.4% | -175 to 280 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.54 | -0.2% | -0.127 to 0.0894 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 319 | +0.8% | -2.67 to 8.03 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,687 | +1.2% | -51.9 to 91.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 141 | +0.2% | -1.81 to 2.35 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.305 | -0.7% | -0.00939 to 0.00499 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 529 | -0.7% | -18.5 to 10.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.21 | -0.7% | -0.109 to 0.0664 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
