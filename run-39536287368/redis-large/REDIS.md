# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 8.55 to 30.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00163 to 0.000334 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00575 to 0.0203 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0126 to 0.0116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0152 to 0.0282 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.98 | -6.5% | -0.111 to -0.0257 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.575 to 2.02 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -0.46 to 1.26 | EVEN, no difference beyond the noise |
| keys evicted | 103,514 | 94,962 | -8.3% | -13,441 to -3,663 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.137 | -3.3% | -0.0413 to 0.0321 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 233 | -3.7% | -81.5 to 63.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.424 | 0.402 | -5.2% | -0.15 to 0.106 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
