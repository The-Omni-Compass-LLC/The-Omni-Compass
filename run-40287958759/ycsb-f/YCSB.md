# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,713 | 5,709 | -0.1% | -27 to 18.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,729 | 5,726 | -0.1% | -21.5 to 15.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.38 | 0.381 | +0.2% | -0.027 to 0.0284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.552 | 0.555 | +0.5% | -0.0785 to 0.0838 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.213 | +0.4% | -0.0146 to 0.0165 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 513 | +0.2% | -0.741 to 2.48 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 418 | +0.4% | 0.266 to 2.68 | power given |
| pages read into the cache (misses) | 687,410 | 683,616 | -0.6% | -12,625 to 5,037 | shown, not judged |
| host CPU busy (share of the run) | 0.291 | 0.296 | +1.7% | -0.0112 to 0.0208 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 537 | +1.9% | -31.7 to 52.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.202 | +2.0% | -0.0115 to 0.0194 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8.33 |  | 4.54 to 12.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 322 | 324 | +0.9% | -18.5 to 24.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 317 | 320 | +0.7% | -18.6 to 23.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.23 | 4.82 | +13.9% | 0.12 to 1.05 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 527 | 538 | +1.9% | -31.6 to 52.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
