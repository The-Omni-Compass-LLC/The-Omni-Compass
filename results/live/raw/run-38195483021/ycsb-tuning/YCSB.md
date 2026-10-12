# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -14.2 to 15.8 | no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,907 | +0.0% | -14 to 15.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.304 | +0.9% | -0.00737 to 0.0127 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.486 | +1.8% | -0.0137 to 0.0311 | no difference beyond the noise |
| latency, mean (ms) | 0.123 | 0.122 | -0.8% | -0.00788 to 0.00603 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -12.7 to 2.5 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 413 | -0.7% | -11.4 to 5.76 | no difference beyond the noise |
| pages read into the cache (misses) | 465,858 | 472,515 | +1.4% | -13,888 to 27,202 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.153 | -0.3% | -0.0261 to 0.0253 | no difference beyond the noise |
| host CPU-seconds | 185 | 184 | -0.6% | -40.2 to 38.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.207 | -0.6% | -0.0447 to 0.0421 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
