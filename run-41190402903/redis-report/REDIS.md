# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,325 | 1,325 | -0.0% | -0.348 to 0.135 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00404 to 0.00162 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.55e-06 to 4.08e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.019 to 0.0198 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.23 | +0.0% | -0.027 to 0.0305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.67 | 0.672 | +0.3% | -0.00834 to 0.0123 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0119 to 0.0519 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0596 | 0.0478 | -19.9% | -0.0657 to 0.042 | EVEN, no difference beyond the noise |
| host CPU-seconds | 42.3 | 33.5 | -20.9% | -48.6 to 30.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.177 | 0.14 | -20.9% | -0.204 to 0.129 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 43.5 | 43.7 | +0.5% | -4.7 to 5.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 5.85 | 5.89 | +0.7% | -0.761 to 0.841 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 37.6 | 37.8 | +0.5% | -3.95 to 4.34 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0473 | 0.0458 | -3.1% | -0.0136 to 0.0106 | shown, not judged |
| host CPU-seconds without steal | 42.3 | 33.5 | -20.9% | -48.6 to 30.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.0491 to 0.0422 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00203 to 0.00102 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -7.6e-06 to 3.65e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.159 | 0.159 | -0.0% | -0.00128 to 0.00116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.47 | -0.0% | -0.0146 to 0.0113 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.225 | -0.1% | -0.00125 to 0.000863 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0124 to 0.0389 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0992 | 0.0861 | -13.2% | -0.0409 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 151 | -14.4% | -78.9 to 28.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.266 | 0.228 | -14.4% | -0.119 to 0.0424 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 169 | 170 | +0.4% | -1.83 to 3.16 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.8 | 22.6 | -0.8% | -0.514 to 0.161 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 146 | 147 | +0.6% | -1.32 to 3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.168 | +0.3% | -0.00117 to 0.00218 | shown, not judged |
| host CPU-seconds without steal | 176 | 151 | -14.4% | -78.9 to 28.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.295 to 0.323 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0187 to 0.0152 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.1% | -0.00911 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00618 to 0.0171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.3% | -0.00654 to 0.0143 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.002 to 0.0687 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.138 | +10.2% | -0.00408 to 0.0296 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 234 | +11.6% | -9.22 to 57.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.397 | 0.444 | +11.6% | -0.0174 to 0.11 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 276 | 279 | +1.2% | -0.835 to 7.4 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32 | 32.9 | +3.0% | -0.935 to 2.86 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 243 | 246 | +1.0% | -1.16 to 5.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.234 | +1.0% | -0.0022 to 0.00666 | shown, not judged |
| host CPU-seconds without steal | 210 | 234 | +11.6% | -9.22 to 57.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0422 to 0.0547 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00722 to 0.00477 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.48 | 5.49 | +0.2% | -0.0272 to 0.0465 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.68 | +0.1% | -0.0143 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.511 | 0.513 | +0.3% | -0.00418 to 0.0072 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0112 to 0.0435 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.101 | -5.5% | -0.0469 to 0.0352 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 180 | -6.1% | -93.4 to 69.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.287 | -6.1% | -0.149 to 0.112 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 175 | 176 | +0.6% | -2.82 to 4.77 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 20.2 | 20.2 | -0.1% | -0.183 to 0.136 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 154 | 155 | +0.6% | -2.71 to 4.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.201 | 0.205 | +1.9% | 0.00145 to 0.00614 | shown, not judged |
| host CPU-seconds without steal | 192 | 180 | -6.1% | -93.4 to 69.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
