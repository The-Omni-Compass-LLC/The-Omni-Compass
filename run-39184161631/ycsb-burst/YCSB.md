# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -8.29 to 5.24 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,895 | -0.0% | -4.65 to 2.52 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.506 | 0.505 | -0.1% | -0.0107 to 0.00937 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.675 | 0.675 | +0.0% | -0.0237 to 0.0237 | EVEN, the same |
| latency, mean (ms) | 0.231 | 0.231 | -0.2% | -0.0118 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.1% | -51.3 to -31.8 | GAIN |
| bytes in the cache, mean (MB) | 400 | 369 | -7.9% | -38.9 to -24.3 | GAIN |
| pages read into the cache (misses) | 268,519 | 275,012 | +2.4% | 316 to 12,670 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.211 | +17.4% | -0.0273 to 0.0896 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 149 | +21.4% | -20.5 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.281 | +21.5% | -0.0383 to 0.138 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
