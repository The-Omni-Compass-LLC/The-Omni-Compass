# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 18.3 to 22.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00281 to 0.00312 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0123 to 0.0153 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0193 to -0.00437 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.1% | -0.0249 to 0.0118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.983 | -7.2% | -0.0896 to -0.0625 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -0.169 to 1.77 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.0297 to 0.981 | power given |
| keys evicted | 103,471 | 94,379 | -8.8% | -10,158 to -8,026 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.122 | -2.2% | -0.0196 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 206 | -2.0% | -37.4 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.356 | -3.6% | -0.0706 to 0.0442 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 27.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
