# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.0392 to 0.0173 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00225 to 0.0011 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -8.65e-06 to 6.67e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.159 | 0.168 | +5.1% | -0.0102 to 0.0264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.42 | 5.46 | +0.8% | -0.0843 to 0.168 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.218 | +1.9% | -0.00619 to 0.0142 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0153 to 0.0429 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0768 | 0.078 | +1.5% | -0.0159 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 136 | 138 | +1.2% | -29.8 to 33.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.206 | 0.208 | +1.2% | -0.045 to 0.05 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
