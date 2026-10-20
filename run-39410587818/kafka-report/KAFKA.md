# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.4/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 339 | -0.4% | -4.99 to 2.17 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | 0.000107 to 0.0104 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,505 | 2,512 | +0.3% | -196 to 209 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,616 | 3,663 | +1.3% | -152 to 247 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.52 | 9.47 | -0.5% | -0.494 to 0.39 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 375 | 383 | +2.3% | -18.1 to 35.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,637 | 1,629 | -0.5% | -91.8 to 76.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 165 | +0.9% | -7.06 to 10 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.294 | 0.295 | +0.1% | -0.014 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 206 | +0.0% | -9.74 to 9.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.36 | +0.5% | -0.158 to 0.189 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.0% | -0.541 to 0.456 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | +0.0% | -0.00128 to 0.00267 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,382 | 2,373 | -0.4% | -64.4 to 45 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,719 | -0.7% | -503 to 447 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -0.1% | -0.0777 to 0.049 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 321 | 321 | -0.2% | -10.7 to 9.64 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 710 | 693 | -2.4% | -68.3 to 33.6 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 59.3 | 58.4 | -1.4% | -2.92 to 1.22 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.288 | 0.285 | -1.0% | -0.00816 to 0.00242 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 505 | -1.0% | -14.7 to 4.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.7 | 7.63 | -1.0% | -0.243 to 0.0932 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 721 | -0.8% | -22 to 10 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 850 | 849 | -0.0% | -1.66 to 1.03 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,260 | 2,968 | +31.4% | -2,353 to 3,769 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,631 | 4,479 | +23.4% | -2,461 to 4,157 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.51 | 7.51 | +0.0% | -0.259 to 0.26 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 300 | 386 | +28.8% | -282 to 454 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,197 | 3,836 | +20.0% | -2,034 to 3,313 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 332 | +28.5% | -238 to 385 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | +0.8% | -0.0752 to 0.106 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.347 | -1.3% | -0.0144 to 0.00554 | EVEN, no difference beyond the noise |
| host CPU-seconds | 624 | 617 | -1.1% | -24.2 to 9.96 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.9 | -0.4% | -0.0634 to 0.0498 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.8/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 388 | +5.8% | -68.8 to 111 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00769 to 0.00314 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 1,619 | -33.9% | -4,173 to 2,512 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,872 | 2,569 | -33.6% | -6,225 to 3,620 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.27 | 8.13 | -1.7% | -0.641 to 0.359 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 219 | -33.4% | -531 to 311 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,719 | 1,180 | -31.3% | -2,762 to 1,685 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 145 | 96.7 | -33.5% | -235 to 138 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.18 | +9.2% | -0.638 to 1.01 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.306 | 0.309 | +0.9% | -0.0038 to 0.00952 | EVEN, no difference beyond the noise |
| host CPU-seconds | 545 | 549 | +0.8% | -8.43 to 17.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.17 | -4.1% | -0.815 to 0.545 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
