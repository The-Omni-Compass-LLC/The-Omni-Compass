# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.358 to 0.36 | EVEN, the same |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0108 to 0.00901 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% | -0.0119 to 0.00164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.77 | -0.1% | -0.0221 to 0.00736 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.806 | 0.804 | -0.2% | -0.00829 to 0.00546 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0242 to 0.0613 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.124 | -6.8% | -0.0632 to 0.045 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.8 | 84.8 | -7.7% | -49.8 to 35.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.384 | 0.355 | -7.7% | -0.208 to 0.149 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 103 | 102 | -0.1% | -0.966 to 0.797 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.6 | 12.7 | +1.1% | -0.655 to 0.921 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 89.9 | 89.7 | -0.2% | -0.312 to -0.122 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0896 | 0.0885 | -1.2% | -0.00452 to 0.00231 | shown, not judged |
| host CPU-seconds without steal | 91.8 | 84.8 | -7.7% | -49.8 to 35.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.123 to 0.276 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000328 to 0.000947 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.26e-06 to 5.24e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.229 | 0.223 | -2.5% | -0.0154 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.0% | -0.0159 to 0.0135 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.283 | 0.281 | -0.7% | -0.00799 to 0.00408 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.00445 to 0.0454 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.1 | -13.2% | -0.0374 to 0.00671 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 169 | -14.7% | -70.9 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.299 | 0.255 | -14.7% | -0.107 to 0.0193 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 243 | 242 | -0.4% | -5.9 to 4.09 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 33.5 | 32.9 | -1.7% | -2.8 to 1.69 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 209 | 209 | -0.2% | -3.35 to 2.65 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.23 | -0.8% | -0.012 to 0.00838 | shown, not judged |
| host CPU-seconds without steal | 198 | 169 | -14.7% | -70.9 to 12.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0501 to 0.0339 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00855 to 0.0181 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | -0.0% | -5.16e-06 to 2.2e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.68 | +0.0% | -0.0169 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0196 to 0.0194 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | -0.0% | -0.00652 to 0.0065 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00387 to 0.0366 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.123 | -13.5% | -0.0888 to 0.0505 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 206 | -15.3% | -172 to 97.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.461 | 0.391 | -15.3% | -0.325 to 0.184 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 277 | -0.2% | -2.11 to 0.739 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 31.2 | 31.2 | +0.2% | -1 to 1.14 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 246 | 245 | -0.3% | -1.4 to -0.108 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.257 | 0.258 | +0.6% | -0.00393 to 0.00688 | shown, not judged |
| host CPU-seconds without steal | 243 | 206 | -15.3% | -172 to 97.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.13 to 0.0917 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00353 to 0.00225 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0162 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0277 to 0.0245 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.561 | 0.561 | -0.0% | -0.00106 to 0.000935 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00335 to 0.0782 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.12 | +8.8% | -0.0886 to 0.108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 207 | +10.0% | -171 to 208 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.3 | 0.33 | +10.0% | -0.272 to 0.332 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 246 | 246 | -0.2% | -1.08 to -0.14 | GAIN |
| the server's own CPU-seconds (redis-server) | 30.4 | 30.3 | -0.5% | -0.289 to 0.00906 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 216 | 215 | -0.2% | -1.03 to 0.0984 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.225 | 0.222 | -1.4% | -0.00898 to 0.00263 | shown, not judged |
| host CPU-seconds without steal | 188 | 207 | +10.0% | -171 to 208 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
