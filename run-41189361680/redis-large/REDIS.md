# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 196 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00125 to 0.000575 | EVEN, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 0.204 | -96.4% | -5.42 to -5.38 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.57 | -2.5% | -0.156 to -0.135 | GAIN |
| latency, mean (ms) | 0.976 | 0.255 | -73.8% | -0.742 to -0.7 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.6% | 249 to 253 | power given |
| keys evicted | 103,429 | 2,766 | -97.3% | -101,903 to -99,422 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.0976 | -10.2% | -0.116 to 0.0939 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 175 | -9.8% | -226 to 188 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.339 | 0.265 | -22.0% | -0.42 to 0.271 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 197 | 170 | -13.5% | -34.3 to -19 | GAIN |
| the server's own CPU-seconds (redis-server) | 25 | 22 | -12.0% | -4.13 to -1.85 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 147 | -14.5% | -31.4 to -18.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.23 |  | 1.17 to 1.29 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.197 | 0.193 | -1.8% | -0.0083 to 0.00115 | shown, not judged |
| host CPU-seconds without steal | 194 | 175 | -9.8% | -226 to 188 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
