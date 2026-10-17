# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.0% | -5.16 to 2.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -4.56 to 2.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.336 | +0.5% | -0.0237 to 0.027 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.571 | +0.5% | -0.00694 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.207 | +1.4% | -0.00392 to 0.00972 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.8 to -3.68 | GAIN |
| bytes in the cache, mean (MB) | 419 | 413 | -1.5% | -16.3 to 3.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,674 | 692,036 | +0.6% | -77,970 to 86,693 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.18 | +2.9% | -0.0695 to 0.0796 | EVEN, no difference beyond the noise |
| host CPU-seconds | 296 | 306 | +3.1% | -142 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.229 | +3.1% | -0.107 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,790 | 2,698 | -3.3% | -322 to 139 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,803 | 2,712 | -3.2% | -324 to 143 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.336 | +1.4% | -0.00784 to 0.0172 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.556 | 0.577 | +3.8% | -0.00347 to 0.0455 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.245 | +4.4% | 0.00148 to 0.0192 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -33.8 to 17.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 395 | 394 | -0.3% | -22.2 to 19.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 260,755 | 240,861 | -7.6% | -68,152 to 28,365 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.158 | -2.3% | -0.069 to 0.0615 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 115 | -3.2% | -57.9 to 50.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.231 | +0.4% | -0.0862 to 0.0881 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 4.23 to 7.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% | -7.9 to 5.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -8.18 to 6.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.318 | -1.1% | -0.031 to 0.0237 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.575 | 0.568 | -1.1% | -0.0302 to 0.0175 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.201 | -0.7% | -0.015 to 0.012 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -109 to 65.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 404 | -3.0% | -86.8 to 61.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,301 | 746,183 | +6.4% | -173,145 to 262,908 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.195 | +8.4% | 0.000792 to 0.0294 | power given |
| host CPU-seconds | 308 | 340 | +10.4% | 5.76 to 58.5 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.255 | +10.4% | 0.00408 to 0.0442 | power given |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,690 | 5,693 | +0.1% | -23.4 to 30.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,704 | 5,708 | +0.1% | -23.4 to 29.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.436 | 0.439 | +0.8% | -0.00892 to 0.0156 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.624 | +0.4% | -0.0034 to 0.00807 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.255 | 0.257 | +0.6% | -0.00569 to 0.00895 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -23.5 to 6.35 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 412 | -1.1% | -15.5 to 6.31 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,709 | 694,325 | +2.9% | 3,513 to 35,719 | shown, not judged |
| host CPU busy (share of the run) | 0.29 | 0.294 | +1.3% | -0.0133 to 0.0211 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 499 | +1.4% | -32.6 to 46.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.188 | +1.2% | -0.012 to 0.0165 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,924 | -0.1% | -5.56 to 2.46 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,933 | 2,931 | -0.1% | -5.86 to 1.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.252 | +0.3% | -0.00507 to 0.0064 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.429 | -1.0% | -0.0115 to 0.00284 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.109 | 0.109 | -0.7% | -0.0089 to 0.00732 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -16.2 to 4.08 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.8% | -12.8 to 6.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,891 | 695,415 | +1.8% | -15,465 to 40,513 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.134 | -1.2% | -0.0713 to 0.068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 242 | -1.9% | -149 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.184 | 0.181 | -2.0% | -0.112 to 0.105 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
