# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0467 to 0.0266 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00708 to 0.00532 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% | -0.016 to 0.00167 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | -0.1% | -0.0156 to 0.00398 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.81 | 0.808 | -0.2% | -0.00838 to 0.00469 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00372 to 0.0598 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.0999 | -15.3% | -0.0478 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 80.6 | 66.9 | -17.0% | -36.4 to 9.06 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.28 | -17.0% | -0.152 to 0.0379 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 103 | 102 | -0.9% | -2.93 to 1.02 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.7 | 12.8 | +0.7% | -0.237 to 0.424 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 90 | 89 | -1.2% | -2.7 to 0.604 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0857 | 0.0857 | +0.0% | -0.00123 to 0.00125 | shown, not judged |
| host CPU-seconds without steal | 80.6 | 66.9 | -17.0% | -36.4 to 9.06 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.134 to 0.0922 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00144 to 0.00374 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 0.255 | 0.253 | -0.9% | -0.0124 to 0.00787 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0128 to 0.0124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.303 | 0.303 | -0.2% | -0.00241 to 0.00138 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 349 | +0.0% | 0.0161 to 0.0462 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0949 | 0.103 | +8.4% | -0.0152 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 173 | +9.3% | -27.7 to 57.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.239 | 0.261 | +9.3% | -0.0418 to 0.0862 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 256 | 257 | +0.3% | -3.19 to 4.58 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 34.8 | 34.7 | -0.2% | -1.77 to 1.63 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 221 | 222 | +0.4% | -2.32 to 3.88 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.301 | 0.29 | -3.7% | -0.0654 to 0.0434 | shown, not judged |
| host CPU-seconds without steal | 158 | 173 | +9.3% | -27.7 to 57.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0351 to 0.0457 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00477 to 0.0047 | EVEN, the same |
| cache hit rate | 0.782 | 0.782 | -0.0% | -5.08e-06 to 2.34e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.00897 to 0.0124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.013 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | -0.0% | -0.00784 to 0.00683 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.013 to 0.0287 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.119 | +0.6% | -0.0402 to 0.0417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 199 | +0.6% | -77.1 to 79.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.378 | +0.6% | -0.146 to 0.151 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 275 | 274 | -0.5% | -4.94 to 2.14 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.5 | 32.6 | +0.4% | -0.304 to 0.544 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 242 | 241 | -0.6% | -4.63 to 1.59 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.3% | -0.0106 to 0.00909 | shown, not judged |
| host CPU-seconds without steal | 198 | 199 | +0.6% | -77.1 to 79.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.143 to 0.0704 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000214 to 0.00347 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -3.11e-06 to 1.14e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.00396 to 0.00636 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | -0.0% | -0.00724 to 0.00645 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.568 | 0.568 | +0.0% | -0.0024 to 0.00275 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0211 to 0.0432 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0896 | -10.7% | -0.0182 to -0.00325 | GAIN |
| host CPU-seconds | 169 | 149 | -11.8% | -33.9 to -6.07 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.27 | 0.238 | -11.8% | -0.0541 to -0.00966 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 243 | 244 | +0.3% | 0.057 to 1.6 | power given |
| the server's own CPU-seconds (redis-server) | 30.9 | 30.6 | -1.0% | -0.868 to 0.235 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 212 | 213 | +0.5% | 0.778 to 1.51 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.7% | -0.00279 to -0.000255 | shown, not judged |
| host CPU-seconds without steal | 169 | 149 | -11.8% | -33.9 to -6.07 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
