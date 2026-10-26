# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,936 | -0.1% | -10.8 to 6.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,938 | -0.1% | -8.9 to 4.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.127 | 0.155 | +22.6% | -0.0335 to 0.0908 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.333 | 0.351 | +5.2% | -0.00718 to 0.0418 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0621 | 0.0647 | +4.2% | -0.0109 to 0.0161 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | +0.0% | -1.79 to 2.32 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,804 | 61,901 | +0.2% | -245 to 439 | shown, not judged |
| host CPU busy (share of the run) | 0.0894 | 0.0732 | -18.1% | -0.0415 to 0.00917 | EVEN, no difference beyond the noise |
| host CPU-seconds | 163 | 131 | -19.9% | -80.3 to 15.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.122 | 0.0977 | -19.9% | -0.0602 to 0.0116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.7 | 54.6 | +5.7% | -6.34 to 12.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.1 | 52.8 | +5.4% | -6.24 to 11.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.59 | 1.81 | +14.3% | -0.105 to 0.56 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 163 | 131 | -19.9% | -80.3 to 15.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,863 | -0.1% | -52.2 to 45.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,881 | 2,878 | -0.1% | -33.3 to 27.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.489 | 0.49 | +0.1% | -0.0854 to 0.0867 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.763 | 0.767 | +0.6% | -0.38 to 0.388 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.233 | 0.234 | +0.6% | -0.0383 to 0.0411 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,505 | 1,500 | -0.3% | -33.9 to 25 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,629 | 77,663 | +0.0% | -625 to 693 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.229 | +2.2% | -0.0999 to 0.11 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 165 | +3.3% | -94.5 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.311 | +3.4% | -0.174 to 0.195 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.6 | 83.3 | +0.9% | -6.81 to 8.21 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.4 | 82.1 | +0.8% | -6.67 to 8.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.14 | 1.17 | +2.6% | -0.14 to 0.2 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 159 | 165 | +3.3% | -94.5 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,886 | -0.0% | -4.29 to 3.28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -4.26 to 3.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.294 | 0.295 | +0.2% | -0.00651 to 0.00784 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.545 | -0.2% | -0.0297 to 0.0277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.184 | +1.2% | -0.00672 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | +0.0% | -3.53 to 4.21 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,635 | 61,658 | +0.0% | -169 to 215 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.175 | +5.3% | -0.0103 to 0.028 | EVEN, no difference beyond the noise |
| host CPU-seconds | 285 | 302 | +5.9% | -19.3 to 53.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.227 | +5.9% | -0.0145 to 0.0399 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 171 | 175 | +2.2% | -13.6 to 21.1 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 168 | 172 | +2.2% | -13.7 to 21 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.62 | +4.7% | 0.0251 to 0.211 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 285 | 302 | +5.9% | -19.3 to 53.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,834 | 5,834 | -0.0% | -20.3 to 20.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,840 | 5,839 | -0.0% | -19.9 to 19.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.162 | 0.166 | +2.3% | -0.00259 to 0.00992 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.369 | 0.376 | +1.9% | -0.037 to 0.051 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0832 | 0.0836 | +0.5% | -5.83e-05 to 0.000914 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,363 | -0.1% | -12.9 to 10 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,287 | 63,531 | +0.4% | -310 to 799 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.127 | -4.7% | -0.0825 to 0.07 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 230 | -5.5% | -173 to 146 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.091 | 0.086 | -5.5% | -0.0645 to 0.0545 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 107 | 108 | +1.1% | -1.19 to 3.56 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 104 | 105 | +1.0% | -1.54 to 3.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.9 | 3.03 | +4.7% | -0.212 to 0.483 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 244 | 230 | -5.5% | -173 to 146 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | +0.0% | -5.86 to 7.98 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | +0.0% | -4.88 to 6.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.344 | -0.6% | -0.011 to 0.00696 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.629 | 0.623 | -1.0% | -0.0297 to 0.0177 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.208 | -2.0% | -0.00945 to 0.00115 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | +0.0% | -7.47 to 8.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,132 | 63,135 | +0.0% | -516 to 522 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.225 | -9.1% | -0.0814 to 0.0365 | EVEN, no difference beyond the noise |
| host CPU-seconds | 445 | 394 | -11.5% | -192 to 89.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.335 | 0.297 | -11.5% | -0.144 to 0.0667 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 237 | 231 | -2.2% | -11.5 to 1.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 234 | 229 | -2.2% | -11.5 to 1.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 2.61 | +1.9% | -0.155 to 0.251 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 445 | 394 | -11.5% | -192 to 89.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
