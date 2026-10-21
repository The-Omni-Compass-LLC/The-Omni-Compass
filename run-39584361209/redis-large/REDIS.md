# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 10.3 to 24.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00402 to 0.00231 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00682 to 0.0161 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.00868 to 0.00815 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.0% | -0.0101 to 0.0151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.87 | 0.812 | -6.7% | -0.0832 to -0.0332 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -0.167 to 1.71 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | -0.811 to 1.84 | EVEN, no difference beyond the noise |
| keys evicted | 103,176 | 95,658 | -7.3% | -10,641 to -4,394 | shown, not judged |
| host CPU busy (share of the run) | 0.0586 | 0.0603 | +2.9% | -0.00925 to 0.0127 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 107 | +3.2% | -17.4 to 23.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.181 | 0.185 | +1.8% | -0.032 to 0.0386 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 16.8 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
