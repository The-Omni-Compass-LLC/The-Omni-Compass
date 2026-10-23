# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -2.93 to 1.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0134 to 0.0135 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,511 | 2,550 | +1.6% | -109 to 187 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,687 | -4.8% | -509 to 136 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.37 | 9.59 | +2.3% | -0.27 to 0.692 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 386 | 387 | +0.2% | -11.6 to 12.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,675 | 1,667 | -0.5% | -179 to 164 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 167 | +0.5% | -1.96 to 3.46 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.296 | 0.292 | -1.3% | -0.0188 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 204 | -1.2% | -12.5 to 7.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.33 | -0.9% | -0.211 to 0.149 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 146 | -0.4% | -1.55 to 0.297 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00588 to 0.00275 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,135 | 2,176 | +1.9% | -66.8 to 148 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,429 | 3,496 | +2.0% | -131 to 265 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.9 | 10.8 | -0.8% | -0.159 to -0.00559 | GAIN |
| end-to-end latency, mean (ms) | 285 | 296 | +4.0% | -11.3 to 34 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 649 | 660 | +1.7% | -48.2 to 70.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 52 | 54 | +3.9% | -0.884 to 4.96 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.297 to 0.788 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.258 | 0.255 | -1.1% | -0.011 to 0.00536 | EVEN, no difference beyond the noise |
| host CPU-seconds | 463 | 458 | -1.1% | -19.8 to 9.58 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7 | 6.95 | -0.7% | -0.235 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.6/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -5.74 to 5.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0174 to 0.00759 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,328 | -0.8% | -161 to 126 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,666 | 3,612 | -1.5% | -362 to 253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.21 | 8.03 | -2.2% | -0.639 to 0.282 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 308 | -1.8% | -33.3 to 22.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,277 | 3,225 | -1.6% | -211 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 267 | -2.1% | -34 to 22.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | +12.2% | -0.296 to 0.786 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.343 | 0.347 | +1.4% | -0.00673 to 0.0163 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 597 | +1.3% | -11 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.83 | +1.3% | -0.0314 to 0.0789 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.8/s; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.0% | -1.88 to 1.65 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.0175 to 0.00999 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,255 | 2,227 | -1.3% | -160 to 103 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,573 | 3,521 | -1.4% | -396 to 293 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.62 | 8.58 | -0.5% | -0.359 to 0.275 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 302 | 299 | -1.1% | -24.4 to 17.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,634 | 1,604 | -1.8% | -97.2 to 37.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 134 | 132 | -1.4% | -13.1 to 9.39 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.313 | 0.311 | -0.6% | -0.0347 to 0.0307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 543 | 541 | -0.4% | -58.4 to 53.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.29 | -0.4% | -0.369 to 0.344 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
