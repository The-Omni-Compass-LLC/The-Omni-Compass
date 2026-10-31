# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,922 | 2,921 | -0.0% | -1.84 to 0.646 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,924 | 2,924 | -0.0% | -2.35 to 0.931 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.198 | +0.5% | -0.0189 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.388 | +0.4% | -0.0436 to 0.047 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.103 | -1.3% | -0.00497 to 0.00228 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 835 | +63.1% | -106 to 752 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 666 | +58.4% | -86.6 to 578 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 724,920 | 463,477 | -36.1% | -472,958 to -49,928 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.123 | +5.9% | -0.0348 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 223 | +7.1% | -71.2 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.156 | 0.167 | +7.1% | -0.0533 to 0.0754 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 99 | 95.8 | -3.3% | -7.39 to 0.872 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 97 | 93.1 | -3.9% | -8.1 to 0.444 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.07 | 2.64 | +27.7% | 0.401 to 0.745 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 208 | 223 | +7.1% | -71.2 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,879 | +0.0% | -3.06 to 4.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -2.56 to 3.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.415 | 0.416 | +0.4% | -0.00774 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.586 | 0.587 | +0.2% | -0.0138 to 0.0165 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.217 | +0.8% | -0.00548 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 401 | 402 | +0.2% | -12.7 to 14.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 257,543 | 276,939 | +7.5% | -4,156 to 42,947 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.19 | -10.7% | -0.142 to 0.0967 | EVEN, no difference beyond the noise |
| host CPU-seconds | 151 | 131 | -13.3% | -124 to 83.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.284 | 0.246 | -13.3% | -0.233 to 0.157 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.1 | 83.1 | +1.2% | -1.78 to 3.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81 | 81.8 | +0.9% | -1.96 to 3.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.03 | 1.27 | +23.2% | 0.17 to 0.308 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 151 | 131 | -13.3% | -124 to 83.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | +0.0% | -2.45 to 3.79 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,915 | +0.0% | -2.08 to 2.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.187 | 0.182 | -2.7% | -0.00997 to -3.13e-05 | GAIN |
| latency, 99th percentile (ms) | 0.352 | 0.348 | -1.2% | -0.0137 to 0.00507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.137 | 0.135 | -1.2% | -0.00564 to 0.00226 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.7% | -341 to 860 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 615 | +46.9% | -262 to 655 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 658,030 | 474,353 | -27.9% | -683,295 to 315,941 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.126 | -17.0% | -0.0616 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 220 | -19.1% | -127 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.165 | -19.1% | -0.0954 to 0.0175 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.3 to 6.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 138 | 135 | -2.5% | -11 to 4.02 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 136 | 132 | -2.9% | -11.6 to 3.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2 | 2.48 | +24.3% | 0.378 to 0.592 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 272 | 220 | -19.1% | -127 to 23.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,846 | 5,839 | -0.1% | -17.8 to 3.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,854 | 5,848 | -0.1% | -16.8 to 4.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.158 | 0.161 | +1.9% | -0.00942 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.362 | +3.0% | -0.00863 to 0.03 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.082 | 0.0831 | +1.4% | -0.00185 to 0.00407 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 667 | +30.2% | -178 to 487 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 537 | +28.1% | -136 to 372 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,105 | 533,930 | -23.7% | -517,270 to 184,921 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.124 | +5.5% | -0.0885 to 0.101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 223 | +5.2% | -183 to 205 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0792 | 0.0833 | +5.3% | -0.068 to 0.0764 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 119 | 122 | +1.8% | -6.37 to 10.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 118 | +1.3% | -6.54 to 9.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.14 | +23.0% | 0.0684 to 1.11 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 212 | 223 | +5.2% | -183 to 205 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,942 | 2,941 | -0.0% | -2.73 to 1.46 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,945 | -0.0% | -1.81 to 1.68 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.119 | 0.116 | -2.8% | -0.0105 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.304 | 0.309 | +1.4% | -0.0276 to 0.0363 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0699 | 0.0686 | -1.8% | -0.00353 to 0.000969 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 916 | +78.9% | 162 to 645 | power given |
| bytes in the cache, mean (MB) | 419 | 725 | +73.0% | 121 to 490 | power given |
| pages read into the cache (misses) | 688,919 | 348,310 | -49.4% | -528,515 to -152,701 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -2.1% | -0.105 to 0.101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 186 | -2.2% | -210 to 201 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.142 | 0.139 | -2.2% | -0.156 to 0.15 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -1.5 to 8.84 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 90.5 | 87.7 | -3.2% | -3.77 to -1.98 | GAIN |
| the server's own CPU-seconds (mongod) | 89.2 | 85.9 | -3.6% | -4.2 to -2.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.36 | 1.74 | +28.0% | 0.33 to 0.43 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 190 | 186 | -2.2% | -210 to 201 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
