# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.1% | -4.53 to 1.02 | no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -4.67 to 0.599 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.328 | +2.8% | -0.00729 to 0.0253 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.559 | 0.561 | +0.4% | -0.0154 to 0.0194 | no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.202 | +1.5% | -0.00856 to 0.0146 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.2% | -63.5 to -61.7 | better |
| bytes in the cache, mean (MB) | 419 | 368 | -12.0% | -53.7 to -47 | better |
| pages read into the cache (misses) | 717,723 | 751,917 | +4.8% | -113,495 to 181,883 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.166 | -7.8% | -0.134 to 0.105 | no difference beyond the noise |
| host CPU-seconds | 309 | 279 | -9.7% | -271 to 211 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.21 | -9.7% | -0.204 to 0.159 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.0% | -2.29 to -0.211 | **WORSE** |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -1.52 to -1.07 | **WORSE** |
| latency, 95th percentile (ms) | 0.495 | 0.498 | +0.5% | -0.00392 to 0.00859 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.625 | 0.626 | +0.2% | -0.0033 to 0.0053 | no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.228 | +1.0% | 0.000899 to 0.00379 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 436 | -14.8% | -115 to -37 | better |
| bytes in the cache, mean (MB) | 402 | 341 | -15.2% | -97.2 to -25.1 | better |
| pages read into the cache (misses) | 266,113 | 286,450 | +7.6% | -30,281 to 70,955 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.161 | -9.5% | -0.187 to 0.153 | no difference beyond the noise |
| host CPU-seconds | 124 | 108 | -12.7% | -151 to 119 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.203 | -12.7% | -0.284 to 0.224 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,908 | -0.1% | -17.8 to 14.6 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -16.7 to 13.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.25 | +1.2% | -0.0121 to 0.0181 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.397 | +0.4% | -0.0173 to 0.0206 | no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.18 | -1.0% | -0.0298 to 0.0264 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -81.1 to -48.5 | better |
| bytes in the cache, mean (MB) | 416 | 365 | -12.2% | -76.1 to -25.6 | better |
| pages read into the cache (misses) | 695,640 | 792,270 | +13.9% | -35,179 to 228,441 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.146 | +0.1% | -0.0815 to 0.0818 | no difference beyond the noise |
| host CPU-seconds | 264 | 262 | -0.6% | -175 to 172 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.196 | -0.6% | -0.132 to 0.129 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,407 | 5,334 | -1.3% | -372 to 226 | no difference beyond the noise |
| throughput (operations a second) | 5,427 | 5,355 | -1.3% | -371 to 227 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.336 | +0.3% | -0.00148 to 0.00348 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.538 | 0.544 | +1.1% | -0.00846 to 0.0198 | no difference beyond the noise |
| latency, mean (ms) | 0.227 | 0.236 | +4.0% | 0.000268 to 0.0178 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 495 | -3.3% | -26.9 to -6.42 | better |
| bytes in the cache, mean (MB) | 413 | 399 | -3.6% | -22.6 to -6.85 | better |
| pages read into the cache (misses) | 644,615 | 658,622 | +2.2% | -55,797 to 83,811 | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.24 | +3.8% | -0.025 to 0.0426 | no difference beyond the noise |
| host CPU-seconds | 420 | 440 | +4.9% | -60.3 to 101 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.168 | 0.179 | +6.5% | -0.0275 to 0.0495 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,886 | -0.1% | -10.6 to 6.81 | no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,894 | -0.1% | -11.6 to 6.68 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.358 | -0.6% | -0.016 to 0.0113 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.554 | 0.548 | -1.1% | -0.0232 to 0.0112 | no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.22 | -1.0% | -0.0111 to 0.00645 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 458 | -10.5% | -90.7 to -17.2 | better |
| bytes in the cache, mean (MB) | 418 | 377 | -9.8% | -72.7 to -9.45 | better |
| pages read into the cache (misses) | 679,201 | 753,696 | +11.0% | 35,022 to 113,969 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.222 | -1.1% | -0.0488 to 0.0439 | no difference beyond the noise |
| host CPU-seconds | 382 | 377 | -1.4% | -100 to 89.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.288 | 0.283 | -1.4% | -0.0759 to 0.0677 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
