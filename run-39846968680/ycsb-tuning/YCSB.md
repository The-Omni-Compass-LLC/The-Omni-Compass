# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,936 | +0.0% | -5.62 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,938 | +0.0% | -4.99 to 7.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.152 | -0.2% | -0.021 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.357 | 0.36 | +0.8% | -0.025 to 0.031 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0746 | 0.0739 | -0.9% | -0.00259 to 0.00119 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | +0.0% | -5.07 to 5.95 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,390 | 63,430 | +0.1% | -877 to 957 | shown, not judged |
| host CPU busy (share of the run) | 0.0961 | 0.0984 | +2.4% | -0.0315 to 0.0361 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 177 | +2.3% | -62.8 to 70.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.129 | 0.132 | +2.3% | -0.0468 to 0.0527 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
