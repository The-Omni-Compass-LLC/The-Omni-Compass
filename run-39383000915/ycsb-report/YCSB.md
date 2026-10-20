# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,929 | 2,928 | -0.1% | -2.01 to -0.957 | LOSS |
| throughput (operations a second) | 2,931 | 2,930 | -0.0% | -2.03 to -0.393 | LOSS |
| latency, 95th percentile (ms) | 0.245 | 0.25 | +1.9% | 0.0018 to 0.00754 | LOSS |
| latency, 99th percentile (ms) | 0.391 | 0.396 | +1.3% | -0.00583 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0854 | 0.0878 | +2.8% | -0.000753 to 0.00556 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,367 | +0.1% | -0.796 to 2.23 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,784 | 61,887 | +0.2% | -116 to 323 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0988 | -2.2% | -0.0154 to 0.011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 183 | 178 | -2.7% | -32.1 to 22.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.136 | 0.133 | -2.7% | -0.024 to 0.0166 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,928 | 2,928 | -0.0% | -10.1 to 8.99 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,932 | 2,931 | -0.0% | -11.4 to 10.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.265 | 0.266 | +0.1% | -0.0011 to 0.00177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.433 | 0.439 | +1.5% | -0.0613 to 0.074 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0956 | 0.0956 | -0.0% | -0.00541 to 0.00535 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,521 | 1,521 | +0.0% | -4 to 4.41 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,645 | 77,708 | +0.1% | -241 to 367 | shown, not judged |
| host CPU busy (share of the run) | 0.085 | 0.0997 | +17.3% | -0.0478 to 0.0772 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.9 | 72.7 | +19.3% | -38.6 to 62.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.114 | 0.136 | +19.3% | -0.0723 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,895 | +0.1% | -0.541 to 3.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,900 | +0.1% | -1.17 to 4.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.4% | -0.0138 to 0.0112 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.558 | 0.552 | -1.1% | -0.0151 to 0.00239 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.19 | -1.5% | -0.00647 to 0.00075 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.1% | -0.65 to 2.66 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,602 | 61,646 | +0.1% | -80.5 to 168 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.169 | -5.4% | -0.0859 to 0.0668 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 289 | -6.3% | -174 to 135 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.217 | -6.3% | -0.131 to 0.102 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,750 | 5,753 | +0.1% | -12.7 to 19.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,759 | 5,762 | +0.1% | -12.1 to 18.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.337 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.535 | 0.535 | -0.1% | -0.00607 to 0.0054 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.184 | -0.7% | -0.00354 to 0.000818 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -1.73 to 1.69 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,994 | 63,070 | +0.1% | -502 to 654 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.242 | -1.9% | -0.0729 to 0.0636 | EVEN, no difference beyond the noise |
| host CPU-seconds | 452 | 441 | -2.3% | -169 to 148 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.166 | -2.3% | -0.0632 to 0.0553 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,893 | +0.0% | -2.2 to 3.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,898 | +0.0% | -1.68 to 2.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.339 | +0.9% | -0.00694 to 0.0129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.519 | +0.2% | -0.00983 to 0.0118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.21 | +0.3% | -0.00661 to 0.00796 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | +0.0% | -0.838 to 0.918 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,902 | 63,055 | +0.2% | -761 to 1,066 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.198 | -8.5% | -0.114 to 0.077 | EVEN, no difference beyond the noise |
| host CPU-seconds | 375 | 336 | -10.4% | -238 to 160 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.282 | 0.252 | -10.4% | -0.178 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
