# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 245 to 256 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0701 to 0.0293 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.7% | -0.0418 to -0.0358 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0283 to -0.00529 | GAIN |
| latency, mean (ms) | 1.71 | 0.792 | -53.8% | -0.953 to -0.889 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.9% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,788 | 77.7 | -99.9% | -72,537 to -70,885 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.12 | -11.9% | -0.0654 to 0.0332 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.1 | 83 | -10.8% | -48.8 to 28.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.481 | 0.348 | -27.7% | -0.318 to 0.0519 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 110 | 93.9 | -14.6% | -17.7 to -14.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 13 | 11.3 | -13.0% | -2.02 to -1.36 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 96.8 | 81.9 | -15.4% | -16.8 to -13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.577 |  | 0.493 to 0.661 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0871 | 0.0832 | -4.5% | -0.00684 to -0.000974 | shown, not judged |
| host CPU-seconds without steal | 93.1 | 83 | -10.8% | -48.8 to 28.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
