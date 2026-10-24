# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -9.72 to 8.28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% | -8.19 to 7.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.174 | 0.177 | +1.7% | -0.0746 to 0.0806 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.358 | 0.371 | +3.6% | -0.0562 to 0.0822 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0715 | 0.0722 | +0.9% | -0.0109 to 0.0122 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -6.83 to -0.19 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -12.7 to 10.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 731,719 | 721,905 | -1.3% | -54,241 to 34,613 | shown, not judged |
| host CPU busy (share of the run) | 0.0914 | 0.11 | +20.7% | -0.0379 to 0.0757 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 203 | +22.7% | -75.3 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.124 | 0.152 | +22.7% | -0.0561 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,877 | +0.1% | -12.5 to 18.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -11.4 to 16.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.503 | 0.502 | -0.2% | -0.0053 to 0.0033 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.67 | 0.665 | -0.7% | -0.0212 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.222 | -0.2% | -0.00714 to 0.00636 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -25.8 to -0.486 | GAIN |
| bytes in the cache, mean (MB) | 399 | 392 | -1.6% | -22.2 to 9.42 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 256,676 | 277,663 | +8.2% | 13,837 to 28,137 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.191 | -6.4% | -0.0848 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 144 | 132 | -7.9% | -74.4 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.271 | 0.249 | -8.0% | -0.139 to 0.0962 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,935 | +0.0% | -6.75 to 9.68 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,937 | +0.0% | -4.9 to 6.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.119 | 0.109 | -8.7% | -0.048 to 0.0274 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.335 | 0.318 | -5.2% | -0.0732 to 0.0386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0669 | 0.0636 | -4.9% | -0.0133 to 0.00676 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.45 to -1.76 | GAIN |
| bytes in the cache, mean (MB) | 419 | 419 | -0.0% | -14 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 736,314 | 714,393 | -3.0% | -212,740 to 168,898 | shown, not judged |
| host CPU busy (share of the run) | 0.0753 | 0.0804 | +6.8% | -0.0136 to 0.0238 | EVEN, no difference beyond the noise |
| host CPU-seconds | 135 | 145 | +7.6% | -25.5 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.101 | 0.108 | +7.6% | -0.019 to 0.0343 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,836 | 5,827 | -0.1% | -20.2 to 3.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,845 | 5,837 | -0.1% | -20.7 to 4.55 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.172 | 0.171 | -0.2% | -0.0316 to 0.0309 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.39 | 0.389 | -0.3% | -0.0368 to 0.0348 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0877 | 0.087 | -0.8% | -0.00742 to 0.00607 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -20.4 to 0.405 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 413 | -1.5% | -13.9 to 1.61 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 692,851 | 718,119 | +3.6% | -5,517 to 56,054 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.139 | +4.3% | -0.0589 to 0.0703 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 253 | +5.5% | -120 to 146 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0895 | 0.0945 | +5.5% | -0.045 to 0.0549 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,873 | +0.0% | -8.18 to 10.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,882 | 2,883 | +0.0% | -10.5 to 12.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.363 | +0.7% | -0.0223 to 0.0277 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.575 | 0.577 | +0.3% | -0.0607 to 0.0647 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.223 | +1.2% | -0.0146 to 0.0197 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -13.9 to 1.85 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -0.9% | -8.52 to 1.28 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,518 | 686,234 | +0.4% | -23,660 to 29,090 | shown, not judged |
| host CPU busy (share of the run) | 0.269 | 0.268 | -0.1% | -0.031 to 0.0305 | EVEN, no difference beyond the noise |
| host CPU-seconds | 479 | 476 | -0.7% | -63.6 to 57.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.362 | 0.359 | -0.8% | -0.0494 to 0.0438 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
