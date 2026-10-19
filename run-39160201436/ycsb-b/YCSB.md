# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,894 | +0.0% | -5.16 to 6.21 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,898 | +0.0% | -4.93 to 6.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.333 | -1.4% | -0.0345 to 0.0252 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.493 | 0.49 | -0.6% | -0.0353 to 0.0293 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.8% | -0.0109 to 0.00792 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -2.56 to 2.03 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,790 | 61,849 | +0.1% | -176 to 294 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.172 | -3.7% | -0.0563 to 0.0431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 291 | -4.3% | -112 to 85.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.219 | -4.3% | -0.084 to 0.0642 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
