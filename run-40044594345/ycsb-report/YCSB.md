# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,882 | -0.1% | -8.88 to 3.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,887 | -0.1% | -7.96 to 3.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.351 | +2.7% | -0.0331 to 0.0518 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.542 | +2.8% | -0.0287 to 0.0581 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.202 | +1.6% | -0.00953 to 0.0159 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.72 to -1.33 | GAIN |
| bytes in the cache, mean (MB) | 418 | 414 | -1.0% | -17 to 8.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 711,102 | 695,745 | -2.2% | -162,128 to 131,415 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.211 | +9.1% | -0.0387 to 0.0739 | EVEN, no difference beyond the noise |
| host CPU-seconds | 333 | 369 | +10.9% | -87 to 159 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.277 | +10.9% | -0.0653 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% | -5.56 to 3.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -3.54 to 2.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.456 | 0.46 | +0.9% | -0.000303 to 0.0083 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.646 | +1.3% | -0.0498 to 0.0658 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.219 | +1.5% | -0.00103 to 0.00746 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -22.2 to -1.98 | GAIN |
| bytes in the cache, mean (MB) | 402 | 393 | -2.2% | -20.7 to 2.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 268,572 | 266,937 | -0.6% | -29,058 to 25,788 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.186 | -5.6% | -0.055 to 0.033 | EVEN, no difference beyond the noise |
| host CPU-seconds | 138 | 128 | -6.8% | -45.7 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.241 | -6.8% | -0.0859 to 0.0506 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.1% | -6.07 to 2.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -5.64 to 2.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.314 | +1.0% | -0.00357 to 0.00957 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.505 | +2.2% | -0.00451 to 0.0265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.193 | +1.0% | -0.00413 to 0.00811 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -4.35 to -0.553 | GAIN |
| bytes in the cache, mean (MB) | 419 | 421 | +0.4% | -12.9 to 16.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 702,811 | 703,372 | +0.1% | -33,402 to 34,526 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.206 | +13.9% | -0.00687 to 0.0571 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 364 | +17.1% | -19.1 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.273 | +17.1% | -0.0142 to 0.094 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,690 | 5,746 | +1.0% | -190 to 302 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,706 | 5,762 | +1.0% | -191 to 303 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.314 | +0.1% | -0.00254 to 0.0032 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.479 | 0.479 | +0.1% | -0.018 to 0.0193 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.186 | -2.9% | -0.0149 to 0.00383 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.44 to 0.0871 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 415 | -0.2% | -3.56 to 2.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,612 | 700,461 | +2.5% | -57,895 to 91,591 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.237 | +4.7% | -0.0285 to 0.0497 | EVEN, no difference beyond the noise |
| host CPU-seconds | 404 | 428 | +5.9% | -62.2 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.153 | 0.16 | +4.7% | -0.0202 to 0.0347 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,864 | 2,860 | -0.1% | -9.78 to 2.03 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,875 | 2,871 | -0.1% | -11.4 to 3.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.395 | 0.394 | -0.3% | -0.0114 to 0.00871 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.635 | -1.3% | -0.0464 to 0.0297 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.238 | 0.236 | -0.6% | -0.00814 to 0.00551 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.86 to -1.82 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -6.16 to 1.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 681,750 | 679,668 | -0.3% | -10,514 to 6,350 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.286 | +2.0% | -0.0303 to 0.0415 | EVEN, no difference beyond the noise |
| host CPU-seconds | 492 | 507 | +2.9% | -77.7 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.372 | 0.383 | +2.9% | -0.0592 to 0.0811 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
