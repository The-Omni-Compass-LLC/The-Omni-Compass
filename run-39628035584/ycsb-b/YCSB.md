# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,906 | -0.1% | -6.14 to 2.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.1% | -5.2 to 1.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.295 | 0.301 | +2.0% | -0.00261 to 0.0146 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.506 | +0.9% | -0.0105 to 0.0198 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.129 | 0.129 | +0.1% | -0.0031 to 0.00345 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.12 to -2.03 | GAIN |
| bytes in the cache, mean (MB) | 416 | 417 | +0.2% | -3.5 to 5.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,664 | 714,644 | +2.0% | -33,187 to 61,147 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.145 | -1.5% | -0.057 to 0.0525 | EVEN, no difference beyond the noise |
| host CPU-seconds | 266 | 262 | -1.8% | -122 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.196 | -1.8% | -0.0913 to 0.0841 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
