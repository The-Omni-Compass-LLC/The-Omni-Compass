# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.51 to 0.341 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00431 to 0.00567 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.55e-06 to 4.08e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.00469 to 0.0124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.00165 to 0.00883 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.809 | 0.81 | +0.1% | -0.00696 to 0.00808 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00821 to 0.0426 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0993 | 0.0949 | -4.4% | -0.0427 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 66.4 | 63.4 | -4.6% | -31.2 to 25.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.278 | 0.265 | -4.6% | -0.131 to 0.105 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
