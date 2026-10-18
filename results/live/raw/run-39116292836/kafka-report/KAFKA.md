# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 972 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 337 | -0.9% | -6.17 to 0.288 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0226 to 0.0298 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,477 | 2,548 | +2.9% | -78.9 to 220 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,616 | 3,787 | +4.7% | -321 to 663 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.75 | 9.53 | -2.3% | -0.967 to 0.513 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 393 | +4.2% | -11.1 to 42.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,628 | 1,651 | +1.4% | -29.8 to 76.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 169 | +2.9% | -6 to 15.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.305 | -2.0% | -0.03 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 213 | -1.9% | -21.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.5 | -1.1% | -0.313 to 0.236 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.45 to 1.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00419 to 0.00419 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,411 | 2,407 | -0.2% | -225 to 216 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,730 | 3,778 | +1.3% | -528 to 624 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.121 to 0.0873 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 326 | 327 | +0.4% | -33.9 to 36.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 708 | 694 | -1.9% | -80.2 to 52.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.9 | 59.7 | -0.3% | -6.06 to 5.73 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.284 | 0.282 | -0.6% | -0.00971 to 0.00632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 497 | -0.6% | -16.8 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.55 | 7.51 | -0.5% | -0.257 to 0.178 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 724 | -0.3% | -5.05 to 0.259 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | +0.0% | -0.0107 to 0.0123 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,291 | 2,305 | +0.6% | -78.3 to 105 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,620 | 3,636 | +0.4% | -222 to 253 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.36 | 7.83 | -6.3% | -1.4 to 0.338 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 310 | +0.8% | -17.2 to 22.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,238 | 3,250 | +0.4% | -82.9 to 107 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 267 | 268 | +0.4% | -15.7 to 17.7 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.4% | -0.299 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.335 | 0.337 | +0.8% | -0.0052 to 0.0104 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 581 | +1.2% | -8.65 to 22.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.76 | 1.78 | +1.5% | -0.0179 to 0.071 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.0% | -1.73 to 1.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.84 to 0.52 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,309 | -1.5% | -242 to 173 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,672 | 3,662 | -0.3% | -278 to 259 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.55 | 8.53 | -0.3% | -0.0738 to 0.0165 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 312 | -0.7% | -20.9 to 16.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,688 | 1,667 | -1.3% | -128 to 85.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 139 | 137 | -0.9% | -9.8 to 7.32 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.308 | 0.307 | -0.3% | -0.00973 to 0.00788 | EVEN, no difference beyond the noise |
| host CPU-seconds | 536 | 535 | -0.0% | -17.1 to 16.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.26 | -0.1% | -0.0859 to 0.0816 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
