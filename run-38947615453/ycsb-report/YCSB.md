# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,897 | -0.1% | -4.22 to 0.879 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -4.05 to 0.785 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.321 | -0.1% | -0.0147 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.458 | 0.461 | +0.7% | -0.00942 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.197 | +1.4% | -0.00195 to 0.00748 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.2% | -107 to 54.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 399 | -4.8% | -82.4 to 41.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,811 | 723,858 | +3.4% | -106,329 to 154,421 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.17 | -2.6% | -0.103 to 0.0933 | EVEN, no difference beyond the noise |
| host CPU-seconds | 297 | 288 | -3.0% | -209 to 191 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.216 | -3.0% | -0.157 to 0.143 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,916 | -0.0% | -2.11 to -0.37 | LOSS |
| throughput (operations a second) | 2,922 | 2,921 | -0.0% | -2.29 to 0.153 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.332 | -0.2% | -0.00354 to 0.0022 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.422 | 0.422 | +0.0% | -0.0131 to 0.0131 | EVEN, the same |
| latency, mean (ms) | 0.161 | 0.16 | -0.4% | -0.00703 to 0.00569 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 497 | -2.9% | -29.8 to -0.374 | GAIN |
| bytes in the cache, mean (MB) | 407 | 393 | -3.4% | -27.2 to -0.677 | GAIN |
| pages read into the cache (misses) | 264,459 | 267,096 | +1.0% | -22,970 to 28,246 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.171 | -0.8% | -0.199 to 0.196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 130 | 126 | -2.9% | -170 to 163 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.235 | -2.9% | -0.319 to 0.305 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,930 | 2,924 | -0.2% | -17.6 to 4.97 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,932 | 2,927 | -0.2% | -12 to 3.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.221 | 0.243 | +10.0% | -0.0213 to 0.0653 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.375 | 0.413 | +10.2% | -0.0499 to 0.127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0852 | 0.0958 | +12.4% | -0.00915 to 0.0303 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -21.8 to 7.19 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 415 | -1.1% | -22.1 to 12.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,492 | 679,994 | -0.7% | -123,889 to 114,892 | shown, not judged |
| host CPU busy (share of the run) | 0.0932 | 0.134 | +44.1% | -0.0081 to 0.0904 | EVEN, no difference beyond the noise |
| host CPU-seconds | 167 | 249 | +48.8% | -11.2 to 174 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.186 | +48.9% | -0.00867 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,721 | 5,720 | -0.0% | -19.5 to 18.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,734 | 5,733 | -0.0% | -19.8 to 19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.413 | +0.1% | -0.0054 to 0.00607 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.585 | 0.585 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, mean (ms) | 0.234 | 0.233 | -0.2% | -0.00436 to 0.00347 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.1% | -6.47 to -4.37 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -5.47 to -0.0285 | GAIN |
| pages read into the cache (misses) | 689,260 | 687,757 | -0.2% | -11,960 to 8,955 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.312 | -1.2% | -0.0418 to 0.0344 | EVEN, no difference beyond the noise |
| host CPU-seconds | 578 | 569 | -1.6% | -106 to 88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.214 | -1.6% | -0.0393 to 0.0322 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,902 | -0.1% | -4.44 to 0.971 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,912 | -0.0% | -4.46 to 1.61 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.31 | -0.5% | -0.00792 to 0.00459 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.532 | 0.532 | -0.1% | -0.0165 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.147 | 0.147 | -0.0% | -0.00823 to 0.00809 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -15 to 2.83 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -0.8% | -11.4 to 4.48 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,972 | 686,958 | +0.6% | -19,712 to 27,683 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.183 | -1.6% | -0.0156 to 0.00972 | EVEN, no difference beyond the noise |
| host CPU-seconds | 337 | 330 | -2.0% | -34.6 to 20.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.248 | -2.0% | -0.0261 to 0.0158 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
