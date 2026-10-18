# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.8 to 11.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0311 to 0.0194 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00718 to 0.00787 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.68 | +0.0% | -0.00862 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.73 | +0.2% | -0.0062 to 0.0235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0441 to -0.0331 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.34 to 1.47 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.19 to 1.27 | power given |
| keys evicted | 243,119 | 234,890 | -3.4% | -8,456 to -8,001 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.132 | -2.6% | -0.0306 to 0.0235 | EVEN, no difference beyond the noise |
| host CPU-seconds | 226 | 220 | -2.9% | -58.2 to 45.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.543 | 0.521 | -4.0% | -0.145 to 0.101 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 13 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
