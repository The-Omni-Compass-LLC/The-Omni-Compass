# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,929 | -0.1% | -11.9 to 6.99 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,933 | -0.1% | -10.1 to 5.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.252 | +2.3% | -0.024 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.424 | 0.436 | +2.8% | -0.0572 to 0.0806 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0841 | 0.0852 | +1.2% | -0.0164 to 0.0185 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 480 | -6.3% | -113 to 49 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 403 | 379 | -5.8% | -95.8 to 49.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 257,102 | 273,001 | +6.2% | -34,364 to 66,161 | shown, not judged |
| host CPU busy (share of the run) | 0.0919 | 0.106 | +15.0% | -0.166 to 0.194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68 | 77.4 | +13.8% | -137 to 156 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.127 | 0.145 | +13.8% | -0.256 to 0.292 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
