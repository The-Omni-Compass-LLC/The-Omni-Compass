# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,929 | -0.1% | -10.6 to 1.88 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.1% | -4.19 to 0.793 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.265 | +7.9% | -0.0304 to 0.0691 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.411 | 0.468 | +14.0% | -0.0873 to 0.203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0798 | 0.0872 | +9.3% | -0.00674 to 0.0215 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -19.5 to -1.46 | GAIN |
| bytes in the cache, mean (MB) | 405 | 400 | -1.1% | -19.1 to 10.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 259,091 | 271,478 | +4.8% | 5,004 to 19,769 | shown, not judged |
| host CPU busy (share of the run) | 0.0649 | 0.0776 | +19.6% | -0.0674 to 0.0929 | EVEN, no difference beyond the noise |
| host CPU-seconds | 45.7 | 55.5 | +21.5% | -52.4 to 72.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0854 | 0.104 | +21.7% | -0.0982 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
