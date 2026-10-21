# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.2 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0183 to 0.00699 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00681 to 0.00829 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.65 | +0.1% | -0.00395 to 0.0176 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.2% | 0.0102 to 0.0177 | LOSS |
| latency, mean (ms) | 2.21 | 2.18 | -1.5% | -0.0515 to -0.016 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.06 to 1.57 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.14 to 1.31 | power given |
| keys evicted | 243,139 | 234,908 | -3.4% | -8,723 to -7,737 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.13 | +4.3% | -0.0367 to 0.0473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 228 | +4.9% | -72.2 to 93.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.522 | 0.54 | +3.6% | -0.178 to 0.216 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 8.03 to 18 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
