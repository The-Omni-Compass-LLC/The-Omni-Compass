# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.6% | 16.3 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0491 to 0.0808 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0113 to 0.0167 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.48 | -0.2% | -0.0351 to 0.0104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00622 to 0.0103 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.956 | 0.883 | -7.6% | -0.0965 to -0.0495 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.904 to 1.93 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | 1.07 to 1.15 | power given |
| keys evicted | 103,241 | 93,999 | -9.0% | -11,045 to -7,438 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.103 | -5.9% | -0.0839 to 0.071 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 181 | -6.8% | -165 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.313 | -8.3% | -0.293 to 0.237 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 16.8 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
