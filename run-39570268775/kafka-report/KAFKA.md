# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 977 messages a second; base rate 109.9/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.0% | -3.17 to 3.21 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | +0.0% | 0.000764 to 0.0238 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,641 | 2,591 | -1.9% | -148 to 48 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,985 | 3,987 | +0.0% | -441 to 445 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.31 | 9.02 | -3.1% | -1.07 to 0.5 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 399 | 393 | -1.4% | -42.3 to 30.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,724 | 1,711 | -0.8% | -55 to 28.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 170 | -1.6% | -17.8 to 12.3 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.309 | -0.5% | -0.0224 to 0.0193 | EVEN, no difference beyond the noise |
| host CPU-seconds | 219 | 218 | -0.4% | -15.6 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.54 | -0.4% | -0.248 to 0.216 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.956 to 0.633 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00175 to 0.00441 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,508 | 2,503 | -0.2% | -275 to 264 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,813 | 3,896 | +2.2% | -98.9 to 264 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.7 | -0.7% | -0.485 to 0.326 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 337 | 341 | +1.2% | -17.5 to 25.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 705 | 722 | +2.5% | -96.8 to 131 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.6 | 62.8 | +2.0% | -3.58 to 5.99 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.288 | 0.285 | -1.2% | -0.0294 to 0.0226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 508 | 502 | -1.2% | -52.7 to 40.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 7.59 | -1.1% | -0.758 to 0.591 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1948 messages a second; base rate 292.2/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 728 | -0.1% | -7.19 to 5.48 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0194 to 0.0183 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,544 | 2,522 | -0.8% | -439 to 396 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,925 | 3,949 | +0.6% | -496 to 545 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.31 | 7.27 | -0.5% | -0.153 to 0.0755 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 339 | 340 | +0.3% | -60.1 to 62.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,445 | 3,479 | +1.0% | -403 to 470 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 295 | 296 | +0.4% | -50.8 to 53 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.418 to 0.654 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.3% | -0.00534 to 0.00699 | EVEN, no difference beyond the noise |
| host CPU-seconds | 562 | 564 | +0.4% | -9.07 to 14.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | +0.6% | -0.035 to 0.0542 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.1/s; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `69eae6a1f2c6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -1.51 to 0.0138 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.837 to 0.517 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,448 | 2,470 | +0.9% | -89.7 to 133 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,815 | 3,769 | -1.2% | -134 to 41.7 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.14 | 8.1 | -0.5% | -0.21 to 0.128 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 327 | +1.5% | -10.5 to 20.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,704 | 1,711 | +0.4% | -49.8 to 64.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 143 | 145 | +1.3% | -5.38 to 9.18 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.304 | 0.303 | -0.4% | -0.0083 to 0.0057 | EVEN, no difference beyond the noise |
| host CPU-seconds | 547 | 545 | -0.3% | -14.2 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.3 | -0.1% | -0.0855 to 0.0788 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
