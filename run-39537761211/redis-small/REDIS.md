# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.9 to 12.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0239 to 0.0128 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00732 to 0.00805 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.61 | -0.1% | -0.0197 to 0.00725 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0138 to 0.0137 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.19 | 2.15 | -2.0% | -0.0531 to -0.0348 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.17 to 1.48 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.23 to 1.29 | power given |
| keys evicted | 243,136 | 234,806 | -3.4% | -8,587 to -8,074 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.135 | -1.0% | -0.0388 to 0.0361 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 242 | -0.8% | -78.2 to 74.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.585 | 0.572 | -2.1% | -0.194 to 0.17 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
