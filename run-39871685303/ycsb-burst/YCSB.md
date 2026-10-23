# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -0.497 to 1.39 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -0.829 to 1.37 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.444 | 0.442 | -0.5% | -0.0141 to 0.00941 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.634 | 0.639 | +0.7% | -0.00568 to 0.015 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | +0.2% | -0.00781 to 0.00875 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -12.6 to -4.71 | GAIN |
| bytes in the cache, mean (MB) | 401 | 395 | -1.6% | -20.3 to 7.44 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,772 | 276,604 | +5.3% | -26,316 to 53,980 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.2 | +3.8% | -0.0595 to 0.0743 | EVEN, no difference beyond the noise |
| host CPU-seconds | 133 | 139 | +4.2% | -51.9 to 63.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.251 | 0.261 | +4.2% | -0.0979 to 0.119 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
