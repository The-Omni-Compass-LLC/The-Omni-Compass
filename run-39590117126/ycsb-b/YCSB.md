# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -4.45 to 4.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,940 | -0.0% | -4.47 to 4.29 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.141 | 0.152 | +7.5% | -0.0119 to 0.0332 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.33 | 0.333 | +0.7% | -0.0191 to 0.0238 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0616 | 0.0626 | +1.8% | -0.00329 to 0.00547 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | +0.0% | -0.743 to 1.62 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,800 | 61,884 | +0.1% | -142 to 311 | shown, not judged |
| host CPU busy (share of the run) | 0.0857 | 0.0753 | -12.2% | -0.0642 to 0.0433 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 136 | -12.8% | -125 to 85.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.116 | 0.101 | -12.8% | -0.0935 to 0.0638 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
