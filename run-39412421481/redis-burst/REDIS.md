# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -2.06 to 1.95 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0171 to 0.0174 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00115 to 0.000668 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0108 to 0.00727 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.0% | -0.0285 to 0.031 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.72 | -0.2% | -0.0237 to 0.0164 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.2% | -3.83 to -0.32 | GAIN |
| memory used, mean (MB) | 57.2 | 56 | -2.0% | -2.92 to 0.66 | EVEN, no difference beyond the noise |
| keys evicted | 71,728 | 71,811 | +0.1% | -195 to 360 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.153 | +5.7% | 0.00379 to 0.0126 | power given |
| host CPU-seconds | 99.5 | 106 | +6.8% | 3.97 to 9.47 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.514 | 0.549 | +6.8% | 0.0202 to 0.0493 | power given |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
