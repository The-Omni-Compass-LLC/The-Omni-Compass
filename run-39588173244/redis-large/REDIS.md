# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.7% | 17.8 to 24.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00212 to 0.00331 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0119 to 0.0163 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.55 | -0.6% | -0.0871 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.69 | -0.2% | -0.0421 to 0.0217 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.966 | 0.886 | -8.2% | -0.107 to -0.0515 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.733 to 1.89 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.2% | -0.934 to 2.43 | EVEN, no difference beyond the noise |
| keys evicted | 103,396 | 94,170 | -8.9% | -11,010 to -7,442 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.105 | +2.5% | -0.0847 to 0.0899 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 188 | +3.6% | -163 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.319 | 0.325 | +1.9% | -0.288 to 0.3 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 9.09 to 34.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
