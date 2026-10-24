# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -7.34 to 7.34 | EVEN, the same |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -6.37 to 6.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.129 | 0.136 | +5.4% | -0.00811 to 0.0221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.35 | +3.6% | -0.00311 to 0.0271 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0714 | 0.0724 | +1.3% | -0.00528 to 0.00718 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.0% | -6.42 to 7.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,386 | 63,223 | -0.3% | -472 to 147 | shown, not judged |
| host CPU busy (share of the run) | 0.0888 | 0.105 | +18.4% | -0.0625 to 0.0951 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 192 | +20.0% | -127 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.143 | +20.0% | -0.0946 to 0.142 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
