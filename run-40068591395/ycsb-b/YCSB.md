# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,924 | -0.1% | -5.83 to 2.59 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,928 | 2,926 | -0.1% | -5.43 to 2.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.224 | 0.228 | +2.1% | -0.0184 to 0.0278 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.432 | +0.5% | -0.0159 to 0.0199 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.114 | 0.116 | +1.3% | -0.00567 to 0.00858 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,366 | +0.0% | -2.54 to 2.75 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,765 | 61,866 | +0.2% | -186 to 387 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.121 | +13.3% | -0.0473 to 0.0756 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 218 | +14.8% | -98.7 to 155 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.142 | 0.163 | +14.9% | -0.0736 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
