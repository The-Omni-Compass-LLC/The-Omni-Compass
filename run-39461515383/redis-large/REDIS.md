# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | 5.27 to 20 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00317 to 0.00404 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | 0.0036 to 0.0133 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.00768 to 0.00155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.0004 to 0.0122 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.01 | -4.1% | -0.0695 to -0.0159 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.1% | -2.96 to 2.83 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.7 | -0.9% | -3.15 to 2.04 | EVEN, no difference beyond the noise |
| keys evicted | 103,319 | 97,971 | -5.2% | -8,737 to -1,959 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.12 | +4.9% | -0.00879 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 201 | +5.6% | -16.6 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.349 | +4.5% | -0.0306 to 0.0608 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.7 |  | 16.7 to 32.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
