# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 13.3 to 22 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0247 to 0.0163 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00957 to 0.015 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% | -0.012 to 0.00894 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.29 | -0.1% | -0.0603 to 0.0527 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.901 | 0.842 | -6.5% | -0.0749 to -0.0425 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | -0.263 to 3.51 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.2 | +1.5% | 0.0446 to 1.81 | power given |
| keys evicted | 103,499 | 95,271 | -7.9% | -10,193 to -6,263 | shown, not judged |
| host CPU busy (share of the run) | 0.0732 | 0.0753 | +2.8% | -0.0191 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 130 | 133 | +2.9% | -36.6 to 44.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.228 | 0.231 | +1.5% | -0.0672 to 0.0739 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 13.4 to 25.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
