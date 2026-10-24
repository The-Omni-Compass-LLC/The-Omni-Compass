# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,924 | -0.1% | -5.83 to 2.59 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,928 | 2,926 | -0.1% | -5.43 to 2.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.224 | 0.228 | +2.1% | -0.0184 to 0.0278 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.432 | +0.5% | -0.0159 to 0.0199 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.114 | 0.116 | +1.3% | -0.00567 to 0.00858 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,366 | +0.0% | -2.54 to 2.75 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,765 | 61,866 | +0.2% | -186 to 387 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.121 | +13.3% | -0.0473 to 0.0756 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 218 | +14.8% | -98.7 to 155 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.142 | 0.163 | +14.9% | -0.0736 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,916 | +0.1% | -11.7 to 18.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,920 | +0.1% | -10.5 to 17.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.313 | 0.313 | +0.2% | -0.0908 to 0.0922 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.497 | -0.3% | -0.0886 to 0.0859 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.118 | -1.4% | -0.0187 to 0.0154 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,516 | 1,518 | +0.1% | -4.47 to 8.69 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,604 | 77,704 | +0.1% | -179 to 378 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.119 | -22.3% | -0.0815 to 0.0134 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 85.8 | -24.5% | -66.1 to 10.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.213 | 0.161 | -24.6% | -0.124 to 0.0191 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,938 | -0.1% | -6.02 to 2.66 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,939 | -0.1% | -5.81 to 2.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0883 | 0.088 | -0.4% | -0.00177 to 0.0011 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.293 | 0.285 | -2.8% | -0.022 to 0.00535 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0554 | 0.0553 | -0.2% | -0.00398 to 0.00379 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | -0.0% | -2.28 to 1.87 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,669 | 61,669 | +0.0% | -112 to 113 | shown, not judged |
| host CPU busy (share of the run) | 0.0893 | 0.0861 | -3.6% | -0.0429 to 0.0365 | EVEN, no difference beyond the noise |
| host CPU-seconds | 165 | 158 | -4.3% | -87.5 to 73.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.123 | 0.118 | -4.3% | -0.0654 to 0.0548 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,680 | -0.0% | -21.9 to 19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,691 | 5,690 | -0.0% | -22.4 to 19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.396 | 0.396 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.59 | 0.588 | -0.3% | -0.0128 to 0.00883 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.221 | -0.2% | -0.000761 to -2.95e-05 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,360 | +0.0% | -6.2 to 7.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,032 | 62,971 | -0.1% | -812 to 691 | shown, not judged |
| host CPU busy (share of the run) | 0.293 | 0.282 | -3.9% | -0.0188 to -0.00385 | GAIN |
| host CPU-seconds | 536 | 507 | -5.4% | -46.2 to -12 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.191 | -5.4% | -0.0179 to -0.0039 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,878 | +0.0% | -7.92 to 9.11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,886 | +0.0% | -6.86 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.351 | 0.348 | -0.9% | -0.0105 to 0.00445 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.629 | 0.626 | -0.4% | -0.0052 to 0.000535 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.21 | -1.0% | -0.00786 to 0.00382 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,361 | -0.1% | -6.39 to 4.95 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,091 | 63,086 | -0.0% | -247 to 237 | shown, not judged |
| host CPU busy (share of the run) | 0.229 | 0.216 | -5.4% | -0.0793 to 0.0545 | EVEN, no difference beyond the noise |
| host CPU-seconds | 401 | 374 | -6.7% | -180 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.302 | 0.282 | -6.7% | -0.136 to 0.0949 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
