# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -5.65 to 3.73 | no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -4.81 to 2.42 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.205 | 0.198 | -3.4% | -0.0555 to 0.0415 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.365 | 0.349 | -4.5% | -0.0868 to 0.0542 | no difference beyond the noise |
| latency, mean (ms) | 0.0836 | 0.0822 | -1.7% | -0.00862 to 0.00569 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 468 | -8.6% | -136 to 48.5 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 422 | 384 | -9.0% | -104 to 28.8 | no difference beyond the noise |
| pages read into the cache (misses) | 726,999 | 774,427 | +6.5% | -163,393 to 258,250 | shown, not judged |
| host CPU busy (share of the run) | 0.0929 | 0.101 | +9.1% | -0.0159 to 0.0329 | no difference beyond the noise |
| host CPU-seconds | 167 | 184 | +10.3% | -32 to 66.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.138 | +10.3% | -0.0239 to 0.0496 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,921 | 2,920 | -0.0% | -2.16 to -0.308 | **WORSE** |
| throughput (operations a second) | 2,926 | 2,925 | -0.0% | -2.7 to 0.181 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.388 | 0.393 | +1.4% | -0.00471 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.547 | 0.553 | +1.2% | -0.0245 to 0.0372 | no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.156 | +0.8% | -0.000949 to 0.00333 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 461 | -10.0% | -83.6 to -19 | better |
| bytes in the cache, mean (MB) | 404 | 364 | -10.0% | -56.9 to -23.7 | better |
| pages read into the cache (misses) | 269,798 | 281,893 | +4.5% | -79,042 to 103,233 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.157 | -2.1% | -0.188 to 0.181 | no difference beyond the noise |
| host CPU-seconds | 120 | 116 | -3.0% | -163 to 156 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.218 | -3.0% | -0.305 to 0.292 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.97 to 7.97 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% | -4.73 to 2.11 | no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% | -4.55 to 1.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.31 | +0.1% | -0.018 to 0.0186 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.487 | +0.1% | -0.00346 to 0.00413 | no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.195 | +0.2% | -0.0105 to 0.0112 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.0% | -125 to 73.3 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 400 | -4.4% | -87.5 to 50.5 | no difference beyond the noise |
| pages read into the cache (misses) | 702,592 | 731,599 | +4.1% | -172,524 to 230,537 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.17 | +7.1% | -0.0187 to 0.0413 | no difference beyond the noise |
| host CPU-seconds | 266 | 289 | +8.6% | -34.7 to 80.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.217 | +8.6% | -0.026 to 0.0603 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,704 | 5,695 | -0.2% | -28.5 to 11.1 | no difference beyond the noise |
| throughput (operations a second) | 5,719 | 5,710 | -0.1% | -27.8 to 10.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.44 | 0.437 | -0.8% | -0.0127 to 0.00607 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.639 | -0.6% | -0.0083 to 0.000303 | no difference beyond the noise |
| latency, mean (ms) | 0.255 | 0.253 | -1.0% | -0.00894 to 0.00383 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.8% | -78.1 to -52.8 | better |
| bytes in the cache, mean (MB) | 417 | 366 | -12.1% | -58.8 to -42.4 | better |
| pages read into the cache (misses) | 679,843 | 779,882 | +14.7% | 80,783 to 119,297 | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.7% | -0.0248 to 0.0211 | no difference beyond the noise |
| host CPU-seconds | 476 | 473 | -0.7% | -54.8 to 48.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.178 | -0.6% | -0.02 to 0.0179 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,879 | -0.1% | -25.1 to 19.9 | no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,888 | -0.1% | -26 to 20.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.365 | 0.368 | +0.8% | 0.000516 to 0.00548 | **WORSE** |
| latency, 99th percentile (ms) | 0.549 | 0.548 | -0.2% | -0.00277 to 0.000101 | no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.225 | +1.4% | -0.000722 to 0.00683 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.2% | -62.5 to -62.5 | better |
| bytes in the cache, mean (MB) | 418 | 369 | -11.5% | -48.9 to -47.5 | better |
| pages read into the cache (misses) | 677,035 | 764,620 | +12.9% | 55,094 to 120,077 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.239 | -2.0% | -0.0584 to 0.0486 | no difference beyond the noise |
| host CPU-seconds | 424 | 411 | -3.2% | -131 to 104 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.32 | 0.31 | -3.1% | -0.099 to 0.079 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
