# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -3.15 to -0.198 | **WORSE** |
| throughput (operations a second) | 2,899 | 2,898 | -0.1% | -3.32 to 0.159 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.341 | -0.5% | -0.0305 to 0.0271 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.511 | +0.6% | -0.00561 to 0.0116 | no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.204 | +0.2% | -0.00542 to 0.00608 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 466 | -9.0% | -138 to 46.3 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 382 | -8.9% | -102 to 27.4 | no difference beyond the noise |
| pages read into the cache (misses) | 732,882 | 736,004 | +0.4% | -157,568 to 163,812 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.19 | -3.2% | -0.0314 to 0.0188 | no difference beyond the noise |
| host CPU-seconds | 339 | 326 | -4.0% | -64 to 36.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.245 | -4.0% | -0.048 to 0.0276 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,804 | 2,686 | -4.2% | -454 to 217 | no difference beyond the noise |
| throughput (operations a second) | 2,815 | 2,698 | -4.1% | -449 to 216 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.351 | +2.1% | -0.0103 to 0.025 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.529 | 0.572 | +8.2% | -0.0299 to 0.117 | no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.25 | +10.9% | -0.0337 to 0.0828 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 455 | -11.1% | -151 to 37.3 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 397 | 353 | -11.1% | -102 to 14.1 | no difference beyond the noise |
| pages read into the cache (misses) | 260,725 | 238,666 | -8.5% | -67,463 to 23,345 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.141 | +0.6% | -0.0927 to 0.0946 | no difference beyond the noise |
| host CPU-seconds | 101 | 102 | +1.4% | -76.6 to 79.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.207 | +5.8% | -0.119 to 0.141 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% | -3.57 to -2.02 | **WORSE** |
| throughput (operations a second) | 2,899 | 2,896 | -0.1% | -2.7 to -2.36 | **WORSE** |
| latency, 95th percentile (ms) | 0.342 | 0.345 | +0.9% | -0.00991 to 0.0159 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.518 | +0.1% | -0.0205 to 0.0218 | no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.205 | +0.6% | -0.00101 to 0.00338 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.1% | -105 to 52.5 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 399 | -4.1% | -78.8 to 44.8 | no difference beyond the noise |
| pages read into the cache (misses) | 721,790 | 715,451 | -0.9% | -171,954 to 159,276 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.176 | -1.8% | -0.0435 to 0.0372 | no difference beyond the noise |
| host CPU-seconds | 306 | 298 | -2.7% | -90.8 to 74.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.224 | -2.7% | -0.0682 to 0.0559 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,688 | 5,678 | -0.2% | -61 to 41.3 | no difference beyond the noise |
| throughput (operations a second) | 5,705 | 5,696 | -0.2% | -60.6 to 41.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.439 | 0.443 | +0.9% | -0.0134 to 0.0214 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.664 | 0.673 | +1.3% | -0.0465 to 0.0638 | no difference beyond the noise |
| latency, mean (ms) | 0.255 | 0.257 | +0.9% | -0.008 to 0.0125 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.8% | -77.7 to -52.9 | better |
| bytes in the cache, mean (MB) | 417 | 365 | -12.4% | -63.2 to -40.7 | better |
| pages read into the cache (misses) | 679,207 | 773,228 | +13.8% | 80,320 to 107,722 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.2% | -0.00873 to 0.00964 | no difference beyond the noise |
| host CPU-seconds | 481 | 482 | +0.1% | -27.4 to 28.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.182 | 0.182 | +0.2% | -0.00849 to 0.00916 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% | -5.11 to 1.2 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -6.32 to 2.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.319 | +1.1% | -0.0108 to 0.0175 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.549 | +1.8% | -0.00284 to 0.0222 | no difference beyond the noise |
| latency, mean (ms) | 0.149 | 0.148 | -0.1% | -0.00141 to 0.00123 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 467 | -8.9% | -120 to 29.1 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 383 | -8.4% | -91.8 to 22 | no difference beyond the noise |
| pages read into the cache (misses) | 682,918 | 738,387 | +8.1% | -55,427 to 166,365 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.206 | +6.5% | -0.0554 to 0.0806 | no difference beyond the noise |
| host CPU-seconds | 355 | 385 | +8.3% | -130 to 189 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.289 | +8.3% | -0.0978 to 0.142 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
