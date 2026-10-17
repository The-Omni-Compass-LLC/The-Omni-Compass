# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% | -7.9 to 5.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -8.18 to 6.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.318 | -1.1% | -0.031 to 0.0237 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.575 | 0.568 | -1.1% | -0.0302 to 0.0175 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.201 | -0.7% | -0.015 to 0.012 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -109 to 65.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 404 | -3.0% | -86.8 to 61.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,301 | 746,183 | +6.4% | -173,145 to 262,908 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.195 | +8.4% | 0.000792 to 0.0294 | power given |
| host CPU-seconds | 308 | 340 | +10.4% | 5.76 to 58.5 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.255 | +10.4% | 0.00408 to 0.0442 | power given |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
