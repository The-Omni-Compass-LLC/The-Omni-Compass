# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,252 | 1,260 | +0.7% | 0.588 to 16.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00523 | EVEN, no difference beyond the noise |
| cache hit rate | 0.835 | 0.84 | +0.7% | 0.00055 to 0.0109 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00526 to 0.00917 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.00808 to 0.0243 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.08 | -2.7% | -0.056 to -0.00296 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.0908 to 2.1 | power given |
| memory used, mean (MB) | 61.3 | 61.7 | +0.8% | -0.37 to 1.32 | EVEN, no difference beyond the noise |
| keys evicted | 73,231 | 70,708 | -3.4% | -4,794 to -252 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.11 | -13.3% | -0.033 to -0.000556 | GAIN |
| host CPU-seconds | 142 | 121 | -14.9% | -41.4 to -1.07 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.379 | 0.321 | -15.5% | -0.114 to -0.00384 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 14.4 to 27.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 188 | 188 | +0.3% | -0.595 to 1.55 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.9 | 24.9 | -0.1% | -0.442 to 0.402 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 163 | 162 | -0.1% | -0.796 to 0.592 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.6 |  | 0.574 to 0.626 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.154 | 0.152 | -1.2% | -0.00601 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 142 | 121 | -14.9% | -41.4 to -1.07 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
