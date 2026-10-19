# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,392 | -0.1% | -6.04 to 3.72 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.014 to 0.0103 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -9.64e-06 to 5.69e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.52 | 5.55 | +0.5% | -0.0864 to 0.137 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.8 | +2.0% | -0.365 to 0.589 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.514 | 0.539 | +4.9% | -0.0732 to 0.124 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.126 to 0.252 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0897 | 0.107 | +19.0% | -0.0409 to 0.0751 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 190 | +20.5% | -81 to 146 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.304 | +20.6% | -0.129 to 0.233 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
