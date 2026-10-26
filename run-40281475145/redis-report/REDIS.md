# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.18 to 0.395 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0769 to 0.072 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00143 to 0.000303 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.00292 to 0.00931 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.000328 to 0.0176 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.69 | 1.69 | +0.5% | 0.00159 to 0.016 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.1 | -2.9% | -3.38 to -0.364 | GAIN |
| memory used, mean (MB) | 57.1 | 56.2 | -1.6% | -2.53 to 0.705 | EVEN, no difference beyond the noise |
| keys evicted | 71,651 | 72,208 | +0.8% | -357 to 1,471 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.119 | -14.8% | -0.0698 to 0.0285 | EVEN, no difference beyond the noise |
| host CPU-seconds | 100 | 83.1 | -16.9% | -56.5 to 22.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.516 | 0.429 | -16.9% | -0.291 to 0.117 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 93.7 | 94.5 | +0.8% | -1.37 to 2.91 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.2 | 10.4 | +1.5% | -0.463 to 0.77 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 83.4 | 83.7 | +0.4% | -1.3 to 1.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.312 |  | 0.297 to 0.328 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0839 | 0.0843 | +0.5% | -0.000862 to 0.00173 | shown, not judged |
| host CPU-seconds without steal | 100 | 83.1 | -16.9% | -56.5 to 22.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,281 | +1.2% | -1.07 to 30.6 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00686 to 0.00328 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | -0.000815 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.00671 to 0.000106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | +0.0% | -0.0151 to 0.0202 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -4.9% | -0.106 to 0.00133 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -2.42 to 3.01 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.2 | -0.2% | -2.84 to 2.57 | EVEN, no difference beyond the noise |
| keys evicted | 103,370 | 96,908 | -6.3% | -13,804 to 882 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.115 | -7.8% | -0.0399 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 192 | -8.7% | -75.5 to 38.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.333 | -9.8% | -0.132 to 0.0602 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 10.2 to 37.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 283 | -0.5% | -4.72 to 1.83 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 37.8 | 37.2 | -1.4% | -1.71 to 0.631 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 246 | 244 | -0.8% | -5.02 to 1.29 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.957 |  | 0.923 to 0.991 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.234 | -0.7% | -0.00686 to 0.00373 | shown, not judged |
| host CPU-seconds without steal | 210 | 192 | -8.7% | -75.5 to 38.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 936 | +1.2% | 10 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0418 to 0.0318 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00657 to 0.00851 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.0% | 0.000486 to 0.0031 | LOSS |
| latency, 99th percentile (ms) | 5.75 | 5.77 | +0.2% | -0.000899 to 0.0277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.7% | -0.0437 to -0.0345 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.35 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.22 to 1.24 | power given |
| keys evicted | 243,220 | 234,998 | -3.4% | -8,858 to -7,588 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.145 | -2.0% | -0.0111 to 0.00519 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 243 | -2.2% | -21.8 to 10.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.597 | 0.576 | -3.4% | -0.0596 to 0.0192 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.3 |  | 9.46 to 15.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 313 | 312 | -0.3% | -2.26 to 0.442 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.7 | 35.3 | -1.0% | -0.721 to -0.0252 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 277 | 276 | -0.5% | -2.54 to -0.375 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.921 |  | 0.838 to 1 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.232 | -1.5% | -0.0134 to 0.00622 | shown, not judged |
| host CPU-seconds without steal | 248 | 243 | -2.2% | -21.8 to 10.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.9% | 3.37 to 17.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.01 to 0.00478 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00241 to 0.0117 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0116 to 0.00858 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00947 to 0.0144 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.28 | -2.7% | -0.0561 to -0.0162 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.0123 to 2.22 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | -0.34 to 1.97 | EVEN, no difference beyond the noise |
| keys evicted | 138,177 | 134,521 | -2.6% | -7,131 to -181 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.136 | -2.8% | -0.0206 to 0.0128 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 236 | -3.1% | -41 to 25.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.457 | 0.439 | -4.0% | -0.0785 to 0.0419 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 11 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 258 | 257 | -0.3% | -3.64 to 2.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 31.5 | 31.5 | -0.2% | -1.78 to 1.63 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 226 | 225 | -0.7% | -3.05 to -0.0518 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.897 |  | 0.839 to 0.954 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.218 | 0.215 | -1.3% | -0.00561 to -2.46e-05 | shown, not judged |
| host CPU-seconds without steal | 244 | 236 | -3.1% | -41 to 25.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
