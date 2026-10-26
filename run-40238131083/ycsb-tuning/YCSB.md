# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d40c4c64109`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -9.76 to 6.93 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -9.51 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.348 | +1.2% | 0.00152 to 0.00648 | LOSS |
| latency, 99th percentile (ms) | 0.62 | 0.621 | +0.2% | -0.00807 to 0.0107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.21 | +0.0% | -0.00461 to 0.00477 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,361 | -0.1% | -5.35 to 1.41 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,862 | 62,903 | +0.1% | -776 to 859 | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.21 | -9.3% | -0.0466 to 0.00347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 409 | 361 | -11.8% | -104 to 7.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.272 | -11.8% | -0.0782 to 0.00575 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 235 | +0.5% | -2.19 to 4.65 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 231 | 232 | +0.5% | -2.29 to 4.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.59 | +2.7% | 0.0263 to 0.109 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 409 | 361 | -11.8% | -105 to 7.83 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
