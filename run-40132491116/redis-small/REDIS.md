# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.053 to 0.0546 | EVEN, the same |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0133 to 0.0191 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | -9.74e-06 to 9.74e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.1% | -0.0174 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.1% | -0.0183 to 0.0121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.1% | -0.00678 to 0.00494 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00921 to 0.036 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +3.9% | 0.000971 to 0.00818 | power given |
| host CPU-seconds | 195 | 204 | +4.7% | 2.01 to 16.2 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.386 | +4.7% | 0.00379 to 0.0307 | power given |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
