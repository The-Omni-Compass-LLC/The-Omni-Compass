# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.477 to -0.22 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0209 to 0.0145 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000336 to -1.23e-05 | LOSS |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0158 to 0.0149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.84 | +0.2% | -0.0114 to 0.0319 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | -0.00632 to 0.0157 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.91 to -1.03 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.931 to -0.129 | GAIN |
| keys evicted | 71,797 | 71,849 | +0.1% | 28.1 to 75.3 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.121 | -1.5% | -0.0729 to 0.0691 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.4 | 79.8 | -2.0% | -55 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.412 | -2.0% | -0.284 to 0.267 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
