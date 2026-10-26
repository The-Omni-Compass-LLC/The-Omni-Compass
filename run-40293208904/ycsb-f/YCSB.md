# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,827 | 5,825 | -0.0% | -8.09 to 4.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,836 | 5,834 | -0.0% | -8.03 to 4.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.181 | 0.182 | +0.6% | -0.0211 to 0.0231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.397 | -0.7% | -0.0501 to 0.0448 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0911 | 0.0911 | -0.0% | -0.00887 to 0.00886 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 527 | +3.0% | -46.3 to 77.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 432 | +3.1% | -34.7 to 60.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,830 | 680,449 | -2.9% | -101,404 to 60,642 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.13 | -12.3% | -0.104 to 0.0676 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 232 | -14.9% | -220 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.102 | 0.0867 | -14.9% | -0.0822 to 0.0519 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 133 | 134 | +0.8% | -10.8 to 13 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 130 | 131 | +0.4% | -11.3 to 12.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.91 | 3.5 | +20.4% | 0.455 to 0.732 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 272 | 232 | -14.9% | -220 to 139 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
