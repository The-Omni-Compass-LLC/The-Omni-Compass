# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -4.45 to 4.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,940 | -0.0% | -4.47 to 4.29 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.141 | 0.152 | +7.5% | -0.0119 to 0.0332 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.33 | 0.333 | +0.7% | -0.0191 to 0.0238 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0616 | 0.0626 | +1.8% | -0.00329 to 0.00547 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | +0.0% | -0.743 to 1.62 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,800 | 61,884 | +0.1% | -142 to 311 | shown, not judged |
| host CPU busy (share of the run) | 0.0857 | 0.0753 | -12.2% | -0.0642 to 0.0433 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 136 | -12.8% | -125 to 85.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.116 | 0.101 | -12.8% | -0.0935 to 0.0638 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,937 | +0.1% | -2.98 to 6.68 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,940 | +0.1% | -3.55 to 7.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.256 | -0.5% | -0.0417 to 0.0391 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.411 | 0.404 | -1.7% | -0.0492 to 0.0352 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0773 | 0.076 | -1.7% | -0.0141 to 0.0114 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,518 | 1,523 | +0.3% | 0.835 to 7.52 | power given |
| pages read into the cache (misses) | 77,629 | 77,718 | +0.1% | -104 to 282 | shown, not judged |
| host CPU busy (share of the run) | 0.074 | 0.0828 | +11.9% | -0.0498 to 0.0674 | EVEN, no difference beyond the noise |
| host CPU-seconds | 53 | 60.5 | +14.1% | -39.1 to 54.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.099 | 0.113 | +14.1% | -0.0731 to 0.101 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,938 | -0.0% | -3.48 to 1.73 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -3.35 to 1.63 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0887 | 0.0893 | +0.8% | -0.00968 to 0.011 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.289 | 0.292 | +0.8% | -0.0184 to 0.023 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0548 | 0.0552 | +0.8% | -0.00334 to 0.00417 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | +0.0% | -0.961 to 1.67 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,650 | 61,685 | +0.1% | -28.8 to 100 | shown, not judged |
| host CPU busy (share of the run) | 0.0761 | 0.082 | +7.8% | -0.0564 to 0.0683 | EVEN, no difference beyond the noise |
| host CPU-seconds | 138 | 150 | +8.4% | -110 to 133 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.103 | 0.112 | +8.4% | -0.0821 to 0.0994 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,663 | 5,666 | +0.1% | -8.51 to 14.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,679 | 5,682 | +0.1% | -7.97 to 13.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.427 | 0.428 | +0.3% | -0.00665 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.682 | 0.681 | -0.0% | -0.0267 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.243 | +0.1% | -0.00752 to 0.00815 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,359 | -0.1% | -7.8 to 5.73 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,985 | 62,804 | -0.3% | -1,457 to 1,094 | shown, not judged |
| host CPU busy (share of the run) | 0.306 | 0.307 | +0.3% | -0.0142 to 0.0159 | EVEN, no difference beyond the noise |
| host CPU-seconds | 551 | 554 | +0.4% | -39.3 to 43.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.209 | +0.4% | -0.0145 to 0.0161 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,901 | +0.0% | -4.82 to 6.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,907 | +0.0% | -6.21 to 7.58 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.329 | 0.329 | -0.2% | -0.0176 to 0.0162 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.586 | 0.576 | -1.8% | -0.0338 to 0.0124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.147 | -0.7% | -0.00938 to 0.00731 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | +0.0% | -8.52 to 9.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,354 | 63,058 | -0.5% | -734 to 143 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.167 | -9.0% | -0.094 to 0.0612 | EVEN, no difference beyond the noise |
| host CPU-seconds | 333 | 297 | -10.7% | -200 to 129 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.223 | -10.7% | -0.15 to 0.0967 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
