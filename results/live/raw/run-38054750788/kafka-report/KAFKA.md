# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 340 | +0.1% | -3.21 to 3.72 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0247 to 0.0308 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,499 | 2,457 | -1.7% | -154 to 70 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,675 | 3,598 | -2.1% | -577 to 424 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.66 | 9.35 | -3.2% | -0.609 to -0.00603 | better |
| end-to-end latency, mean (ms) | 381 | 375 | -1.5% | -35.4 to 23.8 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,623 | 1,613 | -0.6% | -148 to 130 | no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 162 | -2.1% | -15.1 to 8.09 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.294 | 0.29 | -1.3% | -0.0249 to 0.0174 | no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.3% | -17.6 to 12.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.3 | -1.4% | -0.276 to 0.182 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.847 to 0.571 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00192 to 0.00214 | same |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,501 | -0.6% | -172 to 144 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,867 | 3,780 | -2.2% | -567 to 394 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | +0.0% | -0.0635 to 0.0708 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 341 | 339 | -0.6% | -21.2 to 16.9 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 722 | 720 | -0.2% | -20.3 to 17.6 | no difference beyond the noise |
| consumer lag, mean messages waiting | 63.2 | 62 | -2.0% | -4.43 to 1.85 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.5% | -0.00445 to 0.00166 | no difference beyond the noise |
| host CPU-seconds | 497 | 495 | -0.4% | -7.61 to 3.38 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.51 | 7.48 | -0.3% | -0.118 to 0.0685 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.7/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 730 | +0.2% | -0.288 to 2.56 | no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.0176 to 0.0119 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,399 | 2,332 | -2.8% | -139 to 5.92 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,830 | 3,615 | -5.6% | -624 to 194 | no difference beyond the noise |
| end-to-end latency, median (ms) | 7.39 | 7.37 | -0.4% | -0.2 to 0.148 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 314 | -3.6% | -28.9 to 5.4 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,362 | 3,319 | -1.3% | -282 to 195 | no difference beyond the noise |
| consumer lag, mean messages waiting | 284 | 274 | -3.8% | -25 to 3.58 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.314 | 0.312 | -0.5% | -0.0103 to 0.00716 | no difference beyond the noise |
| host CPU-seconds | 559 | 557 | -0.3% | -15.6 to 11.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.7 | -0.5% | -0.053 to 0.036 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 983 messages a second; base rate 147.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 367 | -0.2% | -2.56 to 0.855 | no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 432 | -0.0% | -0.853 to 0.541 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,425 | 2,492 | +2.8% | 48.7 to 85.1 | **WORSE** |
| end-to-end latency, 99th percentile (ms) | 3,891 | 3,847 | -1.1% | -554 to 465 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.05 | 8.01 | -0.5% | -0.147 to 0.0588 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 333 | 339 | +1.7% | -12.6 to 24.2 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,734 | 1,746 | +0.7% | -90 to 115 | no difference beyond the noise |
| consumer lag, mean messages waiting | 150 | 152 | +1.3% | -8.27 to 12.1 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.272 | 0.271 | -0.6% | -0.00696 to 0.00355 | no difference beyond the noise |
| host CPU-seconds | 487 | 484 | -0.5% | -12.9 to 8.19 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.93 | 2.93 | -0.3% | -0.0631 to 0.0459 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
