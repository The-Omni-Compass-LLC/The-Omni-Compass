# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% | -5.69 to 3.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -5.27 to 3.05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.323 | +1.1% | -0.0138 to 0.0211 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.503 | 0.506 | +0.6% | -0.0191 to 0.0251 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.203 | +0.3% | -0.00276 to 0.00413 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.74 to 0.714 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 422 | 419 | -0.5% | -12.5 to 8.22 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 661,866 | 725,456 | +9.6% | 24,210 to 102,969 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.19 | -2.8% | -0.0374 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 327 | -3.4% | -79.3 to 56.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.246 | -3.4% | -0.0595 to 0.0422 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
