# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,887 | +0.0% | -1.52 to 2.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | +0.0% | -0.186 to 0.262 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.304 | +1.0% | -0.00942 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.57 | -0.3% | -0.0153 to 0.012 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.192 | +1.5% | -0.00451 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 519 | +1.3% | -29.5 to 43 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 426 | +1.9% | -21.4 to 37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,475 | 726,034 | +7.0% | -124,975 to 220,093 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.166 | -16.7% | -0.115 to 0.0484 | EVEN, no difference beyond the noise |
| host CPU-seconds | 354 | 283 | -19.9% | -237 to 95.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.213 | -19.9% | -0.178 to 0.0721 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -3.51 to 10.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 182 | 186 | +2.5% | 0.539 to 8.62 | power given |
| the server's own CPU-seconds (mongod) | 179 | 183 | +2.3% | -0.115 to 8.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.46 | 3.01 | +22.1% | 0.391 to 0.695 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 354 | 283 | -19.9% | -237 to 95.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
