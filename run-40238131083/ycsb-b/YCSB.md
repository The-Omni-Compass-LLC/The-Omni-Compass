# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,887 | -0.0% | -5.98 to 3.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -4.64 to 2.77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.328 | +5.8% | -0.025 to 0.061 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.515 | +2.0% | -0.0259 to 0.0465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.189 | +1.6% | -0.0045 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% | -1.89 to 1.63 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,796 | 61,828 | +0.1% | -115 to 177 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.179 | -1.2% | -0.0595 to 0.0553 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 308 | -1.9% | -126 to 114 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.231 | -1.8% | -0.0946 to 0.086 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 182 | 184 | +1.2% | -5.79 to 10.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 179 | 182 | +1.2% | -5.59 to 9.76 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 2.58 | +5.3% | -0.202 to 0.459 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 308 | -1.9% | -126 to 114 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
