# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,887 | -0.0% | -4.54 to 2.48 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -3.59 to 1.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.433 | 0.434 | +0.2% | -0.00761 to 0.00961 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.627 | 0.627 | +0.1% | -0.0401 to 0.0407 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.223 | +0.6% | -0.00303 to 0.00556 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 480 | -6.2% | -72.3 to 9.12 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 380 | -5.6% | -63.2 to 18.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,950 | 287,404 | +8.1% | -32,930 to 75,836 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.153 | -20.5% | -0.0694 to -0.00958 | GAIN |
| host CPU-seconds | 134 | 101 | -24.2% | -55.1 to -9.82 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.191 | -24.2% | -0.104 to -0.0184 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
