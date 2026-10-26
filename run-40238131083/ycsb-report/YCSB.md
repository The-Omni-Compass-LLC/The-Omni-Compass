# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,887 | -0.0% | -5.98 to 3.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -4.64 to 2.77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.328 | +5.8% | -0.025 to 0.061 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.515 | +2.0% | -0.0259 to 0.0465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.189 | +1.6% | -0.0045 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -1.89 to 1.63 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,796 | 61,828 | +0.1% | -115 to 177 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.179 | -1.2% | -0.0595 to 0.0553 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 308 | -1.9% | -126 to 114 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.231 | -1.8% | -0.0946 to 0.086 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 182 | 184 | +1.2% | -5.79 to 10.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 179 | 182 | +1.2% | -5.59 to 9.76 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 2.58 | +5.3% | -0.202 to 0.459 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 308 | -1.9% | -126 to 114 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,920 | 2,918 | -0.1% | -12.7 to 8.77 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,924 | 2,923 | -0.1% | -12.9 to 9.42 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.378 | 0.385 | +1.9% | -0.0104 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.535 | 0.559 | +4.6% | -0.0353 to 0.084 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.139 | 0.142 | +2.5% | -0.00214 to 0.00903 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,518 | +0.2% | -5.09 to 11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,655 | 77,726 | +0.1% | -458 to 602 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.147 | +14.4% | -0.0435 to 0.0805 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.9 | 109 | +15.3% | -39.8 to 68.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.178 | 0.205 | +15.4% | -0.0741 to 0.129 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 38.2 | 39.2 | +2.4% | -0.0682 to 1.92 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 37.4 | 38.3 | +2.3% | -0.0613 to 1.81 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.817 | 0.868 | +6.2% | -0.0088 to 0.111 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 94.9 | 109 | +15.3% | -39.9 to 68.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,910 | -0.1% | -2.35 to -0.596 | LOSS |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -2.93 to -0.65 | LOSS |
| latency, 95th percentile (ms) | 0.178 | 0.179 | +0.7% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.347 | 0.338 | -2.6% | -0.0253 to 0.00729 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.131 | 0.132 | +0.3% | -0.00328 to 0.00406 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -2.18 to 2.81 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,625 | 61,688 | +0.1% | 9.61 to 115 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.4% | -0.087 to 0.0859 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 260 | -1.4% | -183 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.194 | -1.4% | -0.137 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 128 | 129 | +0.8% | -2.18 to 4.13 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 126 | 127 | +0.7% | -2.28 to 4.05 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.14 | +4.1% | -0.168 to 0.338 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 263 | 260 | -1.4% | -183 to 176 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,669 | 5,669 | +0.0% | -20.6 to 21.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,682 | 5,683 | +0.0% | -20.6 to 22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.416 | 0.418 | +0.6% | -0.00914 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.635 | 0.64 | +0.8% | -0.0123 to 0.023 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.237 | 0.238 | +0.4% | -0.00522 to 0.00723 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,360 | -0.1% | -1.6 to 0.142 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,957 | 63,226 | +0.4% | -287 to 826 | shown, not judged |
| host CPU busy (share of the run) | 0.304 | 0.308 | +1.1% | -0.0127 to 0.0192 | EVEN, no difference beyond the noise |
| host CPU-seconds | 552 | 558 | +1.2% | -33.7 to 46.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.211 | +1.2% | -0.0136 to 0.0185 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 314 | 315 | +0.5% | -9.73 to 12.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 309 | 311 | +0.4% | -9.55 to 12.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.37 | 4.48 | +2.6% | -0.186 to 0.411 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 552 | 558 | +1.2% | -33.7 to 46.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -9.76 to 6.93 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -9.51 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.348 | +1.2% | 0.00152 to 0.00648 | LOSS |
| latency, 99th percentile (ms) | 0.62 | 0.621 | +0.2% | -0.00807 to 0.0107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.21 | +0.0% | -0.00461 to 0.00477 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,361 | -0.1% | -5.35 to 1.41 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,862 | 62,903 | +0.1% | -776 to 859 | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.21 | -9.3% | -0.0466 to 0.00347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 409 | 361 | -11.8% | -104 to 7.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.272 | -11.8% | -0.0782 to 0.00575 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 235 | +0.5% | -2.19 to 4.65 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 231 | 232 | +0.5% | -2.29 to 4.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.59 | +2.7% | 0.0263 to 0.109 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 409 | 361 | -11.8% | -105 to 7.83 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
