# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 344 | 343 | -0.2% | -3.16 to 2.12 | no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.1% | -2.07 to 1.3 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,605 | 2,539 | -2.5% | -213 to 80.8 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,805 | +1.5% | -433 to 549 | no difference beyond the noise |
| end-to-end latency, median (ms) | 12 | 9.95 | -17.0% | -11.7 to 7.66 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 395 | 389 | -1.3% | -16.9 to 6.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,710 | 1,678 | -1.9% | -142 to 77.8 | no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 169 | -2.2% | -14.1 to 6.35 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.286 | 0.265 | -7.1% | -0.0828 to 0.0423 | no difference beyond the noise |
| host CPU-seconds | 205 | 191 | -6.9% | -57.3 to 29.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.07 | -6.8% | -0.93 to 0.481 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -1.16 to 0.511 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00184 to 0.00257 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,415 | +0.9% | -72.4 to 117 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,777 | 3,778 | +0.0% | -270 to 272 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.3 | -0.2% | -0.137 to 0.0869 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 328 | +2.3% | -12.6 to 27.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 703 | 694 | -1.4% | -51.4 to 32.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 59.3 | 59.6 | +0.6% | -3.3 to 4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.277 | 0.276 | -0.4% | -0.00873 to 0.00639 | no difference beyond the noise |
| host CPU-seconds | 496 | 494 | -0.4% | -15.9 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.48 | 7.47 | -0.2% | -0.18 to 0.151 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1937 messages a second; base rate 290.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 729 | +0.0% | -12.3 to 13 | no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0109 to 0.0024 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,304 | 2,129 | -7.6% | -1,018 to 668 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,267 | -10.5% | -1,457 to 690 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.45 | 7.41 | -0.5% | -0.335 to 0.265 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 289 | -6.9% | -125 to 82.5 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,306 | 3,054 | -7.6% | -1,074 to 571 | no difference beyond the noise |
| consumer lag, mean messages waiting | 270 | 251 | -6.9% | -109 to 71.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.0115 to 0.00119 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.312 | -0.3% | -0.00633 to 0.0044 | no difference beyond the noise |
| host CPU-seconds | 558 | 556 | -0.3% | -14.9 to 12 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | -0.3% | -0.0576 to 0.0472 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -1.45 to 1.21 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00826 to 0.000224 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,395 | 2,401 | +0.3% | -133 to 146 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,720 | 3,766 | +1.2% | -338 to 429 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.54 | +0.0% | -0.0411 to 0.0451 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 322 | +0.7% | -13.5 to 17.7 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,695 | +1.5% | -11.6 to 60.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 142 | +0.3% | -5.42 to 6.33 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.308 | 0.307 | -0.4% | -0.0145 to 0.0122 | no difference beyond the noise |
| host CPU-seconds | 535 | 532 | -0.5% | -27.6 to 22.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.23 | -0.4% | -0.16 to 0.131 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
