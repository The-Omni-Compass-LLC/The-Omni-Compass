# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 339 | -0.4% | -5.41 to 2.86 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0362 to 0.0344 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,470 | 2,458 | -0.5% | -131 to 107 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,655 | -0.4% | -173 to 141 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.58 | +0.1% | -0.227 to 0.247 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 376 | 384 | +2.1% | -13.8 to 29.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,640 | 1,626 | -0.9% | -102 to 73.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 165 | +0.7% | -8.38 to 10.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -0.9% | -0.0162 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.8% | -10.9 to 7.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.33 | -0.5% | -0.192 to 0.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.843 to 0.493 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00209 to 0.00252 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,493 | 2,511 | +0.7% | -214 to 249 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,813 | 3,828 | +0.4% | -219 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.0312 to 0.0186 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 334 | 336 | +0.7% | -18.4 to 22.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 719 | 713 | -0.9% | -59.2 to 45.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.5 | 61.2 | -0.6% | -3.81 to 3.06 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.29 | -0.7% | -0.0126 to 0.00859 | EVEN, no difference beyond the noise |
| host CPU-seconds | 523 | 519 | -0.7% | -22.6 to 15.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.89 | 7.84 | -0.6% | -0.297 to 0.205 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1936 messages a second; base rate 290.4/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 729 | +0.4% | -10.2 to 15.3 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.0376 to 0.0362 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,380 | 2,091 | -12.1% | -1,535 to 957 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,294 | -12.5% | -2,190 to 1,250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.28 | 7.99 | -3.5% | -1.12 to 0.539 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 288 | -10.8% | -175 to 106 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,309 | 3,060 | -7.5% | -1,399 to 902 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 281 | 251 | -10.8% | -150 to 89.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.297 to 0.788 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.334 | 0.334 | +0.1% | -0.03 to 0.0309 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 575 | +0.1% | -57.1 to 58.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.75 | -0.2% | -0.191 to 0.184 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 964 messages a second; base rate 144.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.3% | -8.25 to 5.71 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 424 | 424 | +0.0% | -0.00572 to 0.00888 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,902 | 1,938 | +1.9% | -264 to 335 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,127 | 3,143 | +0.5% | -383 to 416 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.18 | 8.11 | -0.8% | -0.565 to 0.438 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 246 | 251 | +2.0% | -40.9 to 50.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,469 | 1,467 | -0.2% | -160 to 155 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 108 | 110 | +1.7% | -16.1 to 19.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.38 | +19.1% | 0.377 to 0.388 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.298 | 0.292 | -2.1% | -0.0322 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 521 | -2.1% | -56.2 to 33.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.16 | -1.8% | -0.391 to 0.277 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
