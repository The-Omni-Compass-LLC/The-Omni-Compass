# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,075 | -0.1% | -4.31 to 1.99 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0166 to 0.0183 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00268 to 0.00135 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.58 | 5.6 | +0.4% | -0.0622 to 0.104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.63 | 5.67 | +0.7% | -0.0918 to 0.17 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.65 | +0.9% | -0.0462 to 0.0771 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.68 to -1.22 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -0.9% | -0.801 to -0.201 | GAIN |
| keys evicted | 71,646 | 71,838 | +0.3% | -370 to 756 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.116 | -4.2% | -0.0216 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.2 | 81.5 | -5.4% | -18 to 8.62 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.445 | 0.421 | -5.3% | -0.0931 to 0.0456 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
