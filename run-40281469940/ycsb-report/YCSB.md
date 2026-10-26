# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -2.97 to 2.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.55 to 2.71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.336 | +2.3% | -0.022 to 0.0373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.54 | +2.4% | -0.0235 to 0.0489 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.2 | +1.4% | -0.00678 to 0.0124 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -2.12 to -0.928 | GAIN |
| bytes in the cache, mean (MB) | 417 | 419 | +0.5% | -4.83 to 8.65 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,857 | 734,771 | +5.6% | -38,770 to 116,596 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.206 | -1.6% | -0.0815 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 363 | -2.3% | -181 to 164 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.273 | -2.3% | -0.136 to 0.123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 203 | +2.0% | -7.05 to 15.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 196 | 200 | +1.8% | -7.72 to 14.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.1 | +23.8% | 0.417 to 0.777 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 371 | 363 | -2.3% | -181 to 164 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,902 | +0.1% | -11.5 to 19.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,914 | +0.1% | -11 to 19.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.321 | +5.4% | -0.0239 to 0.0566 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.462 | 0.474 | +2.5% | -0.00202 to 0.0253 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.168 | 0.161 | -4.0% | -0.018 to 0.00451 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 527 | +2.9% | -47.1 to 77 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 418 | +4.2% | -27.5 to 61.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 275,871 | 274,953 | -0.3% | -39,253 to 37,418 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.141 | -9.0% | -0.115 to 0.0874 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 99.1 | -10.6% | -95.6 to 72.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.186 | -10.6% | -0.179 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7 |  | 0.427 to 13.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.5 | 63.1 | +1.0% | -1.36 to 2.56 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.7 | 62.1 | +0.7% | -1.48 to 2.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.83 | 0.996 | +20.0% | 0.102 to 0.229 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 111 | 99.1 | -10.6% | -95.7 to 72.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | +0.0% | -1.31 to 1.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -1.2 to 0.978 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.306 | -0.9% | -0.0107 to 0.00532 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.571 | 0.566 | -0.9% | -0.0205 to 0.0105 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.194 | -0.6% | -0.0116 to 0.00914 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.6 to 0.324 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.3% | -8.69 to 6.56 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 651,796 | 663,393 | +1.8% | -82,164 to 105,356 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.181 | -3.1% | -0.0456 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 325 | 314 | -3.6% | -93.1 to 69.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.244 | 0.236 | -3.6% | -0.0701 to 0.0527 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | -0.838 to 9.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 189 | +0.2% | -14.9 to 15.7 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 186 | -0.1% | -15.4 to 15.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.12 | +22.9% | 0.479 to 0.685 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 325 | 314 | -3.6% | -93.1 to 69.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,835 | 5,829 | -0.1% | -25.5 to 14.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,844 | 5,839 | -0.1% | -24.3 to 13.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.17 | 0.178 | +4.5% | -0.0285 to 0.0439 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.397 | 0.402 | +1.4% | -0.0328 to 0.0442 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0868 | 0.089 | +2.6% | -0.00754 to 0.012 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -56.7 to 83.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 430 | +2.8% | -40 to 63.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,316 | 685,793 | -0.8% | -84,092 to 73,045 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.151 | +17.2% | -0.0384 to 0.0828 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 277 | +19.5% | -76.8 to 167 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0867 | 0.104 | +19.6% | -0.0287 to 0.0626 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 126 | 131 | +4.1% | -15.1 to 25.4 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 123 | 127 | +3.7% | -15.4 to 24.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.73 | 3.39 | +24.3% | 0.293 to 1.04 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 232 | 277 | +19.5% | -76.7 to 167 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,888 | -0.1% | -19.2 to 12.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,898 | -0.1% | -20.5 to 13.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.347 | +0.0% | -0.0108 to 0.0108 | EVEN, the same |
| latency, 99th percentile (ms) | 0.58 | 0.578 | -0.3% | -0.0282 to 0.0242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.185 | 0.184 | -0.5% | -0.00343 to 0.00148 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -41.9 to 116 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 447 | +7.0% | -31.7 to 90.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,627 | 641,685 | -5.2% | -134,753 to 64,869 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.221 | +0.4% | -0.0747 to 0.0764 | EVEN, no difference beyond the noise |
| host CPU-seconds | 396 | 398 | +0.5% | -174 to 178 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.298 | 0.3 | +0.6% | -0.132 to 0.136 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 8.52 to 13.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 227 | 227 | -0.1% | -3.58 to 3.18 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 224 | 223 | -0.3% | -4.15 to 2.59 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.59 | 3.17 | +22.2% | 0.426 to 0.728 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 396 | 398 | +0.5% | -174 to 178 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
