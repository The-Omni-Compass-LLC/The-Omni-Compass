# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -2.14 to 1.89 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -1.11 to 1.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.326 | 0.325 | -0.4% | -0.0101 to 0.00739 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.496 | 0.499 | +0.6% | -0.00357 to 0.00957 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.5% | -0.00353 to 0.00152 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -2.16 to -1.35 | GAIN |
| bytes in the cache, mean (MB) | 418 | 419 | +0.3% | -4.42 to 6.83 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,378 | 705,496 | -0.7% | -66,840 to 57,076 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.189 | -8.4% | -0.0635 to 0.0289 | EVEN, no difference beyond the noise |
| host CPU-seconds | 364 | 327 | -10.2% | -139 to 65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.245 | -10.2% | -0.104 to 0.0488 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -2.4 to 9.07 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 201 | 199 | -0.8% | -4.34 to 1.27 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 198 | 196 | -1.0% | -4.87 to 0.722 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.09 | +21.2% | 0.494 to 0.587 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 364 | 327 | -10.2% | -139 to 65 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
