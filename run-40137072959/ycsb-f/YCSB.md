# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,844 | 5,839 | -0.1% | -22.1 to 11.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,852 | 5,847 | -0.1% | -22.1 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.16 | 0.16 | +0.0% | -0.00861 to 0.00861 | EVEN, the same |
| latency, 99th percentile (ms) | 0.371 | 0.378 | +1.9% | -0.0167 to 0.0307 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0837 | 0.0834 | -0.3% | -0.00539 to 0.00484 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.54 to -3.52 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.4% | -2.53 to -1.03 | GAIN |
| pages read into the cache (misses) | 703,679 | 704,126 | +0.1% | -24,012 to 24,907 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.126 | +1.7% | -0.0353 to 0.0395 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 228 | +2.3% | -74.2 to 84.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0831 | 0.0851 | +2.4% | -0.0277 to 0.0316 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
