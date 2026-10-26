# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,071 | 1,072 | +0.1% | -6.34 to 8.66 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,499 | -0.1% | -4.98 to 3.09 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00151 to 0.000891 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0155 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.49 | 6.13 | -5.5% | -3.42 to 2.71 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.78 | 1.79 | +0.2% | -0.0971 to 0.105 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.3 | -4.2% | -4.8 to -0.551 | GAIN |
| memory used, mean (MB) | 57.2 | 55.4 | -3.0% | -3.83 to 0.427 | EVEN, no difference beyond the noise |
| keys evicted | 71,726 | 71,966 | +0.3% | -318 to 798 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.141 | -2.1% | -0.0418 to 0.0357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.9 | 94.5 | -2.5% | -34.1 to 29.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.503 | 0.489 | -2.6% | -0.176 to 0.15 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 126 | 126 | +0.0% | -4.92 to 4.92 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.4 | 15.5 | +0.8% | -0.379 to 0.626 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 110 | -0.5% | -4.98 to 3.95 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.398 |  | 0.355 to 0.442 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0984 | 0.0963 | -2.1% | -0.0142 to 0.0101 | shown, not judged |
| host CPU-seconds without steal | 96.9 | 94.5 | -2.5% | -34.1 to 29.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,282 | +1.2% | 1.61 to 28.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00887 to 0.00166 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.00103 to 0.0192 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.0155 to 0.0116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.0% | -0.00277 to 0.00464 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.998 | -5.0% | -0.104 to -0.00161 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.49 to 2.47 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | -0.202 to 1.58 | EVEN, no difference beyond the noise |
| keys evicted | 103,497 | 96,906 | -6.4% | -12,722 to -461 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.102 | -10.7% | -0.0464 to 0.022 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 168 | -11.7% | -84.8 to 40.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.292 | -12.7% | -0.151 to 0.0657 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 13.1 to 25.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 276 | -0.5% | -4.88 to 2.28 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 36.8 | 36.6 | -0.5% | -1.81 to 1.47 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 238 | -0.8% | -5.68 to 1.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.918 |  | 0.865 to 0.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.226 | -2.0% | -0.01 to 0.000673 | shown, not judged |
| host CPU-seconds without steal | 191 | 168 | -11.7% | -84.8 to 40.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.2% | 8.24 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.27 to 0.278 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00645 to 0.00888 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0236 to 0.0317 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.39 | +1.0% | -0.116 to 0.224 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.02 | -1.7% | -0.0582 to -0.0112 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.13 to 1.82 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.1 to 1.4 | power given |
| keys evicted | 243,204 | 235,950 | -3.0% | -11,138 to -3,369 | shown, not judged |
| host CPU busy (share of the run) | 0.0608 | 0.0656 | +7.8% | -0.0426 to 0.0521 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 115 | +7.8% | -79.9 to 96.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.257 | 0.274 | +6.5% | -0.195 to 0.228 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 7.08 to 19.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 128 | 132 | +2.9% | -17.1 to 24.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.4 | 17.7 | +1.7% | -2.27 to 2.86 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 113 | +2.6% | -15.3 to 20.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.599 |  | 0.455 to 0.742 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.125 | 0.127 | +1.1% | -0.0114 to 0.0142 | shown, not judged |
| host CPU-seconds without steal | 107 | 115 | +7.8% | -79.9 to 96.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,197 | +1.2% | 12.3 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.01 to 0.00216 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00798 to 0.0108 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | -0.0% | -0.0161 to 0.0128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00745 to 0.0112 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -4.0% | -0.0584 to -0.0414 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.64 to 1.75 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.15 to 1.24 | power given |
| keys evicted | 138,297 | 132,793 | -4.0% | -6,447 to -4,561 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -1.9% | -0.017 to 0.013 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 179 | -2.1% | -32.9 to 25.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.332 | -3.2% | -0.0653 to 0.0432 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 192 | 192 | -0.2% | -1.46 to 0.712 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.3 | 24.4 | +0.1% | -0.472 to 0.505 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 168 | 167 | -0.7% | -1.62 to -0.604 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.725 |  | 0.626 to 0.824 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.166 | 0.163 | -1.9% | -0.00809 to 0.00189 | shown, not judged |
| host CPU-seconds without steal | 182 | 179 | -2.1% | -32.9 to 25.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
