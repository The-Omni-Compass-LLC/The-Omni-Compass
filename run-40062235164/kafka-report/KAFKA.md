# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 341 | -0.5% | -7.71 to 4.01 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.0% | -0.0317 to 0.0183 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,646 | +3.2% | -1.18 to 163 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,787 | -4.9% | -1,030 to 637 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.9 | 10 | -16.2% | -6.5 to 2.63 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 408 | +2.3% | -27.6 to 46.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,733 | 1,730 | -0.2% | -177 to 171 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 175 | 179 | +2.2% | -10.6 to 18.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.27 | +0.7% | -0.0135 to 0.0174 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +0.8% | -9.51 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.11 | 3.15 | +1.3% | -0.0813 to 0.162 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -1.56 to 0.607 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00147 to 0.0047 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,538 | +3.2% | 33.4 to 126 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,843 | 3,824 | -0.5% | -494 to 456 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.3% | -0.0697 to 0.00636 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 344 | +3.4% | -11.6 to 34.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 711 | 720 | +1.2% | -38.6 to 56 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61 | 63.1 | +3.4% | -0.517 to 4.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.281 | -1.2% | -0.0131 to 0.00632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 502 | 496 | -1.2% | -24 to 11.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.5 | -0.9% | -0.283 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 725 | -0.2% | -3.35 to 0.483 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | +0.0% | -0.0131 to 0.0182 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,213 | 2,258 | +2.0% | -114 to 204 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,685 | +0.6% | -305 to 350 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.43 | 8.36 | -0.8% | -0.391 to 0.257 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 310 | +2.0% | -7.73 to 19.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,205 | 3,222 | +0.5% | -168 to 202 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 269 | +1.9% | -8.03 to 18 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.332 | 0.329 | -1.2% | -0.0241 to 0.0165 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 566 | -1.0% | -37.4 to 26.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | -0.8% | -0.11 to 0.0834 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -0.421 to -0.277 | LOSS |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0177 to 0.0173 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,311 | -0.9% | -150 to 108 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,674 | +0.1% | -231 to 237 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.85 | 8.76 | -1.0% | -0.58 to 0.401 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 307 | -1.2% | -17.5 to 10.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,655 | 1,646 | -0.5% | -74.5 to 57.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 135 | -1.0% | -6.5 to 3.69 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.339 | 0.331 | -2.3% | -0.0365 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 576 | -2.1% | -61.4 to 36.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.51 | -2.0% | -0.37 to 0.224 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
