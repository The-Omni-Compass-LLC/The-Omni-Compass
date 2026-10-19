# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,286 | +1.6% | 12.7 to 27 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0025 to 0.00313 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.00866 to 0.0179 | GAIN |
| latency, 95th percentile (ms) | 5.48 | 5.47 | -0.2% | -0.029 to 0.00334 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% | -0.00382 to -5.85e-05 | GAIN |
| latency, mean (ms) | 0.956 | 0.886 | -7.3% | -0.0947 to -0.045 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.2% | -3.15 to 2.92 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.8 | -0.8% | -3.72 to 2.76 | EVEN, no difference beyond the noise |
| keys evicted | 103,641 | 95,051 | -8.3% | -11,962 to -5,216 | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.104 | +13.2% | -0.0151 to 0.0393 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 184 | +14.9% | -28.9 to 76.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.317 | +13.2% | -0.0558 to 0.13 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25.7 |  | 11.1 to 40.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
