# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% | -6.48 to 1.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,907 | -0.1% | -6.4 to 1.81 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.293 | 0.296 | +1.3% | -0.00432 to 0.0117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.464 | 0.463 | -0.2% | -0.0184 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.158 | +0.8% | -0.000704 to 0.00326 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -15.9 to 6.51 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -11.8 to 6.97 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 730,752 | 709,670 | -2.9% | -95,074 to 52,910 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.176 | -0.9% | -0.0255 to 0.0223 | EVEN, no difference beyond the noise |
| host CPU-seconds | 322 | 318 | -1.4% | -56.9 to 47.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.238 | -1.4% | -0.0425 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
