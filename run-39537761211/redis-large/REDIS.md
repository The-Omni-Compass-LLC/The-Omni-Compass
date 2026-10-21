# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 6.7 to 29.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00145 to 0.00222 | EVEN, the same |
| cache hit rate | 0.844 | 0.857 | +1.5% | 0.00456 to 0.0205 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00765 to 0.00826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.26 | +0.1% | -0.00576 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.828 | -6.9% | -0.103 to -0.0206 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | -0.506 to 3.47 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62 | +1.2% | 0.398 to 1.02 | power given |
| keys evicted | 103,739 | 95,343 | -8.1% | -13,699 to -3,094 | shown, not judged |
| host CPU busy (share of the run) | 0.0702 | 0.0607 | -13.5% | -0.0354 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 125 | 107 | -14.4% | -66.5 to 30.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.186 | -15.6% | -0.119 to 0.05 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 18.5 to 23.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
