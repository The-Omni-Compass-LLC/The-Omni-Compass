# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,907 | +0.0% | -10.5 to 12.8 | no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | -0.0% | -7.7 to 7.52 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.277 | 0.273 | -1.3% | -0.00992 to 0.00259 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.447 | 0.424 | -5.2% | -0.0581 to 0.0115 | no difference beyond the noise |
| latency, mean (ms) | 0.102 | 0.0995 | -2.4% | -0.00908 to 0.00416 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -231 to -55.6 | better |
| bytes in the cache, mean (MB) | 416 | 303 | -27.3% | -184 to -43.6 | better |
| pages read into the cache (misses) | 480,944 | 593,742 | +23.5% | -13,086 to 238,681 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.121 | -2.4% | -0.0684 to 0.0624 | no difference beyond the noise |
| host CPU-seconds | 150 | 146 | -2.5% | -93.9 to 86.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.169 | 0.164 | -2.5% | -0.105 to 0.0969 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,859 | 2,860 | +0.0% | -4.91 to 6.96 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,865 | +0.0% | -4.13 to 6.12 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.402 | 0.403 | +0.2% | -0.0033 to 0.0053 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.566 | -0.3% | -0.0253 to 0.0219 | no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.227 | +1.1% | -0.00639 to 0.0113 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 378 | -26.2% | -215 to -52.6 | better |
| bytes in the cache, mean (MB) | 401 | 294 | -26.6% | -178 to -35.8 | better |
| pages read into the cache (misses) | 183,243 | 223,388 | +21.9% | 19,101 to 61,189 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.195 | -11.9% | -0.0781 to 0.0257 | no difference beyond the noise |
| host CPU-seconds | 103 | 87.5 | -15.0% | -45.4 to 14.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.292 | 0.248 | -15.0% | -0.129 to 0.0415 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,856 | -0.1% | -5.88 to 2.29 | no difference beyond the noise |
| throughput (operations a second) | 2,865 | 2,863 | -0.1% | -6.86 to 3.71 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.464 | 0.464 | -0.1% | -0.0032 to 0.00254 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.609 | 0.61 | +0.2% | -0.0121 to 0.0141 | no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.217 | +1.1% | -0.00321 to 0.00781 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -123 to -123 | better |
| bytes in the cache, mean (MB) | 412 | 320 | -22.3% | -100 to -83 | better |
| pages read into the cache (misses) | 478,884 | 615,567 | +28.5% | 7,299 to 266,068 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.195 | -4.3% | -0.0586 to 0.0408 | no difference beyond the noise |
| host CPU-seconds | 234 | 220 | -5.9% | -85.5 to 57.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.265 | 0.249 | -5.9% | -0.0969 to 0.0655 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,769 | 5,760 | -0.1% | -26.1 to 8.95 | no difference beyond the noise |
| throughput (operations a second) | 5,783 | 5,772 | -0.2% | -32.6 to 12 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.264 | 0.262 | -0.6% | -0.00454 to 0.0012 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.454 | -3.5% | -0.0516 to 0.0189 | no difference beyond the noise |
| latency, mean (ms) | 0.12 | 0.12 | +0.2% | -0.00704 to 0.00757 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 327 | -36.1% | -186 to -183 | better |
| bytes in the cache, mean (MB) | 417 | 266 | -36.2% | -152 to -150 | better |
| pages read into the cache (misses) | 476,953 | 686,067 | +43.8% | 182,801 to 235,428 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.169 | +2.1% | -0.0616 to 0.0685 | no difference beyond the noise |
| host CPU-seconds | 199 | 203 | +2.0% | -90.4 to 98.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.112 | 0.114 | +2.0% | -0.0507 to 0.0553 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,840 | 2,839 | -0.0% | -34.2 to 33.4 | no difference beyond the noise |
| throughput (operations a second) | 2,849 | 2,848 | -0.1% | -35.8 to 32.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.383 | 0.385 | +0.7% | -0.0025 to 0.00784 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.579 | 0.57 | -1.6% | -0.028 to 0.00931 | no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.223 | +0.9% | -0.00354 to 0.00773 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 399 | -22.1% | -155 to -71.6 | better |
| bytes in the cache, mean (MB) | 415 | 327 | -21.2% | -121 to -54.8 | better |
| pages read into the cache (misses) | 454,820 | 570,978 | +25.5% | 63,355 to 168,961 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.28 | -1.0% | -0.0426 to 0.037 | no difference beyond the noise |
| host CPU-seconds | 341 | 335 | -1.7% | -70.3 to 58.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.389 | 0.383 | -1.8% | -0.0846 to 0.0709 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
