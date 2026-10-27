# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,045 | 1,045 | -0.0% | -2.64 to 2.36 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0446 to 0.0138 | EVEN, no difference beyond the noise |
| cache hit rate | 0.698 | 0.697 | -0.0% | -0.000729 to 0.000578 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0076 to 0.00745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | +0.0% | -0.00144 to 0.00232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.64 | -0.1% | -0.0138 to 0.00911 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.1 | -1.3% | -0.86 to -0.86 | GAIN |
| memory used, mean (MB) | 56.9 | 57 | +0.1% | 0.0369 to 0.109 | power given |
| keys evicted | 49,885 | 50,552 | +1.3% | 507 to 827 | shown, not judged |
| host CPU busy (share of the run) | 0.0551 | 0.0494 | -10.3% | -0.0357 to 0.0243 | EVEN, no difference beyond the noise |
| host CPU-seconds | 25.7 | 22.9 | -10.9% | -17.5 to 11.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.183 | -10.8% | -0.139 to 0.095 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 32.6 | 32.6 | +0.1% | -0.663 to 0.703 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 4.72 | 4.73 | +0.1% | -0.105 to 0.119 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 27.9 | 27.7 | -0.5% | -0.91 to 0.619 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.16 |  | 0.141 to 0.179 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0313 | 0.03 | -4.0% | -0.00534 to 0.00283 | shown, not judged |
| host CPU-seconds without steal | 25.7 | 22.9 | -10.9% | -17.5 to 11.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,252 | 1,260 | +0.7% | 0.588 to 16.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00523 | EVEN, no difference beyond the noise |
| cache hit rate | 0.835 | 0.84 | +0.7% | 0.00055 to 0.0109 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00526 to 0.00917 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.00808 to 0.0243 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.08 | -2.7% | -0.056 to -0.00296 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.0908 to 2.1 | power given |
| memory used, mean (MB) | 61.3 | 61.7 | +0.8% | -0.37 to 1.32 | EVEN, no difference beyond the noise |
| keys evicted | 73,231 | 70,708 | -3.4% | -4,794 to -252 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.11 | -13.3% | -0.033 to -0.000556 | GAIN |
| host CPU-seconds | 142 | 121 | -14.9% | -41.4 to -1.07 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.379 | 0.321 | -15.5% | -0.114 to -0.00384 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 14.4 to 27.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 188 | 188 | +0.3% | -0.595 to 1.55 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.9 | 24.9 | -0.1% | -0.442 to 0.402 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 163 | 162 | -0.1% | -0.796 to 0.592 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.6 |  | 0.574 to 0.626 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.154 | 0.152 | -1.2% | -0.00601 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 142 | 121 | -14.9% | -41.4 to -1.07 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 837 | +0.6% | 4.97 to 5.66 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0461 to 0.0086 | EVEN, no difference beyond the noise |
| cache hit rate | 0.555 | 0.559 | +0.7% | 0.00352 to 0.00409 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0087 to 0.0147 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 5.46 | +1.7% | 0.0194 to 0.165 | LOSS |
| latency, mean (ms) | 2.37 | 2.36 | -0.6% | -0.0182 to -0.0113 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | 0.505 to 0.505 | power given |
| memory used, mean (MB) | 60.3 | 61 | +1.1% | 0.666 to 0.7 | power given |
| keys evicted | 185,099 | 180,275 | -2.6% | -4,948 to -4,699 | shown, not judged |
| host CPU busy (share of the run) | 0.063 | 0.0702 | +11.4% | -0.0316 to 0.046 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.8 | 82.5 | +11.8% | -40.3 to 57.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.329 | +11.1% | -0.163 to 0.229 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 87.2 | 89.3 | +2.4% | 0.514 to 3.72 | power given |
| the server's own CPU-seconds (redis-server) | 12.2 | 12.4 | +1.5% | -0.131 to 0.491 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.9 | 76.5 | +2.0% | 0.198 to 2.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.413 |  | 0.391 to 0.435 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0856 | 0.0835 | -2.5% | -0.00777 to 0.00348 | shown, not judged |
| host CPU-seconds without steal | 73.8 | 82.6 | +11.8% | -40.3 to 57.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,129 | 1,138 | +0.8% | 5.64 to 12.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0289 to 0.0221 | EVEN, no difference beyond the noise |
| cache hit rate | 0.754 | 0.759 | +0.8% | 0.00286 to 0.00854 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.00636 to 0.00562 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.28 | +0.2% | -0.109 to 0.124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.32 | -2.6% | -0.0471 to -0.0248 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.196 to 2.38 | power given |
| memory used, mean (MB) | 61.1 | 62.1 | +1.6% | 0.267 to 1.7 | power given |
| keys evicted | 106,840 | 104,006 | -2.7% | -5,273 to -396 | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0674 | -8.4% | -0.0438 to 0.0314 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.7 | 79.6 | -9.2% | -55.7 to 39.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.259 | 0.233 | -9.9% | -0.166 to 0.114 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 82.2 | 82.2 | -0.0% | -4.14 to 4.12 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.7 | 11.6 | -1.0% | -0.812 to 0.572 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 70.4 | 70.1 | -0.4% | -3.66 to 3.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.372 |  | 0.292 to 0.452 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0808 | 0.0755 | -6.6% | -0.0124 to 0.0018 | shown, not judged |
| host CPU-seconds without steal | 87.7 | 79.6 | -9.2% | -55.7 to 39.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
