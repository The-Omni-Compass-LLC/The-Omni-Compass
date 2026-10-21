# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.1% | 8.17 to 18.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00574 to 0.00169 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00534 to 0.0122 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0147 to 0.0045 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.2% | -0.0413 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -4.2% | -0.0749 to -0.0221 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.17 to 2.15 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.873 to 1.61 | power given |
| keys evicted | 138,061 | 132,973 | -3.7% | -7,414 to -2,762 | shown, not judged |
| host CPU busy (share of the run) | 0.0566 | 0.0432 | -23.7% | -0.0664 to 0.0396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.6 | 75 | -24.7% | -123 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.187 | 0.139 | -25.6% | -0.232 to 0.136 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
