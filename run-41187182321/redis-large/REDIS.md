# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00367 to 0.00237 | EVEN, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 0.214 | -96.2% | -5.42 to -5.4 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.58 | -2.5% | -0.157 to -0.125 | GAIN |
| latency, mean (ms) | 0.988 | 0.261 | -73.6% | -0.736 to -0.719 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.8% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 248 to 254 | power given |
| keys evicted | 103,318 | 2,753 | -97.3% | -101,372 to -99,758 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.112 | -8.0% | -0.0346 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 202 | -7.1% | -65.1 to 34.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.306 | -19.7% | -0.149 to -0.000481 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 216 | 189 | -12.5% | -30.9 to -23.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.5 | 21.2 | -13.4% | -3.7 to -2.9 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 192 | 167 | -13.0% | -28.4 to -21.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.15 |  | 1.08 to 1.23 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.18 | 0.177 | -1.5% | -0.0101 to 0.00483 | shown, not judged |
| host CPU-seconds without steal | 217 | 202 | -7.1% | -65.1 to 34.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
