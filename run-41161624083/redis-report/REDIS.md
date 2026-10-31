# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0857 to 0.0778 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.164 to 0.171 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.6% | -0.0559 to -0.0122 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.79 | -0.3% | -0.0448 to 0.00588 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.814 | -53.3% | -0.94 to -0.917 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,790 | 75 | -99.9% | -72,753 to -70,677 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.129 | -19.7% | -0.0682 to 0.0049 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 88 | -20.1% | -52.3 to 8.04 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.568 | 0.368 | -35.2% | -0.36 to -0.0405 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 105 | -14.1% | -20.1 to -14.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.3 | 13.2 | -13.9% | -3.08 to -1.17 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 91 | -14.8% | -17.8 to -13.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.691 |  | 0.518 to 0.864 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0944 | 0.0907 | -4.0% | -0.0115 to 0.004 | shown, not judged |
| host CPU-seconds without steal | 110 | 88 | -20.1% | -52.3 to 8.04 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,465 | +15.6% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0062 to -0.00075 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.243 | -95.8% | -5.53 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.3% | -0.103 to -0.0489 | GAIN |
| latency, mean (ms) | 1.05 | 0.313 | -70.3% | -0.756 to -0.723 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.5% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 255 | power given |
| keys evicted | 103,267 | 2,637 | -97.4% | -101,683 to -99,578 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.107 | -27.0% | -0.116 to 0.0375 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 180 | -27.9% | -214 to 75.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.273 | -37.6% | -0.398 to 0.0686 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 285 | 247 | -13.1% | -48.4 to -26.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.9 | 32.9 | -11.0% | -5.29 to -2.87 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 213 | -14.1% | -46.3 to -23.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.67 |  | 1.46 to 1.87 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.257 | 0.246 | -4.3% | -0.0252 to 0.0033 | shown, not judged |
| host CPU-seconds without steal | 250 | 180 | -27.9% | -214 to 75.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,172 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0591 to 0.0386 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.48 | -0.8% | -0.0621 to -0.0256 | GAIN |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.3% | -0.0398 to 0.00436 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.16 | 1.28 | -40.8% | -0.893 to -0.87 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +389.9% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,194 | 0 | -100.0% | -243,839 to -242,549 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.111 | -10.2% | -0.0573 to 0.032 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 197 | -9.8% | -112 to 68.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.524 | 0.373 | -28.9% | -0.338 to 0.0353 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 15.8 to 21.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 219 | 195 | -10.9% | -30.6 to -17.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.4 | 22.6 | -11.0% | -3.26 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 193 | 171 | -11.6% | -29 to -15.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.3 |  | 1.1 to 1.5 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.169 | -2.3% | -0.00802 to 8.18e-05 | shown, not judged |
| host CPU-seconds without steal | 218 | 197 | -9.8% | -112 to 68.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 196 to 209 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0106 to 0.00482 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.7 | -1.0% | -0.0609 to -0.0543 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.5% | -0.0349 to -0.022 | GAIN |
| latency, mean (ms) | 1.35 | 0.592 | -56.0% | -0.78 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.8% | 274 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,057 | 2,381 | -98.3% | -138,723 to -132,630 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.123 | -8.8% | -0.0325 to 0.00868 | EVEN, no difference beyond the noise |
| host CPU-seconds | 227 | 211 | -7.4% | -57 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.427 | 0.337 | -20.9% | -0.156 to -0.0219 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 255 | -12.6% | -38.8 to -34.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.2 | 31.9 | -9.5% | -4.73 to -1.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 256 | 221 | -13.7% | -37.6 to -32.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.39 to 1.84 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.222 | -5.3% | -0.019 to -0.00576 | shown, not judged |
| host CPU-seconds without steal | 227 | 211 | -7.4% | -57 to 23.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
