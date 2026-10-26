# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,886 | -0.7% | -98.8 to 57.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,892 | -0.7% | -99 to 58.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.217 | +1.9% | -0.0212 to 0.0292 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.409 | 0.418 | +2.2% | -0.0427 to 0.0607 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.153 | 0.163 | +6.5% | -0.0127 to 0.0326 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,361 | -0.2% | -9.16 to 5.04 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,793 | 61,888 | +0.2% | -233 to 424 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.171 | +8.0% | -0.0445 to 0.0697 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 316 | +10.3% | -94.8 to 154 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.239 | +11.1% | -0.0684 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 139 | 139 | -0.2% | -7.02 to 6.33 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 137 | 136 | -0.3% | -6.94 to 6.05 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.14 | +5.0% | -0.0819 to 0.287 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 316 | +10.3% | -94.8 to 154 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,939 | -0.0% | -4 to 3.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -4.58 to 4.58 | EVEN, the same |
| latency, 95th percentile (ms) | 0.242 | 0.252 | +4.3% | -0.0155 to 0.0362 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.381 | 0.4 | +4.8% | -0.00937 to 0.046 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0718 | 0.0752 | +4.7% | -0.00278 to 0.00955 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,521 | 1,522 | +0.1% | -4.6 to 6.57 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,695 | 77,745 | +0.1% | -421 to 521 | shown, not judged |
| host CPU busy (share of the run) | 0.0684 | 0.0769 | +12.5% | -0.1 to 0.117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 49.1 | 56.2 | +14.6% | -78.5 to 92.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0916 | 0.105 | +14.6% | -0.147 to 0.173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 21.2 | 22 | +3.9% | 0.335 to 1.33 | power given |
| the server's own CPU-seconds (mongod) | 20.6 | 21.4 | +3.9% | 0.267 to 1.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.616 | 0.646 | +4.8% | -0.0394 to 0.0981 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 49.1 | 56.2 | +14.6% | -78.5 to 92.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,944 | 2,944 | -0.0% | -2.97 to 2.36 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,945 | -0.0% | -2.27 to 1.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.075 | 0.077 | +2.7% | -0.00661 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.266 | 0.274 | +3.3% | -0.0256 to 0.0429 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0494 | 0.05 | +1.2% | -0.00116 to 0.00237 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,351 | 1,349 | -0.1% | -2.41 to -0.176 | GAIN |
| pages read into the cache (misses) | 61,704 | 61,643 | -0.1% | -155 to 32.9 | shown, not judged |
| host CPU busy (share of the run) | 0.0637 | 0.0658 | +3.2% | -0.0808 to 0.0848 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 119 | +3.1% | -156 to 163 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0862 | 0.0888 | +3.1% | -0.116 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 38.9 | 39.3 | +1.1% | -0.268 to 1.14 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 37.5 | 37.9 | +1.0% | -0.264 to 0.998 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.36 | 1.43 | +5.1% | -0.0489 to 0.188 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 116 | 119 | +3.1% | -156 to 163 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,672 | 5,676 | +0.1% | -10.3 to 18.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,682 | 5,686 | +0.1% | -10.7 to 18.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.4 | 0.401 | +0.3% | -0.00397 to 0.00597 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.606 | 0.602 | -0.6% | -0.0121 to 0.00539 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.225 | +0.1% | -0.00262 to 0.00301 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | +0.0% | -6.76 to 7.52 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,939 | 63,017 | +0.1% | -494 to 650 | shown, not judged |
| host CPU busy (share of the run) | 0.299 | 0.287 | -3.7% | -0.024 to 0.00169 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 520 | -5.2% | -59.2 to 1.71 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.196 | -5.3% | -0.0226 to 0.000784 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 309 | 309 | -0.3% | -5.83 to 4.25 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 305 | 304 | -0.3% | -5.57 to 3.95 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.37 | 4.4 | +0.6% | -0.254 to 0.309 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 548 | 520 | -5.2% | -59.2 to 1.72 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | +0.0% | -3.28 to 3.95 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | +0.0% | -3.14 to 4.46 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.341 | 0.343 | +0.6% | -0.0208 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.552 | 0.553 | +0.1% | -0.013 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.205 | -0.2% | -0.0137 to 0.013 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | -0.0% | -3.2 to 3.07 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,976 | 63,358 | +0.6% | -550 to 1,315 | shown, not judged |
| host CPU busy (share of the run) | 0.229 | 0.212 | -7.4% | -0.0825 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 366 | -9.8% | -183 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.305 | 0.275 | -9.8% | -0.138 to 0.0781 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 233 | +0.1% | -17.6 to 17.9 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 231 | 231 | +0.0% | -17.7 to 17.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.6 | +3.0% | 0.0119 to 0.139 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 406 | 366 | -9.8% | -183 to 104 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
