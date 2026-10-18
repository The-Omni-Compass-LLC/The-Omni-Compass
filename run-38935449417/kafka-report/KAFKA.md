# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.0% | -5.55 to 5.46 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0153 to 0.0204 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,522 | 2,504 | -0.7% | -254 to 218 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,803 | 3,733 | -1.8% | -528 to 388 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.86 | 8.9 | +0.5% | -0.0816 to 0.163 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 380 | -0.8% | -31.6 to 25.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,640 | -0.9% | -46.8 to 16.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 163 | -0.8% | -13.3 to 10.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.306 | 0.303 | -0.9% | -0.0151 to 0.00928 | EVEN, no difference beyond the noise |
| host CPU-seconds | 219 | 217 | -1.0% | -10.8 to 6.65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.53 | -0.9% | -0.159 to 0.0917 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 146 | -0.4% | -2.47 to 1.18 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00422 to 0.00409 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,211 | 2,270 | +2.6% | -403 to 520 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,486 | 3,627 | +4.0% | -196 to 478 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -0.9% | -0.438 to 0.233 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 294 | 308 | +4.5% | -47.3 to 73.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 653 | 669 | +2.6% | -53.4 to 86.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 53.5 | 56.1 | +4.8% | -7.33 to 12.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0774 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.279 | 0.274 | -1.8% | -0.0194 to 0.00937 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 491 | -1.8% | -34.4 to 16.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.47 | -1.3% | -0.58 to 0.379 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1939 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 727 | -0.1% | -1.46 to -0.718 | LOSS |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.037 to 0.0285 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,434 | +0.6% | -88.9 to 119 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,686 | 3,687 | +0.0% | -232 to 235 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.7 | 7.61 | -1.2% | -0.323 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 319 | 323 | +1.1% | 0.777 to 6.03 | LOSS |
| consumer lag, most messages waiting at once | 3,334 | 3,324 | -0.3% | -139 to 119 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 279 | 280 | +0.4% | -0.804 to 2.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.338 | 0.34 | +0.5% | -0.0105 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 604 | +0.5% | -16.8 to 22.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.85 | +0.7% | -0.0478 to 0.0719 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.2% | -3.39 to 2.14 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00654 to 0.00197 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,388 | 2,480 | +3.9% | -120 to 305 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,848 | 3,707 | -3.7% | -501 to 218 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.54 | -0.8% | -0.14 to 0.00855 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 324 | 330 | +1.9% | -30.7 to 43 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,703 | 1,711 | +0.5% | -28.1 to 44.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 144 | 146 | +1.5% | -14.4 to 18.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.313 | 0.312 | -0.2% | -0.0125 to 0.0111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 543 | 543 | -0.1% | -18.9 to 18.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.31 | +0.1% | -0.0855 to 0.0932 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
