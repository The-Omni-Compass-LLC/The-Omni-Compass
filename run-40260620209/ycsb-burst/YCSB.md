# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,863 | -0.1% | -52.2 to 45.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,881 | 2,878 | -0.1% | -33.3 to 27.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.489 | 0.49 | +0.1% | -0.0854 to 0.0867 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.763 | 0.767 | +0.6% | -0.38 to 0.388 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.233 | 0.234 | +0.6% | -0.0383 to 0.0411 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,505 | 1,500 | -0.3% | -33.9 to 25 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,629 | 77,663 | +0.0% | -625 to 693 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.229 | +2.2% | -0.0999 to 0.11 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 165 | +3.3% | -94.5 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.311 | +3.4% | -0.174 to 0.195 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.6 | 83.3 | +0.9% | -6.81 to 8.21 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.4 | 82.1 | +0.8% | -6.67 to 8.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.14 | 1.17 | +2.6% | -0.14 to 0.2 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 159 | 165 | +3.3% | -94.5 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
