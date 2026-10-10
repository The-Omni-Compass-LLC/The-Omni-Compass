# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.55 to -0.563 | **WORSE** |
| throughput (messages a second consumed) | 419 | 420 | +0.1% | -1.29 to 2.06 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,594 | 2,588 | -0.2% | -150 to 140 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,818 | 3,813 | -0.1% | -279 to 269 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.74 | 9.85 | +1.1% | -0.678 to 0.888 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 388 | 398 | +2.4% | -15.6 to 34.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,674 | 1,686 | +0.7% | -48.5 to 71.2 | no difference beyond the noise |
| consumer lag, mean messages waiting | 170 | 172 | +1.1% | -10 to 13.7 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.293 | -0.5% | -0.0203 to 0.0173 | no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.6% | -14.1 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.33 | -0.2% | -0.227 to 0.215 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.3% | -0.619 to -0.189 | **WORSE** |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00315 to 0.00201 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,594 | 2,628 | +1.3% | -50.3 to 117 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 4,000 | 4,069 | +1.7% | -478 to 615 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.0% | -0.102 to 0.0993 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 350 | 357 | +1.9% | -7.97 to 20.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 739 | 737 | -0.3% | -30.7 to 26.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 65.1 | 65.7 | +0.8% | -0.209 to 1.31 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.282 | 0.282 | -0.2% | -0.0105 to 0.00933 | no difference beyond the noise |
| host CPU-seconds | 497 | 497 | -0.1% | -17.9 to 16.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.5 | +0.1% | -0.238 to 0.257 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 726 | +0.0% | -4.29 to 4.78 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0256 to 0.017 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,306 | 2,305 | -0.1% | -301 to 298 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,623 | 3,540 | -2.3% | -447 to 280 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.31 | 8.23 | -1.0% | -0.425 to 0.26 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 313 | 310 | -0.9% | -30.4 to 24.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,231 | 3,249 | +0.5% | -143 to 178 | no difference beyond the noise |
| consumer lag, mean messages waiting | 272 | 269 | -0.8% | -25.4 to 21.2 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.331 | 0.327 | -1.4% | -0.0164 to 0.007 | no difference beyond the noise |
| host CPU-seconds | 570 | 563 | -1.3% | -28.4 to 13.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.72 | -1.3% | -0.0876 to 0.0415 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -2.08 to 1.46 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.000648 to 0.00398 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,417 | 2,454 | +1.5% | -129 to 204 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,686 | 3,843 | +4.3% | -349 to 665 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 8.18 | -0.2% | -0.153 to 0.122 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 329 | +3.9% | -21.3 to 45.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,665 | 1,723 | +3.5% | -68.1 to 184 | no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 145 | +3.5% | -10 to 19.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.298 | 0.295 | -1.0% | -0.012 to 0.00603 | no difference beyond the noise |
| host CPU-seconds | 531 | 527 | -0.9% | -20.1 to 10.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.2 | -0.9% | -0.12 to 0.0652 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
