# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 0.917 to 35.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000569 to 0.00178 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000197 to 0.0238 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.54 | -0.1% | -0.0274 to 0.0217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.63 | 5.63 | +0.1% | -0.00419 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.968 | 0.906 | -6.4% | -0.124 to 0.00017 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -3.04 to 4.32 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -3.3 to 3.74 | EVEN, no difference beyond the noise |
| keys evicted | 103,364 | 95,559 | -7.6% | -16,050 to 441 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.109 | +8.4% | -0.0402 to 0.0571 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 193 | +9.8% | -80.4 to 115 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.309 | 0.334 | +8.2% | -0.14 to 0.191 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 13.3 to 32.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
