# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,922 | 2,922 | +0.0% | -7.54 to 8.33 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,925 | 2,925 | +0.0% | -7.01 to 8.27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.364 | 0.367 | +0.6% | -0.0185 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.528 | +2.1% | -0.0325 to 0.0539 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.133 | 0.134 | +0.9% | -0.00659 to 0.00894 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,517 | 1,517 | -0.0% | -5.88 to 5.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,609 | 77,667 | +0.1% | -306 to 422 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.104 | -15.4% | -0.143 to 0.105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 90.7 | 75.5 | -16.7% | -116 to 85.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.142 | -16.7% | -0.217 to 0.16 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
