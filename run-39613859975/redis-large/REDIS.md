# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 13.1 to 26 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00236 to 0.00283 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00903 to 0.0171 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.5 | -0.2% | -0.0278 to 0.00602 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.0022 to 0.00761 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.959 | 0.891 | -7.1% | -0.0932 to -0.0427 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -2.71 to 4.16 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.6% | -2.77 to 3.55 | EVEN, no difference beyond the noise |
| keys evicted | 103,376 | 94,864 | -8.2% | -11,507 to -5,518 | shown, not judged |
| host CPU busy (share of the run) | 0.0913 | 0.0901 | -1.3% | -0.0177 to 0.0153 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 156 | -1.4% | -33.3 to 29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.278 | 0.27 | -2.9% | -0.0635 to 0.0476 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 9.85 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
