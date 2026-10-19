# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | +1.6% | 20.2 to 21.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00842 to 0.00484 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0131 to 0.0146 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.48 | -0.2% | -0.0222 to 0.000264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.1% | -0.00641 to 0.0125 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.958 | 0.887 | -7.4% | -0.0762 to -0.0657 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.3% | -0.00659 to 1.73 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.125 to 0.911 | power given |
| keys evicted | 103,456 | 94,321 | -8.8% | -9,641 to -8,630 | shown, not judged |
| host CPU busy (share of the run) | 0.0892 | 0.095 | +6.5% | -0.0343 to 0.046 | EVEN, no difference beyond the noise |
| host CPU-seconds | 155 | 166 | +7.4% | -65.5 to 88.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.271 | 0.287 | +5.7% | -0.118 to 0.149 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
