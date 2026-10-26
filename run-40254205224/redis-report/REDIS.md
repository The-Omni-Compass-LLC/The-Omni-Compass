# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.848 to 0.155 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.057 to 0.0234 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00059 to 0.000144 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.55 | 5.55 | -0.0% | -0.00981 to 0.00463 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.0% | -0.00505 to 0.00822 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.62 | +0.1% | -0.00868 to 0.0114 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.57 to -1.23 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.7% | -0.574 to -0.234 | GAIN |
| keys evicted | 71,708 | 72,371 | +0.9% | 519 to 807 | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0915 | -2.3% | -0.0396 to 0.0354 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.9 | 63.5 | -2.2% | -30.4 to 27.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.328 | -2.1% | -0.157 to 0.142 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 79.9 | 80 | +0.1% | -0.676 to 0.859 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.1 | 10.2 | +0.7% | -0.00505 to 0.138 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 69.7 | 69.5 | -0.4% | -1.05 to 0.537 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.283 |  | 0.238 to 0.329 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0653 | 0.0634 | -2.9% | -0.00324 to -0.000579 | shown, not judged |
| host CPU-seconds without steal | 64.9 | 63.5 | -2.2% | -30.4 to 27.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 6.92 to 29.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00972 to 0.00381 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00458 to 0.0194 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.48 | -0.3% | -0.0298 to 2.33e-05 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.0% | -0.0144 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.956 | 0.891 | -6.7% | -0.0984 to -0.0301 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | -0.684 to 1.7 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% | -0.846 to 1.46 | EVEN, no difference beyond the noise |
| keys evicted | 103,441 | 95,579 | -7.6% | -12,839 to -2,885 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0917 | -11.2% | -0.0256 to 0.00249 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 160 | -12.1% | -48.2 to 4.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.32 | 0.277 | -13.4% | -0.0864 to 0.00103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 190 | 188 | -1.0% | -2.3 to -1.62 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.9 | 25.6 | -1.1% | -0.935 to 0.388 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 164 | 161 | -1.5% | -2.72 to -2.04 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.698 |  | 0.66 to 0.735 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.16 | -2.8% | -0.00983 to 0.00079 | shown, not judged |
| host CPU-seconds without steal | 182 | 160 | -12.1% | -48.2 to 4.15 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 935 | +1.0% | -6.44 to 24.8 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0357 to 0.049 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.623 | +1.0% | -0.00427 to 0.0166 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0121 to 0.0176 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.0146 to 0.0359 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.4% | -0.0769 to 0.0156 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.8% | -0.286 to 2.63 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 61.5 | +1.3% | -0.203 to 1.84 | EVEN, no difference beyond the noise |
| keys evicted | 243,212 | 241,242 | -0.8% | -4,437 to 496 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.148 | +1.0% | -0.0256 to 0.0286 | EVEN, no difference beyond the noise |
| host CPU-seconds | 247 | 250 | +1.2% | -52.7 to 58.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.592 | 0.593 | +0.3% | -0.141 to 0.144 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 309 | 310 | +0.3% | -7.52 to 9.25 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.2 | 35.7 | +1.2% | -0.978 to 1.84 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 273 | 273 | -0.2% | -7.49 to 6.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.943 |  | 0.899 to 0.986 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.233 | -1.8% | -0.0382 to 0.0297 | shown, not judged |
| host CPU-seconds without steal | 247 | 250 | +1.2% | -52.7 to 58.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 10.5 to 17.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.016 to 0.0029 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00866 to 0.0105 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0106 to 0.00992 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.29 | +0.2% | -0.0224 to 0.0419 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.8% | -0.0669 to -0.0219 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.1 | +3.2% | 1.23 to 2.9 | power given |
| memory used, mean (MB) | 61.2 | 62.7 | +2.4% | 0.826 to 2.16 | power given |
| keys evicted | 138,258 | 132,610 | -4.1% | -6,275 to -5,020 | shown, not judged |
| host CPU busy (share of the run) | 0.0606 | 0.0636 | +4.9% | -0.0346 to 0.0405 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 112 | +5.0% | -64.6 to 75.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.201 | 0.208 | +3.7% | -0.124 to 0.139 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 124 | +1.4% | -4.27 to 7.59 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.1 | 17.2 | +0.5% | -0.33 to 0.503 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 106 | +1.0% | -4.84 to 6.87 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.563 |  | 0.433 to 0.694 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.123 | -2.7% | -0.0205 to 0.0137 | shown, not judged |
| host CPU-seconds without steal | 107 | 112 | +5.0% | -64.6 to 75.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
