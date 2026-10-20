# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,279 | +1.0% | 10 to 14.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00195 to 0.00116 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | 0.00641 to 0.0106 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.1% | -0.00961 to 0.0012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | 0.000762 to 0.00248 | LOSS |
| latency, mean (ms) | 1.02 | 0.979 | -4.3% | -0.052 to -0.0359 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.8 | -0.3% | -2.02 to 1.67 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.6 | -1.1% | -1.9 to 0.505 | EVEN, no difference beyond the noise |
| keys evicted | 103,351 | 97,986 | -5.2% | -6,480 to -4,250 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.133 | +7.0% | -0.00879 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 232 | +8.5% | -17.4 to 53.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.402 | +7.5% | -0.0333 to 0.0895 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.3 |  | 12.6 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
