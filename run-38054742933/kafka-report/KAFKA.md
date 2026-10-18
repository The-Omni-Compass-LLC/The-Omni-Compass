# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 341 | +0.0% | -1.06 to 1.18 | no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0246 to 0.0219 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,525 | 2,503 | -0.9% | -234 to 190 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,776 | 3,763 | -0.3% | -332 to 306 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.68 | 9.58 | -1.1% | -2.03 to 1.81 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 383 | 384 | +0.3% | -10.9 to 13 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,650 | 1,644 | -0.3% | -69.2 to 57.9 | no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 166 | -0.1% | -5.6 to 5.13 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -1.0% | -0.0201 to 0.0142 | no difference beyond the noise |
| host CPU-seconds | 206 | 204 | -1.0% | -13.8 to 9.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -1.0% | -0.214 to 0.148 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -1.62 to 1.49 | no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.000852 to 0.00114 | same |
| end-to-end latency, 95th percentile (ms) | 2,328 | 2,303 | -1.0% | -264 to 216 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,624 | 3,548 | -2.1% | -432 to 281 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% | -0.0537 to 0.0337 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 310 | -0.3% | -35.9 to 34.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 684 | 666 | -2.6% | -69.7 to 33.7 | no difference beyond the noise |
| consumer lag, mean messages waiting | 56.5 | 56.3 | -0.4% | -5.15 to 4.72 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.277 | 0.276 | -0.5% | -0.00936 to 0.00644 | no difference beyond the noise |
| host CPU-seconds | 489 | 487 | -0.4% | -15.7 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.38 | 7.36 | -0.4% | -0.309 to 0.255 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 723 | -0.3% | -8.53 to 3.91 | no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -1.01 to 1.66 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,368 | 2,372 | +0.1% | -343 to 350 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,789 | +4.1% | -94.3 to 392 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.26 | 7.99 | -3.3% | -1.04 to 0.491 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 316 | 323 | +2.1% | -36.6 to 50.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,283 | 3,313 | +0.9% | -138 to 197 | no difference beyond the noise |
| consumer lag, mean messages waiting | 275 | 280 | +1.9% | -36 to 46.7 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% | -0.298 to 0.791 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.336 | 0.336 | -0.1% | -0.032 to 0.031 | no difference beyond the noise |
| host CPU-seconds | 577 | 578 | +0.1% | -53.4 to 54.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.77 | +0.4% | -0.14 to 0.155 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.3% | -3.81 to 1.79 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0338 to 0.035 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,457 | 2,509 | +2.1% | -46.9 to 152 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,887 | -1.6% | -505 to 382 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.59 | -0.6% | -0.129 to 0.0296 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 340 | +2.1% | -23.9 to 38 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,708 | 1,738 | +1.8% | -70.3 to 130 | no difference beyond the noise |
| consumer lag, mean messages waiting | 147 | 150 | +2.1% | -9.84 to 16.1 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.318 | 0.319 | +0.1% | -0.0124 to 0.0129 | no difference beyond the noise |
| host CPU-seconds | 552 | 554 | +0.4% | -22.5 to 26.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.38 | +0.6% | -0.118 to 0.161 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
