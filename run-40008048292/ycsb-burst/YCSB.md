# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,878 | -0.0% | -5.84 to 3.53 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -4.25 to 2.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.43 | +1.3% | -0.0347 to 0.0461 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.582 | 0.597 | +2.5% | -0.045 to 0.0743 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.214 | +1.0% | -0.0163 to 0.0204 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,511 | -0.1% | -3.97 to 2.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,615 | 77,649 | +0.0% | -80.4 to 149 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.215 | -0.2% | -0.0543 to 0.0534 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 153 | -0.8% | -51.8 to 49.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.288 | -0.8% | -0.0971 to 0.0924 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
