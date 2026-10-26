# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,870 | +0.1% | -11.9 to 17.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,880 | 2,882 | +0.1% | -14.4 to 19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.39 | 0.386 | -1.0% | -0.0557 to 0.0477 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.675 | 0.665 | -1.5% | -0.0984 to 0.0784 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.23 | +0.6% | -0.0233 to 0.0258 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 557 | +8.9% | -96.7 to 188 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 452 | +8.3% | -75.5 to 145 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,794 | 628,291 | -7.3% | -212,828 to 113,823 | shown, not judged |
| host CPU busy (share of the run) | 0.261 | 0.268 | +2.7% | -0.0525 to 0.0666 | EVEN, no difference beyond the noise |
| host CPU-seconds | 461 | 476 | +3.2% | -110 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.349 | 0.36 | +3.1% | -0.0825 to 0.104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 12 |  | 12 to 12 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 280 | +1.1% | -22.9 to 28.8 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 274 | 277 | +0.9% | -22.9 to 27.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.2 | +22.2% | -0.0319 to 1.2 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 461 | 476 | +3.2% | -110 to 140 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
