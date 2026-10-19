# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -5.85 to 1.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -6.07 to 1.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.353 | 0.357 | +1.1% | -0.0134 to 0.0214 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.497 | +0.0% | -0.0215 to 0.0215 | EVEN, the same |
| latency, mean (ms) | 0.206 | 0.206 | +0.1% | -0.00328 to 0.00382 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.59 to -0.351 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.2% | -10.6 to 8.72 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,414 | 730,461 | +4.4% | -187,884 to 249,976 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.191 | -5.9% | -0.0609 to 0.0369 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 327 | -7.3% | -129 to 77.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.245 | -7.3% | -0.0968 to 0.0584 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,891 | -0.0% | -2.79 to 1.86 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% | -2.56 to 1.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.428 | 0.421 | -1.6% | -0.012 to -0.00203 | GAIN |
| latency, 99th percentile (ms) | 0.573 | 0.565 | -1.3% | -0.0204 to 0.00508 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.215 | -1.5% | -0.0056 to -0.000856 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 495 | -3.2% | -60.2 to 27 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 394 | -2.0% | -57.4 to 41.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 252,647 | 267,748 | +6.0% | 8,806 to 21,396 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.174 | -2.8% | -0.113 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 119 | -3.4% | -92.7 to 84.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.223 | -3.4% | -0.174 to 0.159 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,918 | 2,903 | -0.5% | -69.7 to 39.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,906 | -0.6% | -70.7 to 38.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.233 | 0.241 | +3.3% | -0.0168 to 0.0322 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.379 | 0.386 | +1.7% | -0.00307 to 0.0157 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.167 | +8.0% | -0.0302 to 0.0549 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.57 to -1.9 | GAIN |
| bytes in the cache, mean (MB) | 420 | 420 | -0.2% | -6.66 to 5.09 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,221 | 732,629 | +4.9% | -83,529 to 152,347 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.152 | -0.3% | -0.0625 to 0.0617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 272 | -0.7% | -125 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.204 | -0.4% | -0.0936 to 0.0919 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,680 | +0.1% | -56.4 to 68.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,691 | 5,697 | +0.1% | -57.2 to 69.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.452 | 0.452 | +0.0% | -0.0129 to 0.0129 | EVEN, the same |
| latency, 99th percentile (ms) | 0.714 | 0.712 | -0.2% | -0.0162 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.257 | 0.257 | +0.2% | -0.00816 to 0.00908 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -5.6 to -3.23 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.6% | -6.18 to 0.944 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,929 | 678,379 | +0.5% | -9,524 to 16,424 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.282 | +0.6% | -0.0151 to 0.0187 | EVEN, no difference beyond the noise |
| host CPU-seconds | 474 | 476 | +0.5% | -38 to 42.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.18 | 0.18 | +0.3% | -0.0166 to 0.0176 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,882 | +0.2% | -7.16 to 17.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,892 | +0.2% | -7.03 to 17.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.37 | 0.37 | +0.1% | -0.00684 to 0.00751 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.582 | 0.582 | +0.0% | -0.0149 to 0.0149 | EVEN, the same |
| latency, mean (ms) | 0.226 | 0.228 | +0.6% | -0.00364 to 0.00652 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -20.1 to 6.08 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -1.0% | -15.2 to 6.89 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,480 | 687,288 | +1.3% | -2,468 to 20,084 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.232 | +1.5% | -0.0144 to 0.0212 | EVEN, no difference beyond the noise |
| host CPU-seconds | 389 | 395 | +1.5% | -33.8 to 45.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.294 | 0.297 | +1.2% | -0.0254 to 0.0327 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
