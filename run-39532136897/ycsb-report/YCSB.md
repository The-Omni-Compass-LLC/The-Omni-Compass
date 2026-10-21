# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,887 | -0.1% | -3.9 to 0.403 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,890 | -0.1% | -3.55 to 0.186 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.319 | +0.1% | -0.00254 to 0.0032 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.472 | +0.2% | -0.00894 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.192 | -0.9% | -0.0108 to 0.0073 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.5% | -109 to 63.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 400 | -4.3% | -91.3 to 55.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,771 | 739,398 | +6.3% | -73,863 to 161,117 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.195 | -6.4% | -0.0378 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 368 | 339 | -7.8% | -82.6 to 24.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.255 | -7.8% | -0.062 to 0.0187 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | -0.0% | -3.97 to 2.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -4.42 to 2.65 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.423 | 0.426 | +0.8% | -0.00465 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.596 | 0.6 | +0.6% | -0.0128 to 0.0195 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.221 | +1.4% | -0.00326 to 0.00945 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.4% | -51.1 to 15.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 403 | 392 | -2.8% | -36.8 to 14.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,095 | 276,674 | +5.2% | -33,348 to 60,506 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.213 | -3.4% | -0.0179 to 0.00309 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 149 | -4.6% | -17.1 to 2.69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.293 | 0.28 | -4.7% | -0.0323 to 0.00504 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,914 | -0.0% | -4.77 to 1.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,916 | -0.0% | -4.39 to 1.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.173 | 0.172 | -0.8% | -0.0065 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.379 | 0.375 | -1.0% | -0.0162 to 0.00884 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.104 | 0.104 | -0.3% | -0.00643 to 0.00574 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -23.4 to 11.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -20.8 to 17.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,682 | 691,935 | -0.7% | -174,341 to 164,848 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.146 | +7.7% | -0.0119 to 0.0327 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 270 | +9.0% | -23.7 to 68 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.185 | 0.202 | +9.0% | -0.0177 to 0.0509 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,775 | 5,766 | -0.2% | -25.2 to 7.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,789 | 5,781 | -0.1% | -23.6 to 6.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.289 | 0.294 | +1.6% | -0.00946 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.533 | +1.1% | -0.0143 to 0.0263 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.147 | 0.148 | +0.7% | -0.00484 to 0.00685 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -6.73 to -4.91 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.7% | -3.55 to -2.21 | GAIN |
| pages read into the cache (misses) | 680,061 | 690,264 | +1.5% | -4,379 to 24,785 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.218 | -0.6% | -0.0449 to 0.0421 | EVEN, no difference beyond the noise |
| host CPU-seconds | 401 | 399 | -0.5% | -97.8 to 93.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.15 | 0.15 | -0.5% | -0.0368 to 0.0353 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -19.3 to 18.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -19.7 to 18.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.342 | -0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.532 | 0.531 | -0.2% | -0.0207 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.207 | 0.208 | +0.5% | -0.00251 to 0.00457 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -21.5 to 6.97 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -1.0% | -15.2 to 7.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 672,157 | 684,328 | +1.8% | -19,191 to 43,533 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.245 | +1.6% | -0.0703 to 0.0779 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 435 | +1.5% | -167 to 180 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.322 | 0.327 | +1.4% | -0.124 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
