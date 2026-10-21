# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,937 | -0.0% | -6.07 to 4.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,938 | -0.0% | -6.19 to 4.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0967 | 0.099 | +2.4% | -0.0102 to 0.0148 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.303 | 0.309 | +1.9% | -0.0254 to 0.0367 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0564 | 0.0576 | +2.2% | 0.000569 to 0.00188 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,351 | 1,350 | -0.1% | -1.63 to -0.604 | GAIN |
| pages read into the cache (misses) | 61,718 | 61,666 | -0.1% | -196 to 92.1 | shown, not judged |
| host CPU busy (share of the run) | 0.0625 | 0.0829 | +32.7% | -0.0106 to 0.0514 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 151 | +35.6% | -22 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0831 | 0.113 | +35.6% | -0.0165 to 0.0756 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
