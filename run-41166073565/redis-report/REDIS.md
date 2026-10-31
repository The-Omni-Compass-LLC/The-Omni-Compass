# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0198 to 0.0351 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.65 | -0.7% | -0.0407 to -0.0367 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0188 to -0.0155 | GAIN |
| latency, mean (ms) | 1.71 | 0.786 | -54.0% | -0.941 to -0.907 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.1% | 162 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,740 | 76.3 | -99.9% | -72,461 to -70,867 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.113 | -26.8% | -0.078 to -0.00459 | GAIN |
| host CPU-seconds | 108 | 77.7 | -28.1% | -60.8 to -0.0536 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.558 | 0.325 | -41.7% | -0.404 to -0.0615 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.01 to 24.7 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 109 | 92.5 | -15.3% | -18.3 to -15.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 13 | 11.2 | -13.2% | -1.83 to -1.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 96.2 | 80.6 | -16.2% | -17.1 to -14 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.58 |  | 0.512 to 0.648 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0879 | 0.0831 | -5.5% | -0.00803 to -0.00172 | shown, not judged |
| host CPU-seconds without steal | 108 | 77.7 | -28.1% | -60.8 to -0.0561 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00684 to 0.00169 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 0.252 | -95.5% | -5.6 to -4.99 | GAIN |
| latency, 99th percentile (ms) | 5.64 | 5.52 | -2.2% | -0.128 to -0.122 | GAIN |
| latency, mean (ms) | 0.982 | 0.263 | -73.2% | -0.733 to -0.706 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.2% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 253 | power given |
| keys evicted | 103,418 | 2,756 | -97.3% | -102,123 to -99,199 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.097 | -10.0% | -0.0329 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 170 | -9.4% | -60.8 to 25.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.259 | -21.7% | -0.144 to 0.000636 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 207 | 182 | -12.1% | -31.6 to -18.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 27.7 | 24.1 | -13.0% | -4.56 to -2.63 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 156 | -12.7% | -28.1 to -17.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.25 |  | 0.848 to 1.65 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.175 | 0.171 | -2.4% | -0.0142 to 0.00586 | shown, not judged |
| host CPU-seconds without steal | 188 | 170 | -9.4% | -60.8 to 25.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.8% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0109 to 0.00295 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0141 to -0.00408 | GAIN |
| latency, 99th percentile (ms) | 5.33 | 5.27 | -1.2% | -0.154 to 0.0258 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 1.2 | -41.4% | -0.852 to -0.847 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,124 | 0 | -100.0% | -243,609 to -242,638 | shown, not judged |
| host CPU busy (share of the run) | 0.0601 | 0.0594 | -1.2% | -0.0524 to 0.051 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 105 | -0.0% | -97.4 to 97.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.199 | -21.2% | -0.235 to 0.128 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 122 | -6.7% | -12.8 to -4.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.5 | 15.5 | -11.0% | -2.43 to -1.4 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 113 | 105 | -7.1% | -11.5 to -4.64 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 0.869 to 1.58 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.132 | 0.126 | -4.6% | -0.0161 to 0.00412 | shown, not judged |
| host CPU-seconds without steal | 105 | 105 | -0.0% | -97.4 to 97.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 195 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.045 to -0.0121 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.13 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.9% | -0.0552 to -0.0497 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.77 | -0.3% | -0.0252 to -0.0142 | GAIN |
| latency, mean (ms) | 1.34 | 0.587 | -56.3% | -0.783 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.9% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 321 | +423.8% | 244 to 275 | power given |
| keys evicted | 138,148 | 2,380 | -98.3% | -139,407 to -132,128 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.134 | -15.4% | -0.055 to 0.00627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 273 | 232 | -15.1% | -104 to 21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.513 | 0.372 | -27.5% | -0.25 to -0.0323 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 250 | -14.1% | -43 to -38.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.8 | 30.4 | -12.7% | -5.37 to -3.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 217 | -14.9% | -40.5 to -35.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.4 to 1.83 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.252 | 0.241 | -4.2% | -0.015 to -0.0062 | shown, not judged |
| host CPU-seconds without steal | 273 | 232 | -15.1% | -104 to 21 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
