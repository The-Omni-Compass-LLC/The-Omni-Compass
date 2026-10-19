# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 932 | +0.7% | -4.7 to 18.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0192 to 0.00933 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.622 | +0.7% | -0.00319 to 0.0122 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.19 | 5.2 | +0.0% | -0.00224 to 0.00411 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.1% | -0.00848 to 0.0232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.04 | 2.01 | -1.1% | -0.0651 to 0.0217 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.000298 to 2.44 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 61.5 | +1.4% | -0.257 to 1.95 | EVEN, no difference beyond the noise |
| keys evicted | 243,062 | 238,956 | -1.7% | -13,568 to 5,355 | shown, not judged |
| host CPU busy (share of the run) | 0.0493 | 0.0543 | +10.3% | -0.0138 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.2 | 95.5 | +10.8% | -25.8 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.228 | +10.0% | -0.0616 to 0.103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16 |  | 5.17 to 26.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
