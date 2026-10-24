# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,744 | -0.1% | -23.7 to 9.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,770 | 5,763 | -0.1% | -23.6 to 8.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.349 | +0.3% | -0.00148 to 0.00348 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.628 | 0.626 | -0.3% | -0.0111 to 0.00774 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.165 | 0.165 | -0.2% | -0.00411 to 0.00361 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -38 to 16.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 410 | -1.5% | -28.2 to 15.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 693,007 | 708,353 | +2.2% | -37,901 to 68,594 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.243 | +3.6% | -0.00783 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 447 | +4.6% | -16.8 to 56.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.168 | +4.7% | -0.0062 to 0.0212 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
