# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 921 | 934 | +1.4% | 11.3 to 14.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0976 to 0.119 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.4% | 0.00766 to 0.00943 | GAIN |
| latency, 95th percentile (ms) | 5.87 | 5.85 | -0.4% | -0.166 to 0.115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.61 | 7.46 | -2.0% | -0.589 to 0.291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.36 | 2.3 | -2.3% | -0.0882 to -0.0224 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 0.711 to 2.35 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.7% | 0.889 to 1.16 | power given |
| keys evicted | 243,398 | 239,575 | -1.6% | -9,473 to 1,827 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.149 | -0.0% | -0.0248 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 260 | 261 | +0.3% | -50.1 to 51.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.628 | 0.621 | -1.1% | -0.13 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 11.7 |  | 7.87 to 15.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
