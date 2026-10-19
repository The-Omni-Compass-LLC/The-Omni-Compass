# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,680 | +0.1% | -56.4 to 68.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,691 | 5,697 | +0.1% | -57.2 to 69.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.452 | 0.452 | +0.0% | -0.0129 to 0.0129 | EVEN, the same |
| latency, 99th percentile (ms) | 0.714 | 0.712 | -0.2% | -0.0162 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.257 | 0.257 | +0.2% | -0.00816 to 0.00908 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -5.6 to -3.23 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.6% | -6.18 to 0.944 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,929 | 678,379 | +0.5% | -9,524 to 16,424 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.282 | +0.6% | -0.0151 to 0.0187 | EVEN, no difference beyond the noise |
| host CPU-seconds | 474 | 476 | +0.5% | -38 to 42.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.18 | 0.18 | +0.3% | -0.0166 to 0.0176 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
