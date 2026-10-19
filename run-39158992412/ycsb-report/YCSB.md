# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,895 | -0.0% | -6.34 to 5.72 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -5.38 to 4.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.329 | -1.9% | -0.0229 to 0.0102 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.5 | 0.491 | -1.9% | -0.0237 to 0.00501 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.2 | -0.6% | -0.00866 to 0.00638 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -23 to 7.6 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 412 | -1.4% | -13 to 1.59 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 706,922 | 694,411 | -1.8% | -97,768 to 72,747 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.169 | -8.6% | -0.0506 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 316 | 284 | -10.2% | -104 to 40 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.213 | -10.2% | -0.0782 to 0.0298 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,928 | 2,930 | +0.1% | -3.48 to 7.59 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,931 | 2,933 | +0.1% | -5.44 to 8.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.281 | +0.4% | -0.0365 to 0.0385 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.437 | -4.1% | -0.169 to 0.132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.103 | +0.7% | -0.0088 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -19.8 to -5.19 | GAIN |
| bytes in the cache, mean (MB) | 408 | 397 | -2.8% | -20 to -3.19 | GAIN |
| pages read into the cache (misses) | 262,314 | 272,259 | +3.8% | -12,953 to 32,844 | shown, not judged |
| host CPU busy (share of the run) | 0.0856 | 0.103 | +20.1% | -0.0622 to 0.0966 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.7 | 74.7 | +23.1% | -48.1 to 76.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.114 | 0.14 | +23.0% | -0.0897 to 0.142 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,930 | -0.1% | -6.36 to 1.69 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,932 | -0.1% | -6.2 to 1.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.217 | 0.212 | -2.0% | -0.0252 to 0.0165 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.369 | 0.361 | -2.0% | -0.0185 to 0.00387 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0818 | 0.0823 | +0.6% | -0.00463 to 0.00564 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.1% | -15.2 to 4.25 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 415 | -1.5% | -10.2 to -2.31 | GAIN |
| pages read into the cache (misses) | 675,688 | 736,670 | +9.0% | 33,742 to 88,222 | shown, not judged |
| host CPU busy (share of the run) | 0.097 | 0.0989 | +2.0% | -0.0391 to 0.0429 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 179 | +2.2% | -78 to 85.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.134 | +2.2% | -0.0584 to 0.0641 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,705 | 5,701 | -0.1% | -51 to 42.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,721 | 5,716 | -0.1% | -49.9 to 41.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.434 | 0.435 | +0.2% | -0.0033 to 0.0053 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.645 | +1.2% | -0.000653 to 0.0153 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.253 | 0.253 | -0.0% | -0.00486 to 0.00461 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -7.23 to -2.96 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -5.51 to -0.368 | GAIN |
| pages read into the cache (misses) | 682,599 | 684,984 | +0.3% | -26,833 to 31,603 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.277 | -2.2% | -0.0155 to 0.00293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 479 | 464 | -3.1% | -35.6 to 5.99 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.175 | -3.1% | -0.0118 to 0.000634 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,876 | -0.2% | -21.1 to 9.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,887 | -0.2% | -19.5 to 8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.373 | -0.3% | -0.0204 to 0.0184 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.597 | 0.596 | -0.1% | -0.053 to 0.0523 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.228 | -0.8% | -0.015 to 0.0113 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -5.34 to -2.08 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.2% | -3.87 to 2.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,402 | 680,339 | +0.9% | -18,383 to 30,256 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.239 | +0.0% | -0.0543 to 0.0545 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 411 | +0.3% | -120 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.309 | 0.31 | +0.5% | -0.0898 to 0.093 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
