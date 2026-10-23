# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.54 to 12.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0877 to 0.0213 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.625 | +1.2% | 0.00644 to 0.00822 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.65 | +0.1% | 0.000403 to 0.00655 | LOSS |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.2% | 0.00437 to 0.0209 | LOSS |
| latency, mean (ms) | 2.22 | 2.18 | -1.6% | -0.0427 to -0.0296 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.32 to 1.5 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.21 to 1.27 | power given |
| keys evicted | 242,995 | 234,914 | -3.3% | -8,712 to -7,450 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.14 | -2.4% | -0.0279 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 243 | -2.9% | -56.6 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.599 | 0.575 | -4.0% | -0.142 to 0.094 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.3 |  | 9.46 to 15.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
