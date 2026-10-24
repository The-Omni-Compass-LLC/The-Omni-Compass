# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 342 | -0.2% | -2.15 to 0.983 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.01 to 0.00908 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,535 | 2,462 | -2.9% | -175 to 28.2 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,659 | 3,679 | +0.5% | -228 to 267 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.46 | 8.51 | +0.5% | -0.251 to 0.336 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 373 | 376 | +0.8% | 1.51 to 4.66 | LOSS |
| consumer lag, most messages waiting at once | 1,656 | 1,663 | +0.4% | 4.52 to 9.48 | LOSS |
| consumer lag, mean messages waiting | 162 | 163 | +0.6% | -2.93 to 5.01 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.283 | 0.282 | -0.6% | -0.00994 to 0.00677 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 202 | -0.6% | -7.1 to 4.77 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | -0.4% | -0.124 to 0.0974 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.2% | 0.195 to 0.383 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00173 to 0.000386 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,493 | 2,462 | -1.2% | -157 to 95 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,896 | 3,674 | -5.7% | -439 to -6.11 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.0% | -0.0279 to 0.0239 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 330 | -3.1% | -16.1 to -4.87 | GAIN |
| consumer lag, most messages waiting at once | 718 | 696 | -3.1% | -90.7 to 46.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.5 | 61 | -2.5% | -4.29 to 1.14 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.281 | -0.0% | -0.00609 to 0.00593 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 494 | -0.0% | -11.1 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 7.46 | -0.2% | -0.181 to 0.151 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1940 messages a second; base rate 291.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 725 | -0.4% | -8.02 to 1.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0251 to 0.00677 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,387 | 2,607 | +9.2% | -254 to 694 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,764 | 4,062 | +7.9% | -177 to 774 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.45 | 7.51 | +0.8% | -0.152 to 0.276 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 355 | +10.6% | -18.6 to 86.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,354 | 3,447 | +2.8% | -380 to 566 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 280 | 307 | +9.7% | -16.6 to 71.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.323 | +2.4% | -0.00132 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 576 | +2.5% | -2.35 to 30.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.77 | +3.0% | 0.00628 to 0.0954 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -2.56 to 2.15 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0129 to 0.00835 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,390 | 2,431 | +1.7% | -226 to 308 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,737 | 3,708 | -0.8% | -354 to 296 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.61 | 8.58 | -0.4% | -0.196 to 0.121 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 321 | +0.7% | -12.9 to 17.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,686 | +1.1% | -85 to 122 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 141 | 142 | +0.5% | -7.18 to 8.71 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.311 | -1.6% | -0.0288 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 539 | -1.6% | -54.4 to 37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.28 | -1.5% | -0.349 to 0.246 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
