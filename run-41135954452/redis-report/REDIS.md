# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 245 to 256 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0701 to 0.0293 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.7% | -0.0418 to -0.0358 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0283 to -0.00529 | GAIN |
| latency, mean (ms) | 1.71 | 0.792 | -53.8% | -0.953 to -0.889 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.9% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,788 | 77.7 | -99.9% | -72,537 to -70,885 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.12 | -11.9% | -0.0654 to 0.0332 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.1 | 83 | -10.8% | -48.8 to 28.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.481 | 0.348 | -27.7% | -0.318 to 0.0519 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 110 | 93.9 | -14.6% | -17.7 to -14.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 13 | 11.3 | -13.0% | -2.02 to -1.36 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 96.8 | 81.9 | -15.4% | -16.8 to -13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.577 |  | 0.493 to 0.661 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0871 | 0.0832 | -4.5% | -0.00684 to -0.000974 | shown, not judged |
| host CPU-seconds without steal | 93.1 | 83 | -10.8% | -48.8 to 28.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,465 | +15.6% | 196 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00389 to -0.00123 | LOSS |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.23 | -96.0% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.73 | -1.2% | -0.0752 to -0.06 | GAIN |
| latency, mean (ms) | 1.04 | 0.305 | -70.6% | -0.739 to -0.729 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.6% | 270 to 276 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 247 to 256 | power given |
| keys evicted | 103,151 | 2,707 | -97.4% | -101,409 to -99,480 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.121 | -0.1% | -0.036 to 0.0358 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 209 | +2.7% | -62.4 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.317 | -11.2% | -0.158 to 0.0787 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 277 | 241 | -12.9% | -36.9 to -34.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 31.9 | -10.2% | -5.41 to -1.86 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 208 | -13.9% | -35.3 to -31.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.4 |  | 1.17 to 1.63 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.227 | 0.214 | -5.9% | -0.0208 to -0.00609 | shown, not judged |
| host CPU-seconds without steal | 203 | 209 | +2.7% | -62.4 to 73.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0152 to 0.0204 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.783 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.61 | -0.5% | -0.0303 to -0.0241 | GAIN |
| latency, 99th percentile (ms) | 5.69 | 5.68 | -0.1% | -0.00978 to -0.00526 | GAIN |
| latency, mean (ms) | 2.23 | 1.33 | -40.2% | -0.897 to -0.894 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +389.9% | 245 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,037 | 0 | -100.0% | -243,519 to -242,555 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.136 | -14.0% | -0.0498 to 0.00543 | EVEN, no difference beyond the noise |
| host CPU-seconds | 276 | 237 | -14.0% | -95.1 to 18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.662 | 0.449 | -32.1% | -0.331 to -0.0941 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 14.9 to 22.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 282 | 248 | -12.0% | -35.8 to -32 | GAIN |
| the server's own CPU-seconds (redis-server) | 31.8 | 28.4 | -10.5% | -3.6 to -3.07 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 250 | 218 | -12.8% | -33.7 to -30.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.47 |  | 1.29 to 1.65 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.217 | 0.21 | -3.3% | -0.0102 to -0.00402 | shown, not judged |
| host CPU-seconds without steal | 276 | 237 | -14.0% | -95.1 to 18 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0059 to -0.00283 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.5 | -2.1% | -0.138 to -0.102 | GAIN |
| latency, 99th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0411 to -0.0145 | GAIN |
| latency, mean (ms) | 1.28 | 0.543 | -57.5% | -0.755 to -0.713 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.4% | 278 to 292 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,095 | 2,690 | -98.1% | -137,751 to -133,059 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.101 | -10.3% | -0.0747 to 0.0515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 178 | -9.6% | -142 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.286 | -22.8% | -0.289 to 0.121 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 211 | 187 | -11.3% | -29.4 to -18.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.9 | 22 | -11.8% | -3.46 to -2.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 186 | 163 | -12.0% | -27.1 to -17.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.27 |  | 1.15 to 1.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.191 | 0.189 | -1.5% | -0.00848 to 0.0029 | shown, not judged |
| host CPU-seconds without steal | 197 | 178 | -9.6% | -142 to 104 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
