# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 959 messages a second; base rate 107.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 337 | -0.4% | -2.07 to -0.342 | **WORSE** |
| throughput (messages a second consumed) | 412 | 412 | -0.0% | -0.00844 to 0.00147 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,202 | +5.1% | -190 to 404 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,068 | 3,245 | +5.8% | 24.2 to 331 | **WORSE** |
| end-to-end latency, median (ms) | 8.87 | 8.78 | -1.0% | -0.292 to 0.116 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 317 | 334 | +5.2% | 0.381 to 32.7 | **WORSE** |
| consumer lag, most messages waiting at once | 1,367 | 1,443 | +5.6% | -40.4 to 192 | no difference beyond the noise |
| consumer lag, mean messages waiting | 137 | 143 | +4.5% | 0.165 to 12.2 | **WORSE** |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.281 | 0.282 | +0.3% | -0.00741 to 0.00892 | no difference beyond the noise |
| host CPU-seconds | 202 | 202 | +0.3% | -5.24 to 6.38 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.32 | +0.6% | -0.082 to 0.124 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.731 to 0.366 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.341 to 0.21 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,435 | 2,447 | +0.5% | -181 to 205 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,793 | 3,844 | +1.4% | -239 to 342 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.1% | -0.0976 to 0.0716 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 329 | 332 | +0.9% | -11.6 to 17.6 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 702 | 710 | +1.1% | -47 to 62.3 | no difference beyond the noise |
| consumer lag, mean messages waiting | 60 | 61.1 | +1.7% | -0.461 to 2.52 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.281 | 0.28 | -0.3% | -0.0125 to 0.0108 | no difference beyond the noise |
| host CPU-seconds | 495 | 493 | -0.2% | -21.7 to 19.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.47 | 7.46 | -0.1% | -0.306 to 0.285 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1931 messages a second; base rate 289.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | -0.0% | -2.74 to 2.41 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0179 to 0.00711 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,302 | -1.7% | -153 to 72.2 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,672 | 3,595 | -2.1% | -247 to 94.2 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.3 | 8.09 | -2.6% | -0.612 to 0.188 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 310 | -1.0% | -20.7 to 14.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,271 | 3,254 | -0.5% | -166 to 133 | no difference beyond the noise |
| consumer lag, mean messages waiting | 273 | 270 | -1.1% | -16.6 to 10.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.338 | 0.339 | +0.2% | -0.00679 to 0.0081 | no difference beyond the noise |
| host CPU-seconds | 581 | 583 | +0.3% | -8.68 to 12.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.78 | 1.78 | +0.3% | -0.0319 to 0.0441 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 974 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.1% | -1.05 to 0.0225 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00451 to 0.00169 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,303 | 2,304 | +0.0% | -154 to 156 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,561 | 3,685 | +3.5% | -128 to 375 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.43 | 8.41 | -0.2% | -0.117 to 0.076 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 309 | +1.3% | -9.48 to 17.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,646 | 1,642 | -0.2% | -47.4 to 40.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 136 | +1.0% | -4.78 to 7.38 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.315 | 0.314 | -0.5% | -0.00858 to 0.00522 | no difference beyond the noise |
| host CPU-seconds | 562 | 559 | -0.5% | -14.6 to 8.88 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.41 | 3.4 | -0.4% | -0.0794 to 0.0543 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
