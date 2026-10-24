# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -6.54 to 1.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,887 | -0.1% | -4.83 to 0.945 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.347 | -0.3% | -0.0184 to 0.0164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.523 | 0.524 | +0.2% | -0.0365 to 0.0385 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.201 | +0.1% | -0.00554 to 0.00594 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.93 to -0.456 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -13.6 to 11.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,387 | 712,642 | +1.9% | -139,259 to 165,769 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.193 | -2.3% | -0.0754 to 0.0662 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 332 | -2.7% | -158 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.25 | -2.7% | -0.119 to 0.105 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,880 | -0.0% | -3.54 to 3.09 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% | -3.65 to 3.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.432 | 0.433 | +0.2% | -0.0189 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.592 | 0.599 | +1.1% | -0.0157 to 0.0291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.214 | +0.3% | -0.00534 to 0.00676 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.5% | -8.49 to -6.5 | GAIN |
| bytes in the cache, mean (MB) | 398 | 400 | +0.4% | -11.5 to 14.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,638 | 271,026 | +2.8% | -14,595 to 29,371 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.19 | -13.9% | -0.101 to 0.0396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 131 | -17.7% | -92.6 to 36.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.299 | 0.246 | -17.7% | -0.174 to 0.068 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,914 | 2,912 | -0.1% | -2.84 to -0.376 | LOSS |
| throughput (operations a second) | 2,917 | 2,915 | -0.1% | -3.21 to 0.0732 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.185 | 0.186 | +0.4% | -0.000768 to 0.0021 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.361 | 0.362 | +0.2% | -0.0168 to 0.0181 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.134 | 0.133 | -0.3% | -0.00389 to 0.00307 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.45 to -1.65 | GAIN |
| bytes in the cache, mean (MB) | 420 | 421 | +0.3% | -4.19 to 7.01 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,906 | 707,350 | +1.1% | -79,193 to 94,081 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.144 | -11.6% | -0.113 to 0.0758 | EVEN, no difference beyond the noise |
| host CPU-seconds | 297 | 257 | -13.4% | -245 to 165 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.193 | -13.5% | -0.183 to 0.123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,687 | 5,679 | -0.1% | -23.9 to 7.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,704 | 5,695 | -0.2% | -22.7 to 5.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.425 | +0.7% | -0.00991 to 0.0159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.642 | +0.2% | -0.0162 to 0.0182 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.243 | +0.4% | -0.00696 to 0.00897 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.36 to -0.0527 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.3% | -1.34 to -0.907 | GAIN |
| pages read into the cache (misses) | 681,978 | 685,733 | +0.6% | -4,913 to 12,423 | shown, not judged |
| host CPU busy (share of the run) | 0.321 | 0.322 | +0.4% | -0.00885 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 578 | 581 | +0.5% | -18.2 to 24.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.219 | +0.6% | -0.00646 to 0.00903 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,931 | -0.1% | -9.44 to 4.95 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,935 | -0.1% | -7.24 to 3.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.156 | 0.169 | +8.6% | 0.00574 to 0.0209 | LOSS |
| latency, 99th percentile (ms) | 0.375 | 0.391 | +4.2% | -0.000875 to 0.0322 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0818 | 0.0835 | +2.0% | -0.00402 to 0.00734 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -5.91 to -1.48 | GAIN |
| bytes in the cache, mean (MB) | 419 | 418 | -0.3% | -4.65 to 2.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 693,867 | 689,096 | -0.7% | -38,902 to 29,359 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.114 | +6.9% | -0.0849 to 0.0996 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 205 | +7.2% | -170 to 198 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.143 | 0.154 | +7.2% | -0.127 to 0.148 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
