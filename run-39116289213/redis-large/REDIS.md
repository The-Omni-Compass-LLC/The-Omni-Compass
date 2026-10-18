# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 19.9 to 22.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000514 to 0.00154 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0134 to 0.0153 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.5 | -0.1% | -0.032 to 0.0171 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.00835 to 0.00885 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.96 | 0.884 | -7.8% | -0.0806 to -0.07 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | -0.0215 to 3.43 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% | -0.000725 to 2.3 | EVEN, no difference beyond the noise |
| keys evicted | 103,486 | 93,949 | -9.2% | -9,894 to -9,180 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0947 | -9.5% | -0.0748 to 0.0548 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 166 | -10.5% | -145 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.285 | -12.0% | -0.258 to 0.18 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 15.5 to 25.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
