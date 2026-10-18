# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -1.69 to 1.27 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00759 to 0.00653 | EVEN, the same |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.00036 to 0.000283 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.56 | -0.1% | -0.0183 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.00716 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.64 | +0.2% | -0.0206 to 0.0259 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.91 to -1.35 | GAIN |
| memory used, mean (MB) | 57.2 | 56.4 | -1.3% | -0.948 to -0.482 | GAIN |
| keys evicted | 71,769 | 71,782 | +0.0% | -65.5 to 90.2 | shown, not judged |
| host CPU busy (share of the run) | 0.0879 | 0.105 | +19.0% | -0.0193 to 0.0528 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.3 | 73 | +20.9% | -14.8 to 40 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.377 | +21.0% | -0.0759 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
