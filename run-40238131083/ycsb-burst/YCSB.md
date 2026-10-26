# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,920 | 2,918 | -0.1% | -12.7 to 8.77 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,924 | 2,923 | -0.1% | -12.9 to 9.42 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.378 | 0.385 | +1.9% | -0.0104 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.535 | 0.559 | +4.6% | -0.0353 to 0.084 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.139 | 0.142 | +2.5% | -0.00214 to 0.00903 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,518 | +0.2% | -5.09 to 11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,655 | 77,726 | +0.1% | -458 to 602 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.147 | +14.4% | -0.0435 to 0.0805 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.9 | 109 | +15.3% | -39.8 to 68.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.178 | 0.205 | +15.4% | -0.0741 to 0.129 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 38.2 | 39.2 | +2.4% | -0.0682 to 1.92 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 37.4 | 38.3 | +2.3% | -0.0613 to 1.81 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.817 | 0.868 | +6.2% | -0.0088 to 0.111 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 94.9 | 109 | +15.3% | -39.9 to 68.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
