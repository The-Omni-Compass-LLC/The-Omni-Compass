# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,914 | 2,915 | +0.0% | -0.621 to 2.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,918 | +0.0% | -0.363 to 2.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.22 | 0.216 | -1.8% | -0.0203 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.419 | 0.424 | +1.0% | -0.0247 to 0.0333 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.115 | 0.114 | -1.0% | -0.00383 to 0.0015 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 419 | 420 | +0.3% | -3.24 to 5.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 707,592 | 731,815 | +3.4% | -119,860 to 168,305 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.125 | -9.9% | -0.0175 to -0.0102 | GAIN |
| host CPU-seconds | 252 | 224 | -11.1% | -39.3 to -16.9 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.168 | -11.2% | -0.0295 to -0.0126 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 109 | 109 | -0.2% | -2.27 to 1.79 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 106 | 106 | -0.8% | -2.88 to 1.24 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.28 | 2.86 | +25.5% | 0.534 to 0.628 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 252 | 224 | -11.1% | -39.3 to -16.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,879 | -0.0% | -9.62 to 7.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% | -8.17 to 6.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.416 | 0.419 | +0.7% | -0.0187 to 0.0247 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.588 | 0.594 | +1.0% | -0.0419 to 0.0539 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.218 | +1.7% | -0.00637 to 0.0136 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 404 | 403 | -0.3% | -5.82 to 3.54 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 274,581 | 273,028 | -0.6% | -69,074 to 65,968 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.209 | +16.9% | -0.0664 to 0.127 | EVEN, no difference beyond the noise |
| host CPU-seconds | 122 | 147 | +20.7% | -54.3 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.277 | +20.7% | -0.102 to 0.197 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.1 | 83.5 | +1.7% | -3.22 to 6.05 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81 | 82.2 | +1.4% | -3.28 to 5.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.02 | 1.28 | +25.1% | 0.061 to 0.451 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 122 | 147 | +20.7% | -54.3 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,904 | +0.0% | -10.1 to 11.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,913 | +0.0% | -7.27 to 9.05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.231 | 0.226 | -2.2% | -0.0599 to 0.0499 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.503 | 0.509 | +1.1% | -0.0729 to 0.0836 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.152 | -1.6% | -0.0196 to 0.0147 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 897 | +75.2% | -14.5 to 785 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 713 | +70.4% | -17.3 to 607 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 714,129 | 386,530 | -45.9% | -606,070 to -49,127 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.158 | -2.2% | -0.06 to 0.0528 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 285 | -2.2% | -126 to 113 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.214 | -2.2% | -0.0947 to 0.0849 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 150 | 146 | -2.7% | -22.7 to 14.7 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 148 | 143 | -3.1% | -23.2 to 14 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.11 | 2.68 | +27.2% | 0.435 to 0.711 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 291 | 285 | -2.2% | -126 to 113 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,746 | 5,742 | -0.1% | -17.1 to 9.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,760 | 5,756 | -0.1% | -16.3 to 8.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.359 | 0.352 | -1.9% | -0.0118 to -0.0015 | GAIN |
| latency, 99th percentile (ms) | 0.565 | 0.558 | -1.2% | -0.0192 to 0.00584 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.19 | -2.2% | -0.00543 to -0.00315 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,403 | +174.1% | 741 to 1,041 | power given |
| bytes in the cache, mean (MB) | 417 | 1,101 | +164.0% | 574 to 794 | power given |
| pages read into the cache (misses) | 691,006 | 257,118 | -62.8% | -515,606 to -352,170 | shown, not judged |
| host CPU busy (share of the run) | 0.26 | 0.268 | +3.3% | -0.0087 to 0.0257 | EVEN, no difference beyond the noise |
| host CPU-seconds | 470 | 494 | +5.1% | -18.4 to 66.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.177 | 0.186 | +5.2% | -0.00637 to 0.0246 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 276 | 267 | -3.2% | -10.5 to -7.09 | GAIN |
| the server's own CPU-seconds (mongod) | 272 | 263 | -3.4% | -11 to -7.68 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.31 | 4.87 | +13.0% | 0.538 to 0.584 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 470 | 494 | +5.1% | -18.4 to 66.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,897 | +0.0% | -0.856 to 2.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,907 | +0.0% | -0.382 to 1.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.331 | -6.5% | -0.0385 to -0.00749 | GAIN |
| latency, 99th percentile (ms) | 0.614 | 0.599 | -2.4% | -0.0367 to 0.00666 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.152 | -6.1% | -0.0195 to -9.55e-05 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,606 | +213.7% | 1,074 to 1,114 | power given |
| bytes in the cache, mean (MB) | 417 | 1,235 | +196.0% | 804 to 831 | power given |
| pages read into the cache (misses) | 680,649 | 125,495 | -81.6% | -568,720 to -541,588 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.4% | -0.0333 to 0.0319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 342 | +0.6% | -71.1 to 75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.257 | +0.6% | -0.0533 to 0.0562 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 193 | 179 | -7.2% | -14.8 to -13.1 | GAIN |
| the server's own CPU-seconds (mongod) | 190 | 176 | -7.6% | -15.4 to -13.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 3.08 | +24.8% | 0.45 to 0.773 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 340 | 342 | +0.6% | -71.1 to 75 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
