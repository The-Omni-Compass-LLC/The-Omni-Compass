# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,856 | -0.1% | -7.07 to 3.29 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,862 | -0.1% | -6.68 to 2.72 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.406 | 0.406 | -0.1% | -0.00607 to 0.0054 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.565 | -0.5% | -0.0401 to 0.0341 | no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.215 | +1.1% | -0.00283 to 0.00757 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -231 to -55.5 | better |
| bytes in the cache, mean (MB) | 415 | 302 | -27.2% | -189 to -37 | better |
| pages read into the cache (misses) | 488,743 | 613,152 | +25.5% | 26,796 to 222,021 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.213 | +1.0% | -0.0356 to 0.0397 | no difference beyond the noise |
| host CPU-seconds | 241 | 242 | +0.7% | -51.4 to 54.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.275 | +0.7% | -0.0583 to 0.062 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,611 | 2,737 | +4.8% | -373 to 625 | no difference beyond the noise |
| throughput (operations a second) | 2,625 | 2,747 | +4.6% | -365 to 609 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.346 | -0.2% | -0.0321 to 0.0308 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.629 | 0.549 | -12.7% | -0.328 to 0.168 | no difference beyond the noise |
| latency, mean (ms) | 0.252 | 0.231 | -8.2% | -0.0902 to 0.0487 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 404 | -21.0% | -123 to -91.6 | better |
| bytes in the cache, mean (MB) | 387 | 305 | -21.2% | -112 to -52.1 | better |
| pages read into the cache (misses) | 178,538 | 200,667 | +12.4% | -46,169 to 90,427 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.183 | +7.0% | -0.0846 to 0.109 | no difference beyond the noise |
| host CPU-seconds | 83.7 | 89.7 | +7.2% | -49.2 to 61.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.268 | +3.0% | -0.127 to 0.143 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,898 | -0.0% | -4.69 to 2.3 | no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.0% | -4.79 to 2.29 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.278 | 0.281 | +0.8% | -0.0191 to 0.0238 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.426 | 0.425 | -0.2% | -0.0118 to 0.00983 | no difference beyond the noise |
| latency, mean (ms) | 0.107 | 0.11 | +2.3% | 0.000923 to 0.00408 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -124 to -122 | better |
| bytes in the cache, mean (MB) | 416 | 320 | -23.2% | -106 to -87.4 | better |
| pages read into the cache (misses) | 466,300 | 583,886 | +25.2% | 55,859 to 179,313 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.146 | +1.5% | -0.0573 to 0.0616 | no difference beyond the noise |
| host CPU-seconds | 176 | 179 | +1.4% | -82.6 to 87.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.201 | +1.4% | -0.0931 to 0.0986 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,656 | 5,601 | -1.0% | -238 to 128 | no difference beyond the noise |
| throughput (operations a second) | 5,675 | 5,618 | -1.0% | -233 to 120 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.347 | +0.8% | -0.0101 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.546 | -0.8% | -0.0508 to 0.0415 | no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.214 | +1.7% | -0.00491 to 0.0121 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 328 | -35.9% | -186 to -182 | better |
| bytes in the cache, mean (MB) | 413 | 266 | -35.6% | -154 to -141 | better |
| pages read into the cache (misses) | 472,245 | 674,851 | +42.9% | 146,641 to 258,570 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.275 | +2.6% | -0.0278 to 0.0417 | no difference beyond the noise |
| host CPU-seconds | 326 | 337 | +3.4% | -52.3 to 74.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.194 | +4.4% | -0.022 to 0.0384 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | -0.0% | -4.79 to 3.78 | no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,886 | -0.1% | -6.22 to 3.19 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.334 | +0.3% | -0.00557 to 0.00757 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.486 | 0.482 | -0.9% | -0.0161 to 0.00741 | no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.186 | -1.1% | -0.0121 to 0.00782 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -124 to -122 | better |
| bytes in the cache, mean (MB) | 415 | 318 | -23.4% | -104 to -90.4 | better |
| pages read into the cache (misses) | 464,294 | 577,605 | +24.4% | 75,637 to 150,983 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.218 | -5.0% | -0.0427 to 0.0198 | no difference beyond the noise |
| host CPU-seconds | 283 | 264 | -6.6% | -72.4 to 34.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.321 | 0.299 | -6.6% | -0.0822 to 0.0398 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
