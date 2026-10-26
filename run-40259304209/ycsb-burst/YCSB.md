# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -4.64 to 2.88 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -3.44 to 2.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.408 | 0.409 | +0.2% | -0.0118 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.577 | 0.579 | +0.4% | -0.0254 to 0.03 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.21 | -0.2% | -0.00485 to 0.00406 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -17 to 22.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 408 | +0.8% | -18.1 to 24.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 256,907 | 272,467 | +6.1% | 3,337 to 27,783 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.178 | -14.6% | -0.0963 to 0.0356 | EVEN, no difference beyond the noise |
| host CPU-seconds | 148 | 122 | -17.7% | -84.1 to 31.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.229 | -17.7% | -0.158 to 0.06 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80 | 80 | -0.0% | -2.73 to 2.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79 | 78.7 | -0.3% | -2.86 to 2.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.22 | +21.2% | 0.127 to 0.301 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 148 | 122 | -17.7% | -84.2 to 32 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
