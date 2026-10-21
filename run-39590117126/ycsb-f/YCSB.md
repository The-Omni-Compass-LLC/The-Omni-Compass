# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,663 | 5,666 | +0.1% | -8.51 to 14.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,679 | 5,682 | +0.1% | -7.97 to 13.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.427 | 0.428 | +0.3% | -0.00665 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.682 | 0.681 | -0.0% | -0.0267 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.243 | +0.1% | -0.00752 to 0.00815 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,359 | -0.1% | -7.8 to 5.73 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,985 | 62,804 | -0.3% | -1,457 to 1,094 | shown, not judged |
| host CPU busy (share of the run) | 0.306 | 0.307 | +0.3% | -0.0142 to 0.0159 | EVEN, no difference beyond the noise |
| host CPU-seconds | 551 | 554 | +0.4% | -39.3 to 43.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.209 | +0.4% | -0.0145 to 0.0161 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
