# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,935 | -0.1% | -9.22 to 3.32 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,937 | -0.1% | -8.53 to 2.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.149 | 0.166 | +11.4% | -0.0392 to 0.0732 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.354 | 0.364 | +2.8% | -0.0205 to 0.0405 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0681 | 0.0697 | +2.3% | -0.00595 to 0.0091 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.83 to -1.76 | GAIN |
| bytes in the cache, mean (MB) | 418 | 419 | +0.2% | -10 to 12.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,552 | 738,240 | +3.6% | -33,898 to 85,274 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.083 | -13.5% | -0.0827 to 0.0567 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 149 | -15.2% | -165 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.111 | -15.1% | -0.123 to 0.0834 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
