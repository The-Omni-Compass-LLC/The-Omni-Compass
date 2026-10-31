# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0198 to 0.0351 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.65 | -0.7% | -0.0407 to -0.0367 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0188 to -0.0155 | GAIN |
| latency, mean (ms) | 1.71 | 0.786 | -54.0% | -0.941 to -0.907 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.1% | 162 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,740 | 76.3 | -99.9% | -72,461 to -70,867 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.113 | -26.8% | -0.078 to -0.00459 | GAIN |
| host CPU-seconds | 108 | 77.7 | -28.1% | -60.8 to -0.0536 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.558 | 0.325 | -41.7% | -0.404 to -0.0615 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.01 to 24.7 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 109 | 92.5 | -15.3% | -18.3 to -15.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 13 | 11.2 | -13.2% | -1.83 to -1.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 96.2 | 80.6 | -16.2% | -17.1 to -14 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.58 |  | 0.512 to 0.648 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0879 | 0.0831 | -5.5% | -0.00803 to -0.00172 | shown, not judged |
| host CPU-seconds without steal | 108 | 77.7 | -28.1% | -60.8 to -0.0561 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
