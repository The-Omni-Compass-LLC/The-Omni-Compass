# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 248 to 252 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00196 to 0.0604 | GAIN |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.32 | -3.8% | -0.328 to -0.0918 | GAIN |
| latency, 99th percentile (ms) | 5.65 | 5.61 | -0.7% | -0.06 to -0.0176 | GAIN |
| latency, mean (ms) | 1.59 | 0.719 | -54.9% | -0.887 to -0.863 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 236 | +268.0% | 168 to 175 | power given |
| memory used, mean (MB) | 57.2 | 199 | +248.1% | 141 to 142 | power given |
| keys evicted | 71,694 | 239 | -99.7% | -71,889 to -71,020 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0904 | -10.6% | -0.0894 to 0.0678 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.2 | 65.1 | -11.1% | -70.1 to 53.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.272 | -27.8% | -0.418 to 0.208 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 68.1 | 61 | -10.3% | -8.79 to -5.26 | GAIN |
| the server's own CPU-seconds (redis-server) | 8.51 | 7.6 | -10.7% | -1.46 to -0.362 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 59.5 | 52.9 | -11.0% | -7.85 to -5.26 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.441 |  | 0.421 to 0.461 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0685 | 0.0656 | -4.1% | -0.00411 to -0.00156 | shown, not judged |
| host CPU-seconds without steal | 73.2 | 65.1 | -11.1% | -70.1 to 53.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
