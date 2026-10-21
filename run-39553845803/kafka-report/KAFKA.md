# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.2% | -2.94 to 1.33 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.1% | -2.05 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,549 | 2,542 | -0.2% | -223 to 210 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,649 | 3,761 | +3.1% | -471 to 694 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.2 | 9.28 | +0.9% | -0.131 to 0.297 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 386 | +0.7% | 1.09 to 4.58 | LOSS |
| consumer lag, most messages waiting at once | 1,684 | 1,679 | -0.3% | -48.4 to 39.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 167 | +0.3% | -0.196 to 1.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.303 | -0.8% | -0.0209 to 0.0159 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 213 | -0.7% | -14.8 to 12 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.48 | 3.46 | -0.5% | -0.245 to 0.21 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.929 to -0.0832 | LOSS |
| throughput (messages a second consumed) | 174 | 174 | -0.0% | -0.0022 to 0.00138 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,617 | 2,719 | +3.9% | -12.3 to 217 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,975 | 4,040 | +1.6% | -59.4 to 190 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.155 to 0.13 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 352 | 365 | +3.8% | 9.24 to 17.1 | LOSS |
| consumer lag, most messages waiting at once | 744 | 749 | +0.7% | -42.3 to 52.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 64.8 | 66.8 | +3.0% | 0.69 to 3.21 | LOSS |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.292 | -0.7% | -0.014 to 0.00983 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 524 | -0.7% | -24.7 to 17.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.94 | 7.91 | -0.3% | -0.362 to 0.307 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1943 messages a second; base rate 291.5/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 725 | -0.5% | -18.8 to 10.9 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.0152 to 0.00803 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 3,149 | +32.4% | -2,134 to 3,674 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,708 | 4,629 | +24.9% | -2,914 to 4,757 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.38 | 7.43 | +0.8% | -0.334 to 0.448 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 412 | +29.4% | -267 to 454 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,325 | 4,017 | +20.8% | -1,873 to 3,257 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 277 | 358 | +29.2% | -227 to 389 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00909 to -0.00273 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.312 | 0.312 | +0.0% | -0.00704 to 0.00722 | EVEN, no difference beyond the noise |
| host CPU-seconds | 554 | 555 | +0.2% | -11.8 to 14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.7 | +0.7% | 0.00822 to 0.0171 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.2% | -1.68 to 0.00184 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00965 to 0.00664 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,381 | 2,413 | +1.3% | -167 to 230 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,731 | 3,730 | -0.0% | -432 to 431 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.52 | +0.1% | -0.176 to 0.189 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 322 | +1.3% | -8.59 to 17.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,677 | -0.6% | -60.9 to 39.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 142 | +1.4% | -4.01 to 8.03 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.317 | -0.5% | -0.0115 to 0.00827 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 554 | -0.5% | -23.6 to 18.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.37 | -0.2% | -0.137 to 0.12 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
