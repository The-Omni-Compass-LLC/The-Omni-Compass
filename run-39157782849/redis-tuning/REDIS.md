# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,193 | +0.9% | 5.13 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0244 to 0.0333 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00317 to 0.0109 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.1% | -0.0197 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.27 | -0.2% | -0.0311 to 0.00718 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.6% | -0.0651 to -0.0201 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.783 to 1.84 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.5% | 0.42 to 1.37 | power given |
| keys evicted | 138,152 | 134,219 | -2.8% | -6,556 to -1,310 | shown, not judged |
| host CPU busy (share of the run) | 0.0725 | 0.0709 | -2.2% | -0.054 to 0.0508 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 126 | -2.0% | -103 to 97.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.242 | 0.235 | -2.8% | -0.194 to 0.181 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
