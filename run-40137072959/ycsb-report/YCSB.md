# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -2.38 to 0.0613 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -2.71 to 0.665 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.346 | +1.2% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.512 | 0.515 | +0.7% | -0.0024 to 0.00907 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.202 | +1.1% | -0.00361 to 0.00803 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -16.4 to 4.49 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 412 | -1.6% | -8.7 to -5.04 | GAIN |
| pages read into the cache (misses) | 734,887 | 694,868 | -5.4% | -82,139 to 2,101 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.18 | -11.2% | -0.0746 to 0.0293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 303 | -13.9% | -160 to 61.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.228 | -13.9% | -0.12 to 0.0464 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -1.51 to -0.717 | LOSS |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -2.29 to 0.394 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.252 | 0.256 | +1.5% | -0.015 to 0.0223 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.411 | 0.411 | -0.1% | -0.0377 to 0.037 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0813 | 0.0814 | +0.2% | -0.00484 to 0.0051 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -9.36 to -8.36 | GAIN |
| bytes in the cache, mean (MB) | 405 | 401 | -1.1% | -23.2 to 14.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,600 | 269,228 | +1.7% | -1,978 to 11,234 | shown, not judged |
| host CPU busy (share of the run) | 0.0881 | 0.119 | +35.2% | -0.0863 to 0.148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.6 | 89.7 | +38.8% | -70.7 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.121 | 0.167 | +38.8% | -0.132 to 0.226 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,908 | -0.1% | -6.12 to 2.48 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,912 | -0.1% | -7.42 to 3.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.189 | 0.187 | -0.7% | -0.00277 to 0.000101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.355 | 0.354 | -0.2% | -0.0411 to 0.0397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.143 | 0.142 | -0.8% | -0.0141 to 0.0117 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -8.42 to 0.802 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 414 | -0.2% | -8.53 to 6.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,685 | 689,427 | -3.0% | -135,625 to 93,110 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.127 | -10.4% | -0.13 to 0.1 | EVEN, no difference beyond the noise |
| host CPU-seconds | 254 | 223 | -12.3% | -270 to 207 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.19 | 0.167 | -12.3% | -0.202 to 0.155 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,844 | 5,839 | -0.1% | -22.1 to 11.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,852 | 5,847 | -0.1% | -22.1 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.16 | 0.16 | +0.0% | -0.00861 to 0.00861 | EVEN, the same |
| latency, 99th percentile (ms) | 0.371 | 0.378 | +1.9% | -0.0167 to 0.0307 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0837 | 0.0834 | -0.3% | -0.00539 to 0.00484 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.54 to -3.52 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.4% | -2.53 to -1.03 | GAIN |
| pages read into the cache (misses) | 703,679 | 704,126 | +0.1% | -24,012 to 24,907 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.126 | +1.7% | -0.0353 to 0.0395 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 228 | +2.3% | -74.2 to 84.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0831 | 0.0851 | +2.4% | -0.0277 to 0.0316 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,877 | -0.1% | -7.21 to 0.0497 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,887 | -0.1% | -6.69 to -0.1 | LOSS |
| latency, 95th percentile (ms) | 0.353 | 0.356 | +0.9% | -0.00197 to 0.00797 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.557 | 0.565 | +1.4% | 0.00143 to 0.0146 | LOSS |
| latency, mean (ms) | 0.215 | 0.218 | +1.4% | -0.00236 to 0.00845 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -8.65 to -2.09 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.6% | -4.6 to -0.214 | GAIN |
| pages read into the cache (misses) | 673,630 | 683,889 | +1.5% | -5,321 to 25,840 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.247 | +2.9% | -0.022 to 0.0356 | EVEN, no difference beyond the noise |
| host CPU-seconds | 417 | 431 | +3.5% | -46.7 to 76.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.314 | 0.325 | +3.6% | -0.0345 to 0.0572 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
