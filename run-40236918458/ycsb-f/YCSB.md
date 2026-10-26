# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,686 | 5,691 | +0.1% | -18.4 to 28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,700 | 5,705 | +0.1% | -18.9 to 28.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.411 | 0.41 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.595 | -0.6% | -0.0094 to 0.00207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.231 | -0.3% | -0.00297 to 0.00145 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 534 | +4.2% | -31.5 to 75 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 435 | +4.2% | -25.7 to 60.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,520 | 664,630 | -3.9% | -85,928 to 32,148 | shown, not judged |
| host CPU busy (share of the run) | 0.311 | 0.311 | -0.3% | -0.0104 to 0.00876 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 563 | -0.5% | -27.1 to 21.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.213 | 0.212 | -0.5% | -0.0103 to 0.00796 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 8.52 to 13.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 346 | 346 | +0.0% | -2.9 to 2.94 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 342 | 341 | -0.2% | -3.67 to 2.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.31 | 4.92 | +14.1% | 0.261 to 0.958 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 565 | 563 | -0.5% | -27.1 to 21.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
