# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | -0.0% | -4.71 to 2.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,919 | 2,918 | -0.0% | -2.46 to 0.902 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.326 | +0.4% | -0.00584 to 0.00851 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.439 | 0.441 | +0.5% | -0.0525 to 0.0565 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.176 | 0.181 | +2.9% | -0.0305 to 0.0406 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 493 | -3.8% | -70.4 to 31.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 406 | 391 | -3.7% | -59.5 to 29.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,641 | 276,899 | +5.0% | -32,693 to 59,209 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.165 | +0.4% | -0.0517 to 0.053 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 120 | +0.3% | -44.2 to 44.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.224 | 0.224 | +0.2% | -0.0831 to 0.0841 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
