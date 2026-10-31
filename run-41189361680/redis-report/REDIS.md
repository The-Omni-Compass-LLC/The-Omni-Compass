# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 248 to 252 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00196 to 0.0604 | GAIN |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.32 | -3.8% | -0.328 to -0.0918 | GAIN |
| latency, 99th percentile (ms) | 5.65 | 5.61 | -0.7% | -0.06 to -0.0176 | GAIN |
| latency, mean (ms) | 1.59 | 0.719 | -54.9% | -0.887 to -0.863 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 236 | +268.0% | 168 to 175 | power given |
| memory used, mean (MB) | 57.2 | 199 | +248.1% | 141 to 142 | power given |
| keys evicted | 71,694 | 239 | -99.7% | -71,889 to -71,020 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0904 | -10.6% | -0.0894 to 0.0678 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.2 | 65.1 | -11.1% | -70.1 to 53.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.272 | -27.8% | -0.418 to 0.208 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 68.1 | 61 | -10.3% | -8.79 to -5.26 | GAIN |
| the server's own CPU-seconds (redis-server) | 8.51 | 7.6 | -10.7% | -1.46 to -0.362 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 59.5 | 52.9 | -11.0% | -7.85 to -5.26 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.441 |  | 0.421 to 0.461 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0685 | 0.0656 | -4.1% | -0.00411 to -0.00156 | shown, not judged |
| host CPU-seconds without steal | 73.2 | 65.1 | -11.1% | -70.1 to 53.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 196 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00125 to 0.000575 | EVEN, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 0.204 | -96.4% | -5.42 to -5.38 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.57 | -2.5% | -0.156 to -0.135 | GAIN |
| latency, mean (ms) | 0.976 | 0.255 | -73.8% | -0.742 to -0.7 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.6% | 249 to 253 | power given |
| keys evicted | 103,429 | 2,766 | -97.3% | -101,903 to -99,422 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.0976 | -10.2% | -0.116 to 0.0939 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 175 | -9.8% | -226 to 188 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.339 | 0.265 | -22.0% | -0.42 to 0.271 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 197 | 170 | -13.5% | -34.3 to -19 | GAIN |
| the server's own CPU-seconds (redis-server) | 25 | 22 | -12.0% | -4.13 to -1.85 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 147 | -14.5% | -31.4 to -18.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.23 |  | 1.17 to 1.29 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.197 | 0.193 | -1.8% | -0.0083 to 0.00115 | shown, not judged |
| host CPU-seconds without steal | 194 | 175 | -9.8% | -226 to 188 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.8% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.135 to 0.216 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0319 to 0.00625 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.39 | 5.3 | -1.8% | -0.21 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 1.21 | -41.4% | -0.863 to -0.841 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.2% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,086 | 0 | -100.0% | -243,577 to -242,594 | shown, not judged |
| host CPU busy (share of the run) | 0.0639 | 0.0679 | +6.2% | -0.00325 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 112 | 120 | +7.7% | -6.48 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.269 | 0.228 | -15.0% | -0.0689 to -0.0119 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 13.7 to 22.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 134 | 121 | -9.6% | -24.4 to -1.38 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.6 | 15.2 | -13.6% | -4.52 to -0.264 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 116 | 104 | -10.1% | -20.5 to -2.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.2 |  | 0.646 to 1.76 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.13 | 0.12 | -7.6% | -0.0432 to 0.0236 | shown, not judged |
| host CPU-seconds without steal | 112 | 120 | +7.7% | -6.48 to 23.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0346 to 0.00381 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.7 | -1.1% | -0.0747 to -0.0527 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.79 | -0.5% | -0.0475 to -0.0158 | GAIN |
| latency, mean (ms) | 1.35 | 0.593 | -56.1% | -0.774 to -0.741 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.5% | 271 to 301 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,037 | 2,397 | -98.3% | -138,356 to -132,925 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.115 | -21.8% | -0.0919 to 0.0277 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 194 | -22.3% | -171 to 59.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.469 | 0.311 | -33.6% | -0.36 to 0.044 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 296 | 257 | -13.2% | -44.3 to -33.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 31.8 | -12.6% | -6.71 to -2.43 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 259 | 223 | -14.0% | -39.3 to -33.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.74 |  | 1.3 to 2.19 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.241 | 0.229 | -4.9% | -0.0275 to 0.00371 | shown, not judged |
| host CPU-seconds without steal | 250 | 194 | -22.3% | -171 to 59.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
