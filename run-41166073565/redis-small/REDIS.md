# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.8% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0109 to 0.00295 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0141 to -0.00408 | GAIN |
| latency, 99th percentile (ms) | 5.33 | 5.27 | -1.2% | -0.154 to 0.0258 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 1.2 | -41.4% | -0.852 to -0.847 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,124 | 0 | -100.0% | -243,609 to -242,638 | shown, not judged |
| host CPU busy (share of the run) | 0.0601 | 0.0594 | -1.2% | -0.0524 to 0.051 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 105 | -0.0% | -97.4 to 97.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.199 | -21.2% | -0.235 to 0.128 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 122 | -6.7% | -12.8 to -4.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.5 | 15.5 | -11.0% | -2.43 to -1.4 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 113 | 105 | -7.1% | -11.5 to -4.64 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 0.869 to 1.58 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.132 | 0.126 | -4.6% | -0.0161 to 0.00412 | shown, not judged |
| host CPU-seconds without steal | 105 | 105 | -0.0% | -97.4 to 97.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
