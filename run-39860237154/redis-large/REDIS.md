# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,284 | +1.4% | 13.6 to 22.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00226 to 0.00189 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00675 to 0.0179 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.73 | -0.6% | -0.15 to 0.0825 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.92 | 5.81 | -1.8% | -0.519 to 0.308 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.07 | 0.992 | -7.3% | -0.104 to -0.0516 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.5% | 0.158 to 1.71 | power given |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.00204 to 1.02 | power given |
| keys evicted | 103,631 | 95,490 | -7.9% | -12,156 to -4,127 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.131 | +8.1% | -0.0036 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 223 | +10.4% | -5.11 to 47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.354 | 0.385 | +8.8% | -0.0145 to 0.077 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
