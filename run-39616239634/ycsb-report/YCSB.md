# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,889 | +0.0% | -4.25 to 6.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,892 | +0.0% | -3.93 to 6.46 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.318 | -0.3% | -0.047 to 0.045 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.485 | -0.4% | -0.0322 to 0.0282 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.188 | -0.0% | -0.0129 to 0.0128 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -1.42 to 1.02 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,769 | 61,826 | +0.1% | -318 to 432 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.198 | -2.9% | -0.126 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 363 | 350 | -3.6% | -280 to 254 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.263 | -3.6% | -0.21 to 0.191 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,804 | 2,764 | -1.4% | -491 to 411 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,819 | 2,777 | -1.5% | -495 to 411 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.339 | +1.1% | -0.0246 to 0.0319 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.569 | 0.534 | -6.1% | -0.133 to 0.0637 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.193 | +1.5% | -0.0371 to 0.0428 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,484 | 7,484 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,431 | 1,402 | -2.0% | -392 to 335 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,262 | 77,146 | -0.2% | -2,518 to 2,285 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.145 | -4.6% | -0.0417 to 0.0278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 104 | -5.7% | -36.1 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.205 | -4.2% | -0.051 to 0.0328 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | +0.0% | -1.97 to 2.72 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | +0.0% | -1.19 to 1.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.3 | -0.9% | -0.00646 to 0.00113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.583 | 0.583 | -0.1% | -0.0215 to 0.0208 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.191 | +0.9% | -0.00583 to 0.00934 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -3.05 to 3.41 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,670 | 61,704 | +0.1% | -143 to 211 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.192 | +6.6% | -0.0236 to 0.0475 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 336 | +7.8% | -54 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.252 | +7.8% | -0.0405 to 0.0768 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,674 | 5,678 | +0.1% | -18.3 to 25.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,688 | 5,691 | +0.1% | -18.7 to 26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.42 | +0.3% | -0.00665 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.64 | 0.639 | -0.1% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.239 | 0.24 | +0.5% | -0.00362 to 0.00586 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,358 | 1,360 | +0.1% | 0.25 to 3.04 | power given |
| pages read into the cache (misses) | 62,871 | 63,131 | +0.4% | 137 to 383 | shown, not judged |
| host CPU busy (share of the run) | 0.303 | 0.307 | +1.2% | -0.00308 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 544 | 553 | +1.6% | -12.8 to 30.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.209 | +1.6% | -0.00436 to 0.0108 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -0.872 to -0.262 | LOSS |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% | -0.888 to 0.0476 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.345 | +1.7% | 0.00187 to 0.00946 | LOSS |
| latency, 99th percentile (ms) | 0.52 | 0.528 | +1.5% | 0.0025 to 0.0128 | LOSS |
| latency, mean (ms) | 0.206 | 0.206 | -0.3% | -0.0029 to 0.00181 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -4.72 to 2.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,057 | 63,108 | +0.1% | -779 to 881 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.237 | +5.1% | -0.0604 to 0.0833 | EVEN, no difference beyond the noise |
| host CPU-seconds | 395 | 420 | +6.5% | -135 to 186 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.297 | 0.316 | +6.5% | -0.102 to 0.14 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
