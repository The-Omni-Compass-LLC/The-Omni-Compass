# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.16 to -0.321 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00268 to 0.00253 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.000709 to -0.000142 | LOSS |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00403 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | -3.1e-05 to 0.0235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% | 0.00451 to 0.0131 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.5 | -4.0% | -4.5 to -0.597 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -2.9% | -3.6 to 0.328 | EVEN, no difference beyond the noise |
| keys evicted | 71,737 | 71,873 | +0.2% | 94.8 to 179 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.128 | -2.2% | -0.06 to 0.0542 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.7 | 85.5 | -2.5% | -45.7 to 41.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.442 | -2.4% | -0.236 to 0.214 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
