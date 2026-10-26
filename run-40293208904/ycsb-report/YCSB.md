# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,910 | +0.2% | -6.13 to 15.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,915 | +0.1% | -6.31 to 14.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.219 | 0.208 | -5.0% | -0.0372 to 0.0152 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.375 | -3.4% | -0.0227 to -0.00393 | GAIN |
| latency, mean (ms) | 0.156 | 0.152 | -2.5% | -0.0123 to 0.00439 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 556 | +8.5% | -20 to 107 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 450 | +8.1% | -11.9 to 79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,493 | 652,271 | -8.5% | -138,382 to 17,937 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.151 | -11.3% | -0.0451 to 0.00686 | EVEN, no difference beyond the noise |
| host CPU-seconds | 310 | 270 | -13.0% | -91.3 to 10.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.202 | -13.0% | -0.0685 to 0.00804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 3.54 to 11.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 150 | 148 | -1.3% | -5.3 to 1.31 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 148 | 146 | -1.6% | -5.78 to 0.918 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.03 | 2.46 | +21.6% | 0.39 to 0.486 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 310 | 270 | -13.0% | -91.3 to 10.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,942 | 2,942 | +0.0% | -2.76 to 2.79 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,945 | +0.0% | -2.97 to 3.36 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.227 | 0.225 | -1.2% | -0.0235 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.347 | 0.339 | -2.1% | -0.05 to 0.0353 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0697 | 0.0692 | -0.8% | -0.00589 to 0.00475 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -5.63 to -4.63 | GAIN |
| bytes in the cache, mean (MB) | 405 | 402 | -0.8% | -22.7 to 16.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,775 | 260,779 | -2.2% | -27,280 to 15,288 | shown, not judged |
| host CPU busy (share of the run) | 0.0738 | 0.0772 | +4.6% | -0.0538 to 0.0606 | EVEN, no difference beyond the noise |
| host CPU-seconds | 53.5 | 56.1 | +4.9% | -42 to 47.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0997 | 0.105 | +4.9% | -0.0783 to 0.088 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 21.4 | 21.5 | +0.2% | -0.884 to 0.971 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 20.9 | 20.8 | -0.4% | -1.02 to 0.856 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.552 | 0.679 | +22.9% | 0.0955 to 0.158 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 53.5 | 56.1 | +4.9% | -42 to 47.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,887 | +0.0% | -1.52 to 2.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | +0.0% | -0.186 to 0.262 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.304 | +1.0% | -0.00942 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.57 | -0.3% | -0.0153 to 0.012 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.192 | +1.5% | -0.00451 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 519 | +1.3% | -29.5 to 43 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 426 | +1.9% | -21.4 to 37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,475 | 726,034 | +7.0% | -124,975 to 220,093 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.166 | -16.7% | -0.115 to 0.0484 | EVEN, no difference beyond the noise |
| host CPU-seconds | 354 | 283 | -19.9% | -237 to 95.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.213 | -19.9% | -0.178 to 0.0721 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -3.51 to 10.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 182 | 186 | +2.5% | 0.539 to 8.62 | power given |
| the server's own CPU-seconds (mongod) | 179 | 183 | +2.3% | -0.115 to 8.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.46 | 3.01 | +22.1% | 0.391 to 0.695 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 354 | 283 | -19.9% | -237 to 95.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,827 | 5,825 | -0.0% | -8.09 to 4.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,836 | 5,834 | -0.0% | -8.03 to 4.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.181 | 0.182 | +0.6% | -0.0211 to 0.0231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.397 | -0.7% | -0.0501 to 0.0448 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0911 | 0.0911 | -0.0% | -0.00887 to 0.00886 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 527 | +3.0% | -46.3 to 77.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 432 | +3.1% | -34.7 to 60.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,830 | 680,449 | -2.9% | -101,404 to 60,642 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.13 | -12.3% | -0.104 to 0.0676 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 232 | -14.9% | -220 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.102 | 0.0867 | -14.9% | -0.0822 to 0.0519 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 133 | 134 | +0.8% | -10.8 to 13 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 130 | 131 | +0.4% | -11.3 to 12.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.91 | 3.5 | +20.4% | 0.455 to 0.732 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 272 | 232 | -14.9% | -220 to 139 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,870 | +0.1% | -11.9 to 17.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,880 | 2,882 | +0.1% | -14.4 to 19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.39 | 0.386 | -1.0% | -0.0557 to 0.0477 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.675 | 0.665 | -1.5% | -0.0984 to 0.0784 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.23 | +0.6% | -0.0233 to 0.0258 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 557 | +8.9% | -96.7 to 188 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 452 | +8.3% | -75.5 to 145 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,794 | 628,291 | -7.3% | -212,828 to 113,823 | shown, not judged |
| host CPU busy (share of the run) | 0.261 | 0.268 | +2.7% | -0.0525 to 0.0666 | EVEN, no difference beyond the noise |
| host CPU-seconds | 461 | 476 | +3.2% | -110 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.349 | 0.36 | +3.1% | -0.0825 to 0.104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 12 |  | 12 to 12 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 280 | +1.1% | -22.9 to 28.8 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 274 | 277 | +0.9% | -22.9 to 27.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.2 | +22.2% | -0.0319 to 1.2 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 461 | 476 | +3.2% | -110 to 140 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
