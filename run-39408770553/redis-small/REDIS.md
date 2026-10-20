# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 9.52 to 13.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0076 to 0.00329 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00629 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.52 | +0.1% | -0.0168 to 0.025 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.1% | -0.0106 to 0.0226 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.1 | -1.8% | -0.0609 to -0.0169 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.926 to 1.9 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.906 to 1.43 | power given |
| keys evicted | 243,113 | 236,851 | -2.6% | -14,784 to 2,259 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.6% | -0.0121 to 0.00626 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 187 | -3.0% | -24.3 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.463 | 0.444 | -4.2% | -0.0657 to 0.0263 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.7 |  | 4.68 to 20.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
