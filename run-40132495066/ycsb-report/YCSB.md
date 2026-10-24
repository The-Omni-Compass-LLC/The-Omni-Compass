# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | +0.0% | -10.6 to 10.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% | -10 to 9.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.345 | 0.345 | -0.1% | -0.0717 to 0.071 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.611 | 0.61 | -0.2% | -0.0526 to 0.0506 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.196 | -0.2% | -0.0233 to 0.0224 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,365 | +0.1% | -0.857 to 3.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,711 | 61,878 | +0.3% | -117 to 451 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.208 | +5.9% | -0.0878 to 0.111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 370 | +7.6% | -179 to 232 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.279 | +7.6% | -0.135 to 0.175 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,880 | +0.0% | -1.03 to 1.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -1.25 to 2.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.457 | 0.454 | -0.7% | -0.0405 to 0.0345 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.618 | 0.62 | +0.3% | -0.0331 to 0.0365 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.214 | -0.9% | -0.0145 to 0.0106 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,509 | 1,510 | +0.0% | -4.34 to 5.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,619 | 77,720 | +0.1% | -35.8 to 238 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.193 | -4.2% | -0.0805 to 0.0637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 142 | 135 | -4.9% | -70.3 to 56.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.254 | -4.9% | -0.132 to 0.106 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | +0.0% | -2.57 to 3.02 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | +0.0% | -2.32 to 2.63 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.299 | -1.0% | -0.00797 to 0.00197 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.51 | -1.2% | -0.0215 to 0.00885 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.186 | -0.7% | -0.00735 to 0.00491 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.1% | -2.39 to 4.15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,618 | 61,670 | +0.1% | -138 to 242 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.208 | +11.7% | -0.0219 to 0.0653 | EVEN, no difference beyond the noise |
| host CPU-seconds | 324 | 373 | +15.0% | -52.1 to 149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.244 | 0.28 | +15.0% | -0.0392 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,671 | 5,665 | -0.1% | -19.8 to 6.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,685 | 5,679 | -0.1% | -18.2 to 6.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.423 | +0.3% | -0.0104 to 0.0131 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.652 | 0.657 | +0.7% | -0.0157 to 0.0244 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.241 | -0.0% | -0.0059 to 0.00571 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,359 | 1,358 | -0.1% | -7.49 to 5.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,825 | 62,897 | +0.1% | -467 to 612 | shown, not judged |
| host CPU busy (share of the run) | 0.307 | 0.307 | -0.0% | -0.0185 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 553 | 554 | +0.1% | -45.7 to 46.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.209 | +0.2% | -0.0177 to 0.0186 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,907 | +0.0% | -6.91 to 7.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,913 | +0.0% | -7.79 to 9.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.211 | 0.214 | +1.6% | -0.011 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.399 | 0.4 | +0.3% | -0.0216 to 0.0243 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.159 | -1.3% | -0.0201 to 0.0161 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.0% | -3.75 to 4.29 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,999 | 63,147 | +0.2% | -432 to 728 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.164 | -15.4% | -0.108 to 0.048 | EVEN, no difference beyond the noise |
| host CPU-seconds | 357 | 292 | -18.0% | -227 to 98.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.219 | -18.0% | -0.17 to 0.0738 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
