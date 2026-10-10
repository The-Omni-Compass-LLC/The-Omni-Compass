# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | -0.2% | -1.79 to 0.434 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | -0.0% | -0.0279 to 0.0125 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,524 | +2.6% | -109 to 238 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,707 | 3,514 | -5.2% | -822 to 436 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.57 | 9.5 | -0.7% | -0.636 to 0.502 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 377 | 380 | +0.6% | -1.5 to 5.95 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,632 | 1,624 | -0.5% | -62.5 to 46.5 | no difference beyond the noise |
| consumer lag, mean messages waiting | 164 | 163 | -0.7% | -4.73 to 2.3 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0165 to -0.0165 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.0% | -0.0182 to 0.0121 | no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.0% | -12.8 to 8.57 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.38 | -0.8% | -0.196 to 0.141 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.2% | -0.833 to 0.228 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00244 to 0.000995 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,437 | +1.5% | -120 to 190 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,795 | 3,718 | -2.0% | -255 to 101 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.3 | 11.3 | -0.0% | -0.114 to 0.104 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 324 | +0.5% | -4.51 to 7.69 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 702 | 701 | -0.2% | -47.8 to 45.2 | no difference beyond the noise |
| consumer lag, mean messages waiting | 59 | 59 | -0.1% | -1.09 to 0.924 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.277 | 0.277 | -0.3% | -0.00924 to 0.00784 | no difference beyond the noise |
| host CPU-seconds | 497 | 496 | -0.2% | -16.7 to 14.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.49 | 7.49 | -0.0% | -0.246 to 0.242 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 727 | +0.1% | -6.96 to 7.93 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.0104 to 0.0118 | same |
| end-to-end latency, 95th percentile (ms) | 2,258 | 2,142 | -5.2% | -1,104 to 871 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,555 | 3,346 | -5.9% | -1,912 to 1,494 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.56 | 7.45 | -1.4% | -0.358 to 0.143 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 304 | 290 | -4.4% | -146 to 119 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,174 | 3,072 | -3.2% | -1,392 to 1,189 | no difference beyond the noise |
| consumer lag, mean messages waiting | 264 | 252 | -4.3% | -121 to 98.3 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.317 | 0.315 | -0.4% | -0.0112 to 0.00846 | no difference beyond the noise |
| host CPU-seconds | 564 | 562 | -0.4% | -20.4 to 15.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.72 | -0.5% | -0.0801 to 0.0634 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 366 | -0.3% | -3.39 to 1.34 | no difference beyond the noise |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.00616 to 0.00251 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,510 | 2,592 | +3.2% | -89.6 to 253 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,834 | 3,913 | +2.1% | -60 to 218 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.19 | 8.17 | -0.2% | -0.126 to 0.0857 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 344 | +2.6% | -23.8 to 41.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,742 | 1,758 | +0.9% | -49.1 to 81.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 149 | 152 | +2.2% | -9.15 to 15.6 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.298 | 0.296 | -0.5% | -0.00565 to 0.00239 | no difference beyond the noise |
| host CPU-seconds | 532 | 529 | -0.6% | -9.97 to 4.02 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.21 | -0.3% | -0.0622 to 0.0442 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
