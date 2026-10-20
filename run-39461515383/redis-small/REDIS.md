# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 11.1 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0071 to -0.000558 | LOSS |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00744 to 0.0092 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.00853 to 0.00473 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.00637 to 0.0159 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0514 to -0.0368 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.2 to 1.62 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.818 to 1.39 | power given |
| keys evicted | 243,244 | 238,747 | -1.8% | -13,177 to 4,183 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.132 | -0.8% | -0.0219 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 219 | -0.9% | -42.6 to 38.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.532 | 0.52 | -2.2% | -0.109 to 0.0862 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
