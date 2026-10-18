# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | -14.2 to 38.5 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00281 to 0.00195 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | -0.00956 to 0.0259 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00513 to 0.00681 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | 0.00635 to 0.0125 | LOSS |
| latency, mean (ms) | 1.05 | 1 | -3.9% | -0.138 to 0.0559 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.1 | +0.2% | -2.1 to 2.38 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | -0.0% | -2.2 to 2.17 | EVEN, no difference beyond the noise |
| keys evicted | 103,208 | 97,902 | -5.1% | -17,228 to 6,616 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.113 | -1.7% | -0.00891 to 0.00494 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 189 | -1.8% | -17.4 to 10.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.328 | -2.8% | -0.027 to 0.0084 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
