# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | +0.0% | -1.74 to 2.24 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00789 to 0.00949 | EVEN, the same |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.00122 to 0.00148 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00633 to 0.00718 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.0111 to 0.0261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.71 | 1.71 | +0.1% | -0.0179 to 0.023 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -3.84 to -0.133 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.9% | -3.19 to 1.03 | EVEN, no difference beyond the noise |
| keys evicted | 71,718 | 71,693 | -0.0% | -406 to 358 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.161 | +20.9% | -0.0293 to 0.0848 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.3 | 114 | +24.3% | -23 to 67.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.472 | 0.586 | +24.3% | -0.12 to 0.349 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
