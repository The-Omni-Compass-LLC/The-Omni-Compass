# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.5 to 13.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0183 to 0.0045 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00706 to 0.00892 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% | -0.000487 to 0.00362 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% | 0.00361 to 0.0055 | LOSS |
| latency, mean (ms) | 2.14 | 2.1 | -1.9% | -0.0464 to -0.0345 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.446 to 2.73 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.697 to 1.62 | power given |
| keys evicted | 243,285 | 236,617 | -2.7% | -14,264 to 927 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.0997 | -4.4% | -0.0288 to 0.0195 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 173 | -4.9% | -55.4 to 37.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.41 | -6.1% | -0.137 to 0.0835 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 1.85 to 28.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
