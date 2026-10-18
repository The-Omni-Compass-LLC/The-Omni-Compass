# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.0% | 3.37 to 20.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0094 to 0.00409 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.0% | 0.00278 to 0.0136 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | +0.0% | -0.0134 to 0.0172 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.6 | +0.1% | -0.0121 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.2 | -3.3% | -0.0835 to 0.000794 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 0.485 to 2.53 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% | 0.376 to 1.76 | power given |
| keys evicted | 138,152 | 133,440 | -3.4% | -8,385 to -1,041 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.105 | +1.0% | -0.0128 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 183 | 185 | +1.0% | -25.1 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.343 | +0.0% | -0.0529 to 0.053 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
