# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,939 | -0.0% | -3.03 to 2.23 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,941 | -0.0% | -2.47 to 1.77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.131 | 0.132 | +0.8% | -0.0454 to 0.0474 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.337 | 0.333 | -1.1% | -0.0471 to 0.0397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0607 | 0.0603 | -0.6% | -0.00712 to 0.0064 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,366 | -0.1% | -4.44 to 2.32 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,827 | 61,842 | +0.0% | -341 to 372 | shown, not judged |
| host CPU busy (share of the run) | 0.0883 | 0.0738 | -16.4% | -0.0726 to 0.0436 | EVEN, no difference beyond the noise |
| host CPU-seconds | 162 | 133 | -18.2% | -149 to 89.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.121 | 0.099 | -18.2% | -0.111 to 0.0671 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,937 | -0.1% | -14.7 to 10.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,940 | -0.1% | -11.8 to 7.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.256 | +3.6% | -0.0304 to 0.0484 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.38 | 0.399 | +5.2% | -0.0907 to 0.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0753 | 0.077 | +2.3% | -0.0231 to 0.0266 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,518 | 1,522 | +0.3% | -0.279 to 9.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,564 | 77,669 | +0.1% | -97.3 to 308 | shown, not judged |
| host CPU busy (share of the run) | 0.06 | 0.0829 | +38.2% | -0.0332 to 0.0789 | EVEN, no difference beyond the noise |
| host CPU-seconds | 42.6 | 60.4 | +41.7% | -26.6 to 62.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0795 | 0.113 | +41.8% | -0.0498 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -15.1 to 11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,899 | -0.1% | -13 to 8.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.203 | 0.206 | +1.6% | -0.0155 to 0.0221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.38 | 0.38 | +0.0% | -0.0587 to 0.0587 | EVEN, the same |
| latency, mean (ms) | 0.148 | 0.152 | +2.5% | -0.0104 to 0.0179 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,347 | 1,346 | -0.0% | -4.09 to 2.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,611 | 61,636 | +0.0% | -96 to 146 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.17 | +8.0% | -0.0229 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 308 | +9.3% | -55.2 to 108 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.231 | +9.4% | -0.0409 to 0.0804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,754 | +0.0% | -11.2 to 14.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,764 | 5,766 | +0.0% | -9.62 to 14.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.307 | -0.1% | -0.0032 to 0.00254 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.468 | +2.6% | -0.0435 to 0.0675 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.179 | 0.179 | -0.2% | -0.00785 to 0.00714 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,364 | +0.2% | -9.71 to 14.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,114 | 63,146 | +0.1% | -373 to 437 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.233 | +2.6% | -0.0655 to 0.0774 | EVEN, no difference beyond the noise |
| host CPU-seconds | 411 | 426 | +3.7% | -153 to 183 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.16 | +3.7% | -0.0576 to 0.0689 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,936 | +0.0% | -5.62 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,938 | +0.0% | -4.99 to 7.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.152 | -0.2% | -0.021 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.357 | 0.36 | +0.8% | -0.025 to 0.031 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0746 | 0.0739 | -0.9% | -0.00259 to 0.00119 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | +0.0% | -5.07 to 5.95 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,390 | 63,430 | +0.1% | -877 to 957 | shown, not judged |
| host CPU busy (share of the run) | 0.0961 | 0.0984 | +2.4% | -0.0315 to 0.0361 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 177 | +2.3% | -62.8 to 70.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.129 | 0.132 | +2.3% | -0.0468 to 0.0527 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
