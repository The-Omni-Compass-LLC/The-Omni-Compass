# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,076 | +0.1% | -0.403 to 1.95 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00668 to 0.00109 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.000731 to 0.00106 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00952 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.31 | -0.5% | -0.233 to 0.18 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.54 | -0.4% | -0.0243 to 0.0117 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.65 to -1.31 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.751 to -0.384 | GAIN |
| keys evicted | 71,730 | 71,700 | -0.0% | -252 to 191 | shown, not judged |
| host CPU busy (share of the run) | 0.0669 | 0.0752 | +12.4% | -0.0808 to 0.0974 | EVEN, no difference beyond the noise |
| host CPU-seconds | 47.6 | 53.5 | +12.5% | -61.8 to 73.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.246 | 0.276 | +12.4% | -0.319 to 0.38 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
