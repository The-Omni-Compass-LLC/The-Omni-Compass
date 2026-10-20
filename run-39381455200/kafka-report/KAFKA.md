# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.97 to -0.233 | LOSS |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.0178 to 0.018 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,570 | 2,568 | -0.1% | -218 to 214 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,694 | 3,744 | +1.4% | -215 to 315 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.28 | 9.24 | -0.5% | -0.523 to 0.427 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 384 | +0.6% | -2.16 to 6.42 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,651 | 1,663 | +0.8% | -34.3 to 59.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 166 | +0.2% | -3.81 to 4.49 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.289 | -0.6% | -0.0188 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 202 | -0.6% | -13.4 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | -0.3% | -0.202 to 0.185 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -0.777 to 0.207 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.0026 to 0.00101 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,387 | 2,424 | +1.6% | -91.6 to 166 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,730 | +0.2% | -304 to 322 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.7 | -0.6% | -0.279 to 0.143 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 326 | +1.4% | -8.95 to 17.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 704 | 699 | -0.7% | -58.2 to 48.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.3 | 59.8 | +0.8% | -1.62 to 2.57 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.287 | -1.8% | -0.0222 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 515 | 505 | -1.8% | -39.3 to 20.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.77 | 7.64 | -1.6% | -0.603 to 0.351 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1924 messages a second; base rate 288.6/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 764 | +5.3% | -150 to 228 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | -0.0% | -0.0296 to 0.0167 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,151 | 1,595 | -25.9% | -4,347 to 3,234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,444 | 2,501 | -27.4% | -6,503 to 4,617 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.51 | 7.16 | -4.7% | -1.58 to 0.875 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 289 | 211 | -26.9% | -578 to 423 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,083 | 2,328 | -24.5% | -5,297 to 3,787 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 250 | 181 | -27.8% | -497 to 358 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.43 | +21.6% | 0.152 to 0.712 | power given |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.32 | 0.333 | +4.1% | -0.00842 to 0.0346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 593 | +3.9% | -15 to 59.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | -0.9% | -0.45 to 0.42 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 365 | -0.3% | -3.08 to 0.883 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.1% | -0.996 to 0.364 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,296 | 2,310 | +0.6% | -12.2 to 38.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,565 | 3,580 | +0.4% | -149 to 178 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.26 | 8.18 | -0.9% | -0.276 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 302 | 306 | +1.6% | -18.7 to 28.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,626 | 1,643 | +1.0% | -37.1 to 69.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 133 | 135 | +1.3% | -7.89 to 11.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.307 | 0.305 | -0.5% | -0.0108 to 0.00753 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 547 | -0.3% | -17.9 to 14.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.32 | -0.1% | -0.103 to 0.0966 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
