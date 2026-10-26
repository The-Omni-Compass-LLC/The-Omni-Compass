# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.72 to 1.35 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.158 to 0.0817 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00197 to 0.0015 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.0% | -0.00799 to 0.00872 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% | -0.00385 to 0.028 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% | 0.00409 to 0.0123 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.3 | -2.6% | -1.86 to -1.53 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.854 to -0.526 | GAIN |
| keys evicted | 71,738 | 72,379 | +0.9% | 209 to 1,073 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.135 | -5.9% | -0.053 to 0.0362 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.3 | 90 | -6.5% | -39.9 to 27.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.497 | 0.465 | -6.5% | -0.207 to 0.142 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 123 | +0.1% | -1.95 to 2.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.4 | 15.3 | -0.8% | -0.544 to 0.311 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 108 | -0.2% | -1.76 to 1.43 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.394 |  | 0.356 to 0.431 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0957 | 0.0947 | -1.1% | -0.00707 to 0.00498 | shown, not judged |
| host CPU-seconds without steal | 96.3 | 90 | -6.5% | -39.9 to 27.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,282 | +1.2% | 0.236 to 30.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0145 to 0.00996 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.00028 to 0.0205 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0224 to 0.00952 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.83 | 5.83 | +0.0% | -0.0257 to 0.0292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -5.1% | -0.103 to -0.00595 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | -0.622 to 2.4 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -0.179 to 1.05 | EVEN, no difference beyond the noise |
| keys evicted | 103,556 | 96,760 | -6.6% | -13,603 to 11.4 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.118 | -5.2% | -0.0413 to 0.0283 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 196 | -5.7% | -78.6 to 54.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.339 | -6.9% | -0.14 to 0.0898 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 12.4 to 29.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 287 | -0.4% | -7.43 to 5.03 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 38.4 | 38.3 | -0.1% | -1.94 to 1.84 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 247 | -0.9% | -6.8 to 2.53 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.986 |  | 0.916 to 1.06 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.242 | 0.237 | -1.9% | -0.0176 to 0.00833 | shown, not judged |
| host CPU-seconds without steal | 208 | 196 | -5.7% | -78.6 to 54.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.1 to 13.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00553 to 0.00684 | EVEN, the same |
| cache hit rate | 0.618 | 0.625 | +1.3% | 0.00694 to 0.00883 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.0% | -0.000502 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.57 | +0.1% | 0.00381 to 0.00664 | LOSS |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% | -0.0503 to -0.0297 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.916 to 1.93 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.985 to 1.47 | power given |
| keys evicted | 243,043 | 236,704 | -2.6% | -14,909 to 2,231 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.105 | -2.4% | -0.058 to 0.0527 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 183 | -2.7% | -114 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.435 | -4.0% | -0.277 to 0.241 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 11.5 to 16.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 204 | 205 | +0.2% | -1.4 to 2.16 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.6 | 24.4 | -0.6% | -0.195 to -0.119 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 179 | -0.1% | -1.84 to 1.53 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.702 |  | 0.642 to 0.761 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.163 | 0.159 | -2.1% | -0.00556 to -0.00121 | shown, not judged |
| host CPU-seconds without steal | 189 | 183 | -2.7% | -114 to 103 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 5.84 to 20.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.02 to 0.0196 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00482 to 0.0122 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0394 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.1% | -0.0923 to 0.0819 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.9% | -0.0692 to -0.0233 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.981 to 2.36 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 0.532 to 1.83 | power given |
| keys evicted | 138,152 | 133,247 | -3.6% | -7,387 to -2,423 | shown, not judged |
| host CPU busy (share of the run) | 0.064 | 0.0581 | -9.2% | -0.024 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 102 | -9.8% | -45 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.213 | 0.19 | -10.8% | -0.0873 to 0.0412 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124 | 123 | -0.6% | -14.8 to 13.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.3 | 17.2 | -0.6% | -2.73 to 2.53 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 105 | -1.2% | -12.6 to 10.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.576 |  | 0.51 to 0.641 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.124 | -3.1% | -0.0261 to 0.0182 | shown, not judged |
| host CPU-seconds without steal | 113 | 102 | -9.8% | -45 to 22.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
