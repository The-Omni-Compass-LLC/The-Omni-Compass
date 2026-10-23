# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,935 | -0.1% | -8.91 to 5.39 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,937 | -0.1% | -9.4 to 6.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.158 | 0.166 | +5.5% | -0.0407 to 0.058 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.345 | 0.353 | +2.1% | -0.0149 to 0.0296 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0693 | 0.0708 | +2.1% | -0.00211 to 0.00502 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -7.26 to -0.414 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -5.03 to 3.27 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 726,996 | 735,272 | +1.1% | -86,652 to 103,204 | shown, not judged |
| host CPU busy (share of the run) | 0.0891 | 0.1 | +12.5% | -0.052 to 0.0742 | EVEN, no difference beyond the noise |
| host CPU-seconds | 161 | 183 | +13.5% | -105 to 149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.12 | 0.137 | +13.5% | -0.0785 to 0.111 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | +0.0% | -5.49 to 5.96 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -3.17 to 4.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.446 | -1.0% | -0.0204 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.684 | 0.69 | +0.9% | -0.0414 to 0.0534 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.219 | -1.4% | -0.011 to 0.00492 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -11.2 to -9.52 | GAIN |
| bytes in the cache, mean (MB) | 400 | 395 | -1.2% | -12.1 to 2.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,598 | 262,280 | -2.0% | -31,948 to 21,313 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.203 | +1.1% | -0.124 to 0.129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 141 | 143 | +1.1% | -112 to 115 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.269 | +1.1% | -0.21 to 0.216 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,941 | 2,937 | -0.2% | -9.42 to 0.531 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,943 | 2,938 | -0.1% | -8.83 to 0.233 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.086 | 0.093 | +8.1% | -0.00791 to 0.0219 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.282 | 0.286 | +1.5% | -0.0464 to 0.0551 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0555 | 0.0594 | +7.0% | -0.00253 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 469 | -8.3% | -126 to 41.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 387 | -7.5% | -102 to 39.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 651,352 | 760,032 | +16.7% | -120,158 to 337,517 | shown, not judged |
| host CPU busy (share of the run) | 0.0791 | 0.0952 | +20.4% | -0.0131 to 0.0453 | EVEN, no difference beyond the noise |
| host CPU-seconds | 144 | 175 | +21.6% | -25.9 to 88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.107 | 0.131 | +21.6% | -0.0194 to 0.0658 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,841 | 5,826 | -0.3% | -31.2 to 0.933 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,850 | 5,835 | -0.2% | -27.3 to -1.57 | LOSS |
| latency, 95th percentile (ms) | 0.167 | 0.187 | +11.6% | -0.0503 to 0.089 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.376 | 0.405 | +7.7% | -0.0633 to 0.121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0862 | 0.0923 | +7.1% | -0.0199 to 0.0322 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -8.47 to -1.78 | GAIN |
| bytes in the cache, mean (MB) | 420 | 416 | -0.9% | -8.98 to 1.83 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,477 | 692,554 | -1.1% | -37,118 to 21,272 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.156 | +11.6% | -0.0885 to 0.121 | EVEN, no difference beyond the noise |
| host CPU-seconds | 255 | 288 | +13.1% | -184 to 251 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0952 | 0.108 | +13.2% | -0.0689 to 0.0941 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,870 | +0.0% | -11.7 to 11.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,882 | 2,882 | +0.0% | -10 to 11.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.375 | +0.5% | -0.0159 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.627 | 0.644 | +2.6% | -0.0629 to 0.0955 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.223 | +0.1% | -0.0148 to 0.0154 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -5.25 to -2.25 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -4.7 to -0.632 | GAIN |
| pages read into the cache (misses) | 678,322 | 678,954 | +0.1% | -23,040 to 24,303 | shown, not judged |
| host CPU busy (share of the run) | 0.274 | 0.251 | -8.4% | -0.0836 to 0.0377 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 437 | -11.2% | -191 to 80.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.372 | 0.33 | -11.2% | -0.145 to 0.0619 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
