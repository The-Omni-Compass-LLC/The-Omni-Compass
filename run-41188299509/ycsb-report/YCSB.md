# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,912 | -0.1% | -4.47 to 1.49 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,916 | -0.0% | -4.55 to 2.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.202 | 0.202 | -0.2% | -0.00906 to 0.00839 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.371 | 0.376 | +1.3% | -0.0284 to 0.0384 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.138 | +0.1% | -0.0091 to 0.00938 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 774 | +51.2% | -420 to 944 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 617 | +47.6% | -309 to 706 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 721,091 | 509,409 | -29.4% | -724,207 to 300,843 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.7% | -0.0891 to 0.0913 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 298 | +1.1% | -193 to 199 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.223 | +1.1% | -0.144 to 0.149 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -2.46 to 5.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 145 | -2.1% | -12.6 to 6.28 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 143 | -2.5% | -13.3 to 5.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.95 | 2.46 | +26.4% | 0.353 to 0.674 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 295 | 298 | +1.1% | -193 to 199 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,889 | -0.0% | -3.3 to 1.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -3.28 to 1.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.376 | 0.376 | +0.0% | -0.0114 to 0.0114 | EVEN, the same |
| latency, 99th percentile (ms) | 0.506 | 0.508 | +0.3% | -0.00837 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.192 | -0.1% | -0.00649 to 0.00616 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 565 | +10.3% | -78.6 to 184 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 403 | 443 | +10.0% | -65.6 to 146 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 255,634 | 256,398 | +0.3% | -30,780 to 32,308 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.212 | +4.8% | -0.106 to 0.125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 156 | +4.7% | -103 to 117 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.292 | +4.7% | -0.192 to 0.219 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.4 | 77.3 | -0.2% | -3.7 to 3.38 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.5 | 76.1 | -0.5% | -3.86 to 3.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.954 | 1.19 | +24.3% | 0.159 to 0.305 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 149 | 156 | +4.7% | -103 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,909 | +0.1% | -17.4 to 25.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,913 | +0.1% | -17.7 to 24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.194 | 0.188 | -3.3% | -0.0178 to 0.00514 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.378 | 0.37 | -2.1% | -0.0487 to 0.0327 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.15 | 0.143 | -4.8% | -0.0282 to 0.0137 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 870 | +69.9% | -662 to 1,378 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 693 | +65.8% | -521 to 1,071 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 725,012 | 423,294 | -41.6% | -1,041,857 to 438,421 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.149 | -6.9% | -0.0561 to 0.0341 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 268 | -7.7% | -120 to 75.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.201 | -7.7% | -0.09 to 0.0563 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -4.45 to 10.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 143 | 136 | -4.4% | -23.6 to 11 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 141 | 134 | -4.8% | -24.2 to 10.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.55 | +24.7% | 0.396 to 0.616 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 291 | 268 | -7.7% | -120 to 75.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,781 | 5,789 | +0.1% | -0.0705 to 15.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,795 | 5,802 | +0.1% | 0.731 to 14.3 | GAIN |
| latency, 95th percentile (ms) | 0.274 | 0.261 | -4.7% | -0.0304 to 0.00439 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.511 | 0.5 | -2.0% | -0.0394 to 0.0188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.133 | -5.2% | -0.0112 to -0.00354 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.9% | 154 to 367 | power given |
| bytes in the cache, mean (MB) | 417 | 615 | +47.5% | 112 to 284 | power given |
| pages read into the cache (misses) | 680,585 | 440,691 | -35.2% | -298,018 to -181,772 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.187 | -9.4% | -0.0526 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 376 | 337 | -10.2% | -110 to 33.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.141 | 0.126 | -10.3% | -0.0412 to 0.0123 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 188 | -5.8% | -16.4 to -6.69 | GAIN |
| the server's own CPU-seconds (mongod) | 196 | 184 | -6.1% | -16.8 to -7.14 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.56 | 3.94 | +10.9% | 0.31 to 0.462 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 376 | 337 | -10.2% | -110 to 33.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,873 | +0.0% | -2.61 to 2.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,884 | 2,884 | +0.0% | -3.83 to 3.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.362 | 0.356 | -1.5% | -0.0233 to 0.0126 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.581 | 0.577 | -0.7% | -0.0461 to 0.0374 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.218 | -2.1% | -0.0172 to 0.00795 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,409 | +175.2% | 810 to 984 | power given |
| bytes in the cache, mean (MB) | 417 | 1,105 | +164.7% | 621 to 753 | power given |
| pages read into the cache (misses) | 677,365 | 268,962 | -60.3% | -528,138 to -288,668 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.255 | +0.5% | -0.0103 to 0.0127 | EVEN, no difference beyond the noise |
| host CPU-seconds | 443 | 448 | +1.0% | -17.6 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.334 | 0.338 | +1.1% | -0.0129 to 0.02 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 279 | 273 | -2.2% | -23.9 to 11.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 276 | 269 | -2.5% | -24.5 to 10.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.69 | 3.37 | +25.2% | 0.544 to 0.809 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 443 | 448 | +1.0% | -17.6 to 26.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
