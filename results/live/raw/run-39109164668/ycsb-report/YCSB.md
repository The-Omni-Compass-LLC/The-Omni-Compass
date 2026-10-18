# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% | -2.05 to -0.384 | LOSS |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% | -1.74 to -0.245 | LOSS |
| latency, 95th percentile (ms) | 0.322 | 0.326 | +1.2% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.478 | 0.483 | +1.0% | -0.00742 to 0.0174 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.201 | +0.4% | -0.00485 to 0.00652 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.67 to -3.23 | GAIN |
| bytes in the cache, mean (MB) | 419 | 415 | -0.8% | -9.86 to 3.43 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 709,938 | 704,361 | -0.8% | -150,345 to 139,191 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.162 | -9.0% | -0.0485 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 270 | -10.9% | -105 to 38.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.202 | -10.9% | -0.0786 to 0.0289 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,888 | -0.1% | -3.02 to 0.113 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -2.54 to -0.214 | LOSS |
| latency, 95th percentile (ms) | 0.436 | 0.435 | -0.2% | -0.0053 to 0.0033 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.601 | +0.3% | -0.0173 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.222 | +0.1% | -0.00898 to 0.0094 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -12.6 to -4.89 | GAIN |
| bytes in the cache, mean (MB) | 404 | 399 | -1.2% | -23 to 13.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 269,691 | 264,617 | -1.9% | -32,549 to 22,400 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.161 | -6.2% | -0.12 to 0.0989 | EVEN, no difference beyond the noise |
| host CPU-seconds | 117 | 107 | -8.3% | -99.7 to 80.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.202 | -8.3% | -0.187 to 0.151 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -1.05 to 0.861 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -1.18 to 0.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.315 | +0.4% | -0.0044 to 0.00707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.485 | -1.2% | -0.0206 to 0.00931 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.197 | +1.2% | -0.00186 to 0.00643 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -76.6 to 41.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 401 | -4.5% | -70.9 to 33.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 744,406 | 693,091 | -6.9% | -155,421 to 52,793 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.183 | +12.7% | 0.0067 to 0.0346 | power given |
| host CPU-seconds | 273 | 314 | +15.1% | 13.4 to 69.1 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.236 | +15.1% | 0.00994 to 0.0519 | power given |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,644 | 5,662 | +0.3% | -7.41 to 43.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,665 | 5,682 | +0.3% | -8.91 to 43.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.455 | 0.453 | -0.4% | -0.0183 to 0.0143 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.729 | 0.718 | -1.6% | -0.0217 to -0.00099 | GAIN |
| latency, mean (ms) | 0.258 | 0.258 | +0.1% | -0.0102 to 0.0107 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -6.2 to -1.25 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.5% | -5.49 to 1.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 671,319 | 679,345 | +1.2% | -17,527 to 33,579 | shown, not judged |
| host CPU busy (share of the run) | 0.287 | 0.292 | +1.6% | -0.0199 to 0.029 | EVEN, no difference beyond the noise |
| host CPU-seconds | 487 | 498 | +2.1% | -38.4 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.189 | +1.7% | -0.0148 to 0.0212 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,878 | -0.2% | -21.2 to 6.78 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,887 | -0.3% | -21.1 to 6.03 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.367 | 0.364 | -0.9% | -0.0199 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.567 | 0.561 | -1.1% | -0.0394 to 0.0274 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.225 | -0.3% | -0.0149 to 0.0133 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.5% | -18 to 3.05 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -0.9% | -10.9 to 3.33 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,242 | 688,688 | +1.2% | -16,144 to 33,035 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.23 | -6.6% | -0.0661 to 0.0335 | EVEN, no difference beyond the noise |
| host CPU-seconds | 429 | 393 | -8.4% | -155 to 82.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.323 | 0.297 | -8.2% | -0.117 to 0.0636 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
