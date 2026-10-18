# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.6 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.015 to 0.00324 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00716 to 0.00844 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.49 | +0.0% | -0.00838 to 0.00887 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.56 | +0.1% | -0.00289 to 0.0113 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% | -0.0493 to -0.0306 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.37 to 1.64 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.19 to 1.38 | power given |
| keys evicted | 243,216 | 234,806 | -3.5% | -8,871 to -7,949 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.096 | -12.9% | -0.0223 to -0.00604 | GAIN |
| host CPU-seconds | 194 | 166 | -14.2% | -42.4 to -12.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.394 | -15.3% | -0.107 to -0.0354 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
