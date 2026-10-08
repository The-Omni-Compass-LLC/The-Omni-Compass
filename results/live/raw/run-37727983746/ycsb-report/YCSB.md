# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,858 | +0.0% | -3.7 to 3.72 | no difference beyond the noise |
| throughput (operations a second) | 2,863 | 2,863 | -0.0% | -2.91 to 2.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.407 | 0.403 | -1.1% | -0.0147 to 0.00537 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.542 | -1.4% | -0.0277 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.216 | +0.5% | -0.0109 to 0.0131 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 259 | -49.5% | -253 to -253 | better |
| bytes in the cache, mean (MB) | 418 | 214 | -48.7% | -215 to -192 | better |
| pages read into the cache (misses) | 486,224 | 712,413 | +46.5% | 213,039 to 239,338 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.204 | -3.8% | -0.087 to 0.0707 | no difference beyond the noise |
| host CPU-seconds | 241 | 229 | -5.0% | -121 to 97.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.259 | -5.0% | -0.138 to 0.11 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,864 | -0.1% | -10.8 to 5.87 | no difference beyond the noise |
| throughput (operations a second) | 2,874 | 2,872 | -0.1% | -11.2 to 6.85 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.491 | 0.494 | +0.7% | -0.00184 to 0.0085 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.701 | 0.704 | +0.3% | -0.00771 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.216 | +3.7% | 0.00475 to 0.0105 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 304 | -40.6% | -385 to -31.4 | better |
| bytes in the cache, mean (MB) | 397 | 244 | -38.6% | -296 to -10.6 | better |
| pages read into the cache (misses) | 179,920 | 261,693 | +45.5% | -13,021 to 176,568 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.229 | +16.4% | -0.0216 to 0.086 | no difference beyond the noise |
| host CPU-seconds | 94.4 | 114 | +20.6% | -14.7 to 53.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.323 | +20.7% | -0.0418 to 0.152 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,861 | 2,861 | +0.0% | -17.9 to 18.7 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,865 | +0.0% | -17.1 to 17.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.392 | 0.391 | -0.2% | -0.0196 to 0.0183 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.503 | -0.3% | -0.0451 to 0.0417 | no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.211 | +3.2% | -0.0097 to 0.0226 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 259 | -49.5% | -253 to -253 | better |
| bytes in the cache, mean (MB) | 415 | 216 | -48.0% | -209 to -189 | better |
| pages read into the cache (misses) | 456,407 | 719,563 | +57.7% | 210,652 to 315,661 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.215 | +10.7% | -0.00527 to 0.0469 | no difference beyond the noise |
| host CPU-seconds | 219 | 247 | +12.8% | -8.16 to 64.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.28 | +12.8% | -0.00898 to 0.0725 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,108 | 4,970 | -2.7% | -499 to 224 | no difference beyond the noise |
| throughput (operations a second) | 5,131 | 4,993 | -2.7% | -497 to 220 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.362 | +0.6% | -0.000535 to 0.0052 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.61 | 0.609 | -0.1% | -0.0441 to 0.0428 | no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.257 | +4.5% | -0.00804 to 0.0303 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 379 | -25.9% | -156 to -110 | better |
| bytes in the cache, mean (MB) | 409 | 309 | -24.4% | -117 to -83 | better |
| pages read into the cache (misses) | 415,673 | 521,046 | +25.3% | 7,115 to 203,631 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.24 | -7.5% | -0.0308 to -0.00823 | better |
| host CPU-seconds | 319 | 290 | -9.1% | -43.5 to -14.4 | better |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.188 | -6.6% | -0.029 to 0.00223 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,894 | +0.1% | -0.855 to 4.56 | no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,903 | +0.1% | 0.432 to 3.93 | better |
| latency, 95th percentile (ms) | 0.372 | 0.377 | +1.2% | -0.0106 to 0.0193 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.556 | 0.562 | +1.0% | -0.00471 to 0.0154 | no difference beyond the noise |
| latency, mean (ms) | 0.16 | 0.163 | +1.9% | -0.000367 to 0.00634 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -63.8 to -63.8 | better |
| bytes in the cache, mean (MB) | 416 | 367 | -11.7% | -51.3 to -46.3 | better |
| pages read into the cache (misses) | 464,965 | 511,410 | +10.0% | 40,823 to 52,067 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.205 | +2.7% | -0.114 to 0.124 | no difference beyond the noise |
| host CPU-seconds | 246 | 254 | +3.3% | -174 to 190 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.287 | +3.3% | -0.197 to 0.215 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
