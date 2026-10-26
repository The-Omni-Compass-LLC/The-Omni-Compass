# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.342 to 0.322 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0409 to 0.0677 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -7.24e-06 to 5.62e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.65 | 5.65 | -0.1% | -0.0158 to 0.00917 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.00643 to -0.00076 | GAIN |
| latency, mean (ms) | 0.783 | 0.785 | +0.2% | -0.0076 to 0.0103 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.017 to 0.0855 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.118 | -4.1% | -0.0771 to 0.0669 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.2 | 82.5 | -4.4% | -60.5 to 53 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.345 | -4.4% | -0.253 to 0.222 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 92.3 | 92.1 | -0.3% | -0.7 to 0.156 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.4 | 11.3 | -0.7% | -0.403 to 0.243 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 80.8 | 80.6 | -0.2% | -0.725 to 0.341 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0847 | 0.0851 | +0.4% | -0.00261 to 0.00326 | shown, not judged |
| host CPU-seconds without steal | 86.2 | 82.5 | -4.4% | -60.5 to 53 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,469 | -0.0% | -1.48 to 0.569 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00213 to 0.00578 | EVEN, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | -0.0% | -3.17e-06 to 1.23e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.126 | 0.122 | -3.4% | -0.0125 to 0.00408 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.23 | +0.1% | -0.0261 to 0.0317 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.19 | +0.5% | -0.0103 to 0.0121 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0414 to 0.121 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0716 | 0.0576 | -19.5% | -0.0455 to 0.0176 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 102 | -20.6% | -86.1 to 33.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.193 | 0.154 | -20.5% | -0.13 to 0.0508 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 118 | 117 | -0.8% | -10.5 to 8.58 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 16.5 | 16.3 | -1.1% | -1.77 to 1.4 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 101 | 100 | -0.8% | -8.72 to 7.16 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.134 | 0.133 | -0.9% | -0.0228 to 0.0204 | shown, not judged |
| host CPU-seconds without steal | 128 | 102 | -20.6% | -86.1 to 33.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,174 | 1,174 | +0.0% | -0.0183 to 0.0442 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0233 to 0.0149 | EVEN, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | -0.0% | -6.12e-06 to 5.13e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.56 | 5.57 | +0.1% | -0.0479 to 0.0555 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | +0.1% | -0.0408 to 0.0467 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.3 | +0.2% | -0.0192 to 0.0251 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00549 to 0.0572 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.107 | +4.2% | -0.0318 to 0.0404 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 189 | +4.6% | -61.3 to 77.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.358 | +4.5% | -0.116 to 0.147 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 201 | 203 | +1.0% | -13.6 to 17.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 18.6 | 18.8 | +0.8% | -1.51 to 1.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 184 | +1.0% | -12.1 to 15.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.175 | 0.176 | +0.6% | -0.017 to 0.0191 | shown, not judged |
| host CPU-seconds without steal | 181 | 189 | +4.6% | -61.3 to 77.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.0631 to 0.0511 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00467 to 0.00447 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -3.11e-06 to 1.14e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.00404 to 0.00869 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.1% | -0.00399 to 0.00984 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.565 | 0.565 | +0.1% | -0.00458 to 0.0058 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0511 to 0.0847 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0779 | 0.0843 | +8.2% | -0.0315 to 0.0442 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 140 | +9.0% | -57.1 to 80.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.224 | +9.0% | -0.0911 to 0.128 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 242 | 242 | +0.2% | -1.36 to 2.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 30.3 | 30.5 | +0.6% | -1.07 to 1.43 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 211 | 211 | +0.1% | -1.83 to 2.28 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.222 | 0.22 | -0.7% | -0.00785 to 0.00482 | shown, not judged |
| host CPU-seconds without steal | 129 | 140 | +9.0% | -57.1 to 80.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
