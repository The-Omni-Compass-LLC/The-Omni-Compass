# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 1.65 to 30.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0104 to 0.0125 | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.000947 to 0.0201 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0174 to 0.00999 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% | -0.0301 to 0.0255 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.998 | -5.5% | -0.106 to -0.00989 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.0101 to 0.709 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.4 | +0.1% | -0.695 to 0.798 | EVEN, no difference beyond the noise |
| keys evicted | 103,447 | 96,580 | -6.6% | -13,289 to -445 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.123 | +8.8% | -0.0175 to 0.0374 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 207 | +10.3% | -32.8 to 71.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.359 | +8.9% | -0.063 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
