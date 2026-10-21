# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 0.877 to 17.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00114 to 0.00553 | GAIN |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00062 to 0.0121 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00956 to 0.0124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.00974 to 0.0345 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.1% | -0.0562 to -0.000691 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.164 to 3.05 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | -0.225 to 2.58 | EVEN, no difference beyond the noise |
| keys evicted | 138,076 | 134,058 | -2.9% | -9,172 to 1,136 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.14 | +5.7% | -0.0266 to 0.0417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 236 | +6.7% | -53.4 to 83 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.415 | 0.439 | +5.9% | -0.106 to 0.155 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.7 |  | 2.54 to 30.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
