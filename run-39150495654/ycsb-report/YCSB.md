# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.0% | -2.38 to 1.31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -1.88 to 1.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.343 | +1.7% | -0.0291 to 0.0405 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.521 | +0.7% | -0.00781 to 0.0151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.197 | +1.2% | -0.00645 to 0.0111 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% | -0.893 to 1.72 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,772 | 61,888 | +0.2% | -165 to 397 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.185 | +3.0% | -0.00905 to 0.0198 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 318 | +3.3% | -23.7 to 44.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.239 | +3.4% | -0.0178 to 0.0333 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -7.79 to 6.66 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -3.53 to 2.61 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.505 | 0.504 | -0.1% | -0.0143 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.667 | 0.665 | -0.3% | -0.0582 to 0.0535 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.228 | +1.1% | -0.00597 to 0.0111 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,506 | 1,507 | +0.1% | -7.29 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,632 | 77,724 | +0.1% | -117 to 302 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.197 | +4.1% | -0.0649 to 0.0803 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 138 | +4.6% | -55.9 to 68.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.259 | +4.6% | -0.104 to 0.127 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,897 | -0.0% | -3.51 to 1.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,901 | -0.0% | -2.3 to 0.987 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.302 | +0.3% | -0.00796 to 0.00996 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.512 | 0.514 | +0.3% | -0.0211 to 0.0237 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.189 | +1.2% | -0.00595 to 0.0104 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.0% | -2.36 to 3.51 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,636 | 61,673 | +0.1% | -98.4 to 173 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.7% | -0.0299 to 0.0323 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 283 | +0.8% | -61.4 to 66.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.213 | +0.8% | -0.0462 to 0.0498 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,605 | 5,582 | -0.4% | -102 to 56 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,620 | 5,598 | -0.4% | -98.7 to 54.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.462 | 0.464 | +0.6% | -0.00854 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.679 | 0.691 | +1.7% | -0.0173 to 0.0407 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.269 | 0.27 | +0.4% | -0.00419 to 0.00661 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,354 | 1,354 | -0.0% | -6.44 to 5.41 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,550 | 62,641 | +0.1% | -818 to 999 | shown, not judged |
| host CPU busy (share of the run) | 0.298 | 0.304 | +2.1% | -0.023 to 0.0354 | EVEN, no difference beyond the noise |
| host CPU-seconds | 506 | 517 | +2.2% | -46.5 to 68.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.193 | 0.198 | +2.6% | -0.0193 to 0.0293 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,865 | 2,843 | -0.8% | -204 to 160 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,874 | 2,851 | -0.8% | -203 to 158 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.267 | 0.266 | -0.6% | -0.0104 to 0.00706 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.428 | -0.5% | -0.0111 to 0.00639 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.209 | -2.1% | -0.0389 to 0.0299 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,338 | -0.8% | -70.3 to 47.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,011 | 62,028 | -1.6% | -5,534 to 3,568 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.174 | +1.1% | -0.0918 to 0.0956 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 316 | +1.5% | -197 to 206 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.242 | +2.0% | -0.147 to 0.156 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
