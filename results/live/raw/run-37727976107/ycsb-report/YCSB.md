# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,874 | -0.1% | -5.43 to 2.38 | no difference beyond the noise |
| throughput (operations a second) | 2,879 | 2,877 | -0.1% | -5.2 to 2.26 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.359 | 0.361 | +0.4% | -0.00807 to 0.0107 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.522 | +0.8% | -0.0139 to 0.0219 | no difference beyond the noise |
| latency, mean (ms) | 0.168 | 0.175 | +4.2% | 0.00111 to 0.0129 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 261 | -49.0% | -262 to -240 | better |
| bytes in the cache, mean (MB) | 416 | 218 | -47.6% | -206 to -190 | better |
| pages read into the cache (misses) | 477,661 | 719,280 | +50.6% | 204,886 to 278,350 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.222 | +9.2% | -0.00307 to 0.0403 | no difference beyond the noise |
| host CPU-seconds | 247 | 274 | +11.1% | -10.8 to 65.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.31 | +11.1% | -0.012 to 0.0742 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,849 | 2,846 | -0.1% | -10.2 to 4.18 | no difference beyond the noise |
| throughput (operations a second) | 2,859 | 2,856 | -0.1% | -10.1 to 4.52 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.449 | 0.456 | +1.6% | -0.00438 to 0.0184 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.672 | 0.682 | +1.5% | -0.018 to 0.038 | no difference beyond the noise |
| latency, mean (ms) | 0.244 | 0.25 | +2.7% | 0.0019 to 0.0115 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 298 | -41.8% | -365 to -63.2 | better |
| bytes in the cache, mean (MB) | 397 | 238 | -40.0% | -282 to -36 | better |
| pages read into the cache (misses) | 176,149 | 264,188 | +50.0% | 22,857 to 153,222 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.218 | +4.8% | -0.0857 to 0.106 | no difference beyond the noise |
| host CPU-seconds | 93.8 | 98.6 | +5.1% | -49.2 to 58.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.28 | +5.1% | -0.14 to 0.167 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,912 | -0.1% | -6.86 to 1.17 | no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,915 | -0.1% | -5.53 to -0.166 | **WORSE** |
| latency, 95th percentile (ms) | 0.254 | 0.256 | +1.1% | -0.00113 to 0.00646 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.392 | +0.9% | -0.01 to 0.0173 | no difference beyond the noise |
| latency, mean (ms) | 0.0843 | 0.088 | +4.4% | -0.00241 to 0.00984 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 258 | -49.6% | -254 to -253 | better |
| bytes in the cache, mean (MB) | 418 | 217 | -48.1% | -210 to -192 | better |
| pages read into the cache (misses) | 472,121 | 721,837 | +52.9% | 141,280 to 358,151 | shown, not judged |
| host CPU busy (share of the run) | 0.0958 | 0.106 | +11.0% | -0.0172 to 0.0383 | no difference beyond the noise |
| host CPU-seconds | 115 | 128 | +11.6% | -22.7 to 49.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.129 | 0.144 | +11.7% | -0.0256 to 0.0557 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,551 | 5,535 | -0.3% | -81.6 to 49.6 | no difference beyond the noise |
| throughput (operations a second) | 5,570 | 5,552 | -0.3% | -82.6 to 46.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.462 | 0.467 | +1.0% | 0.000872 to 0.00846 | **WORSE** |
| latency, 99th percentile (ms) | 0.7 | 0.695 | -0.7% | -0.0222 to 0.0122 | no difference beyond the noise |
| latency, mean (ms) | 0.266 | 0.268 | +1.0% | -0.000971 to 0.00613 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 324 | -36.8% | -263 to -114 | better |
| bytes in the cache, mean (MB) | 415 | 263 | -36.6% | -215 to -88.8 | better |
| pages read into the cache (misses) | 456,436 | 677,907 | +48.5% | 127,032 to 315,911 | shown, not judged |
| host CPU busy (share of the run) | 0.32 | 0.318 | -0.6% | -0.0138 to 0.0101 | no difference beyond the noise |
| host CPU-seconds | 364 | 361 | -0.9% | -21.3 to 14.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.209 | -0.7% | -0.0111 to 0.00834 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,812 | 2,809 | -0.1% | -7.77 to 1.57 | no difference beyond the noise |
| throughput (operations a second) | 2,841 | 2,841 | -0.0% | -7.07 to 6.95 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.483 | 0.497 | +2.8% | -0.0187 to 0.046 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.967 | 1.02 | +5.0% | -0.0354 to 0.133 | no difference beyond the noise |
| latency, mean (ms) | 0.258 | 0.264 | +2.4% | 0.000383 to 0.0119 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 434 | -15.3% | -142 to -15.3 | better |
| bytes in the cache, mean (MB) | 415 | 356 | -14.4% | -108 to -11.4 | better |
| pages read into the cache (misses) | 457,429 | 533,039 | +16.5% | 5,712 to 145,509 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.286 | +3.2% | -0.0323 to 0.0499 | no difference beyond the noise |
| host CPU-seconds | 319 | 330 | +3.5% | -51.5 to 73.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.367 | 0.38 | +3.6% | -0.0589 to 0.0853 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
