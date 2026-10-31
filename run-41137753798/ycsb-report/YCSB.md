# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,939 | -0.0% | -4.27 to 3.57 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -4.13 to 3.52 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.119 | 0.128 | +7.9% | -0.00101 to 0.0197 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.309 | 0.329 | +6.3% | 0.00188 to 0.0368 | LOSS |
| latency, mean (ms) | 0.0587 | 0.0605 | +3.1% | 0.000833 to 0.00286 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | +0.0% | -4.8 to 4.93 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,801 | 61,879 | +0.1% | -484 to 640 | shown, not judged |
| host CPU busy (share of the run) | 0.0673 | 0.0822 | +22.2% | -0.00203 to 0.0318 | EVEN, no difference beyond the noise |
| host CPU-seconds | 120 | 149 | +24.1% | -4.7 to 62.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0898 | 0.111 | +24.1% | -0.00346 to 0.0467 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.1 | 51.2 | +2.3% | 0.833 to 1.45 | power given |
| the server's own CPU-seconds (mongod) | 48.5 | 49.6 | +2.3% | 0.91 to 1.28 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.57 | 1.62 | +2.7% | -0.0791 to 0.166 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 120 | 149 | +24.1% | -4.71 to 62.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,876 | -0.0% | -10.6 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.04 to 7.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.522 | 0.528 | +1.1% | -0.0128 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.665 | 0.676 | +1.7% | -0.0191 to 0.0411 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.226 | +1.0% | -0.0125 to 0.0171 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,501 | -0.1% | -9.41 to 6.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,576 | 77,650 | +0.1% | -195 to 343 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.191 | +3.8% | -0.0369 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 127 | 133 | +4.4% | -31.7 to 43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.25 | +4.5% | -0.0604 to 0.0817 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.6 | 79.1 | +1.9% | -2.77 to 5.77 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.6 | 78 | +1.9% | -2.8 to 5.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.09 | +4.1% | -0.0358 to 0.123 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 127 | 133 | +4.4% | -31.7 to 43 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -12.7 to 8.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -12.1 to 7.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.298 | 0.305 | +2.6% | -0.0154 to 0.0308 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.593 | 0.598 | +1.0% | -0.034 to 0.0453 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.19 | +1.1% | -0.00536 to 0.00964 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | -0.1% | -2.96 to 1.35 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,689 | 61,613 | -0.1% | -237 to 85.3 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.193 | +6.8% | -0.00847 to 0.0332 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 338 | +7.9% | -17.9 to 67.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.255 | +7.9% | -0.0134 to 0.0508 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 178 | +1.8% | -7.21 to 13.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 175 | +1.7% | -7.1 to 13.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 2.73 | +9.4% | -0.172 to 0.64 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 338 | +7.9% | -17.9 to 67.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,731 | 5,735 | +0.1% | -8.38 to 16.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,741 | 5,744 | +0.1% | -9.86 to 16.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.348 | +0.0% | -0.00896 to 0.00896 | EVEN, the same |
| latency, 99th percentile (ms) | 0.553 | 0.553 | +0.0% | -0.0237 to 0.0237 | EVEN, the same |
| latency, mean (ms) | 0.188 | 0.188 | -0.0% | -0.00339 to 0.00329 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.0% | -3.14 to 2.23 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,845 | 62,672 | -0.3% | -1,473 to 1,128 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.26 | +6.2% | -0.0405 to 0.0709 | EVEN, no difference beyond the noise |
| host CPU-seconds | 446 | 482 | +8.2% | -103 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.168 | 0.181 | +8.2% | -0.0385 to 0.0658 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 241 | 241 | -0.1% | -3.18 to 2.61 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 237 | 237 | -0.2% | -3.38 to 2.58 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.37 | 4.49 | +2.6% | 0.0118 to 0.217 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 446 | 482 | +8.2% | -103 to 176 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,904 | +0.1% | -2.25 to 5.96 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,910 | +0.1% | -1.39 to 4.72 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.312 | -1.2% | -0.014 to 0.00668 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.554 | 0.553 | -0.1% | -0.0129 to 0.0116 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.144 | 0.14 | -2.7% | -0.00752 to -0.00014 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | +0.1% | -2.06 to 5.65 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,166 | 63,313 | +0.2% | -592 to 888 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.168 | -11.4% | -0.101 to 0.0579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 303 | -13.8% | -223 to 127 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.227 | -13.8% | -0.168 to 0.095 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 151 | 149 | -1.2% | -4.99 to 1.25 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 148 | 146 | -1.3% | -5 to 1.14 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.41 | 2.47 | +2.3% | 0.00638 to 0.106 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351 | 303 | -13.8% | -223 to 127 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
