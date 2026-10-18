# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | -0.0% | -3.13 to 2.48 | no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,907 | -0.0% | -2.98 to 0.267 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.276 | 0.279 | +1.1% | -0.00197 to 0.00797 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.447 | 0.445 | -0.3% | -0.0524 to 0.0497 | no difference beyond the noise |
| latency, mean (ms) | 0.101 | 0.103 | +2.1% | -0.00264 to 0.00676 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 328 | -35.9% | -184 to -184 | better |
| bytes in the cache, mean (MB) | 420 | 268 | -36.2% | -164 to -139 | better |
| pages read into the cache (misses) | 504,732 | 667,884 | +32.3% | 96,428 to 229,878 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.139 | +0.9% | -0.0808 to 0.0833 | no difference beyond the noise |
| host CPU-seconds | 169 | 170 | +0.5% | -115 to 117 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.19 | 0.191 | +0.5% | -0.129 to 0.131 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,847 | 2,846 | -0.0% | -9.65 to 8.17 | no difference beyond the noise |
| throughput (operations a second) | 2,857 | 2,856 | -0.0% | -9.19 to 7.78 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.453 | 0.454 | +0.1% | -0.00907 to 0.00974 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.674 | 0.669 | -0.8% | -0.0452 to 0.0345 | no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.245 | +1.4% | -0.00525 to 0.0118 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 397 | -22.4% | -116 to -113 | better |
| bytes in the cache, mean (MB) | 395 | 310 | -21.5% | -91.8 to -78.4 | better |
| pages read into the cache (misses) | 178,096 | 216,574 | +21.6% | 22,958 to 53,997 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.224 | +3.6% | -0.066 to 0.0815 | no difference beyond the noise |
| host CPU-seconds | 98.4 | 103 | +4.3% | -37.5 to 46 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.292 | +4.3% | -0.107 to 0.131 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,862 | 2,862 | -0.0% | -3.31 to 2.15 | no difference beyond the noise |
| throughput (operations a second) | 2,866 | 2,866 | -0.0% | -3.04 to 1.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.387 | 0.39 | +0.6% | -0.00146 to 0.00613 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.508 | +0.5% | -0.0139 to 0.0192 | no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.207 | +2.3% | 0.00335 to 0.00574 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -124 to -122 | better |
| bytes in the cache, mean (MB) | 415 | 320 | -22.8% | -101 to -88.5 | better |
| pages read into the cache (misses) | 454,017 | 588,209 | +29.6% | 102,327 to 166,057 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.212 | +7.6% | -0.0557 to 0.0855 | no difference beyond the noise |
| host CPU-seconds | 224 | 244 | +8.8% | -81.9 to 121 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.254 | 0.276 | +8.8% | -0.0927 to 0.137 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,546 | 5,536 | -0.2% | -89 to 69.3 | no difference beyond the noise |
| throughput (operations a second) | 5,566 | 5,555 | -0.2% | -87.8 to 66 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.458 | 0.462 | +0.9% | -0.0115 to 0.0195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.698 | 0.695 | -0.4% | -0.0325 to 0.0272 | no difference beyond the noise |
| latency, mean (ms) | 0.264 | 0.266 | +0.5% | -0.0076 to 0.0105 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -231 to -55.1 | better |
| bytes in the cache, mean (MB) | 415 | 299 | -28.0% | -187 to -45 | better |
| pages read into the cache (misses) | 456,254 | 617,406 | +35.3% | 40,550 to 281,754 | shown, not judged |
| host CPU busy (share of the run) | 0.316 | 0.32 | +1.3% | -0.00761 to 0.0156 | no difference beyond the noise |
| host CPU-seconds | 361 | 364 | +0.9% | -15.5 to 21.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.211 | +0.9% | -0.00575 to 0.00958 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,841 | 2,837 | -0.1% | -11.1 to 2.93 | no difference beyond the noise |
| throughput (operations a second) | 2,852 | 2,848 | -0.2% | -11.8 to 2.73 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.426 | +2.0% | -0.0106 to 0.0273 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.631 | +1.5% | -0.0245 to 0.0432 | no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.236 | +2.2% | -0.0089 to 0.0192 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 409 | -20.0% | -189 to -16.1 | better |
| bytes in the cache, mean (MB) | 415 | 335 | -19.3% | -150 to -9.92 | better |
| pages read into the cache (misses) | 458,125 | 569,667 | +24.3% | 32,940 to 190,144 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.27 | +7.0% | -0.0197 to 0.055 | no difference beyond the noise |
| host CPU-seconds | 287 | 313 | +8.8% | -30 to 80.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.328 | 0.357 | +8.9% | -0.0337 to 0.0918 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
