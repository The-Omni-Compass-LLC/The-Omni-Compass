# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 341 | +0.2% | -1.33 to 2.76 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 419 | -0.1% | -2.05 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,607 | 2,593 | -0.5% | -160 to 132 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,832 | 3,722 | -2.9% | -749 to 528 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.39 | 9.29 | -1.0% | -0.474 to 0.278 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 397 | 386 | -2.8% | -34.9 to 12.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 1,664 | -2.1% | -130 to 60.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 167 | -3.3% | -17.8 to 6.38 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.293 | 0.289 | -1.2% | -0.0175 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 202 | -1.2% | -12.3 to 7.54 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.29 | -1.5% | -0.184 to 0.0873 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -0.328 to 0.0375 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000872 to 0.00204 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,327 | 2,365 | +1.7% | -92.1 to 169 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,727 | 3,636 | -2.5% | -503 to 320 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.2 | 11.1 | -0.3% | -0.107 to 0.0374 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 314 | 314 | -0.2% | -15.4 to 14 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 671 | 691 | +3.0% | -3.96 to 44 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 57.7 | 57.5 | -0.4% | -4.09 to 3.58 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.273 | 0.271 | -0.9% | -0.00586 to 0.000882 | EVEN, no difference beyond the noise |
| host CPU-seconds | 489 | 484 | -0.9% | -10.4 to 1.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.37 | 7.31 | -0.8% | -0.153 to 0.0353 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.3/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 719 | -0.8% | -19.2 to 7.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.00643 to 0.00458 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,242 | 2,299 | +2.5% | -90.5 to 203 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,587 | 3,682 | +2.6% | -7.19 to 197 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.32 | 8.15 | -2.0% | -1.07 to 0.73 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 305 | 318 | +4.1% | 0.451 to 24.4 | LOSS |
| consumer lag, most messages waiting at once | 3,206 | 3,244 | +1.2% | -112 to 189 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 265 | 276 | +4.0% | -2.26 to 23.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.2% | -0.421 to 0.667 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.327 | -0.4% | -0.00314 to 0.00031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 563 | -0.4% | -5.38 to 1.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.5% | -0.0137 to 0.0306 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 983 messages a second; base rate 147.5/s; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 368 | -0.2% | -2.7 to 1.55 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 433 | 433 | -0.0% | -0.0019 to 0.00106 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,430 | 2,487 | +2.4% | -203 to 318 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,861 | 3,866 | +0.1% | -696 to 705 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.98 | 8 | +0.3% | -0.0518 to 0.0965 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 331 | 338 | +2.3% | -21.8 to 36.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,743 | 1,753 | +0.6% | -191 to 211 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 148 | 151 | +2.0% | -10.6 to 16.6 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.268 | 0.266 | -0.7% | -0.00569 to 0.00212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 479 | 475 | -0.8% | -11.2 to 3.32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 2.89 | 2.87 | -0.7% | -0.0652 to 0.0267 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
