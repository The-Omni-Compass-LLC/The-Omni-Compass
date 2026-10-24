# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,916 | +0.1% | -11.7 to 18.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,920 | +0.1% | -10.5 to 17.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.313 | 0.313 | +0.2% | -0.0908 to 0.0922 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.497 | -0.3% | -0.0886 to 0.0859 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.118 | -1.4% | -0.0187 to 0.0154 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,516 | 1,518 | +0.1% | -4.47 to 8.69 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,604 | 77,704 | +0.1% | -179 to 378 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.119 | -22.3% | -0.0815 to 0.0134 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 85.8 | -24.5% | -66.1 to 10.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.213 | 0.161 | -24.6% | -0.124 to 0.0191 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
