# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 969 messages a second; base rate 109.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 337 | -0.9% | -12.7 to 6.43 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 417 | 417 | +0.0% | -0.00352 to 0.00801 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,406 | 2,577 | +7.1% | -36.3 to 378 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,762 | 3,788 | +0.7% | -206 to 257 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.75 | 8.63 | -1.4% | -0.558 to 0.32 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 372 | 394 | +5.9% | -8.17 to 52.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,686 | 1,665 | -1.3% | -220 to 177 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 162 | 169 | +4.6% | -9.03 to 24.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.1 | +5.1% | -0.158 to 0.363 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.284 | 0.283 | -0.4% | -0.0134 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 202 | -0.4% | -9.51 to 8.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.32 | +0.6% | -0.0296 to 0.0666 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.523 to 0.115 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00561 to 0.00307 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,321 | 2,347 | +1.1% | -93.7 to 146 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,672 | 3,582 | -2.5% | -291 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.6% | -0.0974 to -0.0512 | GAIN |
| end-to-end latency, mean (ms) | 311 | 313 | +0.5% | -2.41 to 5.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 666 | 680 | +2.2% | -26.1 to 54.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57.3 | 57.4 | +0.3% | -0.442 to 0.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.285 | -1.5% | -0.0101 to 0.00117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 518 | 510 | -1.5% | -17.6 to 2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.82 | 7.71 | -1.4% | -0.242 to 0.0283 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -2.89 to 2.28 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 850 | +0.0% | -1.04 to 1.66 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,330 | 2,318 | -0.5% | -40.7 to 16.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,571 | -3.2% | -325 to 85.5 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.93 | 7.73 | -2.5% | -0.592 to 0.2 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 312 | 309 | -0.8% | -16.9 to 12 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,256 | 3,220 | -1.1% | -128 to 56 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 268 | -0.8% | -12.9 to 8.67 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.346 | 0.346 | -0.0% | -0.0194 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 601 | 601 | +0.1% | -36.8 to 37.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.84 | +0.1% | -0.113 to 0.118 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 367 | -0.2% | -3.09 to 1.76 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | +0.0% | -0.0119 to 0.0129 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,300 | 2,311 | +0.5% | -136 to 158 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,621 | 3,667 | +1.3% | -467 to 560 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.15 | 8.15 | -0.1% | -0.115 to 0.104 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 311 | 315 | +1.2% | -23.8 to 31.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,644 | 1,674 | +1.8% | -120 to 180 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 140 | +0.4% | -8.88 to 10.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.28 | 0.281 | +0.5% | -0.0151 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 499 | 502 | +0.7% | -27.4 to 34.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.02 | 3.04 | +0.9% | -0.161 to 0.213 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
