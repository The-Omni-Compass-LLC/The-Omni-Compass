# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,892 | -0.1% | -2.48 to -1.29 | LOSS |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -3.39 to -0.465 | LOSS |
| latency, 95th percentile (ms) | 0.315 | 0.313 | -0.4% | -0.00707 to 0.0044 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.563 | -0.8% | -0.0106 to 0.00192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.201 | -0.2% | -0.00505 to 0.00419 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.2% | -105 to 52.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 400 | -4.8% | -91.5 to 51.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,286 | 706,566 | +1.5% | -138,711 to 159,271 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.174 | -10.4% | -0.169 to 0.129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 298 | -12.2% | -344 to 261 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.224 | -12.2% | -0.258 to 0.196 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
