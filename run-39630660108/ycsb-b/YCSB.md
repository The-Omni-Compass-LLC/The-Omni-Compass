# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,941 | 2,938 | -0.1% | -6.25 to 0.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,943 | 2,940 | -0.1% | -3.77 to -0.777 | LOSS |
| latency, 95th percentile (ms) | 0.125 | 0.133 | +6.7% | -0.0333 to 0.05 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.321 | 0.342 | +6.5% | -0.056 to 0.098 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0634 | 0.0656 | +3.4% | -0.00724 to 0.0115 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -4.34 to -1.29 | GAIN |
| bytes in the cache, mean (MB) | 417 | 419 | +0.5% | -9.82 to 13.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,617 | 741,790 | +7.3% | 4,414 to 95,932 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0833 | -19.0% | -0.0559 to 0.0167 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 151 | -20.8% | -112 to 33.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.142 | 0.112 | -20.8% | -0.0836 to 0.0247 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
