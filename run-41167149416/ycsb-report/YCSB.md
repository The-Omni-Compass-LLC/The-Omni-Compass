# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,879 | +0.1% | -14 to 21.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -2.86 to 3.84 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.392 | 0.357 | -8.9% | -0.186 to 0.117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.617 | -6.8% | -0.258 to 0.167 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.199 | -2.9% | -0.0266 to 0.0149 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | -0.0% | -1.82 to 1.71 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,758 | 61,804 | +0.1% | -209 to 301 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.193 | +0.4% | -0.041 to 0.0425 | EVEN, no difference beyond the noise |
| host CPU-seconds | 331 | 335 | +1.2% | -82.3 to 90.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.252 | +1.1% | -0.0632 to 0.0686 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 194 | 191 | -1.8% | -14.4 to 7.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 191 | 188 | -1.9% | -14.2 to 7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.77 | 2.81 | +1.5% | -0.218 to 0.298 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 331 | 335 | +1.2% | -82.3 to 90.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,835 | -2.3% | -344 to 212 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,848 | -2.2% | -335 to 207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.321 | +2.8% | -0.0139 to 0.0312 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.496 | +6.2% | -0.103 to 0.161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.166 | 0.168 | +1.0% | -0.0216 to 0.025 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,466 | -2.8% | -214 to 129 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,723 | 77,391 | -0.4% | -1,437 to 773 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.111 | +2.6% | -0.0711 to 0.0768 | EVEN, no difference beyond the noise |
| host CPU-seconds | 74.3 | 76.7 | +3.2% | -54.2 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.139 | 0.146 | +5.1% | -0.0945 to 0.109 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.2 | 57.2 | -1.7% | -5.44 to 3.44 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 57.4 | 56.4 | -1.7% | -5.4 to 3.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.81 | 0.798 | -1.5% | -0.0646 to 0.0399 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 74.3 | 76.7 | +3.2% | -54.2 to 59 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,886 | +0.0% | -1.68 to 2.15 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -0.742 to 1.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.294 | 0.293 | -0.5% | -0.0262 to 0.0236 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.582 | 0.581 | -0.2% | -0.0189 to 0.0169 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.186 | -0.7% | -0.00898 to 0.00649 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,347 | 1,348 | +0.1% | -1.93 to 4.35 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,604 | 61,665 | +0.1% | -138 to 260 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.172 | -12.0% | -0.0403 to -0.00653 | GAIN |
| host CPU-seconds | 347 | 297 | -14.6% | -94.4 to -6.77 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.223 | -14.6% | -0.0709 to -0.00516 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 175 | 174 | -0.4% | -10.3 to 8.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 172 | -0.5% | -10.2 to 8.5 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.54 | +2.8% | -0.0904 to 0.226 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 347 | 297 | -14.6% | -94.4 to -6.77 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,841 | 5,838 | -0.1% | -31.6 to 25.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,848 | 5,845 | -0.0% | -30.3 to 24.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.153 | 0.171 | +11.5% | -0.0502 to 0.0855 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.36 | 0.386 | +7.1% | -0.0576 to 0.109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0797 | 0.0836 | +4.9% | -0.0211 to 0.0289 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -3.65 to 3.07 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,090 | 63,415 | +0.5% | -72.1 to 721 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.127 | +4.6% | -0.0369 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 232 | +4.6% | -75.6 to 96.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0827 | 0.0865 | +4.7% | -0.0281 to 0.0358 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 102 | 106 | +4.2% | -24.6 to 33.1 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 99 | 103 | +4.1% | -24 to 32 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.63 | 2.85 | +8.4% | -0.622 to 1.07 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 221 | 232 | +4.6% | -75.6 to 96.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,937 | 2,938 | +0.0% | 0.754 to 1.37 | GAIN |
| throughput (operations a second) | 2,939 | 2,940 | +0.0% | 0.219 to 1.58 | GAIN |
| latency, 95th percentile (ms) | 0.134 | 0.135 | +0.7% | -0.0189 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.324 | 0.321 | -0.9% | -0.0245 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0713 | 0.0712 | -0.1% | -0.00537 to 0.00527 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.1% | -5.03 to 2.59 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,455 | 63,589 | +0.2% | -289 to 558 | shown, not judged |
| host CPU busy (share of the run) | 0.0901 | 0.0966 | +7.3% | -0.0579 to 0.0709 | EVEN, no difference beyond the noise |
| host CPU-seconds | 161 | 175 | +8.5% | -112 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.12 | 0.13 | +8.5% | -0.0836 to 0.104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.4 | 80.7 | -0.9% | -6.36 to 4.9 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79.8 | 79 | -1.0% | -6.43 to 4.87 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.6 | 1.65 | +3.1% | -0.00381 to 0.104 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 161 | 175 | +8.5% | -112 to 139 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
