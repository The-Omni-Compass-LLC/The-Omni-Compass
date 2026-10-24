# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,888 | -0.1% | -1.89 to -1.12 | LOSS |
| throughput (operations a second) | 2,893 | 2,892 | -0.1% | -1.93 to -1.07 | LOSS |
| latency, 95th percentile (ms) | 0.3 | 0.3 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.506 | 0.504 | -0.3% | -0.012 to 0.00868 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.188 | -0.1% | -0.00749 to 0.00719 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -8.94 to 0.234 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 419 | +0.3% | -11.8 to 14.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,904 | 691,550 | -2.7% | -161,196 to 122,488 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.16 | -17.6% | -0.153 to 0.0847 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 272 | -21.0% | -322 to 177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.204 | -21.0% | -0.241 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
