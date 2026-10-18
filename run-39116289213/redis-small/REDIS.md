# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 9.55 to 13.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0581 to 0.024 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00721 to 0.00867 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0216 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.36 | 5.51 | +2.7% | -0.186 to 0.473 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 2.02 | -1.7% | -0.0641 to -0.0065 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.05 to 1.61 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.982 to 1.41 | power given |
| keys evicted | 243,246 | 235,808 | -3.1% | -12,333 to -2,542 | shown, not judged |
| host CPU busy (share of the run) | 0.0742 | 0.0598 | -19.4% | -0.078 to 0.0492 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 105 | -20.7% | -147 to 92 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.318 | 0.249 | -21.7% | -0.355 to 0.217 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12 |  | 9.52 to 14.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
