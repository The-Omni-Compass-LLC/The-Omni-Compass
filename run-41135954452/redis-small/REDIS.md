# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
