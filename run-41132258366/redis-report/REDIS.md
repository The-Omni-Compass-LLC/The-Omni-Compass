# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0206 to 0.0406 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.5% | -0.0668 to 0.0081 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.2% | -0.0451 to 0.0266 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.817 | -53.0% | -0.945 to -0.899 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.4% | 163 to 197 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.9% | 141 to 145 | power given |
| keys evicted | 71,754 | 76 | -99.9% | -72,546 to -70,809 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.142 | +2.2% | -0.0183 to 0.0245 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.3 | 98.6 | +5.7% | -11.4 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.413 | -14.3% | -0.151 to 0.0131 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 106 | -12.8% | -20.8 to -10.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.7 | 13.2 | -10.2% | -2 to -0.984 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106 | 91.7 | -13.7% | -19.4 to -9.84 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.64 |  | 0.43 to 0.849 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0943 | 0.091 | -3.5% | -0.00863 to 0.00193 | shown, not judged |
| host CPU-seconds without steal | 93.3 | 98.6 | +5.7% | -11.4 to 22 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 193 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0168 to 0.00234 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.129 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.237 | -95.9% | -5.51 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.72 | -1.3% | -0.0939 to -0.0565 | GAIN |
| latency, mean (ms) | 1.04 | 0.306 | -70.7% | -0.763 to -0.715 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.5% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,445 | 2,637 | -97.5% | -103,106 to -98,510 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.11 | -18.5% | -0.0556 to 0.00558 | EVEN, no difference beyond the noise |
| host CPU-seconds | 230 | 188 | -18.4% | -101 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.285 | -29.5% | -0.214 to -0.0236 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 241 | -13.1% | -39.8 to -32.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.8 | -10.1% | -5.84 to -1.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 207 | -14.2% | -35.6 to -32.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.49 |  | 1.17 to 1.81 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.222 | -3.2% | -0.017 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 230 | 188 | -18.4% | -101 to 16.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00569 to 0.0172 | GAIN |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.66 | -0.4% | -0.0353 to -0.0157 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0171 to 0.003 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.9% | -0.906 to -0.895 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.7% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,084 | 0 | -100.0% | -243,447 to -242,721 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.126 | -15.1% | -0.0619 to 0.017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 213 | -14.9% | -114 to 39.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.601 | 0.404 | -32.9% | -0.369 to -0.026 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 307 | 271 | -11.7% | -38.7 to -33.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.8 | 31.4 | -9.7% | -4.39 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 272 | 238 | -12.5% | -35.7 to -32.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.32 to 1.69 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.225 | -4.0% | -0.0129 to -0.00554 | shown, not judged |
| host CPU-seconds without steal | 250 | 213 | -14.9% | -114 to 39.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00334 to 0.00534 | EVEN, the same |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.59 | -2.1% | -0.209 to -0.0323 | GAIN |
| latency, 99th percentile (ms) | 5.78 | 5.72 | -1.0% | -0.111 to -0.00866 | GAIN |
| latency, mean (ms) | 1.31 | 0.551 | -58.0% | -0.791 to -0.73 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.3% | 276 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,259 | 2,716 | -98.0% | -137,820 to -133,265 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.104 | -25.0% | -0.0664 to -0.00315 | GAIN |
| host CPU-seconds | 247 | 184 | -25.5% | -128 to 1.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.464 | 0.295 | -36.4% | -0.268 to -0.0698 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 237 | 195 | -18.1% | -67.3 to -18.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.4 | 21.1 | -16.9% | -5.84 to -2.78 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 212 | 172 | -18.8% | -62.8 to -16.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.31 |  | 1.2 to 1.43 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.208 | -6.7% | -0.0285 to -0.00134 | shown, not judged |
| host CPU-seconds without steal | 247 | 184 | -25.5% | -128 to 1.74 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
