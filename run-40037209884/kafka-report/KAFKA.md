# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 983 messages a second; base rate 110.5/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.3% | -3 to 0.818 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.0% | -0.00955 to 0.00505 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,550 | 2,550 | +0.0% | -136 to 137 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,909 | 3,947 | +1.0% | -358 to 433 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 19.9 | 18.2 | -8.7% | -30.6 to 27.2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 404 | 408 | +1.1% | -5.13 to 13.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,722 | 1,716 | -0.3% | -59.1 to 47.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 176 | 179 | +1.6% | -4.14 to 9.73 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.259 | 0.259 | -0.2% | -0.00923 to 0.00841 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 186 | -0.2% | -6.52 to 5.95 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.01 | 3.01 | +0.2% | -0.0904 to 0.101 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.0909 to 0.468 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00509 to 0.00195 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,448 | 2,354 | -3.9% | -281 to 92.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,816 | 3,737 | -2.1% | -314 to 157 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | +0.0% | -0.128 to 0.133 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 334 | 322 | -3.6% | -21.4 to -2.34 | GAIN |
| consumer lag, most messages waiting at once | 706 | 690 | -2.2% | -47.8 to 17.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.4 | 59.2 | -3.7% | -3.6 to -0.911 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.282 | -0.4% | -0.0131 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 496 | -0.5% | -23.7 to 19.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.54 | 7.5 | -0.6% | -0.37 to 0.282 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1963 messages a second; base rate 294.5/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.2% | -5.91 to 3.53 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 864 | 864 | +0.0% | -0.117 to 0.137 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,641 | 2,644 | +0.1% | -277 to 282 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,061 | 4,011 | -1.2% | -295 to 196 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.91 | 8.24 | -7.6% | -1.02 to -0.329 | GAIN |
| end-to-end latency, mean (ms) | 362 | 363 | +0.1% | -39.5 to 40.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,609 | 3,582 | -0.8% | -203 to 149 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 321 | 320 | -0.3% | -34.4 to 32.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.321 | +7.5% | -0.0169 to 0.0615 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 571 | +7.3% | -29.8 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.61 | 1.73 | +7.5% | -0.0924 to 0.333 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.8/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -0.726 to 0.134 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | +0.0% | -0.531 to 0.838 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,282 | 2,294 | +0.5% | -52.5 to 76.6 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,628 | 3,637 | +0.2% | -358 to 375 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.59 | 8.64 | +0.6% | -0.193 to 0.3 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 307 | +0.8% | -0.412 to 5.54 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,644 | 1,632 | -0.7% | -54.5 to 30.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 134 | 136 | +1.1% | -0.951 to 3.91 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.314 | +0.7% | -0.00182 to 0.00617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 541 | 544 | +0.6% | -3.7 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.31 | +0.7% | -0.0246 to 0.0711 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
