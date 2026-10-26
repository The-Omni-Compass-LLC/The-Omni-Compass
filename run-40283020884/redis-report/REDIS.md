# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.324 to 0.203 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0013 to 0.00685 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -4.08e-06 to 6.55e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.1% | -0.00097 to 0.00848 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.0% | -0.0082 to 0.013 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.816 | 0.817 | +0.1% | -0.0119 to 0.0141 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0706 to 0.126 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.101 | -8.3% | -0.0946 to 0.0765 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.9 | 66.8 | -9.6% | -70.7 to 56.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.309 | 0.279 | -9.6% | -0.296 to 0.236 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 106 | 106 | -0.6% | -1.82 to 0.592 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 13.6 | 13.3 | -1.8% | -0.49 to -0.0104 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 92.6 | 92.3 | -0.4% | -1.77 to 1.05 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0961 | 0.0951 | -1.0% | -0.00366 to 0.00172 | shown, not judged |
| host CPU-seconds without steal | 73.9 | 66.8 | -9.6% | -70.7 to 56.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.0129 to 0.0295 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000994 to 0.00128 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -6.12e-06 to 5.13e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.189 | 0.185 | -2.2% | -0.024 to 0.0157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.55 | +0.1% | -0.00218 to 0.0136 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.244 | -0.5% | -0.00608 to 0.00368 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0173 to 0.0591 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.106 | +2.5% | -0.0303 to 0.0356 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 190 | +2.9% | -58.8 to 69.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.279 | 0.287 | +2.9% | -0.0887 to 0.105 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 182 | 181 | -0.2% | -8.29 to 7.53 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.9 | 24.6 | -1.0% | -0.95 to 0.47 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 157 | 157 | -0.1% | -7.43 to 7.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.192 | 0.191 | -0.3% | -0.00305 to 0.00194 | shown, not judged |
| host CPU-seconds without steal | 185 | 190 | +2.9% | -58.8 to 69.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0438 to 0.00989 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.027 to 0.0405 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | -5.13e-06 to 6.12e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0325 to 0.0272 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0348 to 0.0269 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | -0.1% | -0.014 to 0.012 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0265 to 0.0419 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.104 | -15.6% | -0.0869 to 0.0484 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 172 | -16.9% | -159 to 89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.393 | 0.327 | -16.9% | -0.301 to 0.168 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 276 | 272 | -1.5% | -16.3 to 7.76 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.6 | 32 | -1.9% | -3.66 to 2.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 243 | 240 | -1.5% | -12.7 to 5.41 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.23 | -2.4% | -0.0108 to -0.000421 | shown, not judged |
| host CPU-seconds without steal | 208 | 172 | -16.9% | -159 to 89 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,390 | 1,390 | -0.0% | -1.85 to 0.474 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0132 to 0.00729 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -6.23e-06 to 2.27e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.21 | +0.1% | -0.0124 to 0.021 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.27 | +0.5% | 0.0196 to 0.029 | LOSS |
| latency, mean (ms) | 0.455 | 0.463 | +1.8% | -0.00278 to 0.0192 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0354 to 0.114 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0536 | 0.0583 | +8.7% | -0.0421 to 0.0514 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.2 | 103 | +9.3% | -78.3 to 95.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.151 | 0.165 | +9.3% | -0.125 to 0.153 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 115 | 120 | +4.7% | -0.499 to 11.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.3 | 16 | +4.7% | -0.0344 to 1.48 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 99.5 | 104 | +4.7% | -0.467 to 9.87 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.135 | 0.137 | +0.9% | -0.00815 to 0.0105 | shown, not judged |
| host CPU-seconds without steal | 94.2 | 103 | +9.3% | -78.3 to 95.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
