# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,886 | -0.7% | -98.8 to 57.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,892 | -0.7% | -99 to 58.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.217 | +1.9% | -0.0212 to 0.0292 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.409 | 0.418 | +2.2% | -0.0427 to 0.0607 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.153 | 0.163 | +6.5% | -0.0127 to 0.0326 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,361 | -0.2% | -9.16 to 5.04 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,793 | 61,888 | +0.2% | -233 to 424 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.171 | +8.0% | -0.0445 to 0.0697 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 316 | +10.3% | -94.8 to 154 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.239 | +11.1% | -0.0684 to 0.116 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 139 | 139 | -0.2% | -7.02 to 6.33 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 137 | 136 | -0.3% | -6.94 to 6.05 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.14 | +5.0% | -0.0819 to 0.287 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 316 | +10.3% | -94.8 to 154 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
