# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,873 | -1.3% | -193 to 120 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,879 | -1.2% | -189 to 118 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.199 | 0.204 | +2.5% | -0.00815 to 0.0181 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.379 | 0.389 | +2.7% | -0.0131 to 0.0338 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.153 | +5.9% | -0.0267 to 0.0437 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,361 | -0.4% | -20 to 9.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,806 | 61,852 | +0.1% | -292 to 385 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.153 | +7.8% | -0.0344 to 0.0564 | EVEN, no difference beyond the noise |
| host CPU-seconds | 253 | 277 | +9.4% | -71.4 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.21 | +10.7% | -0.0495 to 0.09 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
