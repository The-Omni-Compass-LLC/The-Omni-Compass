# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | -0.1% | -2.36 to 1.56 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00666 to 0.0121 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,433 | 2,507 | +3.0% | -224 to 372 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,615 | 3,511 | -2.9% | -723 to 514 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.5 | 8.62 | +1.4% | -0.193 to 0.429 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 365 | 368 | +0.8% | -0.447 to 6.18 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,605 | 1,592 | -0.8% | -55.4 to 30.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 158 | 159 | +0.2% | -0.981 to 1.65 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.286 | 0.284 | -0.7% | -0.0135 to 0.00922 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -0.7% | -9.68 to 6.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.31 | -0.6% | -0.164 to 0.123 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -0.818 to 0.28 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00103 to 0.00195 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,108 | 2,157 | +2.3% | -105 to 203 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,470 | 3,485 | +0.4% | -177 to 207 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.9 | 11 | +0.2% | -0.124 to 0.164 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 283 | 291 | +3.1% | -14.3 to 31.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 657 | 663 | +1.0% | -63.4 to 76.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 51.9 | 53.6 | +3.2% | -2.47 to 5.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.262 | 0.261 | -0.2% | -0.00944 to 0.0086 | EVEN, no difference beyond the noise |
| host CPU-seconds | 471 | 470 | -0.2% | -17.2 to 15.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.09 | 7.09 | +0.0% | -0.264 to 0.268 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1931 messages a second; base rate 289.7/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -3.43 to 3.35 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0314 to 0.0218 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,345 | 2,292 | -2.2% | -250 to 145 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,642 | 3,636 | -0.2% | -365 to 352 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.47 | 7.46 | -0.1% | -0.214 to 0.198 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 302 | -1.0% | -26.2 to 20.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,248 | 3,211 | -1.1% | -175 to 102 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 263 | 260 | -1.0% | -22.2 to 17 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.426 to 0.666 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.354 | 0.356 | +0.6% | -0.0214 to 0.0254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 629 | 633 | +0.6% | -39 to 47.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.93 | 1.94 | +0.7% | -0.127 to 0.153 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.2% | -0.928 to -0.337 | LOSS |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0124 to 0.0151 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,336 | 2,364 | +1.2% | -15 to 70.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,702 | 3,753 | +1.4% | -50.7 to 153 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.59 | +0.3% | -0.125 to 0.177 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 319 | +1.5% | -1.48 to 10.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,653 | 1,674 | +1.3% | -34.3 to 75.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 141 | +1.6% | -2.54 to 6.85 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.314 | +0.6% | -0.00299 to 0.00674 | EVEN, no difference beyond the noise |
| host CPU-seconds | 541 | 544 | +0.6% | -6.77 to 13.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.28 | 3.31 | +0.8% | -0.0373 to 0.0877 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
