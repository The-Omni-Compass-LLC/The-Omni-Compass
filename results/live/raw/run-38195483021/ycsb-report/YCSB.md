# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,855 | 2,852 | -0.1% | -4.94 to -0.558 | **WORSE** |
| throughput (operations a second) | 2,862 | 2,860 | -0.1% | -6.06 to 2.85 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.397 | 0.399 | +0.5% | -0.0111 to 0.0151 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.581 | +2.2% | -0.0156 to 0.0409 | no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.218 | +0.8% | -0.00426 to 0.0079 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -5.18 to 0.189 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 414 | -0.3% | -8.79 to 6.37 | no difference beyond the noise |
| pages read into the cache (misses) | 477,208 | 490,120 | +2.7% | -26,830 to 52,652 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.221 | +0.7% | -0.019 to 0.0221 | no difference beyond the noise |
| host CPU-seconds | 251 | 253 | +0.6% | -26.9 to 30.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.285 | 0.287 | +0.7% | -0.0306 to 0.0345 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,849 | 2,851 | +0.1% | -3.19 to 6.68 | no difference beyond the noise |
| throughput (operations a second) | 2,859 | 2,860 | +0.0% | -2.57 to 4.39 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.456 | -2.6% | -0.043 to 0.0183 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.708 | 0.683 | -3.4% | -0.0797 to 0.031 | no difference beyond the noise |
| latency, mean (ms) | 0.239 | 0.236 | -1.2% | -0.0194 to 0.0135 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -5.68 to -5.68 | better |
| bytes in the cache, mean (MB) | 397 | 392 | -1.2% | -14.5 to 5.06 | no difference beyond the noise |
| pages read into the cache (misses) | 188,142 | 181,759 | -3.4% | -31,834 to 19,069 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.195 | -8.0% | -0.0701 to 0.0361 | no difference beyond the noise |
| host CPU-seconds | 97.1 | 87.7 | -9.7% | -38.1 to 19.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.249 | -9.7% | -0.109 to 0.0552 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,859 | 2,858 | -0.0% | -5.18 to 2.9 | no difference beyond the noise |
| throughput (operations a second) | 2,866 | 2,865 | -0.0% | -5.09 to 2.28 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.453 | 0.455 | +0.4% | -0.0129 to 0.0162 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.598 | -0.3% | -0.0144 to 0.0111 | no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.7% | -0.0099 to 0.0128 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -21.6 to 5.79 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 410 | -1.3% | -21.4 to 10.7 | no difference beyond the noise |
| pages read into the cache (misses) | 470,117 | 472,905 | +0.6% | -195,373 to 200,949 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.193 | -3.5% | -0.0383 to 0.0244 | no difference beyond the noise |
| host CPU-seconds | 229 | 219 | -4.6% | -54.6 to 33.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.248 | -4.6% | -0.0622 to 0.0385 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,582 | 5,565 | -0.3% | -73.7 to 38.5 | no difference beyond the noise |
| throughput (operations a second) | 5,601 | 5,584 | -0.3% | -72.9 to 39.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.455 | +1.0% | -0.0197 to 0.0291 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.685 | 0.695 | +1.5% | -0.0365 to 0.0565 | no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.261 | +0.8% | -0.0114 to 0.0157 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -14.8 to 2.88 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 409 | -1.1% | -11.6 to 2.37 | no difference beyond the noise |
| pages read into the cache (misses) | 455,571 | 466,323 | +2.4% | -11,283 to 32,788 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.318 | +2.8% | -0.0152 to 0.0327 | no difference beyond the noise |
| host CPU-seconds | 351 | 362 | +3.1% | -22.6 to 44.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.208 | +3.3% | -0.0149 to 0.0284 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -14.2 to 15.8 | no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,907 | +0.0% | -14 to 15.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.304 | +0.9% | -0.00737 to 0.0127 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.486 | +1.8% | -0.0137 to 0.0311 | no difference beyond the noise |
| latency, mean (ms) | 0.123 | 0.122 | -0.8% | -0.00788 to 0.00603 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -12.7 to 2.5 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 413 | -0.7% | -11.4 to 5.76 | no difference beyond the noise |
| pages read into the cache (misses) | 465,858 | 472,515 | +1.4% | -13,888 to 27,202 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.153 | -0.3% | -0.0261 to 0.0253 | no difference beyond the noise |
| host CPU-seconds | 185 | 184 | -0.6% | -40.2 to 38.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.207 | -0.6% | -0.0447 to 0.0421 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
