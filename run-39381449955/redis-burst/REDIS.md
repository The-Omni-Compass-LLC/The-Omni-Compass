# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.69 to 1.04 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0361 to 0.0548 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00106 to 0.000791 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.00394 to 0.00252 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% | 0.00349 to 0.0228 | LOSS |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | -0.00731 to 0.0177 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.4 | -4.0% | -5.03 to -0.0932 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -3.0% | -4.17 to 0.791 | EVEN, no difference beyond the noise |
| keys evicted | 71,738 | 71,792 | +0.1% | -205 to 313 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.142 | -1.8% | -0.107 to 0.102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.1 | 95.7 | -2.5% | -86.4 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.494 | -2.5% | -0.445 to 0.42 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
