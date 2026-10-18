# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,889 | -0.0% | -4.62 to 2.72 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% | -3.76 to 1.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.5 | 0.498 | -0.3% | -0.00277 to 0.000101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.636 | 0.637 | +0.1% | -0.00907 to 0.00974 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.228 | -0.1% | -0.00494 to 0.0047 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -13.4 to -3.46 | GAIN |
| bytes in the cache, mean (MB) | 402 | 400 | -0.4% | -16.9 to 13.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,592 | 272,124 | +2.8% | -4,409 to 19,474 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.147 | -12.0% | -0.0774 to 0.0373 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 96.9 | -14.1% | -61.1 to 29.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.182 | -14.1% | -0.115 to 0.0555 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
