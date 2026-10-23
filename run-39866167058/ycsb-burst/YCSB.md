# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,940 | 2,940 | -0.0% | -5.12 to 4.33 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,942 | -0.0% | -5.23 to 4.41 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.23 | +0.9% | -0.0159 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.355 | 0.355 | +0.1% | -0.027 to 0.0277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0697 | 0.0696 | -0.0% | -0.00233 to 0.00231 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,522 | +0.2% | -1.1 to 6.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,714 | 77,738 | +0.0% | -86.4 to 134 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.0599 | -47.2% | -0.0812 to -0.0259 | GAIN |
| host CPU-seconds | 85.6 | 42.7 | -50.1% | -65.7 to -20.2 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.0797 | -50.1% | -0.123 to -0.0377 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
