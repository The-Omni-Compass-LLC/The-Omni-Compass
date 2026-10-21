# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,192 | +0.7% | -1.29 to 18.5 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00142 to 0.0018 | EVEN, the same |
| cache hit rate | 0.789 | 0.795 | +0.7% | -0.000706 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.00649 to 0.00644 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.00731 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.29 | -2.3% | -0.0767 to 0.0154 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | -1.9 to 4.62 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.1 | +1.6% | -1.42 to 3.33 | EVEN, no difference beyond the noise |
| keys evicted | 138,243 | 134,878 | -2.4% | -10,330 to 3,600 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.146 | +8.7% | -0.0264 to 0.0499 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 257 | +10.0% | -52.7 to 99.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.439 | 0.48 | +9.2% | -0.105 to 0.186 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 6.29 to 26.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
