# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 936 | +1.3% | 10 to 13.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0389 to 0.00738 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00736 to 0.0081 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.0277 to 0.028 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.36 | 5.34 | -0.4% | -0.232 to 0.188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.01 | -2.1% | -0.0566 to -0.0284 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.38 to 1.59 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.21 to 1.31 | power given |
| keys evicted | 243,076 | 234,709 | -3.4% | -8,615 to -8,119 | shown, not judged |
| host CPU busy (share of the run) | 0.0599 | 0.0612 | +2.1% | -0.0461 to 0.0487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 108 | +2.4% | -84.1 to 89.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.255 | +1.1% | -0.203 to 0.209 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 13 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
