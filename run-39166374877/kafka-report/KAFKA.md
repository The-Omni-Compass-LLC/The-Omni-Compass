# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 979 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.3% | -2.79 to 0.906 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 421 | 421 | -0.1% | -2.07 to 1.29 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,581 | 2,593 | +0.5% | -85.5 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,763 | 3,855 | +2.4% | -418 to 602 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.51 | 9.61 | +1.0% | -0.518 to 0.713 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 396 | 398 | +0.6% | -2.65 to 7.77 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,715 | 1,720 | +0.3% | -59.6 to 70.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 172 | 174 | +1.3% | -2.82 to 7.46 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.291 | -0.4% | -0.013 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 203 | -0.3% | -8.44 to 7.38 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.3 | -0.1% | -0.143 to 0.138 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.0946 to 0.00891 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00267 to 0.00122 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,391 | 2,437 | +1.9% | -63.6 to 156 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,786 | 3,661 | -3.3% | -361 to 110 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.0335 to -0.0185 | GAIN |
| end-to-end latency, mean (ms) | 327 | 326 | -0.2% | -6.1 to 5.1 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 698 | 711 | +1.9% | -30.7 to 56.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 60.2 | 60.1 | -0.0% | -0.216 to 0.182 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.282 | 0.28 | -0.6% | -0.00778 to 0.00415 | EVEN, no difference beyond the noise |
| host CPU-seconds | 497 | 493 | -0.7% | -14.4 to 7.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.5 | 7.45 | -0.6% | -0.218 to 0.122 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 290.0/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 725 | +0.0% | -1.42 to 1.42 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 850 | +0.0% | -0.0178 to 0.0256 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,328 | 2,328 | +0.0% | -43.2 to 45.1 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,799 | 3,716 | -2.2% | -493 to 327 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.23 | 8.04 | -2.3% | -1.11 to 0.726 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 317 | -0.5% | -6.09 to 3.16 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,307 | 3,275 | -1.0% | -150 to 85.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 277 | 275 | -0.5% | -4.26 to 1.41 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.342 | 0.338 | -1.3% | -0.0302 to 0.0211 | EVEN, no difference beyond the noise |
| host CPU-seconds | 588 | 581 | -1.2% | -57.3 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.78 | -1.2% | -0.178 to 0.136 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.1/s; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 367 | -0.1% | -0.969 to 0.58 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.85 to 0.533 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,536 | 2,513 | -0.9% | -335 to 288 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,966 | 3,841 | -3.1% | -706 to 456 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.22 | 8.17 | -0.5% | -0.239 to 0.158 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 339 | 335 | -1.1% | -53 to 45.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,761 | 1,755 | -0.4% | -229 to 215 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 151 | 148 | -1.7% | -22.7 to 17.5 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -1.2% | -0.0111 to 0.00386 | EVEN, no difference beyond the noise |
| host CPU-seconds | 534 | 528 | -1.1% | -18.7 to 6.55 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.2 | -1.1% | -0.118 to 0.0454 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
