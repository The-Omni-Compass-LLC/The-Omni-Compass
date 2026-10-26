# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,835 | 5,829 | -0.1% | -25.5 to 14.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,844 | 5,839 | -0.1% | -24.3 to 13.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.17 | 0.178 | +4.5% | -0.0285 to 0.0439 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.397 | 0.402 | +1.4% | -0.0328 to 0.0442 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0868 | 0.089 | +2.6% | -0.00754 to 0.012 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -56.7 to 83.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 430 | +2.8% | -40 to 63.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,316 | 685,793 | -0.8% | -84,092 to 73,045 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.151 | +17.2% | -0.0384 to 0.0828 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 277 | +19.5% | -76.8 to 167 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0867 | 0.104 | +19.6% | -0.0287 to 0.0626 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 126 | 131 | +4.1% | -15.1 to 25.4 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 123 | 127 | +3.7% | -15.4 to 24.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.73 | 3.39 | +24.3% | 0.293 to 1.04 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 232 | 277 | +19.5% | -76.7 to 167 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
