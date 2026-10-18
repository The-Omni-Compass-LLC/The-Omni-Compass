# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -1.05 to 0.861 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -1.18 to 0.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.315 | +0.4% | -0.0044 to 0.00707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.485 | -1.2% | -0.0206 to 0.00931 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.197 | +1.2% | -0.00186 to 0.00643 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -76.6 to 41.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 401 | -4.5% | -70.9 to 33.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 744,406 | 693,091 | -6.9% | -155,421 to 52,793 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.183 | +12.7% | 0.0067 to 0.0346 | power given |
| host CPU-seconds | 273 | 314 | +15.1% | 13.4 to 69.1 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.236 | +15.1% | 0.00994 to 0.0519 | power given |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
