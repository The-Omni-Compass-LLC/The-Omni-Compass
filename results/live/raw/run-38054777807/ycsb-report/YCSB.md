# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -2.66 to 1.29 | no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% | -2.54 to 1.34 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.218 | 0.219 | +0.5% | -0.0443 to 0.0463 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.357 | +1.5% | -0.0511 to 0.0618 | no difference beyond the noise |
| latency, mean (ms) | 0.083 | 0.0839 | +1.1% | -0.00254 to 0.0044 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 445 | -13.1% | -80.1 to -54.1 | better |
| bytes in the cache, mean (MB) | 420 | 366 | -12.8% | -79.2 to -28.5 | better |
| pages read into the cache (misses) | 694,101 | 794,493 | +14.5% | -47,216 to 248,000 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.125 | +10.8% | -0.0171 to 0.0414 | no difference beyond the noise |
| host CPU-seconds | 207 | 232 | +12.4% | -37.4 to 88.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.173 | +12.4% | -0.028 to 0.0661 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,889 | -0.0% | -4 to 1.55 | no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,895 | -0.0% | -3.8 to 1.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.423 | 0.43 | +1.7% | 0.00203 to 0.012 | **WORSE** |
| latency, 99th percentile (ms) | 0.559 | 0.565 | +1.2% | 0.000929 to 0.0124 | **WORSE** |
| latency, mean (ms) | 0.219 | 0.223 | +1.4% | -0.00358 to 0.00991 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 452 | -11.7% | -60.6 to -59.6 | better |
| bytes in the cache, mean (MB) | 408 | 355 | -12.9% | -61 to -44.3 | better |
| pages read into the cache (misses) | 275,598 | 299,411 | +8.6% | -27,500 to 75,126 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.172 | -5.5% | -0.0693 to 0.0494 | no difference beyond the noise |
| host CPU-seconds | 125 | 116 | -7.2% | -55.8 to 37.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.218 | -7.1% | -0.105 to 0.0714 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.1% | -3.01 to -1.09 | **WORSE** |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -2.9 to -0.975 | **WORSE** |
| latency, 95th percentile (ms) | 0.308 | 0.31 | +0.9% | -0.000202 to 0.00554 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.478 | 0.48 | +0.3% | -0.00706 to 0.0104 | no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.198 | +1.5% | -0.00298 to 0.00874 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 465 | -9.3% | -107 to 11.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 384 | -8.0% | -88.1 to 21.1 | no difference beyond the noise |
| pages read into the cache (misses) | 691,164 | 787,717 | +14.0% | -10,782 to 203,887 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.17 | +2.8% | -0.0551 to 0.0645 | no difference beyond the noise |
| host CPU-seconds | 280 | 288 | +2.9% | -116 to 132 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.216 | +2.9% | -0.0868 to 0.0992 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.3 to 6.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,696 | 5,697 | +0.0% | -25.7 to 27 | no difference beyond the noise |
| throughput (operations a second) | 5,711 | 5,711 | +0.0% | -26.4 to 26.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.433 | -1.1% | -0.0212 to 0.0119 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.635 | 0.629 | -1.0% | -0.0188 to 0.00617 | no difference beyond the noise |
| latency, mean (ms) | 0.254 | 0.251 | -1.2% | -0.0134 to 0.00745 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -80.1 to -56 | better |
| bytes in the cache, mean (MB) | 417 | 364 | -12.8% | -59.7 to -47.3 | better |
| pages read into the cache (misses) | 677,539 | 785,502 | +15.9% | 76,489 to 139,436 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% | -0.0195 to 0.0171 | no difference beyond the noise |
| host CPU-seconds | 473 | 471 | -0.4% | -45.2 to 41.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.178 | -0.5% | -0.0181 to 0.0162 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,882 | -0.2% | -24.2 to 10.8 | no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,891 | -0.2% | -25.2 to 11.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.366 | 0.365 | -0.3% | -0.001 to -0.001 | better |
| latency, 99th percentile (ms) | 0.613 | 0.61 | -0.5% | -0.0168 to 0.0108 | no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.225 | +0.2% | -0.00202 to 0.00311 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.3% | -64.8 to -60.8 | better |
| bytes in the cache, mean (MB) | 417 | 369 | -11.7% | -50.6 to -46.9 | better |
| pages read into the cache (misses) | 677,075 | 759,667 | +12.2% | 56,298 to 108,886 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.239 | +3.6% | -0.0677 to 0.0841 | no difference beyond the noise |
| host CPU-seconds | 400 | 417 | +4.4% | -156 to 192 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.314 | +4.6% | -0.119 to 0.147 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
