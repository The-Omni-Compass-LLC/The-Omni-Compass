# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.8% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.135 to 0.216 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0319 to 0.00625 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.39 | 5.3 | -1.8% | -0.21 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 1.21 | -41.4% | -0.863 to -0.841 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.2% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,086 | 0 | -100.0% | -243,577 to -242,594 | shown, not judged |
| host CPU busy (share of the run) | 0.0639 | 0.0679 | +6.2% | -0.00325 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 112 | 120 | +7.7% | -6.48 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.269 | 0.228 | -15.0% | -0.0689 to -0.0119 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 13.7 to 22.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 134 | 121 | -9.6% | -24.4 to -1.38 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.6 | 15.2 | -13.6% | -4.52 to -0.264 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 116 | 104 | -10.1% | -20.5 to -2.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.2 |  | 0.646 to 1.76 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.13 | 0.12 | -7.6% | -0.0432 to 0.0236 | shown, not judged |
| host CPU-seconds without steal | 112 | 120 | +7.7% | -6.48 to 23.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
