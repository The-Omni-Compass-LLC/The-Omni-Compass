# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,885 | +0.0% | -1.05 to 2.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,889 | +0.0% | -0.379 to 2.26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.333 | +0.1% | -0.0297 to 0.0304 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.507 | +0.3% | -0.0186 to 0.0219 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.192 | +0.6% | -0.00587 to 0.00809 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% | -4.03 to 4.15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,806 | 61,887 | +0.1% | -359 to 523 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.201 | -3.9% | -0.0264 to 0.01 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 352 | -5.0% | -63.9 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.265 | -5.0% | -0.0479 to 0.0201 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,894 | -0.2% | -14.2 to 1.96 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,908 | -0.1% | -13.4 to 5.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.32 | +3.6% | -0.024 to 0.046 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.508 | +6.6% | -0.00604 to 0.0687 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.163 | 0.176 | +8.0% | -0.0158 to 0.0417 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,514 | 1,505 | -0.6% | -31.7 to 13.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,673 | 77,723 | +0.1% | -489 to 590 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.163 | +13.0% | -0.0509 to 0.0884 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 119 | +15.5% | -45.4 to 77.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.194 | 0.224 | +15.6% | -0.0849 to 0.146 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -2.57 to 2.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | -0.0% | -2.43 to 1.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.296 | 0.301 | +1.7% | -0.0174 to 0.0274 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.58 | 0.581 | +0.1% | -0.02 to 0.0214 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.187 | +0.7% | -0.00304 to 0.00561 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | -0.0% | -2.9 to 1.89 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,671 | 61,635 | -0.1% | -206 to 133 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.171 | -4.1% | -0.0277 to 0.0131 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 293 | -5.1% | -57.8 to 26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.22 | -5.1% | -0.0433 to 0.0194 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,754 | 5,758 | +0.1% | -2.39 to 11.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,771 | +0.1% | -1.87 to 11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.331 | +0.3% | -0.0033 to 0.0053 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.6 | +0.3% | -0.0108 to 0.0142 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.155 | -0.7% | -0.00518 to 0.00302 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,361 | -0.1% | -5.71 to 3.42 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,013 | 63,144 | +0.2% | -956 to 1,217 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.22 | -5.0% | -0.0216 to -0.00135 | GAIN |
| host CPU-seconds | 430 | 403 | -6.4% | -51.4 to -3.56 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.151 | -6.4% | -0.0193 to -0.00152 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | -0.0% | -3.98 to 3.63 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | -0.0% | -3.81 to 3.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.346 | +2.3% | -0.00407 to 0.0194 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.529 | 0.531 | +0.4% | -0.00484 to 0.00951 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.206 | +0.4% | -0.00302 to 0.00474 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -3.24 to 0.942 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,141 | 63,460 | +0.5% | -1,011 to 1,648 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.214 | -11.0% | -0.091 to 0.0382 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 367 | -14.4% | -212 to 88.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.322 | 0.276 | -14.4% | -0.159 to 0.066 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
