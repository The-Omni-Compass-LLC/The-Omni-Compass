# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7483 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,729 | +0.1% | -9.34 to 16.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,740 | 5,742 | +0.0% | -14.5 to 18.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.372 | 0.37 | -0.5% | -0.0232 to 0.0192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.645 | 0.637 | -1.3% | -0.0467 to 0.0294 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | -0.2% | -0.00969 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,483 | 7,483 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -8.21 to 7.34 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,970 | 62,955 | -0.0% | -1,348 to 1,319 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.248 | -2.4% | -0.0113 to -0.000952 | GAIN |
| host CPU-seconds | 467 | 452 | -3.3% | -28.5 to -2.44 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.17 | -3.4% | -0.011 to -0.000842 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
