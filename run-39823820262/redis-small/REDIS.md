# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 11 to 12.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0461 to 0.0242 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00754 to 0.00872 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0121 to 0.0237 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.45 | +2.2% | 0.0716 to 0.167 | LOSS |
| latency, mean (ms) | 2.06 | 2.02 | -1.7% | -0.0405 to -0.0309 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.48 to 1.71 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.23 to 1.4 | power given |
| keys evicted | 243,278 | 235,724 | -3.1% | -12,202 to -2,906 | shown, not judged |
| host CPU busy (share of the run) | 0.0699 | 0.0674 | -3.5% | -0.032 to 0.027 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 118 | -4.1% | -59.6 to 49.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.281 | -5.3% | -0.146 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
