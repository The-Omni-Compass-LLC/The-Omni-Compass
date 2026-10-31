# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.924 to 1.38 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.000117 to 0.00117 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.2 | 5.19 | -0.0% | -0.00825 to 0.00623 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.00678 to 0.0043 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.658 | 0.657 | -0.2% | -0.0071 to 0.00421 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0132 to 0.0574 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0496 | 0.0485 | -2.2% | -0.0355 to 0.0334 | EVEN, no difference beyond the noise |
| host CPU-seconds | 34.9 | 34.1 | -2.2% | -26.2 to 24.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.146 | 0.143 | -2.2% | -0.11 to 0.104 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 41.1 | 40.5 | -1.4% | -1.55 to 0.415 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 5.39 | 5.36 | -0.5% | -0.163 to 0.11 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 35.7 | 35.1 | -1.5% | -1.66 to 0.581 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0408 | 0.0402 | -1.6% | -0.00347 to 0.00217 | shown, not judged |
| host CPU-seconds without steal | 34.9 | 34.1 | -2.2% | -26.2 to 24.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | +0.0% | -0.822 to 0.903 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00276 to 0.00365 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -5.13e-06 to 6.12e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.248 | 0.243 | -2.0% | -0.033 to 0.0228 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0285 to 0.0192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.291 | 0.288 | -1.0% | -0.0101 to 0.00411 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 349 | 349 | +0.0% | -0.0801 to 0.0964 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.108 | -14.0% | -0.0812 to 0.046 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 183 | -15.6% | -158 to 90.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.327 | 0.276 | -15.6% | -0.239 to 0.137 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 249 | 248 | -0.5% | -8.14 to 5.77 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 33.5 | 33.3 | -0.6% | -0.487 to 0.0934 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 215 | 214 | -0.5% | -8.2 to 6.22 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.237 | -0.1% | -0.00939 to 0.0089 | shown, not judged |
| host CPU-seconds without steal | 216 | 183 | -15.6% | -158 to 90.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0175 to 0.14 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0052 to 0.0107 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | -0.0% | -9.76e-06 to 8.77e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.00762 to 0.00826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0101 to 0.00746 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.00239 to 0.00296 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00427 to 0.0401 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.14 | +7.2% | -0.00937 to 0.028 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 239 | +8.2% | -18.8 to 55 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.418 | 0.452 | +8.2% | -0.0356 to 0.104 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 280 | +0.6% | -1.35 to 4.96 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.5 | 32.6 | +0.5% | -1.04 to 1.36 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 245 | 247 | +0.7% | -0.473 to 3.76 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.234 | +0.2% | -0.00533 to 0.00632 | shown, not judged |
| host CPU-seconds without steal | 221 | 239 | +8.2% | -18.8 to 55 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.221 to 0.305 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00284 to 0.000596 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.43 | 5.43 | -0.1% | -0.0309 to 0.0243 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.0% | -0.0155 to 0.0162 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.505 | 0.505 | +0.1% | -0.00545 to 0.00613 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0236 to 0.0622 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0843 | 0.088 | +4.4% | -0.0113 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 147 | 154 | +4.9% | -21.3 to 35.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.234 | 0.246 | +4.9% | -0.0339 to 0.0568 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 174 | 174 | -0.2% | -2.06 to 1.29 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 21.6 | 21.6 | +0.2% | -0.672 to 0.779 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 152 | 152 | -0.3% | -1.5 to 0.626 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.171 | 0.171 | +0.1% | -0.00986 to 0.0103 | shown, not judged |
| host CPU-seconds without steal | 147 | 154 | +4.9% | -21.3 to 35.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
