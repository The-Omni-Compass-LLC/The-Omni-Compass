# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,930 | 2,924 | -0.2% | -17.6 to 4.97 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,932 | 2,927 | -0.2% | -12 to 3.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.221 | 0.243 | +10.0% | -0.0213 to 0.0653 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.375 | 0.413 | +10.2% | -0.0499 to 0.127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0852 | 0.0958 | +12.4% | -0.00915 to 0.0303 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -21.8 to 7.19 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 415 | -1.1% | -22.1 to 12.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,492 | 679,994 | -0.7% | -123,889 to 114,892 | shown, not judged |
| host CPU busy (share of the run) | 0.0932 | 0.134 | +44.1% | -0.0081 to 0.0904 | EVEN, no difference beyond the noise |
| host CPU-seconds | 167 | 249 | +48.8% | -11.2 to 174 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.186 | +48.9% | -0.00867 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
