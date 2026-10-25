# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,908 | -0.1% | -6.12 to 2.48 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,912 | -0.1% | -7.42 to 3.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.189 | 0.187 | -0.7% | -0.00277 to 0.000101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.355 | 0.354 | -0.2% | -0.0411 to 0.0397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.143 | 0.142 | -0.8% | -0.0141 to 0.0117 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -8.42 to 0.802 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 414 | -0.2% | -8.53 to 6.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,685 | 689,427 | -3.0% | -135,625 to 93,110 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.127 | -10.4% | -0.13 to 0.1 | EVEN, no difference beyond the noise |
| host CPU-seconds | 254 | 223 | -12.3% | -270 to 207 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.19 | 0.167 | -12.3% | -0.202 to 0.155 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
